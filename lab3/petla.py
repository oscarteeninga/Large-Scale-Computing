import requests
import time
import base64

def get_proxy():
    creds_file = open("usercred.p12", "r").read()
    return base64.b64encode(creds_file)

def get_data(cmd):
    return '{"host": "zeus.cyfronet.pl", "command": "{cmd}"}'

def get_header():
    return """{
        Content-Type:application/json,
        PROXY:{proxy}
    }"""

url = "https://submit.plgrid.pl/api/process"
responses = {}
commands = ["pwd", "ls", "ps", "man", "echo"]
proxy = get_proxy()


for cmd in commands:
    responses[cmd] = requests.post(url, headers=get_header(), data=get_data(cmd))

for _ in range(100):
    time.sleep(10)
    for cmd in commands:
        print(responses[cmd].status_code)
