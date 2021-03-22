from typing import Any, List
from lib import user

from typing import TypedDict

class CreateUser(TypedDict):
      username: str
      email: str
      interests: List[str]
      based_in: str

def lambda_handler(event: CreateUser, context: Any):

    username = event['username']
    email = event['email']
    interests = event['interests']
    based_in = event['based_in']

    res = user.create_user(username=username, email=email, interests=interests, based_in=based_in)

    return { 
          "statusCode": 200,
          "body": res,
    }


# aws lambda invoke \
#     --function-name my_func \
#                 --cli-binary-format raw-in-base64-out \
#                 --payload '{ "username": "bob", "email": "bob@cool.com", "interests": ["flying"], "based_in": "Chicago" }' \
#     response.json