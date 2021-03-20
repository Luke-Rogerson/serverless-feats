# https://stackoverflow.com/a/62065323
# https://www.davidbegin.com/the-most-minimal-aws-lambda-function-with-python-terraform/

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "../src/lambda"
  output_path = "../lambda.zip"
}

resource "aws_lambda_function" "lambda_function" {
  role             = aws_iam_role.feats_dynamo_role.arn
  handler          = var.handler
  runtime          = var.runtime
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = var.function_name
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256 
}

resource "aws_iam_role_policy" "feats_dynamo_policy" {
  name = "feats_dynamo_policy"
  role = aws_iam_role.feats_dynamo_role.id
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
