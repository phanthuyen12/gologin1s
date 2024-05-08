import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time
import random
import string
def check_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        response = requests.get("https://geo.myip.link/", proxies=proxies, timeout=10)
        if response.status_code == 200:
            timezone = response.json()
            return timezone['timezone']
        else:
            return False
    except Exception as e:
        print(f"Không thể kết nối đến proxy: {e}")
        return False
class GoLoginAPI:
    def __init__(self, api_token,host= None,port= None,username= None,passworld= None,timezone= None):
        self.api_token = api_token
        self.host = host
        self.port = port
        self.username = username
        self.passworld = passworld
        self.timezone = timezone
        
        self.base_url = 'https://api.gologin.com'
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-type': 'application/json'
        }
        self.data = {
       
    "name": "phangiathuyen",
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
        "local": False,
        "extensions": False,
        "bookmarks": False,
        "history": False,
        "passwords": False,
        "session": False
    },
    "proxyEnabled": False,
    "proxy": {
        "mode": "http",
        "host": self.host,
        "port": self.port,
        "username": self.username,
        "password": self.passworld
    },
    "dns": "string",
    "plugins": {
        "enableVulnerable": False,
        "enableFlash": False
    },
    "timezone": {
        "enabled": True,
        "fillBasedOnIp": False,
        "timezone": self.timezone
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
        "enableMasking": False,
        "enableDomRect": False
    },
    "mediaDevices": {
        "videoInputs": 0,
        "audioInputs": 0,
        "audioOutputs": 0,
        "enableMasking": False
    },
    "webRTC": {
        "mode": "alerted",
        "enabled": False,
        "customize": False,
        "localIpMasking": False,
        "fillBasedOnIp": False,
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
    def get_browser_fingerprint(self, os='win', resolution='1680x1050', output_file='fingerprint_data1.json'):
        url = 'https://api.gologin.com/browser/fingerprint'
        headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }
        params = {
            'os': os,
            'resolution': resolution
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            fingerprint_data = response.json()
            # Replace keys in fingerprint_data with self.data if they match
            for key, value in fingerprint_data.items():
                if key in self.data:
                    fingerprint_data[key] = self.data[key]
            with open(output_file, 'w') as file:
                json.dump(fingerprint_data, file, indent=4)
            print(f"Data saved to {output_file}")
        else:
            print("Error:", response.status_code)
    def create_browser_profile(self):
        url = f'https://api.gologin.com/browser?os=mac,win,lin&audioContext=mode:noise,off&canvas=mode:noise,off&webRTC=mode:alerted,disabled,real&webGL=mode:noise,off&clientRects=mode:off&webGLMetadata=mode:mask,off'
        response = requests.post(url, headers=self.headers, data=json.dumps(self.data))
        if response.status_code == 201:
            print("Yêu cầu đã được gửi thành công!")
            return response.json().get('id')
        else:
            print("Có lỗi xảy ra:", response.status_code)
            return None

    def start_profile(self, profile_id):
        url = f'http://localhost:36912/browser/start-profile'
        data_start = {
            "profileId": profile_id,
            "sync": True
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data_start))
        if response.status_code == 200:
            print("Yêu cầu đã được gửi thành công!")
            return response.json()['wsUrl']
        else:
            print("Có lỗi xảy ra:", response.status_code)
            return None

    def stop_profile(self, profile_id):
        url = f'http://localhost:36912/browser/stop-profile'
        data_stop = {
            "profileId": profile_id
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data_stop))
        if response.status_code == 204:
            print("Yêu cầu đã được gửi thành công!")
            return True
        else:
            print("Có lỗi xảy ra:", response.status_code)
            return None

    def delete_profile(self, profile_id):
        url = f'{self.base_url}/browser/{profile_id}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print("Yêu cầu đã được gửi thành công!")
            return True
        else:
            print("Có lỗi xảy ra:", response.status_code)
            return None
    def generate_random_name(self):
        # Danh sách ký tự tiếng Việt không dấu
        vietnamese_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Danh sách tên người Việt Nam
        vietnamese_names = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Huynh", "Phan", "Vu", "Vo", "Dang", "Bui", "Do", "Ho", "Ngo", "Duong", "Ly"]

        # Chọn ngẫu nhiên một tên từ danh sách
        first_name = random.choice(vietnamese_names)

        # Sinh ngẫu nhiên một số có 5 chữ số
        random_number = ''.join(random.choices(string.digits, k=5))

        # Sinh ngẫu nhiên một chuỗi chữ cái có 5 ký tự từ danh sách ký tự tiếng Việt không dấu
        random_letters = ''.join(random.choices(vietnamese_characters, k=5))

        # Kết hợp tên, số và chuỗi chữ cái lại với nhau
        random_name = f"{first_name}{random_number}{random_letters}"

        return random_name
    def initialize_driver(self, ws_url):
        # Thêm command_line vào trong hàm
        command_line = [
            "--disable-encryption",
            "--donut-pie=undefined",
            "--webrtc-ip-handling-policy=default_public_interface_only",
            "--font-masking-mode=2",
            "--load-extension=",
            "--restore-last-session",
            "--app=https://signup.live.com/"  # Đây là nơi bạn muốn thêm command_line
        ]

        chrome_options = Options()
        chrome_options.add_experimental_option('debuggerAddress', ws_url)
        # Bỏ dòng này vì đã thêm "--app" vào command_line
        # chrome_options.add_argument("--app=https://signup.live.com/")
        for arg in command_line:
            chrome_options.add_argument(arg)
        
        service = Service(executable_path='C:\\Users\\thuye\\Downloads\\chromedriver 122\\chromedriver-win64\\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    def get_multi_browser_fingerprint(self, profile_ids):
        url = 'https://api.gologin.com/browser/fingerprints'
        headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "resolution": "1280x720",
            "language": "en-US",
            "browsersIds": [
                profile_ids
            ]
        }

        response = requests.patch(url, headers=headers, json=data)

        if response.status_code ==200:
            fingerprint_data = response.json()
            print(fingerprint_data)
            return True
        else:
            print("Error:", response.status_code)
            return None

