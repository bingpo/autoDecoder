# -*- coding:utf-8 -*-
# author:f0ngf0ng

# -*- coding:utf-8 -*-
# author:f0ngf0ng

from flask import Flask,Response,request
from pyDes import *
import base64,re
app = Flask(__name__)

@app.route('/encode',methods=["POST"])
def encrypt():
    body = request.form.get('dataBody')  # 获取  post 参数,不可更改 必需必需必需
    headers = request.form.get('dataHeaders')  # 获取  post 参数  可选

#被#隔开的部分是处理header头的部分
################################################################
################################################################
    if headers != None: # 开启了请求头加密
        print(headers)
        param_uri = re.findall(r'[POST|GET|PUT] /(.*?)[ ]', headers)[0] # 提取请求的uri及参数
        print(param_uri)
        param_uri_total = param_uri + "&b=22222222"
        headers = headers.replace(param_uri, param_uri_total, 1) # 用修改后的uri替换原参数中的uri
        headers = headers + "aaaa:bbbb\r\n"
        headers = headers + "f0ng:test"
        print(headers + "\r\n\r\n\r\n\r\n" + body)
        return headers + "\r\n\r\n\r\n\r\n" + body # 返回值为固定格式，不可更改 必需必需必需
################################################################
################################################################

    return  body  # 返回值为固定格式，不可更改 必需必需必需

@app.route('/decode',methods=["POST"]) # 不解密
def decrypt():
    body = request.form.get('dataBody')  # 获取  post 参数 必需必需必需
    headers = request.form.get('dataHeaders')  # 获取  post 参数  可选
# 被#隔开的部分是处理header头的部分
################################################################
################################################################
    if headers != None: # 开启了响应头加密
        print(headers)
        param_uri = re.findall(r'[POST|GET|PUT] /(.*?)[ ]', headers)[0] # 提取请求的uri及参数
        print(param_uri)
        param_uri_total = param_uri + "&b=22222222"
        headers = headers.replace(param_uri, param_uri_total, 1) # 用修改后的uri替换原参数中的uri
        headers = headers + "yyyy:zzzz\r\n"
        headers = headers + "f0ng:onlysecurity"
        return headers.replace(param_uri,param_uri_total,1) + "\r\n\r\n\r\n\r\n" + body # 返回值为固定格式，不可更改 必需必需必需
################################################################
################################################################

    return body # 返回值为固定格式，不可更改 必需必需必需

if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run(host="0.0.0.0",port="8888")
