import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv("config.env")

COOLIFY_API_URL = os.getenv("COOLIFY_API_URL")
COOLIFY_TOKEN = os.getenv("COOLIFY_TOKEN")
GITHUB_APP_UUID = "dgw0ccww4sogowscgo88gg4s" 
SERVER_UUID = "d0s0kccs0wgw0gcokog08g04"

headers = {
    "Authorization": f"Bearer {COOLIFY_TOKEN}",
    "Content-Type": "application/json"
}

def provision_factory(project_name, repo_path):
    print(f"Provisioning Factory for: {project_name}")
    
    resp = requests.get(f"{COOLIFY_API_URL}/projects", headers=headers)
    projects = resp.json()
    project = next((p for p in projects if p.get('name') == project_name), None)
    
    if project:
        project_uuid = project.get('uuid')
    else:
        payload = {"name": project_name}
        resp = requests.post(f"{COOLIFY_API_URL}/projects", headers=headers, json=payload)
        resp.raise_for_status()
        project = resp.json()
        project_uuid = project.get('uuid')
    
    time.sleep(2)
    resp = requests.get(f"{COOLIFY_API_URL}/projects/{project_uuid}", headers=headers)
    project_detail = resp.json()
    envs = project_detail.get('environments', [])
    production_env_uuid = next((e.get('uuid') for e in envs if e.get('name') == 'production'), None)
    
    # Required fields based on errors
    app_payload = {
        "name": "production",
        "project_uuid": project_uuid,
        "environment_uuid": production_env_uuid,
        "server_uuid": SERVER_UUID,
        "github_app_uuid": GITHUB_APP_UUID,
        "git_repository": repo_path,
        "git_branch": "main",
        "build_pack": "nixpacks",
        "ports_exposes": "3000"
    }
    
    print(f"Sending request to create application...")
    resp = requests.post(f"{COOLIFY_API_URL}/applications/private-github-app", headers=headers, json=app_payload)
    if resp.status_code not in [200, 201]:
        print(f"Error creating app: {resp.text}")
        return
    
    app = resp.json()
    app_uuid = app.get('uuid')
    print(f"Created Application: {app_uuid}")
    
    # NEW: Domain Handshake Prompt & Instructions
    print("\n" + "="*50)
    print("🚀 INFRASTRUCTURE READY!")
    print("="*50)
    print(f"Temporary URL: http://{app_uuid}.170.64.136.227.sslip.io")
    print("\n--- 🌐 CUSTOM DOMAIN & HTTPS SETUP ---")
    print(f"1. Point your domain's A Record to: 170.64.136.227")
    print("2. Once pointed, you can enable HTTPS/SSL by updating the FQDN.")
    print("="*50)
    
    # Check for non-interactive flag
    import sys
    if "--non-interactive" in sys.argv:
        print("\nSkipping custom domain handshake (Non-Interactive Mode).")
        print(f"Note: You can run 'python execution/handshake_domain.py {app_uuid}' later.")
        return app_uuid

    choice = input("\nWould you like to configure a custom domain right now? (y/n): ").lower()
    if choice == 'y':
        import subprocess
        subprocess.run(["python", "execution/handshake_domain.py", app_uuid])
    else:
        print("\nNote: You can run 'python execution/handshake_domain.py " + app_uuid + "' at any time to add a domain.")
    
    return app_uuid

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        p_name = sys.argv[1]
        r_path = sys.argv[2]
        provision_factory(p_name, r_path)
    else:
        # Fallback to interactive/default if no args
        provision_factory("St Kilda Window Cleaning", "stevenraykelly-arch/st-kilda-window-cleaner")
