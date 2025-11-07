# eLearning CI/CD Project (5 Microservices)

This repository contains five FastAPI microservices for an e-learning platform:

- svc-courses
- svc-students
- svc-instructors
- svc-enrollment
- svc-notifications

Each service has its own CI/CD workflow (GitHub Actions) that:
- Runs tests
- Builds a Docker image
- Pushes it to Amazon ECR (per-service repo)
- Triggers deployment to Amazon ECS Fargate (per-service ECS service)

## Quick Start (Local Dev)

```bash
# Example for svc-courses
cd svc-courses
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
# visit http://127.0.0.1:8000/health
```

## AWS Prereqs

- ECR repos: one per service (same names as service folders)
- ECS cluster: **elearn-cluster**
- ECS services: svc-<name>-service (e.g., svc-courses-service) with container port 8000
- IAM OIDC role (for GitHub Actions): `GitHubOIDC-ECS-Deploy`
  - Policies: AmazonECSFullAccess, AmazonEC2ContainerRegistryFullAccess
  - Trust: token.actions.githubusercontent.com, audience sts.amazonaws.com
  - Limit to your repo if desired via `sub` = `repo:<org>/<repo>:*`

## GitHub Secrets (Repo → Settings → Secrets and variables → Actions)

- `AWS_ROLE_ARN` = arn:aws:iam::411189321627:role/GitHubOIDC-ECS-Deploy

The workflows use environment variables for region and resource names.

## Verify CI/CD

- Edit any file under a service directory (e.g., `svc-courses/app.py`)
- Commit and push
- Watch the corresponding workflow in the Actions tab
- After success, confirm new image in ECR and new task in ECS
- Hit the task public IP: `http://<public-ip>:8000/health`

## Notes

- Region: **us-east-2**
- AWS Account: **411189321627**
- Cluster: **elearn-cluster**
- Container port: **8000**
- Uvicorn binds to `0.0.0.0` for ECS
