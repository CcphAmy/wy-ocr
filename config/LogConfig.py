# -*- coding: utf-8 -*- 
# @Time : 2019/6/26 上午2:05 
# @Author : CcphAmy 
# @Site :  
# @File : LogConfig.py 
# @Software: PyCharm

import logging

class LogConfig(object):
    """docstring for LogConfig"""

    def __init__(self):
        super(LogConfig, self).__init__()
        logging.basicConfig(level=logging.DEBUG)