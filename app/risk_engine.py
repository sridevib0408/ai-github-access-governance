import json
from app.bedrock_client import analyze_access_request


def evaluate_request(request_data):
    response = analyze_access_request(request_data)

    parsed_response = parse_bedrock_response(response)

    return {
        "repo": request_data["repo"],
        "duration": request_data["duration"],
        "reason": request_data["reason"],
        "risk_score": parsed_response.get("risk_score"),
        "recommendation": parsed_response.get("recommendation"),
        "recommended_duration": parsed_response.get("recommended_duration"),
        "security_concerns": parsed_response.get("security_concerns", [])
    }


def parse_bedrock_response(response):
    try:
        completion = response.get("completion", "")
        return json.loads(completion)
    except Exception:
        return {
            "risk_score": "Unknown",
            "recommendation": "Manual Review",
            "recommended_duration": None,
            "security_concerns": ["Unable to parse AI response"]
        }
