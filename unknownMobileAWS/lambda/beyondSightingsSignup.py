import json
import requests
import os
import uuid


def lambda_handler(event, context):
    try:
        req_body = json.loads(event["body"])

        response = requests.post(
            # f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={os.environ["KEY"]}',
            f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyD6I6zduyTqSyF0bLt988ecg0rZcYDWWM0",
            headers={"Content-Type": "application/json"},
            json=req_body,
        )

        if response:
            try:
                item_data = {
                    "id": str(uuid.uuid4()),
                    "username": req_body["displayName"],
                    "email": req_body["email"],
                    "avatar": req_body["avatar"],
                }
                dynamoAddAttempt = requests.post(
                    "https://fww9stggsd.execute-api.us-east-1.amazonaws.com/dev/create-user",
                    headers={"Content-Type": "application/json"},
                    json=item_data,
                )

                print({"statusCode": 200, "body": "user added to db"})
            except Exception as e:
                print({"statusCode": 500, "body": json.dumps({"error": str(e)})})

        data = response.json()

        return {"statusCode": 200, "body": json.dumps(data)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
