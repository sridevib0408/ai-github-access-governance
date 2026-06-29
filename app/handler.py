import json
import boto3
import os
from urllib.parse import parse_qs

stepfunctions = boto3.client("stepfunctions")

STATE_MACHINE_ARN = os.environ.get("STATE_MACHINE_ARN")


def lambda_handler(event, context):
    try:
        body = event.get("body", "")
        parsed = parse_qs(body)

        text = parsed.get("text", [""])[0]

        request_data = parse_command(text)

        response = stepfunctions.start_execution(
            stateMachineArn=STATE_MACHINE_ARN,
            input=json.dumps(request_data)
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Access request submitted successfully",
                "executionArn": response["executionArn"]
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }


def parse_command(text):
    """
    Example:
    repo=payments-api duration=4h reason=urgent prod hotfix
    """
    parts = text.split()

    data = {}

    for part in parts:
        if "=" in part:
            key, value = part.split("=", 1)
            data[key] = value

    return {
        "repo": data.get("repo"),
        "duration": data.get("duration"),
        "reason": data.get("reason")
    }
