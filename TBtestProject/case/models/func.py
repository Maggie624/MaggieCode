import inspect
import os
import time

import re

def get_pngs_dir():
    """获取图片存储路径，一天的截图放在一个文件夹中"""
    now = time.strftime('%Y-%m-%d-%H:%M:%S')
    screenshot_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + \
                     '/report/' + now[0:10]
    isExist = os.path.exists(screenshot_dir)
    if not isExist:
        print('新建文件夹')
        os.makedirs(screenshot_dir)
    return screenshot_dir

def get_dict_id(target_dict, target):
    """
    return: 在字典中对应的key值,int型
    """
    return [k for k, v in target_dict.items() if v == target][0]

def filter_to_get_word(item):
    """获取字符串中的中文字符"""
    res = re.sub('[A-Za-z0-9\!\%\[\]\,\。\.\<\>\"\?\=\=\:\：\;\&\//\/\_]', '', item)
    return res.replace(' ', '')

def get_current_func_name():
    """return:当前的函数名"""
    return inspect.stack()[1][3]