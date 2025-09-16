import requests

# Add your actual Hugging Face Spaces below
spaces = [
   "https://huggingface.co/spaces/Kenox786/XsmartBot",
    "https://huggingface.co/spaces/Kenox786/YoutubeHindi"
]

for space in spaces:
    try:
        response = requests.get(space, timeout=10)
        if response.status_code == 200:
            print(f"✅ Pinged {space} successfully")
        else:",
    "https://huggingface.co/spaces/Kenox786/YoutubeHindi"
            print(f"⚠️ Pinged {space}, but got status {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to ping {space}: {e}")

"https://huggingface.co/spaces/Kenox786/XsmartBot
