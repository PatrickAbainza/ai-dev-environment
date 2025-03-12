#!/usr/bin/env python3
import os
import requests
import json

def test_brave_search():
    # API key placeholder; if required by Brave Search API, update accordingly.
    api_key = os.environ.get("BRAVE_SEARCH_API_KEY", "YOUR_API_KEY_HERE")
    query = "OpenAI"
    url = "https://search.brave.com/search"
    params = {
        "q": query,
        "format": "json"
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("Brave Search API returned response:")
        print(json.dumps(data, indent=2))
    except Exception as e:
        print("Error during Brave Search API request:", e)

if __name__ == "__main__":
    test_brave_search()