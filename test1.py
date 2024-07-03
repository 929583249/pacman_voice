import requests

# Define the URL and the payload for the POST request
url = 'http://127.0.0.1:9966/tts'
data = {
    "text": "this is test API ",
    "prompt": "",
    "voice": "2222",
    "temperature": 0.3,
    "top_p": 0.7,
    "top_k": 20,
    "refine_max_new_token": "384",
    "infer_max_new_token": "2048",
    "skip_refine": 0,
    "is_split": 1,
    "custom_voice": 42
}

# Send the POST request
response = requests.post(url, data=data)

# Check if the response was successful
if response.status_code == 200:
    response_data = response.json()
    if response_data.get('code') == 0:
        print("API call successful!")
        print("Audio files:", response_data['audio_files'])
    else:
        print("API call failed with error:", response_data.get('msg'))
else:
    print("Failed to reach the API. Status code:", response.status_code)