
terraform {
  required_version = ">= 1.0"       

  backend "s3" {                     
    bucket = "your-state-bucket"
    key    = "portfolio/terraform.tfstate"
    region = "us-east-1"
  }
}