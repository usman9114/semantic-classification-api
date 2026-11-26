<p align="center"><img src="docs/assets/hero.jpg" alt="Banner: a risograph paper-cut illustration of a brass compass whose needle points at the nearest of three paper islands, a coral lighthouse island, with a mustard and a teal island farther away. Title: Semantic classification API." width="100%"></p>

# Semantic Classification using Transformer and Deployment with FastAPI, Kubernetes, and AWS ECS Fargate + ALB

This project utilizes the all-MiniLM-L6-v2 model. This model maps sentences and paragraphs to a 384-dimensional dense vector space, making it suitable for tasks like clustering or semantic search. The project employs FastAPI to create an endpoint serving the transformer model.

## How it works

Zero-shot classification: no training step and no fixed label set. The sentence and every candidate label are embedded with the same model, and the label whose vector is closest to the sentence (highest cosine similarity) wins.

```mermaid
flowchart LR
    C["Client<br/>sentence + labels"] -->|POST /query| API["FastAPI<br/>routes/classifier.py"]
    API --> T["Tokenizer +<br/>all-MiniLM-L6-v2"]
    T --> P["Mean pooling +<br/>L2 normalise<br/>384-d vectors"]
    P --> S["Cosine similarity<br/>sentence vs each label"]
    S --> R["Sort by score"]
    R -->|/query| B["Best label"]
    R -->|/query/details| D["All labels with scores"]
```

## Architecture

Client request -> FastAPI endpoint -> transformer classification -> JSON response. Docker Compose runs the API locally; Kubernetes and AWS ECS examples show deployment paths without relying on a public live endpoint.

```mermaid
flowchart TB
    IMG["Docker image<br/>FastAPI + model, port 8002"]
    IMG --> L["Local<br/>docker-compose up<br/>localhost:8002"]
    IMG --> K["Kubernetes<br/>k8s/deployment.yaml"]
    IMG --> A["AWS CDK stack<br/>deploy-aws/app.py"]
    K --> KS["LoadBalancer Service<br/>port 80 to 8002"]
    K --> KH["HorizontalPodAutoscaler<br/>1 to 10 pods at 50% CPU"]
    A --> AF["ECS Fargate service<br/>2 tasks, 1 vCPU, 4 GiB"]
    AF --> ALB["Application Load Balancer"]
```

Deployment note: Replace example endpoints and credentials with your own environment values before deploying.

## Usage

The model takes a sentence `S` to be classified, along with labels `L = {l1, l2, ...}`, and returns the most suitable label.

## Run locally

`docker-compose` is used to run locally.

### Start the API locally

```bash
docker-compose up
```

### Call the API

```bash
curl http://127.0.0.1:8002/query -X POST -H 'Content-Type: application/json' \
  -d '{"sentence": "feeling like a million bucks", "labels": ["happy", "sad", "rich"]}'
```

`/query` returns the best label:

```json
"rich"
```

`/query/details` returns every label with its cosine similarity, highest first (scores from `src/model`, rounded here):

```json
[["rich", 0.353], ["happy", 0.238], ["sad", 0.205]]
```

## Kubernetes deployment

    kubectl apply -f k8s/deployment.yaml

## Kubernetes Service

Creates a load balancer that exposes the service outside of the cluster.

    kubectl apply -f k8s/service.yaml

## HorizontalPodAutoscaler

To scale the deployment, apply a HorizontalPodAutoscaler.
Kubernetes will monitor the CPU usage of your pods, and if the CPU utilization exceeds the target average utilization, it will scale up the number of replicas.

    kubectl apply -f k8s/autoscale.yaml

A minikube run with ten `fast-mimilm` pods, each using about 150m CPU and 550 MiB:

<img src="images/img.png" alt="Terminal output of 'minikube kubectl top pods' showing ten fast-mimilm pods, each at about 150m CPU and 550 MiB memory" width="70%">

## AWS ECS Fargate + ALB

The CDK stack in `deploy-aws/` runs the image on Fargate behind an Application Load Balancer. Steps: [deploy-aws/readme.md](deploy-aws/readme.md).

<img src="images/aws.png" alt="Deployment flow: FastAPI app built into a Docker image, pushed to Amazon ECR, then Amazon ECS creates a cluster, an AWS Fargate task definition and the API service" width="80%">

## Visual assets

The banner illustration was generated from a written brief (`docs/assets/briefs/hero.md`, with the references it drew on); its sidecar `docs/assets/hero-art.png.json` records the prompt. The text and scores are set by `docs/assets/tools/compose_banner.py`. `docs/assets/social-preview.jpg` (1280x640) is for the repository's social preview.
