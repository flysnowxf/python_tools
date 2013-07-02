'''
Created on 2013-7-1

@author: fengxuefeng
'''

import unittest
from pt_time import datetime_util

class Test(unittest.TestCase):
    
    def test_all(self):
        print "day:" + datetime_util.get_stat_day()
        print "hour:" + datetime_util.get_stat_hour()
        
        self.assertEqual(datetime_util.get_hour_via_date("2011-04-19 11:03:12"), "11")
        self.assertEqual(datetime_util.get_week_via_date("2018-01-01"), "01")
        
        startTime, endTime = datetime_util.get_start_end_date_via_week(2009, 2)
        self.assertEqual(startTime.strftime('%Y-%m-%d'), "2009-01-05")
        self.assertEqual(endTime.strftime('%Y-%m-%d'), "2009-01-11")
        startTime, endTime = datetime_util.get_start_end_date_via_week(2011, 20)
        self.assertEqual(startTime.strftime('%Y-%m-%d'), "2011-05-16")
        self.assertEqual(endTime.strftime('%Y-%m-%d'), "2011-05-22")
        startTime, endTime = datetime_util.get_start_end_date_via_week(2021, 0)
        self.assertEqual(startTime.strftime('%Y-%m-%d'), "2020-12-28")
        self.assertEqual(endTime.strftime('%Y-%m-%d'), "2021-01-03")
        startTime, endTime = datetime_util.get_start_end_date_via_week(2012, 10)
        self.assertEqual(startTime.strftime('%Y-%m-%d'), "2012-03-05")
        self.assertEqual(endTime.strftime('%Y-%m-%d'), "2012-03-11")
        
        start_day = "2011-05-30"
        end_day = "2011-05-31"
        self.assertEqual(1, datetime_util.get_delta_day_start_end_date(start_day, end_day))

        day = "2011-06-30"
        first_day, last_day = datetime_util.get_first_last_day_on_month(day)
        self.assertEqual("2011-06-01", first_day)
        self.assertEqual("2011-06-30", last_day)