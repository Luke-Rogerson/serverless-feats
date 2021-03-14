import sys
import boto3

from typing import cast
from boto3_type_annotations.dynamodb import ServiceResource, Table
from datetime import datetime

from src.constants import TABLE_NAME
from src.dynamo.user import User

ddb: ServiceResource = boto3.resource("dynamodb")
table = cast(Table, ddb.Table(TABLE_NAME))

def create_feat(username: str, feat: str) -> None:
    timestamp = datetime.now().replace(microsecond=0).isoformat()

    pk = "USER#{}".format(username)
    sk = "FEAT#{}#{}".format(username, timestamp)

    try:
      table.put_item(Item={
        "PK": pk,
        "SK": sk,
        "username": username,
        "timestamp": timestamp,
        "feat": feat
      })
    except Exception as e:
      print(f"Could not create feat: {e}")
      sys.exit(1)

    print(f"Successfully created new feat \"{feat}\"")

def get_user_and_feats(username: str) -> User:
    pk = "USER#{}".format(username)
    metadata = "#METADATA#{}".format(username)
    print(pk)
    print(metadata)
    try:
      res = table.query(
        KeyConditionExpression="PK = :pk AND SK BETWEEN :metadata AND :feats",
        ExpressionAttributeValues={
          ":pk": pk,
          ":metadata": metadata,
          ":feats": "FEAT$" 
        },
        ScanIndexForward=True
      )
    except Exception as e:
      print(f"Could not retrieve user and feats: {e}")
      sys.exit(1)

    user: User = res['Items'][0]
    user['feats'] = [item['feat'] for item in res['Items'][1:]]

    return user


if __name__ == "__main__":
  # create_feat(username="luke", feat="Ate ice cream")
  user = get_user_and_feats(username="luke")
  for feat in user['feats']:
    print(feat)
