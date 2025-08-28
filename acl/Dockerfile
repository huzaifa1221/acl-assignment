# Use an official lightweight Python image
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000

# Run the Flask app
CMD ["python3", "app.py"]