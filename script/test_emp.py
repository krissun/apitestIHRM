# 导包
# 创建测试类 ,继承unittest.TestCase
# 初始化unittest函数
# 创建测试函数
import logging
import unittest

import pymysql
import requests
import time

import app
from API.emp_api import Employee
from API.login_api import LoginApi
from utils import common_assert


class TestEmp(unittest.TestCase):
    def setUp(self):
        self.emp_api =Employee()
        self.login_api= LoginApi()


    def tearDown(self):
        pass

    def test_add_emp(self):
        pass

    def test01_emp_management(self):
        response =self.emp_api.login("13800000002","123456")

        app.init_logging()
        logging.info("员工的登陆模块为:{}".format(response.json()))
        headers = self.login_api.get_headers(response)
        # 调用登陆
        logging.info("员工模块请求头为:{}".format(headers))
        # 调用添加员工
        response_add_emp =self.emp_api.add_emp("wrr3", "13343227661",headers)
        logging.info("添加员工接口的结果为:{}".format(response_add_emp.json()))
        common_assert(self,response_add_emp,200,True,10000,"操作成功")


        # 调用查询员工
        emp_id = response_add_emp.json().get("data").get("id")
        logging.info("保存的员工id为{}".format(emp_id))
        response_find_emp =self.emp_api.find_emp(emp_id,headers)
        logging.info("查询员工的结果为:{}".format(response_find_emp.json()))
        common_assert(self,response_find_emp,200,True,10000,"操作成功")

        # 调用修改员工
        response_modify_emp = self.emp_api.modify_emp(emp_id,"#JDJ@",headers)
        logging.info("修改员工结果为：{}".format(response_modify_emp.json()))
        # 与数据库建立连接
        conn = pymysql.connect(host ="182.92.81.159",user="readuser",password="ihrm_user_2019",
                               database ="ihrm")
        # 获取游标
        cursor =conn.cursor()
        # 执行sql
        sql = "select username from bs_user where id ={};".format(emp_id)
        cursor.execute(sql)
        result = cursor.fetchall()
        logging.info("查询出来的员工姓名为:{}".format(result[0][0]))

        # 断言结果：响应状态码，success，code，message
        common_assert(self,response_modify_emp,200,True,10000,"操作成功")

        # 调用删除员工
        response_delete_emp = self.emp_api.del_emp(emp_id,headers)
        logging.info("删除员工的结果为：{}".format(response_delete_emp.json()))