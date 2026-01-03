import os
import requests
import json
from dotenv import load_dotenv

load_dotenv("config.env")

COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_TOKEN = os.getenv("COOLIFY_TOKEN")
APP_UUID = "usooswc4wsgg48884g4kscsw"

headers = {
    "Authorization": f"Bearer {COOLIFY_TOKEN}",
    "Content-Type": "application/json"
}

def get_app_details(app_uuid):
    print(f"Getting details for App: {app_uuid}")
    resp = requests.get(f"{COOLIFY_API_URL}/applications/{app_uuid}", headers=headers)
    print(json.dumps(resp.json(), indent=2))

if __name__ == "__main__":
    import sys
    app_id = APP_UUID
    if len(sys.argv) > 1:
        app_id = sys.argv[1]
    
    get_app_details(app_id)
