import json
from typing import Any, Dict, Optional, TypedDict, List, Union, cast
# from lib import user

from aws_lambda_types.api_gw import (
    APIGWPayloadV1RequestContextDict,
    APIGWPayloadV1RequestDict,
    APIGWPayloadV1ResponseDict,
)
class CreateUser(TypedDict):
    username: str
    email: str
    interests: List[str]
    based_in: str

def lambda_handler(
    event: APIGWPayloadV1RequestDict, context: APIGWPayloadV1RequestContextDict
) -> APIGWPayloadV1ResponseDict:
    
    # remove prepended "dev"
    path = event["requestContext"]["path"][4:]
    return cast(APIGWPayloadV1ResponseDict, switch(path=path, event=event))

def construct_success_response(body: Union[Dict[str, Any], APIGWPayloadV1RequestDict], status_code: Optional[int] = 200):
    return {
        "statusCode": status_code,
        "headers": {
            'Content-Type': 'application/json',
        },
        "body": json.dumps(body),
    }   


def switch(path: str, event: APIGWPayloadV1RequestDict):
    if path == "/createuser":
        return construct_success_response(body={"path": "createuser"})
    elif path == "/createfeat":
        return construct_success_response(body={"path": "createfeat"})
    return construct_success_response(body=event)
