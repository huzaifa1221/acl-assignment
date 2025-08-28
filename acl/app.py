from flask import Flask, jsonify
import psycopg2
import yaml

app = Flask(__name__)

# Load configuration from YAML (mounted from ConfigMap)
# Mount path in Kubernetes
with open("./config/api-config.yaml", "r") as f:
    mappings = yaml.safe_load(f)

api_mappings = {m["api_endpoint"].lstrip("/"): m for m in mappings["mappings"]}

# Database connection details
db_config = {
    'user': 'postgres',
    'host': 'database',  # Kubernetes service name
    'database': 'postgres',
    'password': 'password',
    'port': 5432,
}

# healthcheck
@app.route("/health", methods=["GET"])
def healthcheck():
    return jsonify({"status": "ok", "message": "API is healthy"}), 200


@app.route("/<string:path>")
@app.route("/<path:path>")
def index(path):
    if path not in api_mappings:
        return jsonify({"error": f"No mapping found for path: /{path}"}), 404

    mapping = api_mappings[path]
    query = mapping["query"]
    columns_map = mapping["columns"]

    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        col_names = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()

        return jsonify(transform_data(rows, col_names, columns_map))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def transform_data(rows, col_names, columns_map):
    data = []
    for row in rows:
        row_dict = {}
        for db_col, value in zip(col_names, row):
            if db_col in columns_map:  # only map defined columns
                api_field = columns_map[db_col]
                row_dict[api_field] = value
        data.append(row_dict)
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
