# 🚀 Rohit Singh Gusain — Portfolio Website

A professional cloud-native portfolio website built and deployed entirely on AWS using Infrastructure as Code (Terraform), containerization-free static hosting on S3, and a fully automated CI/CD pipeline via GitHub Actions. Features an AI-powered chatbox integrated with AWS Bedrock (Claude 3 Sonnet) through API Gateway and Lambda.

![AWS](https://img.shields.io/badge/AWS-Deployed-orange?logo=amazon-aws)
![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?logo=terraform)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions)
![S3](https://img.shields.io/badge/Hosting-AWS%20S3-569A31?logo=amazon-s3)

---

## 📁 Project Structure

```
.
├── api_gateway_module/         # Terraform module — API Gateway (HTTP API v2)
│   ├── main.tf                 # API, Lambda integration, route, stage
│   ├── output.tf               # Exports chat_api_url
│   └── variable.tf
│
├── bedrock_python_code/        # Lambda function source code
│   ├── bedrock.py              # Calls AWS Bedrock (Claude 3 Sonnet) via boto3
│   └── bedrock.zip             # Packaged Lambda deployment artifact
│
├── IAM_ROLES/                  # Terraform module — IAM roles & policies
│   ├── main.tf                 # Lambda execution role, least-privilege policies
│   ├── output.tf
│   └── variable.tf
│
├── lambda_bedrock_module/      # Terraform module — Lambda function
│   ├── main.tf                 # Lambda config, env vars, zip deployment
│   ├── output.tf
│   └── variable.tf
│
├── S3-tf-module/               # Terraform module — S3 static website hosting
│   ├── main.tf                 # Bucket, policy, versioning, website config
│   ├── output.tf
│   └── variable.tf
│
├── screenshots/
│   └── portfolio.png
│
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline — Terraform + S3 deploy
│
├── index.html                  # Portfolio frontend
├── styles.css                  # Stylesheet
├── script.js                   # Chatbox logic + API Gateway integration
│
├── backend.tf                  # S3 remote backend for Terraform state
├── main.tf                     # Root module — calls all child modules
├── output.tf                   # Root outputs (chat_api_url, etc.)
├── providers.tf                # AWS provider configuration
├── variable.tf                 # Input variable declarations
├── version.tf                  # Terraform + provider version constraints
├── terraform.tfvars            # Variable values
└── README.md
```

---

## 🏗️ Architecture Overview

```
User Browser
     │
     ▼
 AWS S3 (Static Website Hosting)
     │  index.html / styles.css / script.js
     │
     │  Chat Message (POST)
     ▼
 API Gateway (HTTP API v2)
     │  POST /chat
     ▼
 AWS Lambda (Python 3.12)
     │  bedrock.py
     ▼
 AWS Bedrock (Claude 3 Sonnet)
     │  AI Response
     └──────────────────► User Browser
```
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/023e3f45-b6f7-4dae-8111-e7da150d4c66" />


---

## ⚙️ CI/CD Pipeline

Every `git push` to `main` triggers the GitHub Actions workflow:

```
git push origin main
       │
       ▼
  Checkout Code
       │
       ▼
  Configure AWS Credentials (GitHub Secrets)
       │
       ▼
  Terraform Init  ──► reads state from S3 backend (rohit-luffy-portfolio-tfstate)
       │
       ▼
  Terraform Apply ──► provisions/updates all infrastructure
       │
       ▼
  terraform output -json ──► extracts chat_api_url
       │
       ▼
  sed inject ──► replaces REPLACE_WITH_API_URL in script.js
       │
       ▼
  aws s3 sync ──► deploys html + css + js to portfolio bucket
```

---

## 🧩 Terraform Modules

| Module | Purpose |
|---|---|
| `S3-tf-module` | S3 bucket with static website hosting, bucket policy, versioning |
| `api_gateway_module` | HTTP API Gateway v2, Lambda integration, POST /chat route |
| `lambda_bedrock_module` | Lambda function deployed from `bedrock.zip` |
| `IAM_ROLES` | Lambda execution role with least-privilege Bedrock + CloudWatch permissions |

---

## 🤖 AI Chatbox — AWS Bedrock Integration

The portfolio includes a floating AI chatbox powered by **AWS Bedrock (Claude 3 Sonnet)**:

- **Frontend** — `script.js` sends `POST /chat` with `{ "message": "..." }` to API Gateway
- **API Gateway** — HTTP API v2 routes request to Lambda
- **Lambda** — `bedrock.py` calls Bedrock using `boto3`, returns AI response
- **IAM** — Lambda role has only `bedrock:InvokeModel` and `logs:*` permissions

The API Gateway endpoint URL is **automatically injected** into `script.js` during the CI/CD pipeline via `terraform output` — no manual copy-paste required.

---

## 🔐 Security

- AWS credentials stored in **GitHub Secrets** — never hardcoded
- Terraform state stored in **private S3 bucket** (`rohit-luffy-portfolio-tfstate`)
- Lambda IAM role follows **least privilege** — only required permissions granted
- API Gateway endpoint injected at deploy time — not hardcoded in source code

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Hosting | AWS S3 Static Website |
| IaC | Terraform |
| CI/CD | GitHub Actions |
| AI Backend | AWS Bedrock (Claude 3 Sonnet) |
| Compute | AWS Lambda (Python 3.12) |
| API | AWS API Gateway HTTP API v2 |
| State Backend | AWS S3 |
| Frontend | HTML, CSS, Vanilla JavaScript |

---

## 🚀 Deployment

### Prerequisites
- AWS CLI configured
- Terraform >= 1.7.0
- GitHub repository with the following secrets set:

| Secret | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | AWS access key |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key |
| `AWS_REGION` | AWS region (e.g. `us-east-1`) |
| `S3_BUCKET_NAME` | Portfolio S3 bucket name |

# ScreenShots
<img width="1573" height="1001" alt="image" src="https://github.com/user-attachments/assets/4be539ff-4992-46b7-ab0a-81130fbf2e3c" />

<img width="449" height="616" alt="image" src="https://github.com/user-attachments/assets/5f0216e5-e14d-4df0-9246-930c472088c0" />




## 👤 Author


**Rohit Singh Gusain**
- 📧 rohitgusain9930@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/rohit-singh-754a48257)
- 🐙 [GitHub](https://github.com/Rohit-singh-gusain)
- 📍 Dehradun, Uttarakhand, India
