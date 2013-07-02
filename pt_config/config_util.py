#encoding: utf-8
'''
Created on 2013-7-1

@author: fengxuefeng
'''

import ConfigParser
import MySQLdb
import os,sys
import datetime

config = ConfigParser.RawConfigParser()
# 读取conf.properties
config.read(os.path.split(os.path.realpath(__file__))[0] + 'conf.properties')

# 获取数据库连接简单函数
get_connection = lambda : MySQLdb.connect( host = config.get('db', 'host'),
									port = config.getint('db', 'port'),
									user = config.get('db', 'user') ,
									passwd = config.get('db', 'passwd'),
									db = config.get('db', 'database'),
									charset = config.get('db', 'charset'))

get_connection_by_name = lambda name : MySQLdb.connect( host = config.get(name, 'host'),
									port = config.getint(name, 'port'),
									user = config.get(name, 'user') ,
									passwd = config.get(name, 'passwd'),
									db = config.get(name, 'database'),
									charset = config.get(name, 'charset'))

# 简单时间处理函数
get_yesterday = lambda x=1: (datetime.datetime.now() - datetime.timedelta(days = x)).strftime('%Y-%m-%d')
get_lasthour = lambda x=1: (datetime.datetime.now() - datetime.timedelta(hours = x)).strftime('%H')

def get_time(stime):
	if stime != None:
		return (datetime.datetime.strptime(stime, '%Y-%m-%d') - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')
	else:
		return get_yesterday()

# 日志
def get_log(logname = 'default.log', ttime = get_yesterday()):
	conf = Config(ttime)
	runlogpath = conf.get('env', 'runlog')
	if not os.path.exists(runlogpath):
		os.makedirs(runlogpath)
	if conf.get('run','runprint') == 'file':
		runlog = open(runlogpath + '/' + logname , 'aw')
	else:
		runlog = sys.stdout
	return runlog

class Config :
	def __init__(self, ttime = get_yesterday(), hhour = get_lasthour()):
		self._time = ttime
		self._hour = hhour
		array = self._time.split('-')
		self._year = array[0]
		self._month = array[1]
		self._date = array[2]
		self.rp = {"@Y" : self._year,   
				   "@M" : self._month,         
                   "@D" : self._date,
                   "@H" : self._hour}
	def get(self, group, key):
		result = config.get(group,key)
		#挨个替换通配符		
		for wildcard in self.rp.keys():
			result = result.replace(wildcard, self.rp[wildcard])
		return result
	def get_norp(self, group, key):
		return config.get(group,key)
	def get_int(self,group,key):
		return config.getint(group,key)
	def get_time(self): return self._time
	def get_hour(self): return self._hour 