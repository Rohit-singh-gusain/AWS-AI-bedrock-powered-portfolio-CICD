import json
import boto3

bedrock = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

PROFILE = """
Rohit Singh Gusain
Dehradun, Uttarakhand | +91 8077476177 | rohitgusain9930@gmail.com
LinkedIn: https://www.linkedin.com/in/rohit-singh-754a48257 | Github: https://github.com/Rohit-singh-gusain
PROFESSIONAL SUMMARY
Motivated and detail-oriented BCA graduate with practical expertise in AWS cloud infrastructure, DevOps tooling, and
Infrastructure as Code (IaC). Experienced in provisioning and managing scalable cloud environments using Terraform,
automating CI/CD pipelines with GitHub Actions, containerizing applications with Docker, and deploying production-
grade workloads on AWS services including EC2, S3, VPC, ALB, CloudWatch, and Route 53. Demonstrated ability to
build real-world cloud projects independently — from infrastructure provisioning to automated deployment pipelines.
Actively pursuing entry-level Cloud Engineer or DevOps Engineer roles to contribute technical skills, accelerate
learning, and deliver value in a fast-paced cloud-first environment.
EDUCATION
Bachelor of Computer Applications (BCA) | Dev Bhoomi Uttarakhand University (2023–2026)
TECHNICAL SKILLS
Cloud Platforms: AWS (EC2, S3, IAM, Lambda, VPC, CloudWatch, Route 53, ALB, SNS, EventBridge)
Infrastructure & DevOps: Terraform, Docker, Git, GitHub, Nginx.
Scripting Languages: Python, Bash (Basics)
Databases: MySQL, SQL, MongoDB (Basics)
Support Tools: CloudWatch Logs, grep, journalctl, Jira (basic)
Networking & OS: TCP/IP, DNS, HTTP/HTTPS, VPN, Subnetting, Linux (Ubuntu), Windows Server Basics
CI/CD Tools: GitHub Actions, Jenkins (Basics)
PROJECTS
AWS Lambda EC2 Cost Guardian | EventBridge, Lambda, SNS, Terraform, Python
• Built a fully serverless AWS pipeline that automatically monitors running EC2 instances daily and sends detailed
email alerts via SNS — solving the real problem of forgotten instances causing unexpected cloud bills.
• Developed the core Lambda function in Python using boto3 to call ec2:DescribeInstances API, extracting
instance details including ID, name, type, region, availability zone, running duration, and IP addresses.
• Configured Amazon EventBridge cron rule to trigger Lambda automatically on a daily schedule — zero manual
intervention, no server required.
• Provisioned entire infrastructure using Terraform with a modular architecture — separate modules for IAM,
Lambda, SNS, and EventBridge — enabling fully reproducible deployment with a single terraform apply.• Implemented IAM least privilege security — Lambda uses an execution role with only ec2:DescribeInstances and
sns:Publish permissions, with zero hardcoded credentials in code.
• Passed sensitive values (SNS Topic ARN, AWS region) via Terraform environment variables into Lambda —
eliminating hardcoded configuration and following AWS security best practices.
Github: https://github.com/Rohit-singh-gusain/lambda-ec2-watchdog-
Movie Ticket Booking Application | AWS Deployment
• Deployed a full-stack Movie Ticket Booking application on Amazon Web Services using services including EC2,
VPC, Application Load Balancer (ALB), AWS Systems Manager Parameter Store, Security Groups, and Route
configuration.
• Designed and developed reusable Terraform modules from scratch to provision and manage scalable AWS
infrastructure using Infrastructure as Code (IaC) practices.
• Containerized the website with Docker.
• Configured a custom domain and mapped it to the ALB endpoint for public access and improved application
availability.
• Implemented networking components such as public/private subnets and secure traffic routing within the AWS
environment.
• Created an Amazon Simple Notification Service (SNS) topic integrated with Amazon CloudWatch alarms to send
automated email notifications whenever EC2 CPU utilization exceeded the defined threshold.
Github: https://github.com/Rohit-singh-gusain/AWS-Terraform
Portfolio Deployment CI/CD Pipeline | AWS S3, Terraform, GitHub Actions
• Provisioned AWS S3 static website hosting using Terraform IaC with reusable modules managing bucket
policies, versioning, and public access configuration.
• Automated deployment via GitHub Actions CI/CD pipeline that syncs portfolio files to S3 on every push to main
branch, eliminating manual uploads.
• Secured AWS credentials using GitHub Secrets ensuring zero hardcoded sensitive information across the entire
codebase and pipeline.
Github: https://github.com/Rohit-singh-gusain/CI-CD-Portfolio
CERTIFICATIONS
• AWS Cloud Practitioner Certified
• JLPT N5
SOFT SKILLS
Problem Solving | Team Collaboration | Adaptability | Effective Communication
LANGUAGES
English | Hindi | Japanese
"""


def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])

        user_message = body.get("message", "")

        prompt = f"""
        {PROFILE}

        User Question:
        {user_message}
        """

        response = bedrock.invoke_model(
            modelId="amazon.nova-lite-v1:0",
            body=json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            })
        )

        response_body = json.loads(
            response["body"].read()
        )

        answer = response_body["output"]["message"]["content"][0]["text"]

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "answer": answer
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }