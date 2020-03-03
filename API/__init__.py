#初始化日志配置的代码, 应该放在api.__init__.pyz中
# 因为后续的所有接口测试,会通过script脚本运行
# 而script脚本中会调用api封装的接口
# 每次调用api的接口时,都会先运行api模块下的init文件
# 从未利用这个机制自动对日志进行初始化操作
#初始化后,只要在调用api的代码,都能使用logging的打印日志

# 导包
import app
import logging
# 初始化日志
app.init_logging()
#测试
logging.info("测试日志是否正常打印")