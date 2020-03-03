import requests
import unittest
# 创建API类
class Employee:
    def __init__(self):
        pass

    def login(self, mobile, password):
        login_url = "http://182.92.81.159/api/sys/login"
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(login_url, json=jsonData)
    # 调用添加员工
    def add_emp(self, username, mobile, headers):
        self.response_add_emp = requests.post("http://182.92.81.159/api/sys/user",
                                         json={"username": username,
                                               "mobile": mobile,
                                               "timeOfEntry": "2020-02-01",
                                               "formOfEmployment": 1,
                                               "departmentName": "酱油2部",
                                               "departmentId": "1205026005332635648",
                                               "correctionTime": "2020-02-03T16:00:00.000Z"}, headers=headers)
        return self.response_add_emp

    def find_emp(self,emp_id,headers):
        find_emp_url ="http://182.92.81.159/api/sys/user" + "/" + emp_id
        response_find_emp = requests.get(find_emp_url, headers=headers)
        return response_find_emp

    def modify_emp(self,emp_id, username, headers):
        modify_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        response_modify = requests.put(modify_url,
                                       json={"username": username},
                                       headers=headers)
        return response_modify

    def del_emp(self,emp_id, headers):
        delete_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        response_delete = requests.delete(delete_url, headers=headers)
        return response_delete



