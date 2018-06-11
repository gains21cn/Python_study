# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/31
# Time:13:33

import os
import sys
import logging

# 程序文件主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

# 添加环境变量
sys.path.append(BASE_DIR)

# 数据库
DATABASE = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR,
}

# 日志级别及类型
LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

# 定义交易类型，利息
TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0},
}





