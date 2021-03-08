import boto3
from typing import List
from boto3_type_annotations.dynamodb import Table

import constants

ddb = boto3.resource("dynamodb")


def create_user(username: str, email: str, based_in: str, interests: List[str]) -> None:
    pk = "USER#{}".format(username)
    sk = "METADATA#{}".format(username)

    table: Table = ddb.Table(constants.TABLE_NAME)

    try:
        table.put_item(
            Item={
                "PK": pk,
                "SK": sk,
                "email": email,
                "based_in": based_in,
                "interests": interests,
                "following": 0,
                "followers": 0,
            }
        )
    except Exception as e:
        print(f"Could not create user: {e}")


# create_user(
#     username="luke",
#     email="luke@aol.com",
#     based_in="UK",
#     interests=["eating", "drinking", "partying"],
# )
