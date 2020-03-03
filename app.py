# 存放全局变量,公有的配置函数或者类
import logging
import os
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "http://182.92.81.159"
HEADERS = {"Content-Type":"application/json"}

# 1.定义一个初始化日志配置的函数, 初始化日志的输出路径(例如,输出到控制台和文件中)
def init_logging():
    # 2,创建日志器
    logger = logging.getLogger()
    # 3设置日志等级
    logger.setLevel(logging.INFO)
    # 4 创建处理器,通过处理控制日志的打印(控制台处理器.streamhandler)
    sh = logging.StreamHandler()
    # 创建文件处理器,# 按大小,按时间拆分日志
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # backupcount: 保留的日志文件数据
    fh = logging.handlers.TimedRotatingFileHandler(base_dir + "/log/ihrm.log",
                                                   when="S", interval=10, backupCount=3, encoding='utf-8')
    # 5.设置日志的格式
    #     fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] -% (message)s'# 错的

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 6.将格式器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 7.将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)


if __name__ == '__main__':
    # 初始化日志配置是,由于没有返回日志,所有这个配置函数中的全部配置会配置到logging的root节点
    init_logging()
    logging.info("测试日志打印")
