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

# Deployments



# Config as code YAML
