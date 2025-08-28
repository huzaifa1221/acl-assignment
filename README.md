install docker-desktop for kubernetes cluster and local docker registry, it will include docker as well

or install using any other approach as wished.

# CI/CD

1. ### acl.yaml - for the deployment of Anti Corruption Layer (Python app)
    * This workflow is triggered when a code is committed to the main branch on either "acl/**" or "helm/acl/**" of the paths.
    * It will build the docker image and deploy to the default branch of the local kubernetes cluster.
    * change helm install --> helm upgrade for future deployments.
      
2. ### api-config.yaml - for the deployment of config map
    * This workflow is triggered when a code is committed to the main branch on "./api-config.yaml".
    * it will create a new config map for the **first time** only.
    * uncomment the commented lines for future deployments that will delete the config map, create a new one and restart the acl deployment in order for the new changes to be picked up.
  
3. ### db.yaml - for the deployment of postgres database
    * This workflow is triggered when a code is committed to the main branch on "helm/database/**".
    * it will create a postgres database when runs for the **first time** only.
    * change helm install --> helm upgrade for future deployments.

# Deployments / Iaac / helm

1. ### Acl (Anti-corruption Layer)
   * this folder holds all the configuration for the acl.
   * we have a config map api-config (api configuration yaml file) being mounted to path app/config which is used in the acl container for mapping.
  
2. ### database
   * this folder holds all the configuration for the database.
   * we have a postgres database which needs to be pre seeded with the sql data.
   * To preseed the database follow the steps one by one ->

      1. after the postgres pod is created execute ``kubectl exec -it <pod id> bash``
      2. once logged in log in to psql ``psql -U postgres``
      3. create db ``CREATE DATABASE mydb;``
      4. switch to the db ``\c mydb``
      5. execute the follwing queries to pre-seed the database.
            ```
            CREATE TABLE IF NOT EXISTS mytable (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            
            CREATE TABLE IF NOT EXISTS othertable (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            
            INSERT INTO mytable (name) VALUES
            ('Alice'),
            ('Bob');
            
            INSERT INTO othertable (name) VALUES
            ('Charlie'),
            ('Diana');
            
# Config as code YAML