# Sử dụng lớp GoLoginAPI
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjM2ZjE0MGU1MjQzNzFiYmY4OTE2MWQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NjM5MzgyYmY2YmQ3NGRhNTMyZDkyM2UifQ.9vrXE16JbHQ6WP496dUisoLX4Khzl3G7poPz_ikrbsg'     
proxy ='116.106.44.152:27309'  
timezone = check_proxy(proxy)
print(timezone)

# Sử dụng phương thức split để cắt chuỗi proxy thành hai phần
proxy_parts = proxy.split(':')

# Lấy hai phần ra khỏi proxy_parts
host = proxy_parts[0]
port = proxy_parts[1]

print(host)  # In ra phần 1
print(port)  # In ra phần 2

apigologin = GoLoginAPI(token,host,port,None,None,timezone)
profile_id = apigologin.create_browser_profile()
print(profile_id)
# id_profile = [f'{profile_id}']

check = apigologin.get_multi_browser_fingerprint(profile_id)
print(check)
if check == True:
    start_profile = apigologin.start_profile(profile_id)
    print(start_profile)
    time.sleep(2)
    start_profile = start_profile.split("ws://")[1]
    print(start_profile)

    time.sleep(2)
    driver = apigologin.initialize_driver(start_profile)
    # driver.get('https://www.google.com/')
    # driver.get("https://accounts.google.com/SignUp")
    driver.get("https://www.youtube.com/")
    time.sleep(1)
    try:
        sign_in_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Đăng nhập")))
        sign_in_button.click()
        time.sleep(2)
        sign_in_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "n3Clv")))
        sign_in_button.click()
        time.sleep(2)
        sign_in_buttons = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "VfPpkd-StrnGf-rymPhb-ibnC6b")))

        # Click on the first matching element
        if sign_in_buttons:
            sign_in_buttons[0].click()
        else:
            print("No sign-in buttons found.")
        firstName = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "firstName")))

        # Chuỗi cần gửi
        input_text = "thanh"

        # Gửi từng ký tự một
        for char in input_text:
            firstName.send_keys(char)
            time.sleep(0.1)
        time.sleep(2)

        lastName = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "lastName")))

        # Chuỗi cần gửi
        input_text = "lam"

        # Gửi từng ký tự một với khoảng thời gian chờ 2 giây
        for char in input_text:
            lastName.send_keys(char)
            time.sleep(0.1)
        time.sleep(2)

        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d")))
        element.click()
        month_select = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "month")))
        month_options = Select(month_select)
        time.sleep(2)

        month_options.select_by_value(str(random.randint(1, 12)))
        day_select = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "day")))
        day_select.send_keys(str(random.randint(1, 31)))
        time.sleep(2)

        year_select = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "year")))
        year_select.send_keys(str(random.randint(1980, 2000)))
        time.sleep(2)

        gender_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "gender")))
        gender_options = Select(gender_element)
        gender_options.select_by_value(str(random.randint(1, 3)))
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "birthdaygenderNext")))
        element.click()
        time.sleep(2)

        if "Pick a Gmail address or create your own" in driver.page_source:
            click_user = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "selectionc3")))
            click_user.click()
            time.sleep(1)
            click_user = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "TNTaPb")))
            click_user.click()

        else:
            time.sleep(2)
            if "Cách bạn đăng nhập" in driver.page_source:
                print('Use your existing email')
                print(apigologin.generate_random_name())
                email = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME, "whsOnd")))
                email.send_keys(apigologin.generate_random_name())
                
                
                click_next = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "VfPpkd-dgl2Hf-ppHlrf-sM5MNb")))
                click_next.click()
            else:
                if "Sử dụng email hiện tại của bạn" in driver.page_source:
                    # print("Cách bạn đăng nhập")
                    # username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "Username")))
                    # email = apigologin.generate_random_name()+"@gmail.com"
                    # print(email)
                    # username.send_keys(email)
                    # element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-dgl2Hf-ppHlrf-sM5MNb")))
                    # element.click()
                    click_next = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "dMNVAe")))
                    click_next.click()
                    if "Chọn địa chỉ Gmail của bạn" in driver.page_source:
                        print('chon gia tri 31')
                        click_user = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "selectionc3")))
                        click_user.click()
                        click_next = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "TNTaPb")))
                        click_next.click()
                    else:
                
                        email = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME, "whsOnd")))
                        email.send_keys(apigologin.generate_random_name())
                    
                    
                        click_next = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "VfPpkd-dgl2Hf-ppHlrf-sM5MNb")))
                        click_next.click()
                else:
                    
                    print('chon gia tri 3')
                    click_user = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "selectionc3")))
                    click_user.click()
                    click_next = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "TNTaPb")))
                    click_next.click()
        password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "Passwd")))

        # Chuỗi cần gửi
        input_text = "thuyen200412"

        # Gửi từng ký tự một với khoảng thời gian chờ 0.1 giây
        for char in input_text:
            password.send_keys(char)
            time.sleep(0.1)
        time.sleep(2)

        password2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "PasswdAgain")))

        # Chuỗi cần gửi
        input_text = "thuyen200412"

        # Gửi từng ký tự một với khoảng thời gian chờ 0.1 giây
        for char in input_text:
            password2.send_keys(char)
            time.sleep(0.1)
        createpasswordNext = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "createpasswordNext")))
        time.sleep(2)

        createpasswordNext.click()
        print('dai doan 1')
        if "Add recovery email" in driver.page_source:
            print('dai doan mail')
            click_recovery = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "VfPpkd-RLmnJb")))
            click_recovery.click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            click_recovery = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "GERNzc")))
            click_recovery.click()
            click_recovery = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "TNTaPb")))
            click_recovery.click()
            print('dai doan 3')
            button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-id='ssJRIf']")))


            # Nhấp vào nút
            button.click()
        else:
            print('dai doan 4')
    except TimeoutException as e:
        print("TimeoutException:", e.msg)
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print('test')
        time.sleep(1000000)  # Sleep for 10 seconds for review
