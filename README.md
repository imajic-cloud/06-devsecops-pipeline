# 06 - DevSecOps CI/CD Pipeline

## Overview
A fully automated DevSecOps pipeline that integrates security scanning at every stage of the software development lifecycle.

## Architecture
```
Code Push → GitHub Actions → SonarCloud → Docker Build → Trivy Scan → Kubernetes Deploy → OWASP ZAP
```

## Tools Used
- **GitHub Actions** - CI/CD pipeline automation
- **SonarCloud** - Static code analysis and security scanning
- **Docker** - Container image building
- **Trivy** - Container image vulnerability scanning
- **Kubernetes (Minikube)** - Container orchestration and deployment
- **OWASP ZAP** - Dynamic application security testing (DAST)

## Pipeline Stages
1. Code pushed to GitHub triggers the pipeline
2. SonarCloud scans code for bugs and vulnerabilities
3. Docker builds the container image
4. Trivy scans the image for critical CVEs
5. App deploys to Kubernetes (2 replicas)
6. OWASP ZAP scans the live app for security issues

## Application
Simple Python Flask app with:
- `GET /` - Returns pipeline status
- `GET /health` - Health check endpoint

## Security Features
- Pipeline fails automatically on CRITICAL vulnerabilities
- Code quality gate must pass before deployment
- Live app scanned for OWASP Top 10 vulnerabilities
- Container image scanned for known CVEs

## How to Run Locally
```bash
# Build image
docker build -t devsecops-app:v1 ./app

# Deploy to Kubernetes
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml

# Access the app
minikube service devsecops-app-service --url
```
