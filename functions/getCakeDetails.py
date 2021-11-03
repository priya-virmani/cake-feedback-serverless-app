import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

# creates the dynamo OBJECT
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

#create table object
tableName = dynamodb.Table("cakes")

def lambda_handler(event, context):
    """This lambda function will fetch the details of a cake from DynamoDB table 'cakes'"""
    print(event)
    
    nm = event["name"]
    response = tableName.scan(
        FilterExpression = Attr('Name').eq(nm)
    )
    print(response["Items"][0])
    return response["Items"][0]