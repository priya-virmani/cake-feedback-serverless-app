import json
import boto3

# creates the dynamo OBJECT
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('cakes')

def lambda_handler(event, context):
    """This lambda function will add a new cake to DynamoDB table  'cakes'"""
    
    print(event)
    id = event["id"]
    name = event["name"]
    comment = event["comment"]
    image = event["imageURL"]
    yum = event["yumFactor"]

    table.put_item(
        Item={
            "id":id,
            "Name":name,
            "Comment":comment,
            "ImageURL":image,
            "YumFactor":yum
        }
    )
                   
    return 'Record for ' + event['name'] + ' added Successfully'