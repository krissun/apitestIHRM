import logging

import requests

# from app import HOST, HEADERS
import app
from app import HOST, HEADERS


class LoginApi:
    def __init__(self):
        self.login_url = HOST+"/api/sys/login"
        # self.headers = app.HEADERS
    def login(self,mobile,password):
        data ={"mobile":mobile,"password":password}
        response_login = requests.post(self.login_url,json =data)
#         发送登陆请求,返回响应数据
        return response_login

    def login_parms(self, **kwargs):
        return requests.post(self.login_url,json=kwargs)
    def login_parms2(self,jsonData):
        return requests.post(self.login_url,json=jsonData)
    def get_headers(self, response_login):
        token = "Bearer "+response_login.json().get("data")
        logging.info("取出的令牌为{}".format(token))
        headers = {"Content-Type": "application/json", "Authorization": token}
        return headers

