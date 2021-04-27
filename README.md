# flask-ml

## 1. Build and Push Docker Container
```bash
docker build -t ml-k8s .

docker tag ml-k8s gcr.io/[PROJECT-ID]/ml-k8s

docker push gcr.io/[PROJECT-ID]/ml-k8s
```
## 2. Deploy on Kubernetes
```bash
gcloud container clusters create k8s-ml-cluster --num-nodes 3 --machine-type g1-small --zone us-west1-b

gcloud container clusters get-credentials k8s-ml-cluster --zone us-west1-b --project [PROJECT_ID]

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
curl http://[EXTERNAL_IP_ADDRESS]:5000/score \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"X": [1, 2]}'
```