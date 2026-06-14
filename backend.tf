
terraform {
  required_version = ">= 1.0"       

  backend "s3" {                     
    bucket = "rohit-luffy-portfolio-tfstate"
    key    = "portfolio/terraform.tfstate"
    region = "us-east-1"
  }
}