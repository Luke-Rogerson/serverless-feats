import sys
import boto3

from typing import List, Optional, cast
from dataclasses import dataclass
from boto3_type_annotations.dynamodb import ServiceResource, Table

from src.constants import TABLE_NAME

ddb: ServiceResource = boto3.resource("dynamodb")
table = cast(Table, ddb.Table(TABLE_NAME))

# Closest I can find to a TypeScript interface
@dataclass
class User:
    username: str
    email: str
    based_in: str
    interests: List[str]
    following: int
    followers: int
    feats: Optional[List[str]]

def create_user(username: str, email: str, based_in: str, interests: List[str]) -> None:
    pk = "USER#{}".format(username)
    sk = "#METADATA#{}".format(username)

    try:
        table.put_item(
            Item={
                "PK": pk,
                "SK": sk,
                "username": username,
                "email": email,
                "based_in": based_in,
                "interests": interests,
                "following": 0,
                "followers": 0,
            }
        )
    except Exception as e:
        print(f"Could not create user: {e}")
        sys.exit(1)

    print(f"Successfully created user \"{username}\"")

def get_user(username: str) -> User:
    pk = "USER#{}".format(username)
    sk = "METADATA#{}".format(username)

    try:
        res = table.get_item(Key={'PK': pk, 'SK': sk})
    except Exception as e:
        print(f"Could not retrieve user: {e}")
        sys.exit(1)

    user: User = res['Item']

    return user

if __name__ == "__main__":
    create_user(
        username="luke",
        email="luke@aol.com",
        based_in="USA",
        interests=["eating", "drinking", "partying"],
    )




