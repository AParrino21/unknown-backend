import json
import requests
import os


def lambda_handler(event, context):
    try:
        req_body = json.loads(event["body"])

        response = requests.post(
            # f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={os.environ["KEY"]}',
            f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyD6I6zduyTqSyF0bLt988ecg0rZcYDWWM0",
            headers={"Content-Type": "application/json"},
            json=req_body,
        )

        data = response.json()

        return {"statusCode": 200, "body": json.dumps(data)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
