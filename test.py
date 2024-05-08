import requests
import json

# Dữ liệu JSON
data = {
    "name": "string",
    "notes": "string",
    "browserType": "chrome",
    "os": "lin",
    "startUrl": "string",
    "googleServicesEnabled": False,
    "lockEnabled": False,
    "debugMode": False,
    "navigator": {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "resolution": "string",
        "language": "string",
        "platform": "string",
        "doNotTrack": False,
        "hardwareConcurrency": 0,
        "deviceMemory": 1,
        "maxTouchPoints": 0
    },
    "geoProxyInfo": {},
    "storage": {
        "local": True,
        "extensions": True,
        "bookmarks": True,
        "history": True,
        "passwords": True,
        "session": True
    },
    "proxy": {
        "mode": "http",
        "host": "66.135.11.109",
        "port": 10004,
        "username": "usrraOpc",
        "password": "passZZ1IS"
    },
    "dns": "string",
    "plugins": {
        "enableVulnerable": True,
        "enableFlash": True
    },
    "timezone": {
        "enabled": True,
        "fillBasedOnIp": True,
        "timezone": "string"
    },
    "audioContext": {
        "mode": "off",
        "noise": 0
    },
    "canvas": {
        "mode": "off",
        "noise": 0
    },
    "fonts": {
        "families": [
            "string"
        ],
        "enableMasking": True,
        "enableDomRect": True
    },
    "mediaDevices": {
        "videoInputs": 0,
        "audioInputs": 0,
        "audioOutputs": 0,
        "enableMasking": False
    },
    "webRTC": {
        "mode": "alerted",
        "enabled": True,
        "customize": True,
        "localIpMasking": False,
        "fillBasedOnIp": True,
        "publicIp": "string",
        "localIps": [
            "string"
        ]
    },
    "webGL": {
        "mode": "off",
        "getClientRectsNoise": 0,
        "noise": 0
    },
    "clientRects": {
        "mode": "off",
        "noise": 0
    },
    "webGLMetadata": {
        "mode": "mask",
        "vendor": "string",
        "renderer": "string"
    },
    "webglParams": [],
    "profile": "string",
    "googleClientId": "string",
    "updateExtensions": True,
    "chromeExtensions": [
        "string"
    ]
}

# URL của API và mã thông báo xác thực
url = 'https://api.gologin.com/browser'
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjM2ZjE0MGU1MjQzNzFiYmY4OTE2MWQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NjM5MzgyYmY2YmQ3NGRhNTMyZDkyM2UifQ.9vrXE16JbHQ6WP496dUisoLX4Khzl3G7poPz_ikrbsg',
    'Content-type': 'application/json'
}

# Gửi yêu cầu POST
response = requests.post(url, headers=headers, data=json.dumps(data))

# Xử lý phản hồi
if response.status_code == 201:
    print("Yêu cầu đã được gửi thành công!")
    id_profile = response.json()['id']
    print(id_profile)

else:
    print("Có lỗi xảy ra:", response.status_code)
