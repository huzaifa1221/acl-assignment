# Invoicing DevOps Guide


# CI-CD

 - **Main Deployment :** Triggers everytime there is a push to the main branch. It deploys k8s manifests using the ./helm/values-prod.yaml in the prod namespace.
 - **Stage Deployment :** Triggers everytime there is a push to the Stage branch and also manually using workflow dispatch. It deploys k8s manifests using the ./helm/values-stage.yaml in the stage namespace.

## Helm

 - Each service has a helm folder which contains all the deployment
   related config.
 - Seperate values file per environment is present in this folder with all the configuration regarding the service.
 - Values file uses two types of secrets docker-registry-secret and app-secrets for dockerhub authentication and env variables respectively.

## Nginx server

The nginx server is configured to route all the requests coming to /stage/ location to the ingress controller, which further handles routing using ingress rules.

In future, to run production update the /main/ location to forward requests to ingress-controller-service.

## Secrets

 - **app-secrets :** these are env variables deployed directly to the both namespace from the app-secrets.yaml present in the /etc/invoice-stage and /etc/invoice-main directory.
 - **docker-registry-secrets :** These are dockerhub credentials deployed on the prod and stage namespace.