import json
from typing import TypedDict, List
# from lib import user

from aws_lambda_types.api_gw import (
    APIGWPayloadV1RequestContextDict,
    APIGWPayloadV1RequestDict,
    APIGWPayloadV2ResponseDict,
)
class CreateUser(TypedDict):
    username: str
    email: str
    interests: List[str]
    based_in: str

def lambda_handler(
    event: APIGWPayloadV1RequestDict, context: APIGWPayloadV1RequestContextDict
) -> APIGWPayloadV2ResponseDict:
    
    path = event["requestContext"]["path"]
    return switch(path=path)


def switch(path: str):
    if path == "createuser":
        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
            },
            "body": json.dumps({"path": "createuser"}),
        }
    elif path == "createfeat":
        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
            },
            "body": json.dumps({"path": "createfeat"}),
        }
    return {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'application/json',
        },
        "body": json.dumps({"path": "default"}),
    }
