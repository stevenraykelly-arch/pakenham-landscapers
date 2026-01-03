import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv("config.env")

COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_TOKEN = os.getenv("COOLIFY_TOKEN")
APP_ID = "42447" 

headers = {
    "Authorization": f"Bearer {COOLIFY_TOKEN}",
    "Content-Type": "application/json"
}

def monitor_job():
    print(f"Monitoring Deployments for ID: {APP_ID}")
    
    while True:
        resp = requests.get(f"{COOLIFY_API_URL}/deployments", headers=headers)
        deployments = resp.json()
        
        # Find the latest deployment for our app
        app_deployments = [d for d in deployments if str(d.get('application_id')) == APP_ID]
        
        if not app_deployments:
            print("No deployments found for this app.")
        else:
            latest = app_deployments[0]
            status = latest.get('status')
            print(f"Status: {status} (Updated: {latest.get('updated_at')})")
            
            if status in ['finished', 'failed', 'cancelled']:
                print(f"Final Status: {status}")
                break
        
        time.sleep(15)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        APP_ID = sys.argv[1]
    
    monitor_job()
