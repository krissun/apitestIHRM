# 封装断言通用函数


def common_assert(self,response_emp,status_code,success,code,message):
    self.assertEqual(status_code, response_emp.status_code)
    self.assertEqual(success, response_emp.json().get("success"))
    self.assertEqual(code, response_emp.json().get("code"))
    self.assertIn(message, response_emp.json().get("message"))