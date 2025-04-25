import boto3
import json

dynamodb = boto3.resource("dynamodb")
table_name = "dev-beyondSightings-users"
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    body = json.loads(event["body"])

    try:
        table_response = table.put_item(Item=body)
        return {"statusCode": 200, "body": json.dumps(table_response)}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
