# main.py
import os
import boto3
import json
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
    prompt: str

# Retrieve API keys from AWS Secrets Manager
def get_secret(secret_name: str) -> str:
    if os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=os.environ["AWS_REGION"]
        )
        try:
            secret_value = client.get_secret_value(SecretId=secret_name)
            return json.loads(secret_value['SecretString'])
        except Exception as e:
            raise HTTPException(500, f"Secret retrieval failed: {str(e)}")
    else:  # Local development
        return {
            "PERPLEXITY_KEY": os.environ["PERPLEXITY_KEY"],
            "AWS_KEY": os.environ["AWS_KEY"]
        }

@app.post("/predict")
async def predict(request: PredictionRequest):
    secrets = get_secret("finance-tracker/secrets")
    
    # Example: Call Perplexity API
    import requests
    headers = {
        "Authorization": f"Bearer {secrets['PERPLEXITY_KEY']}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(
        "https://api.perplexity.ai/chat/completions",
        json={
            "model": "sonar-medium",
            "messages": [{"role": "user", "content": request.prompt}]
        },
        headers=headers
    )
    
    return {"prediction": response.json()["choices"][0]["message"]["content"]}

handler = Mangum(app)
