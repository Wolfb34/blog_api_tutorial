# !/bin/bash

# Delete the blogdb deployments and services and such 
microk8s kubectl delete -f blogdb-config.yaml
microk8s kubectl delete -f blogdb-deployment.yaml
microk8s kubectl delete -f blogdb-secret.yaml
microk8s kubectl delete -f blogdb-service.yaml
microk8s kubectl delete -f blogdb-storage.yaml

# Delete flask-api stuff
microk8s kubectl delete -f flask-api-deployment.yml
microk8s kubectl delete -f flask-api-service.yml

# Delete blog-ui stuff
microk8s kubectl delete -f blog-ui-deployment.yaml
microk8s kubectl delete -f blog-ui-service.yaml

