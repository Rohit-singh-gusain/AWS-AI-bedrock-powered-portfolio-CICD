
output "chat_api_url" {
  value = "${aws_apigatewayv2_api.chat_api.api_endpoint}/chat"
}