module "my_portfolio_bucket" {
    source = "./S3-tf-module"
    bucket_name = var.bucket_name
}

module "lambda_module" {
  source = "./lambda_bedrock_module"
  lambda_role_arn = module.iam_role_module.iam_role_arn
}

module "iam_role_module" {
  source = "./IAM_ROLES"
}

module "api_gateway_module" {
  source = "./api_gateway_module"
  lambda_invoke_arn = module.lambda_module.lambda_invoke_arn
  lambda_function_name = module.lambda_module.labmda_function_name
  lambda_function_arn = module.lambda_module.lambda_function_arn
}

