# ai-github-access-governance
An AI-powered temporary GitHub elevated access governance platform built using Python and AWS serverless services.

## Problem

Engineering teams often require temporary elevated GitHub repository access for emergency fixes, production incidents, or urgent pull request merges. Traditional approval processes are manual, slow, and lack risk intelligence.

## Solution

This project automates GitHub access governance by integrating Slack, AWS Step Functions, Bedrock, DynamoDB, and GitHub APIs.

The platform:

* Accepts access requests via Slack slash commands
* Uses Amazon Bedrock for AI-based risk analysis
* Generates approval recommendations
* Stores requests with TTL-based expiration
* Grants temporary repository access
* Automatically revokes access after expiration

## Architecture

Slack → API Gateway → Lambda → Step Functions → Bedrock → DynamoDB → GitHub API → EventBridge Scheduler → Revoke Lambda

## Tech Stack

* Python
* AWS Lambda
* API Gateway
* Step Functions
* Amazon Bedrock
* DynamoDB
* EventBridge
* GitHub API
* Slack API
* AWS SAM

## Features

* AI-powered risk scoring
* Temporary access governance
* Approval workflows
* TTL-based automatic revocation
* Audit logging
* Compliance tracking
* Slack notifications
