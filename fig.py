import requests
import json

def get_browser_fingerprint(api_token, os='win', resolution='1680x1050', output_file='fingerprint_data1.json'):
    url = 'https://api.gologin.com/browser/fingerprint'
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    params = {
        'os': os,
        'resolution': resolution
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        fingerprint_data = response.json()
        with open(output_file, 'w') as file:
            json.dump(fingerprint_data, file, indent=4)
        print(f"Data saved to {output_file}")
    else:
        print("Error:", response.status_code)

# Sử dụng hàm
api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjM2ZjE0MGU1MjQzNzFiYmY4OTE2MWQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NjM5MzgyYmY2YmQ3NGRhNTMyZDkyM2UifQ.9vrXE16JbHQ6WP496dUisoLX4Khzl3G7poPz_ikrbsg'
get_browser_fingerprint(api_token)
