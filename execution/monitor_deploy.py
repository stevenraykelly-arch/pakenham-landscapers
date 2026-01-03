import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv("config.env")

COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_TOKEN = os.getenv("COOLIFY_TOKEN")
APP_UUID = "usooswc4wsgg48884g4kscsw"

headers = {
    "Authorization": f"Bearer {COOLIFY_TOKEN}",
    "Content-Type": "application/json"
}

def monitor_deployment():
    print(f"Checking status for App: {APP_UUID}")
    
    # Trigger deployment just in case it didn't auto-start
    print("Triggering deployment...")
    resp = requests.get(f"{COOLIFY_API_URL}/applications/{APP_UUID}/deploy", headers=headers)
    print(f"Trigger Response: {resp.status_code}")
    
    # Wait and check deployments
    for i in range(10):
        resp = requests.get(f"{COOLIFY_API_URL}/applications/{APP_UUID}/deployments", headers=headers)
        deployments = resp.json()
        if deployments:
            latest = deployments[0]
            print(f"Current Status: {latest.get('status')} (ID: {latest.get('deployment_uuid')})")
            if latest.get('status') in ['finished', 'failed']:
                break
        else:
            print("No deployments found yet...")
        time.sleep(10)

if __name__ == "__main__":
    monitor_deployment()
