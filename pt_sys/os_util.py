#encoding: utf-8
'''
Created on 2013-7-1

@author: fengxuefeng
'''
import sys

# os工具类

# 获取popen
# 这里可直接使用platform.popen方法替换
def get_popen():
    popen = None
    if sys.platform == "win32":                # on a Windows port
        try:
            import win32pipe
            popen = win32pipe.popen
        except ImportError:
            raise ImportError, "The win32pipe module could not be found"
    else:                                      # else on POSIX box
        import os
        popen = os.popen
        
    return popen

def get_cat_or_type_cmd():
    if sys.platform == "win32": 
        return "type"
    else:
        return "cat"
    
def get_grep_or_findstr_cmd():
    if sys.platform == "win32": 
        return "| findstr"
    else:
        return "| grep"