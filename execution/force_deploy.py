import sys
import requests
import time

def trigger_deploy(webhook_uuid):
    # Coolify Webhook Structure
    url = f"https://app.coolify.io/api/v1/deploy?uuid={webhook_uuid}&force=true"
    
    print(f"Triggering deployment for UUID: {webhook_uuid}...")
    try:
        # Try standard GET without auth (Public Webhook)
        response = requests.get(url) 
        # Common Coolify webhook is: https://[domain]/api/v1/deploy?uuid=...
        # Let's try standard GET
        
        if response.status_code == 200:
            print(f"Deployment triggered successfully: {response.json()}")
        else:
            # Try POST
            response = requests.post(url)
            if response.status_code == 200:
                 print(f"Deployment triggered successfully (POST): {response.json()}")
            else:
                print(f"Failed to trigger deployment. Status: {response.status_code}, Body: {response.text}")
                
    except Exception as e:
        print(f"Error triggering deployment: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python force_deploy.py <webhook_uuid>")
        sys.exit(1)
        
    webhook_uuid = sys.argv[1]
    trigger_deploy(webhook_uuid)
