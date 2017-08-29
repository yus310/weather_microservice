# weather_microservice
Micro service to can display the past weeks weather information, based on a location.

# Run Follow Commands from Unix or Linux Terminal

# Set Up Google Cloud for Project, Kubernetes Clusters & Vms

$ gcloud config set project forecast-dev-1

$ gcloud config set compute/zone us-east1-d

$ gcloud container clusters get-credentials dev-1

$ gcloud config set container/cluster dev-1

$ gcloud container clusters get-credentials dev-1

$ gcloud components install kubectl


# Build the Docker image from Repo

$ docker build --no-cache -t gcr.io/forecast-dev-1/forecast:latest -f ${WORKSPACE}/DockerFile ${WORKSPACE}/.

# Push the Docker image to gcr.io

$ gcloud docker -- push gcr.io/forecast-dev-1/forecast:latest

#  Deploy Kubernetes Configuration file for Forecast Service

$ cd ${WORKSPACE}/kubernetes/

$ kubectl create -f forecast.yaml

#  Expose Forecast Services on Kubernetes Cluster

$ kubectl expose deploy forecast-svc --port=80 --target-port=80 --type="LoadBalancer" --name=forecast-backend

# Implement Horizontal Pod Scaler

$ kubectl autoscale deploy forecast-svc --cpu-percent=70 --min=30 --max=300

# Get list of Kubernetes deployments, pods, and services

$ kubectl get deployment,pods,services

