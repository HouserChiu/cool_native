# coding: utf-8

import requests
import pprint
import json
import time
import hashlib
import base64

def get_x_app_token():
    timestamp = int(time.time())
    md5_timestamp = hashlib.md5(str(timestamp).encode("utf-8")).hexdigest()
    encrypt_str = "token://com.coolapk.market/c67ef5943784d09750dcfbb31020f0ab?" + md5_timestamp + "$" + "6c72aa7b-7a76-36cd-a543-8c1afbdca24e" + "&" + "com.coolapk.market"
    first_md5_result = base64.b64encode(encrypt_str.encode('utf-8'))
    second_md5 = hashlib.md5(str(first_md5_result, 'utf-8').encode('utf-8')).hexdigest()
    x_app_token = second_md5 + "6c72aa7b-7a76-36cd-a543-8c1afbdca24e" + hex(timestamp)

    return x_app_token

def get_data():
    url = "https://api.coolapk.com/v6/main/indexV8?page=1&firstItem=21672183"
    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; 1605-A01 Build/NMF26F) (#Build; 360; 1605-A01; V091; 7.1.1) +CoolMarket/10.3.1-2006162',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Sdk-Int': '25',
        'X-Sdk-Locale': 'zh-CN',
        'X-App-Id': 'com.coolapk.market',
        'X-App-Token': '%s' % get_x_app_token(),
        'X-App-Version': '10.3.1',
        'X-App-Code': '2006162',
        'X-Api-Version': '10',
        'X-App-Device': 'EDMB1SNwYTMgsDM2MDI7AjNzAyO3QjO2QkOBNkOGVjODFkO0cDI7YDMzUTM3cTM5YjMwAjN0AyO5YzN3gDMyMDMwkDNyYDOgsDMkZmZlhjY4YGMjNWM1EGN',
        'X-Dark-Mode': '0',
        'Host': 'api.coolapk.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }
    res = json.loads(requests.get(url, headers=headers, verify=False).text)
    pprint.pprint(res)

get_data()



