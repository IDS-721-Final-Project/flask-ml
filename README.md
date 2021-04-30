# flask-ml
[![Python application](https://github.com/IDS-721-Final-Project/flask-ml/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/IDS-721-Final-Project/flask-ml/actions/workflows/python-app.yml)
## 1. Build and Push Docker Container
```bash
docker build -t ml-k8s .

docker tag ml-k8s gcr.io/[PROJECT-ID]/ml-k8s

docker push gcr.io/[PROJECT-ID]/ml-k8s
```
## 2. Deploy on Kubernetes
The overall structure of the project is as follows
```
| api.py
| base
  | namespace.yaml
  | deployment.yaml
  | service.yaml
  | kustomize.yaml
| Dockerfile
```

### 2.1 Setting up Kubernetes Clusters
Create a cluster called `k8s-ml-cluster`:
```bash
gcloud container clusters create k8s-ml-cluster --num-nodes 3 --machine-type g1-small --zone us-west1-b
```
Connect to the cluster `k8s-ml-cluster`:
```bash
gcloud container clusters get-credentials k8s-ml-cluster --zone us-west1-b --project [PROJECT_ID]
```
### 2.2 Install Kustomize
`Kustomize` is used to easily customize raw, template-free YAML files, without touching the hard-to-manage original YAML.
```bash
tar xzf ./kustomize_v4.1.2_linux_amd64.tar.gz

sudo mv kustomize /usr/bin/
```
### 2.3 Deploy the Pod
After setting up the YAML, we use the following command to deploy our app:
```bash
kubectl apply --kustomize=${PWD}/base/ --record=true
```
#### Optional:
See all components deployed into the namespace:
```bash
kubectl get ns
```
See the status of the deployment:
```bash
kubectl get deployment -n mlops
```

See the status of the service:
```bash
kubectl get service -n mlops
```

## 3. Test the Deployed Model
Test the model (You can get `[EXTERNAL_IP_ADDRESS]` by using the previous command (to see the status of the service)):
```bash
curl http://[EXTERNAL_IP_ADDRESS]:5000/
```

## 4. Make Predictions with Real Time Data
 ```bash
 python3 predict.py --name=TWTR
 ```
