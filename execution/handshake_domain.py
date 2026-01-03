import os
import requests
import json
import sys
from dotenv import load_dotenv

load_dotenv("config.env")

COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_TOKEN = os.getenv("COOLIFY_TOKEN")
SERVER_IP = "170.64.136.227"

def handshake_domain(app_uuid):
    print("\n--- 🌐 CUSTOM DOMAIN HANDSHAKE ---")
    print(f"Step 1: Point your domain's A Record to: {SERVER_IP}")
    print("Step 2: Wait for DNS propagation (can take 1-5 minutes).")
    
    domain = input("\n👉 Please enter your custom domain (e.g., mysite.com) or press Enter to skip: ").strip()
    
    if not domain:
        print("Skipping custom domain configuration.")
        return

    if not domain.startswith("http"):
        # We always prefer HTTPS for production
        domain = f"https://{domain}"

    print(f"Configuring Coolify for: {domain}...")
    
    headers = {
        "Authorization": f"Bearer {COOLIFY_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "fqdn": domain
    }
    
    try:
        resp = requests.patch(f"{COOLIFY_API_URL}/applications/{app_uuid}", headers=headers, json=payload)
        if resp.status_code == 200:
            print(f"✅ Success! Coolify is now requesting SSL for {domain}.")
            print("The site should be live and secure in about 60 seconds.")
        else:
            print(f"❌ Error updating domain: {resp.text}")
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python handshake_domain.py <app_uuid>")
    else:
        handshake_domain(sys.argv[1])
