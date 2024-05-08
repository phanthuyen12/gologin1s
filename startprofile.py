import requests
import json
def start_profile(profile_id, api_token, app_url):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-type': 'application/json'
    }
    url = 'http://localhost:36912/browser/start-profile'

    data_start = {
        "profileId": profile_id,
        "sync": True,
        "--app": app_url  # Thêm app_url vào dữ liệu yêu cầu
    }

    response = requests.post(url, headers=headers, data=json.dumps(data_start))

    if response.status_code == 200:
        print("Yêu cầu đã được gửi thành công!")
        return response.json()['wsUrl']
    else:
        print("Có lỗi xảy ra:", response.status_code)
        return None

id = "663b236e1e1bf7daeabe6af0"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjM2ZjE0MGU1MjQzNzFiYmY4OTE2MWQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NjM5MzgyYmY2YmQ3NGRhNTMyZDkyM2UifQ.9vrXE16JbHQ6WP496dUisoLX4Khzl3G7poPz_ikrbsg"
app_url = "https://signup.live.com/"  # URL của ứng dụng bạn muốn mở
ws_url = start_profile(id, api_token, app_url)
print(ws_url)