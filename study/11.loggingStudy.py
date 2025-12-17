"""
import logging
logging.basicConfig(filename="log/demo.log",  level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)-8s    %(message)s')
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
"""

import logging
# 1.创建logger日志管理器：初始化/实例化对象
logger = logging.getLogger()
# 设计日志级别
logger.setLevel(logging.DEBUG)
# 清除已有的处理器
logger.handlers = []

# 2.定义处理器Handler
# 控制台：StreamHandler
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
# 日志文件：FileHandler
fh = logging.FileHandler(filename='log/demo.log', encoding="utf-8")
fh.setLevel(logging.INFO)

# 3.定义日志输出格式
formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s    %(message)s')

# 4.日志处理器和输出格式关联
sh.setFormatter(formatter)
fh.setFormatter(formatter)

# 5.logging添加自定义日志处理器
logger.addHandler(sh)
logger.addHandler(fh)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
