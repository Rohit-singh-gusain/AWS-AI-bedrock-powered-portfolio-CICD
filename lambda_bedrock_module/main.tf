data "archive_file" "bedrock_code" {
    type = "zip"
    source_file = "${path.root}/bedrock_python_code/bedrock.py"
    output_path = "${path.root}/bedrock_python_code/bedrock.zip"
}


resource "aws_lambda_function" "bedrock_lambda_function" {
    function_name = "lambda_bedrock_function"
    description = "lambda fucntion which will invoke by an api gateway and run bedrock api"
    filename = data.archive_file.bedrock_code.output_path

    source_code_hash = data.archive_file.bedrock_code.output_base64sha256
    runtime          = "python3.12"
    handler          = "bedrock.lambda_handler"  
    role             = var.lambda_role_arn
    timeout          = 30  
    memory_size      = 128  

  
}