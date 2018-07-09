# 练习Python访问互联网的API

import requests
import json

base_url = "https://api.github.com"

def get_url(url):

    return base_url+url

resp = requests.get(get_url("/users?page=0&per_page=1'"))

result = resp.text

print(resp.url , "返回结果为:" , json.dumps(result)) 