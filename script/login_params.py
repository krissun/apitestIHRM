import logging
import unittest

from parameterized import parameterized

from API.login_api import LoginApi
from utils import common_assert, read_login_data


class TestIhrmLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
    @parameterized.expand(read_login_data())
    def test01_login_success(self,case_data,mobile,password,http_code,success,code,message):
        # 发出请求
        response =self.login_api.login(mobile,password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("登陆成功接口返回数据为:{}".format(jsonData))
        common_assert(self,response,http_code,success,code,message)
    @parameterized.expand(read_login_data())
    def test02_login_no_username(self,case_data,mobile,password,http_code,success,code,message):
        response =self.login_api.login(mobile,password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("用户名为空返回数据为:{}".format(jsonData))
        common_assert(self,response,http_code,success,code,message)
    @parameterized.expand(read_login_data())
    def test03_login_no_password(self,case_data,mobile,password,http_code,success,code,message):
        response =self.login_api.login(mobile,password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("密码为空返回数据为:{}".format(jsonData))
        common_assert(self,response,http_code,success,code,message)
    def test04_login_noparams_username(self):
        response =self.login_api.login_parms(password="123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("缺少用户名参数返回数据为:{}".format(jsonData))
        common_assert(self,response,200,False,20001,"用户名或密码错误")

    def test05_login_noparams_password(self):
        response = self.login_api.login_parms(mobile= "13800000002")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("缺少密码参数返回数据为:{}".format(jsonData))
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")
    def test06_login_wrongparams_mobile(self):
        response =self.login_api.login_parms(mobe="13800000002",password ="123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("参数错误返回的结果为:{}".format(jsonData))
        common_assert(self,response,200,False,20001,"用户名或密码错误")
    def test07_login_wrong_mobile(self):
        response =self.login_api.login("13806600002","123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("用户名错误返回数据为:{}".format(jsonData))
        common_assert(self,response,200,False,20001,"用户名或密码错误")
    def test08_login_wrong_password(self):
        response =self.login_api.login("13800000002","122333")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("密码错误返回数据为:{}".format(jsonData))
        common_assert(self,response,200,False,20001,"用户名或密码错误")

    #多参数
    def test09_login_add_parms(self):
        response = self.login_api.login_parms2({"mobile":"13800000002","password":"123456","add" :"7788"})
        logging.info("多参的返回数据:{}".format(response.json()))
        common_assert(self,response,200,True,10000,"操作成功！")




    # def test10(self):
    #     response=self.login_api.login_parms2({"username":"13800000002","password":"123456"})
    #     logging.info("用jsonData传参结果为:{}".format(response.json()))