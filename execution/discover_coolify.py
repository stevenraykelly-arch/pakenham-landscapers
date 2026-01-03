import os
import requests
from dotenv import load_dotenv

load_dotenv("config.env")

COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_TOKEN = os.getenv("COOLIFY_TOKEN")

headers = {
    "Authorization": f"Bearer {COOLIFY_TOKEN}",
    "Content-Type": "application/json"
}

def discover_coolify():
    print("Listing Projects...")
    resp = requests.get(f"{COOLIFY_API_URL}/projects", headers=headers)
    projects = resp.json()
    for p in projects:
        print(f"\n- Project: {p.get('name')} (UUID: {p.get('uuid')})")
        for env in p.get('environments', []):
            print(f"  - Env: {env.get('name')} (ID: {env.get('id')})")

if __name__ == "__main__":
    discover_coolify()
