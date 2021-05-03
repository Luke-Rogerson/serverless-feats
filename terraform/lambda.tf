locals {
  lambda_src_path = "../app/lambda"
}

resource "random_uuid" "lambda_src_hash" {
  keepers = {
    for filename in setunion(
      fileset(local.lambda_src_path, "*.py"),
      fileset(local.lambda_src_path, "requirements.txt"),
      fileset(local.lambda_src_path, "lib/**/*.py")
    ) :
    filename => filemd5("${local.lambda_src_path}/${filename}")
  }
  depends_on = [
    aws_iam_role_policy_attachment.lambda_logs,
    aws_cloudwatch_log_group.example,
  ]
}

resource "aws_lambda_function" "lambda_function" {
  role             = aws_iam_role.feats_dynamo_role.arn
  handler          = var.handler
  runtime          = var.runtime
  filename         = "../lambda.zip"
  source_code_hash = random_uuid.lambda_src_hash.result
  function_name    = var.function_name
}

resource "aws_iam_role_policy" "feats_dynamo_policy" {
  name   = "feats_dynamo_policy"
  role   = aws_iam_role.feats_dynamo_role.id
  policy = <<-EOF
  {  
   "Version": "2012-10-17",
   "Statement":[{
     "Effect": "Allow",
     "Action": [
      "dynamodb:BatchGetItem",
      "dynamodb:GetItem",
      "dynamodb:Query",
      "dynamodb:Scan",
      "dynamodb:BatchWriteItem",
      "dynamodb:PutItem",
      "dynamodb:UpdateItem"
     ],
    "Resource": "${aws_dynamodb_table.feat_table.arn}"
    }
   ]
  }
  EOF
}

resource "aws_iam_role" "feats_dynamo_role" {
  name = "feats_dynamo_role"

  assume_role_policy = <<-EOF
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  }
  EOF
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = var.function_name
  principal     = "apigateway.amazonaws.com"

  # The "/*/*" portion grants access from any method on any resource
  # within the API Gateway REST API.
  source_arn = "${aws_api_gateway_rest_api.feats.execution_arn}/*/*"
}

resource "aws_cloudwatch_log_group" "example" {
  name              = "/aws/lambda/${var.function_name}"
  retention_in_days = 14
}

resource "aws_iam_policy" "lambda_logging" {
  name = "lambda_logging"
  path = "/"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.feats_dynamo_role.name
  policy_arn = aws_iam_policy.lambda_logging.arn
}

output "base_url" {
  value = aws_api_gateway_deployment.feats.invoke_url
}