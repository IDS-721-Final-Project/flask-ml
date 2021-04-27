# flask-ml
[![Python application](https://github.com/IDS-721-Final-Project/flask-ml/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/IDS-721-Final-Project/flask-ml/actions/workflows/python-app.yml)
## 1. Build and Push Docker Container
```bash
docker build -t ml-k8s .

docker tag ml-k8s gcr.io/[PROJECT-ID]/ml-k8s

docker push gcr.io/[PROJECT-ID]/ml-k8s
```
## 2. Deploy on Kubernetes
### 2.1 Setting up Kubernetes Clusters
```bash
gcloud container clusters create k8s-ml-cluster --num-nodes 3 --machine-type g1-small --zone us-west1-b

gcloud container clusters get-credentials k8s-ml-cluster --zone us-west1-b --project [PROJECT_ID]
```
### 2.2 Install Kustomization
```bash
tar xzf ./kustomize_v4.1.2_linux_amd64.tar.gz

sudo mv kustomize /usr/bin/
```
### 2.3 Deploy the Pod
```bash
kubectl apply --kustomize=${PWD}/base/ --record=true
```
Optional:
```bash
kubectl get ns

kubectl get deployment -n mlops

kubectl get service -n mlops
```

## 3. Test the Deployed Model
```bash
curl http://[EXTERNAL_IP_ADDRESS]:5000/
```
Note: You can get the external ip address from this command:
```bash
kubectl get service -n mlops
```
## 4. Make Predictions with Real Time Data
 ```bash
 python3 predict.py --name=TWTR
 ```
