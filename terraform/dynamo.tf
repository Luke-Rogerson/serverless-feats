resource "aws_dynamodb_table" "todo_table" {
  name           = var.dynamo_table_name
  billing_mode   = "PAY_PER_REQUEST"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "Id"
  range_key      = "DateModified"

  attribute {
    name = "Id"
    type = "S"
  }

  attribute {
    name = "DateModified"
    type = "S"
  }

  tags = {
    Name        = "${var.app_name}-dynamodb"
    Environment = "staging"
  }
}