# 🚀 Portfolio Auto-Deployment — AWS S3 + Terraform + GitHub Actions


> Automated CI/CD pipeline that deploys a static portfolio website to AWS S3 using Terraform for infrastructure provisioning and GitHub Actions for continuous deployment.

---

<img width="1920" height="960" alt="image" src="https://github.com/user-attachments/assets/00c8afc3-8c89-4a6b-af50-459d0358f902" />


## 📌 Project Overview

This project demonstrates a fully automated DevOps workflow where every push to the `main` branch triggers a GitHub Actions pipeline that syncs the latest portfolio files directly to an AWS S3 static website bucket — no manual uploads, no AWS Console clicks.

Infrastructure is provisioned and managed entirely through **Terraform**, following Infrastructure as Code (IaC) best practices with reusable modules.

---

## 🏗️ Architecture

```
Developer (Local)
      │
      │  git push
      ▼
 GitHub Repository
      │
      │  Triggers on push to main
      ▼
 GitHub Actions CI/CD
      │
      ├── Configure AWS Credentials
      ├── Sync files to S3
      └── (CloudFront invalidation — coming soon)
      │
      ▼
 AWS S3 Bucket
 (Static Website Hosting)
      │
      ▼
 Live Portfolio Website 🌐
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Terraform** | Infrastructure as Code — provision AWS resources |
| **AWS S3** | Static website hosting |
| **GitHub Actions** | CI/CD pipeline — auto deploy on push |
| **HTML & CSS** | Portfolio website |

---

## 📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions CI/CD pipeline
├── S3-tf-module/               # Reusable Terraform S3 module
│   ├── main.tf
│   ├── output.tf
│   └── variable.tf
├── index.html                  # Portfolio website
├── style.css
├── main.tf                     # Root Terraform config
├── output.tf
├── providers.tf
├── variable.tf
├── version.tf
├── terraform.tfvars.example    # Example variables (safe to commit)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Deployment

### Prerequisites
- [Terraform](https://developer.hashicorp.com/terraform/install) v1.3+
- AWS account with IAM user (S3)
- GitHub repository

### 1. Clone the repository
```bash
git clone https://github.com/Rohit-singh-gusain/CI-CD-Portfolio.git
cd CI-CD-Portfolio

### 2. Provision infrastructure with Terraform

# Initialize and apply
create your own root terraform files according to your configuration e.g(aws_region,bucket_name)
terraform init
terraform plan
terraform apply


### 3. Add GitHub Secrets

| Secret | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key |
| `AWS_REGION` | AWS region (e.g. `us-east-1`) |
| `S3_BUCKET_NAME` | Your S3 bucket name |

### 4. Deploy
Just push to `main` — the pipeline handles the rest!
```bash
git add .
git commit -m "Update portfolio"
git push origin main
```

---

## 🔄 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs on every push to `main`:

1. ✅ Checkout latest code
2. ✅ Configure AWS credentials via GitHub Secrets
3. ✅ Sync `html`, `css`, `js`, and image files to S3
4. ✅ Remove deleted files from S3 automatically (`--delete` flag)


## 🔐 Security Notes

- AWS credentials are stored as **GitHub Secrets** — never hardcoded
- `terraform.tfvars` is excluded via `.gitignore` to prevent secret leaks
- State files (`*.tfstate`) are excluded from version control

---

## 👤 Author

**Rohit Singh Gusain**
- GitHub: https://github.com/Rohit-singh-gusain?tab=repositories
- LinkedIn: https://www.linkedin.com/in/rohit-singh-754a48257/
