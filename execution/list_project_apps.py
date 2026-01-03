import os
import requests
import json
import sys
from dotenv import load_dotenv

load_dotenv("config.env")

COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_TOKEN = os.getenv("COOLIFY_TOKEN")

def list_project_apps(project_uuid):
    headers = {
        "Authorization": f"Bearer {COOLIFY_TOKEN}",
        "Content-Type": "application/json"
    }
    resp = requests.get(f"{COOLIFY_API_URL}/projects/{project_uuid}", headers=headers)
    project = resp.json()
    envs = project.get('environments', [])
    for env in envs:
        print(f"\nEnvironment: {env.get('name')} (UUID: {env.get('uuid')})")
        print(json.dumps(env, indent=2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        list_project_apps(sys.argv[1])
    else:
        print("Usage: python list_project_apps.py <project_uuid>")
