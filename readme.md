# Semantic Classification using Transformer and Deployment with FastAPI, Kubernetes, and AWS ECS Fargate + ALB

This project utilizes the all-MiniLM-L6-v2 model. This model maps sentences and paragraphs to a 384-dimensional dense vector space, making it suitable for tasks like clustering or semantic search. The project employs FastAPI to create an endpoint serving the transformer model.

## Architecture

Client request -> FastAPI endpoint -> transformer classification -> JSON response. Docker Compose runs the API locally; Kubernetes and AWS ECS examples show deployment paths without relying on a public live endpoint.

Deployment note: Replace example endpoints and credentials with your own environment values before deploying.

## Usage

The model takes a sentence `S` to be classified, along with labels `L = {l1, l2, ...}`, and returns the most suitable label.

## Run locally

`docker-compose` is used to run locally.

### Start the API locally

```bash
$ docker-compose up
```

### Call the API

```bash
$ curl http://127.0.0.1:8002//query -X POST -d '{"sentence": "feeling like a million bucks", "labels": ["happy", "sad", "rich"]}'

{
    "sentence": "feeling like a million bucks",
    "labels": ["happy", "sad", "rich"]
}
```

## Kubernetes deployment

    kubectl apply -f k8s/deployment.yaml

## Kubernetes Service

Creates a load balancer that exposes the service outside of the cluster.

    kubectl apply -f k8s/service.yaml

## HorizontalPodAutoscaler

To scale the deployment, apply a HorizontalPodAutoscaler.
Kubernetes will monitor the CPU usage of your pods, and if the CPU utilization exceeds the target average utilization, it will scale up the number of replicas.

    kubectl apply -f k8s/hpa.yaml
