import os
import requests

# Read Hugging Face token from environment variable
HF_TOKEN = os.getenv("HF_TOKEN")

# Hugging Face Spaces to ping
spaces = [
    "Kenox786/XsmartBot",
    "Kenox786/YoutubeHindi"
]

headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}

for space in spaces:
    url = f"https://huggingface.co/spaces/{space}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"✅ Pinged {url} successfully")
        else:
            print(f"⚠️ Pinged {url}, but got status {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to ping {url}: {e}")
