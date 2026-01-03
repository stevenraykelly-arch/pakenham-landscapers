import os
import requests
import json
import sys
from dotenv import load_dotenv

load_dotenv("config.env")

COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_TOKEN = os.getenv("COOLIFY_TOKEN")

def list_app_deployments(app_uuid):
    headers = {
        "Authorization": f"Bearer {COOLIFY_TOKEN}",
        "Content-Type": "application/json"
    }
    resp = requests.get(f"{COOLIFY_API_URL}/applications/{app_uuid}/deployments", headers=headers)
    print(json.dumps(resp.json(), indent=2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        list_app_deployments(sys.argv[1])
    else:
        print("Usage: python list_app_deployments.py <app_uuid>")
