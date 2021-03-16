from typing import Any

def lambda_handler(event: Any, context: Any):
    return { 
          "statusCode": 200,
          "body": "Hello world",
    }
