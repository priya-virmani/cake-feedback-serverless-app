import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


# creates the dynamo OBJECT

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

#create table object
tableName = dynamodb.Table("cakes")

def lambda_handler(event, context):
    """This lambda function will delete an entry of a cake from DynamoDB table 'cakes'"""

    print(event)
    
    nm = event["name"]
    try:
        response = tableName.scan(FilterExpression = Attr('Name').eq(nm))
        nm_id =  response["Items"][0]["id"]
        res =tableName.delete_item(Key = {'id':nm_id})
        return {"message": "Entry Deleted"}
    except:
        return {"message": "No records found"}