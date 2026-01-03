import os
import requests
import json
from dotenv import load_dotenv

load_dotenv("config.env")

COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_TOKEN = os.getenv("COOLIFY_TOKEN")

headers = {
    "Authorization": f"Bearer {COOLIFY_TOKEN}",
    "Content-Type": "application/json"
}

def list_all_deployments():
    print("Listing All Deployments...")
    resp = requests.get(f"{COOLIFY_API_URL}/deployments", headers=headers)
    print(json.dumps(resp.json(), indent=2))

if __name__ == "__main__":
    list_all_deployments()
