# 导包
# 创建测试类 ,继承unittest.TestCase
# 初始化unittest函数
# 创建测试函数
import logging
import random
import unittest

import pymysql
import requests
import time

import app
from API.emp_api import Employee
from API.login_api import LoginApi
from utils import common_assert, DBUtils


class TestEmp(unittest.TestCase):

    def setUp(self):
        self.emp_api =Employee()
        self.login_api= LoginApi()

    # 分离登陆成功用例
    def test02_login_success(self):
        response_login = self.emp_api.login("13800000002","123456")
        logging.info("员工模块的登陆结果为:{}".format(response_login.json()))
        token ="Bearer "+response_login.json().get("data")
        # 得到请求头数据
        # global headers # 把局部变量变成全局变量,但是其他文件也需要调用,只能配置到app.py里
        headers = {"Content-Type":"application/json","Authorization":token}
        app.HEADERS = headers
        logging.info("取出的令牌为:{}".format(token))
        logging.info("请求头为:{}".format(headers))
        print(33)
        common_assert(self, response_login, 200, True, 10000, "操作成功")
    # 添加员工
    def test03_add_emp(self):
        mobile = "179"+time.strftime("%d%H%M%S")
        name ="rose"+time.strftime("%d%H%M%S")
        response_add_emp = self.emp_api.add_emp(name, mobile, app.HEADERS)
        logging.info("添加员工的结果是:{}".format(response_add_emp.json()))
        emp_id =response_add_emp.json().get("data").get("id")
        app.EMP_ID =emp_id
        logging.info("添加员工的id是{}".format(app.EMP_ID))
        common_assert(self,response_add_emp,200,True,10000,"操作成功")

    def test04_find_emp(self):
        response_find_emp = self.emp_api.find_emp(app.EMP_ID, app.HEADERS)  #小写headers有个同名模块,容易进坑
        logging.info("查询员工的结果为:{}".format(response_find_emp.json()))
        common_assert(self,response_find_emp,200,True,10000,"操作成功")

    def test05_modify_emp(self):
        response_modify_emp = self.emp_api.modify_emp(app.EMP_ID,"happy",app.HEADERS)
        logging.info("修改员工的结果为:{}".format(response_modify_emp.json()))
        common_assert(self,response_modify_emp,200,True,10000,"操作成功")

        with DBUtils() as db:
            sql = 'select username from bs_user where id ={}'.format(app.EMP_ID)
            db.execute(sql)
            result = db.fetchone()
            self.assertEqual("happy", result[0])
            logging.info("数据库查询结果为:{}".format(result[0]))

        # # 连接数据库
        # conn = pymysql.connect(host="182.92.81.159", user="readuser", password="iHRM_user_2019", database="ihrm")
        # cursor = conn.cursor()
        # sql = 'select username from bs_user where id = {}'.format(app.EMP_ID)
        # cursor.execute(sql)
        # result = cursor.fetchone()
        # self.assertEqual("happy",result[0])

    def test06_del_emp(self):
        response_del_emp =self.emp_api.del_emp(app.EMP_ID, app.HEADERS)
        logging.info("删除员工的结果为:{}".format(response_del_emp.json()))
        common_assert(self,response_del_emp,200,True,10000,"操作成功")
        self.assertEqual(None,response_del_emp.json().get("data"))


# if __name__ == "__main__":
#     logging.info("请求头为:{}".format(headers))


