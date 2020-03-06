import os
import time
import unittest

from HTMLTestRunner_PY3 import HTMLTestRunner

from script.login_params import TestIhrmLogin
from script.test_emp_parms import TestEmp

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestIhrmLogin))
suite.addTest(unittest.makeSuite(TestEmp))
report_path = os.path.dirname(os.path.abspath(__file__))+"/report/{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(report_path,"wb") as f:
    runner = HTMLTestRunner(f,verbosity=2,title= '软件测试报告',description='win7-chrome')
    runner.run(suite)