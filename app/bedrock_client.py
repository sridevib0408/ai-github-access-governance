import boto3
import json

bedrock = boto3.client("bedrock-runtime")


MODEL_ID = "anthropic.claude-v2"


def analyze_access_request(request_data):
    prompt = build_prompt(request_data)

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 300,
            "temperature": 0.2
        })
    )

    result = json.loads(response["body"].read())

    return result


def build_prompt(request_data):
    return f"""
You are a GitHub access governance risk analyzer.

Analyze this request:

Repository: {request_data['repo']}
Requested Duration: {request_data['duration']}
Reason: {request_data['reason']}

Return JSON in this format:

{{
  "risk_score": "Low | Medium | High",
  "recommendation": "Approve | Reject",
  "recommended_duration": "value",
  "security_concerns": ["list"]
}}
"""
