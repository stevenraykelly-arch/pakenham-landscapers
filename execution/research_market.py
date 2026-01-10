import json
import os
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python research_market.py <Trade> <Location> [BusinessName]")
        sys.exit(1)

    trade = sys.argv[1]
    location = sys.argv[2]
    business_name = sys.argv[3] if len(sys.argv) > 3 else "My Business"
    
    output_path = ".tmp/market_data.json"
    
    # 1. Define the Search Strategy
    strategy = {
        "context": f"Researching {trade} in {location}",
        "search_queries": [
            f"Best {trade} in {location} reviews",
            f"{trade} services {location}",
            f"{trade} {location} competitors",
            f"common problems with {trade} in {location}"
        ],
        "extraction_goals": {
            "competitors": "Top 3 rated competitors with URLs",
            "services": "List of core services and niche services offered by them",
            "keywords": "SEO keywords they target (H1/H2 tags)",
            "gaps": "What are they missing? (e.g. no pricing, bad mobile site)"
        },
        "output_schema": {
            "competitors": [
                {"name": "", "url": "", "services": [], "pros": "", "cons": ""}
            ],
            "common_services": [],
            "niche_services": [],
            "visual_style": {"colors": [], "imagery": ""},
            "geo_keywords": []
        }
    }

    # 2. Check if data already exists
    if os.path.exists(output_path):
        print(f"--- Market Data Exists at {output_path} ---")
        try:
            with open(output_path, 'r') as f:
                data = json.load(f)
                print(json.dumps(data, indent=2))
        except:
             print("Error reading existing data.")
        return

    # 3. Output Instructions for the Agent
    print("--- AUTOMATED RESEARCH INSTRUCTIONS ---")
    print(json.dumps(strategy, indent=2))
    print("\n[AGENT ACTION REQUIRED]")
    print(f"1. Execute 'search_web' for the queries above.")
    print(f"2. Synthesize findings into the 'output_schema'.")
    print(f"3. Save the JSON to '{output_path}'.")

if __name__ == "__main__":
    main()
