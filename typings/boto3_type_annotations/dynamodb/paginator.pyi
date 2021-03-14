"""
This type stub file was generated by pyright.
"""

from typing import Dict, List
from datetime import datetime
from botocore.paginate import Paginator

class ListBackups(Paginator):
    def paginate(self, TableName: str = ..., TimeRangeLowerBound: datetime = ..., TimeRangeUpperBound: datetime = ..., BackupType: str = ..., PaginationConfig: Dict = ...) -> Dict:
        ...
    


class ListTables(Paginator):
    def paginate(self, PaginationConfig: Dict = ...) -> Dict:
        ...
    


class ListTagsOfResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = ...) -> Dict:
        ...
    


class Query(Paginator):
    def paginate(self, TableName: str, IndexName: str = ..., Select: str = ..., AttributesToGet: List = ..., ConsistentRead: bool = ..., KeyConditions: Dict = ..., QueryFilter: Dict = ..., ConditionalOperator: str = ..., ScanIndexForward: bool = ..., ReturnConsumedCapacity: str = ..., ProjectionExpression: str = ..., FilterExpression: str = ..., KeyConditionExpression: str = ..., ExpressionAttributeNames: Dict = ..., ExpressionAttributeValues: Dict = ..., PaginationConfig: Dict = ...) -> Dict:
        ...
    


class Scan(Paginator):
    def paginate(self, TableName: str, IndexName: str = ..., AttributesToGet: List = ..., Select: str = ..., ScanFilter: Dict = ..., ConditionalOperator: str = ..., ReturnConsumedCapacity: str = ..., TotalSegments: int = ..., Segment: int = ..., ProjectionExpression: str = ..., FilterExpression: str = ..., ExpressionAttributeNames: Dict = ..., ExpressionAttributeValues: Dict = ..., ConsistentRead: bool = ..., PaginationConfig: Dict = ...) -> Dict:
        ...
    


