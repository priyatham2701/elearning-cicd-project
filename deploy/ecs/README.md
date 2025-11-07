# ECS/Fargate Deploy Notes

Cluster: elearn-cluster
Region: us-east-2
Account: 411189321627

Per service:
- ECR repo: same as folder (e.g., svc-courses)
- Task definition family: svc-<name>-task (create via console)
- ECS service: svc-<name>-service (Fargate, port 8000, SG allows 8000 inbound)
- After the first image is pushed, update-service will roll out new tasks.

OIDC Role (GitHub → AWS):
- Name: GitHubOIDC-ECS-Deploy
- Provider: token.actions.githubusercontent.com
- Audience: sts.amazonaws.com
- Policies: AmazonECSFullAccess, AmazonEC2ContainerRegistryFullAccess
- Scope to your repo if desired using a trust condition on `sub`.
