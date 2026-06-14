output "lambda_function_arn" {
  value = aws_lambda_function.bedrock_lambda_function.arn
}

output "lambda_invoke_arn" {
  value = aws_lambda_function.bedrock_lambda_function.invoke_arn
}

output "labmda_function_name" {
  value = aws_lambda_function.bedrock_lambda_function.function_name
}