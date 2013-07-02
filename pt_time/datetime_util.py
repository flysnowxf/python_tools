#encoding: utf-8
'''
Created on 2013-7-1

@author: fengxuefeng
'''

import calendar
from pt_config import config_util
import datetime

# 获取统计日期
def get_stat_day():
    # 判断当前的小时
    curr_hour = datetime.datetime.now().hour;
    # 如果为0点，取昨天日期
    if curr_hour == 0:
        return config_util.get_yesterday()
    else:
        return datetime.datetime.now().strftime('%Y-%m-%d')
    
# 获取统计小时
def get_stat_hour():
    # 返回上个小时
    return config_util.get_lasthour()

# 根据日期获取小时
def get_hour_via_date(date):
    day = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return day.strftime("%H")

# 根据日期获取年份
def get_year_via_date(date):
    year = datetime.datetime.strptime(date, '%Y-%m-%d')
    return year.strftime('%Y')

# 根据日期获取月份
def get_month_via_date(date):
    month = datetime.datetime.strptime(date, '%Y-%m-%d')
    return month.strftime('%m')

#根据日期获取第几周，0-53，以周一为第一天
def get_week_via_date(date):
    day = datetime.datetime.strptime(date, '%Y-%m-%d')
    return day.strftime("%W")

# 根据年和周获取周的开始时间和结束时间，以周一为第一天
def get_start_end_date_via_week(year, week): 
    d = datetime.date(year, 1, 1) 
    if(d.weekday() > 3): 
        d = d + datetime.timedelta(7 - d.weekday()) 
    else: 
        d = d - datetime.timedelta(d.weekday()) 
    dlt = datetime.timedelta(days = (week - 1) * 7) 
    return d + dlt,  d + dlt + datetime.timedelta(days = 6)

# 根据日期获取当前周的开始时间和结束时间，以周一为第一天
def get_week_start_end_date(date):
    year = get_year_via_date(date)
    week = get_week_via_date(date)
    return get_start_end_date_via_week(int(year), int(week))

# 根据开始日期和结束日期返回时间差，单位为天
def get_delta_day_start_end_date(start_date, end_date):
    return (datetime.datetime.strptime(end_date, "%Y-%m-%d") - 
        datetime.datetime.strptime(start_date, "%Y-%m-%d")).days

# 根据日期返回当前月的第一天和最后一天
def get_first_last_day_on_month(date):
    year = int(get_year_via_date(date))
    month = int(get_month_via_date(date))
    first_day = datetime.date(year, month, 1).strftime('%Y-%m-%d')
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1]).strftime('%Y-%m-%d')
    return first_day, last_day