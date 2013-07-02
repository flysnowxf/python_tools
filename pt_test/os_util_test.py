'''
Created on 2013-7-1

@author: fengxuefeng
'''
import unittest

from pt_sys import os_util

class Test(unittest.TestCase):

    def test_all(self):
        os_util.get_popen()
