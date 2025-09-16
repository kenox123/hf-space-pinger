import requests
import os

# Get token from environment variable
HF_TOKEN = os.getenv("HF_TOKEN")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

spaces = [
    "https://huggingface.co/spaces/Kenox786/XsmartBot",
    "https://huggingface.co/spaces/Kenox786/YoutubeHindi"
]

for space in spaces:
    try:
        response = requests.get(space, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"✅ Pinged {space} successfully")
        else:
            print(f"⚠️ Pinged {space}, but got status {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to ping {space}: {e}")
