import requests

# Add your Hugging Face Space URLs here
spaces = [
    "https://huggingface.co/spaces/Kenox786/XsmartBot",
    "https://huggingface.co/spaces/Kenox786/YoutubeHindi"
]

for space in spaces:
    try:
        response = requests.get(space)
        print(f"✅ Pinged {space} - Status {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to ping {space}: {e}")
