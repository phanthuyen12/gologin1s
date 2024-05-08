import requests
import json

def post_to_gologin():
    url = 'https://api.gologin.com/browser?os=mac,win,lin&audioContext=mode:noise,off&canvas=mode:noise,off&webRTC=mode:alerted,disabled,real&webGL=mode:noise,off&clientRects=mode:off&webGLMetadata=mode:mask,off'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjM2ZjE0MGU1MjQzNzFiYmY4OTE2MWQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NjM5MzgyYmY2YmQ3NGRhNTMyZDkyM2UifQ.9vrXE16JbHQ6WP496dUisoLX4Khzl3G7poPz_ikrbsg',
        'Content-Type': 'application/json'
    }
    data = {
        "name": "test",
        "notes": "string",
        "browserType": "chrome",
        "os": "lin",
        "startUrl": "string",
        "googleServicesEnabled": False,
        "lockEnabled": False,
        "debugMode": False,
        "navigator": {
            "userAgent": "string",
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
        "proxyEnabled": False,
        "proxy": {
            "mode": "http",
            "host": "string",
            "port": 0,
            "username": "string",
            "password": "string"
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
            "mode": "noise",
            "getClientRectsNoise": 0,
            "noise": 0
        },
        "clientRects": {
            "mode": "noise",
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

    response = requests.post(url, headers=headers, json=data)
    print(response.text)
    # if response.status_code == 200:
    #     print("Success:", response.text)
    # else:
    #     print("Error:", response.status_code)

# Gọi hàm để thực hiện yêu cầu POST
post_to_gologin()
