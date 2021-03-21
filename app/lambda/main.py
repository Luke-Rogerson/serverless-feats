from typing import Any
from lib import user


def lambda_handler(event: Any, context: Any):
    res = user.create_user(username="here", email="here@aol.com", interests=["reading", "writing"], based_in="London")
    
    return { 
          "statusCode": 200,
          "body": res,
    }
