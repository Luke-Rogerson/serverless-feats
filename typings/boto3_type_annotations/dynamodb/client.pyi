"""
This type stub file was generated by pyright.
"""

from typing import Dict, List
from botocore.client import BaseClient
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter

class Client(BaseClient):
    def batch_get_item(self, RequestItems: Dict, ReturnConsumedCapacity: str = ...) -> Dict:
        ...
    
    def batch_write_item(self, RequestItems: Dict, ReturnConsumedCapacity: str = ..., ReturnItemCollectionMetrics: str = ...) -> Dict:
        ...
    
    def can_paginate(self, operation_name: str = ...):
        ...
    
    def create_backup(self, TableName: str, BackupName: str) -> Dict:
        ...
    
    def create_global_table(self, GlobalTableName: str, ReplicationGroup: List) -> Dict:
        ...
    
    def create_table(self, AttributeDefinitions: List, TableName: str, KeySchema: List, LocalSecondaryIndexes: List = ..., GlobalSecondaryIndexes: List = ..., BillingMode: str = ..., ProvisionedThroughput: Dict = ..., StreamSpecification: Dict = ..., SSESpecification: Dict = ..., Tags: List = ...) -> Dict:
        ...
    
    def delete_backup(self, BackupArn: str) -> Dict:
        ...
    
    def delete_item(self, TableName: str, Key: Dict, Expected: Dict = ..., ConditionalOperator: str = ..., ReturnValues: str = ..., ReturnConsumedCapacity: str = ..., ReturnItemCollectionMetrics: str = ..., ConditionExpression: str = ..., ExpressionAttributeNames: Dict = ..., ExpressionAttributeValues: Dict = ...) -> Dict:
        ...
    
    def delete_table(self, TableName: str) -> Dict:
        ...
    
    def describe_backup(self, BackupArn: str) -> Dict:
        ...
    
    def describe_continuous_backups(self, TableName: str) -> Dict:
        ...
    
    def describe_endpoints(self) -> Dict:
        ...
    
    def describe_global_table(self, GlobalTableName: str) -> Dict:
        ...
    
    def describe_global_table_settings(self, GlobalTableName: str) -> Dict:
        ...
    
    def describe_limits(self) -> Dict:
        ...
    
    def describe_table(self, TableName: str) -> Dict:
        ...
    
    def describe_time_to_live(self, TableName: str) -> Dict:
        ...
    
    def generate_presigned_url(self, ClientMethod: str = ..., Params: Dict = ..., ExpiresIn: int = ..., HttpMethod: str = ...):
        ...
    
    def get_item(self, TableName: str, Key: Dict, AttributesToGet: List = ..., ConsistentRead: bool = ..., ReturnConsumedCapacity: str = ..., ProjectionExpression: str = ..., ExpressionAttributeNames: Dict = ...) -> Dict:
        ...
    
    def get_paginator(self, operation_name: str = ...) -> Paginator:
        ...
    
    def get_waiter(self, waiter_name: str = ...) -> Waiter:
        ...
    
    def list_backups(self, TableName: str = ..., Limit: int = ..., TimeRangeLowerBound: datetime = ..., TimeRangeUpperBound: datetime = ..., ExclusiveStartBackupArn: str = ..., BackupType: str = ...) -> Dict:
        ...
    
    def list_global_tables(self, ExclusiveStartGlobalTableName: str = ..., Limit: int = ..., RegionName: str = ...) -> Dict:
        ...
    
    def list_tables(self, ExclusiveStartTableName: str = ..., Limit: int = ...) -> Dict:
        ...
    
    def list_tags_of_resource(self, ResourceArn: str, NextToken: str = ...) -> Dict:
        ...
    
    def put_item(self, TableName: str, Item: Dict, Expected: Dict = ..., ReturnValues: str = ..., ReturnConsumedCapacity: str = ..., ReturnItemCollectionMetrics: str = ..., ConditionalOperator: str = ..., ConditionExpression: str = ..., ExpressionAttributeNames: Dict = ..., ExpressionAttributeValues: Dict = ...) -> Dict:
        ...
    
    def query(self, TableName: str, IndexName: str = ..., Select: str = ..., AttributesToGet: List = ..., Limit: int = ..., ConsistentRead: bool = ..., KeyConditions: Dict = ..., QueryFilter: Dict = ..., ConditionalOperator: str = ..., ScanIndexForward: bool = ..., ExclusiveStartKey: Dict = ..., ReturnConsumedCapacity: str = ..., ProjectionExpression: str = ..., FilterExpression: str = ..., KeyConditionExpression: str = ..., ExpressionAttributeNames: Dict = ..., ExpressionAttributeValues: Dict = ...) -> Dict:
        ...
    
    def restore_table_from_backup(self, TargetTableName: str, BackupArn: str) -> Dict:
        ...
    
    def restore_table_to_point_in_time(self, SourceTableName: str, TargetTableName: str, UseLatestRestorableTime: bool = ..., RestoreDateTime: datetime = ...) -> Dict:
        ...
    
    def scan(self, TableName: str, IndexName: str = ..., AttributesToGet: List = ..., Limit: int = ..., Select: str = ..., ScanFilter: Dict = ..., ConditionalOperator: str = ..., ExclusiveStartKey: Dict = ..., ReturnConsumedCapacity: str = ..., TotalSegments: int = ..., Segment: int = ..., ProjectionExpression: str = ..., FilterExpression: str = ..., ExpressionAttributeNames: Dict = ..., ExpressionAttributeValues: Dict = ..., ConsistentRead: bool = ...) -> Dict:
        ...
    
    def tag_resource(self, ResourceArn: str, Tags: List):
        ...
    
    def transact_get_items(self, TransactItems: List, ReturnConsumedCapacity: str = ...) -> Dict:
        ...
    
    def transact_write_items(self, TransactItems: List, ReturnConsumedCapacity: str = ..., ReturnItemCollectionMetrics: str = ..., ClientRequestToken: str = ...) -> Dict:
        ...
    
    def untag_resource(self, ResourceArn: str, TagKeys: List):
        ...
    
    def update_continuous_backups(self, TableName: str, PointInTimeRecoverySpecification: Dict) -> Dict:
        ...
    
    def update_global_table(self, GlobalTableName: str, ReplicaUpdates: List) -> Dict:
        ...
    
    def update_global_table_settings(self, GlobalTableName: str, GlobalTableBillingMode: str = ..., GlobalTableProvisionedWriteCapacityUnits: int = ..., GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Dict = ..., GlobalTableGlobalSecondaryIndexSettingsUpdate: List = ..., ReplicaSettingsUpdate: List = ...) -> Dict:
        ...
    
    def update_item(self, TableName: str, Key: Dict, AttributeUpdates: Dict = ..., Expected: Dict = ..., ConditionalOperator: str = ..., ReturnValues: str = ..., ReturnConsumedCapacity: str = ..., ReturnItemCollectionMetrics: str = ..., UpdateExpression: str = ..., ConditionExpression: str = ..., ExpressionAttributeNames: Dict = ..., ExpressionAttributeValues: Dict = ...) -> Dict:
        ...
    
    def update_table(self, TableName: str, AttributeDefinitions: List = ..., BillingMode: str = ..., ProvisionedThroughput: Dict = ..., GlobalSecondaryIndexUpdates: List = ..., StreamSpecification: Dict = ..., SSESpecification: Dict = ...) -> Dict:
        ...
    
    def update_time_to_live(self, TableName: str, TimeToLiveSpecification: Dict) -> Dict:
        ...
    


