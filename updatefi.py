import requests

def get_multi_browser_fingerprint(api_token, profile_ids):
    url = 'https://api.gologin.com/browser/fingerprint/multi'
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'instanceIds': profile_ids
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code ==201:
        fingerprint_data = response.json()
        print(fingerprint_data)
        return True
    else:
        print("Error:", response.status_code)
        return None

# Sử dụng hàm
api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjM2ZjE0MGU1MjQzNzFiYmY4OTE2MWQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NjM5MzgyYmY2YmQ3NGRhNTMyZDkyM2UifQ.9vrXE16JbHQ6WP496dUisoLX4Khzl3G7poPz_ikrbsg'
profile_ids = ['663a09a9814ad3fd747e65d5']
get_multi_browser_fingerprint(api_token, profile_ids)
