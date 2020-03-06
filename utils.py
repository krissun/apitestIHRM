# 封装断言通用函数
import json
import os

import pymysql


def common_assert(self,response_emp,status_code,success,code,message):
    self.assertEqual(status_code, response_emp.status_code)
    self.assertEqual(success, response_emp.json().get("success"))
    self.assertEqual(code, response_emp.json().get("code"))
    self.assertIn(message, response_emp.json().get("message"))

class DBUtils:
    def __init__(self):
        self.host ="182.92.81.159"
        self.user = "readuser"
        self.password = "iHRM_user_2019"
        self.database ="ihrm"

    def __enter__(self): #使用with语法会先运行enter的代码
        self.conn=pymysql.connect(host=self.host,user=self.user,password =self.password,database=self.database)
        self.cursor =self.conn.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
       # 退出with语法会执行的代码
def read_login_data():
    # 定义数据文件路径
    login_data_path =os.path.dirname(os.path.abspath(__file__)) +"/data/login.json"
    # print(login_data_path)
    # 读取
    with open(login_data_path,mode='r',encoding='utf-8') as f :
        jsonData = json.load(f) # 文件中json格式的字符串load读取为字典
        # print(jsonData)
        list =[]
        for case_data in jsonData:

            list.append(tuple(case_data.values()))#直接转为元组格式
        # print(type(list),list)
        return list



def read_add_emp_data():
    emp_data_path = os.path.dirname(os.path.abspath(__file__))+"./data/emp.json"
    with open(emp_data_path,mode="r",encoding="utf-8") as f:
        jsonData = json.load(f)# 得到字典类型的json字符串
        list = []
        list2=[]
        add_emp_data =jsonData.get("add_emp")
        # case_name = add_emp_data.get("case_name")
        for data in add_emp_data.values():
            list.append(data)
        list2.append(tuple(list))
        # print(list) #列表格式
        # print(list2)
        return list2               #//[("","","",200,True)]

def read_emp_data(emp_data):
    emp_data_path = os.path.dirname(os.path.abspath(__file__)) + "./data/emp.json"
    with open(emp_data_path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)  # 得到字典类型的json字符串
        list = []
        list2 = []

        add_emp_data = jsonData.get(emp_data)
        # case_name = add_emp_data.get("case_name")
        for data in add_emp_data.values():
            list.append(data)
        list2.append(tuple(list))
        # print(list) #列表格式
        # print(list2)
        return list2



if __name__=="__main__":
    read_login_data()
    read_add_emp_data()
    read_emp_data("add_emp")