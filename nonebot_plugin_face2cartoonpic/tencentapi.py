# -*- coding: utf8 -*-
import base64
import hashlib
import hmac
import time

import requests
from .config import FaceCartoonPic_config


class timestamp:
  def get_ts():
    ts = time.time()
    ts = int(ts)
    return ts

  def get_nonce(ts):
    nc = ts + 1
    return nc

def get_redirect_url(url):
    # 重定向前的链接

    # 请求头，这里我设置了浏览器代理
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    # 请求网页
    response = requests.get(url, headers=headers)
    # 返回重定向后的网址
    return response.__dict__

url = "https://ft.tencentcloudapi.com"
SecretId = FaceCartoonPic_config.Secret_Id
SecretKey = FaceCartoonPic_config.Secret_Key
Action = "FaceCartoonPic"

Version ="2020-03-04"
Region="ap-shanghai"


secret_id = SecretId
secret_key = SecretKey

#############这是tx云Signature获取
def get_string_to_sign(method, endpoint, params):
    s =  method + endpoint + "/?"
    query_str = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str

def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str)
##############

async def get_pic(pic_input): 

    endpoint = "ft.tencentcloudapi.com"
    data = {
        'Action' : Action,
        'Url' : pic_input,

        'Nonce' : timestamp.get_nonce(timestamp.get_ts()),
        'RspImgType':'url',
        'Region' : Region,
        'SecretId' : secret_id,
        'Timestamp' : timestamp.get_ts(), # int(time.time())
        'Version': Version
    }
    s = get_string_to_sign("GET", endpoint, data)
    try:
      data["Signature"] = sign_str(secret_key, s, hashlib.sha1)
    except:
      print('没有设置Secret_key')
      return 1
    print("key输入成功\n证书签名如下\n["+str(data["Signature"])+"] ")

    resp =  requests.get("https://" + endpoint, params=data)
    print(resp)
    msg_raw =  resp.json()
    try: 
        msg = msg_raw["Response"]["ResultUrl"]
        print(msg)
    except:
        print("输入的不是人像")
        return 2
    return msg
