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

def list_servers():
    print("Listing Servers...")
    resp = requests.get(f"{COOLIFY_API_URL}/servers", headers=headers)
    servers = resp.json()
    print(json.dumps(servers, indent=2))

if __name__ == "__main__":
    list_servers()
