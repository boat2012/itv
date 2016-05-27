# encoding: utf-8

import getitv

import datetime
import random,time
import os,sys

abspath = "/data/wwwroot/default/itv"

def logprint(text):
   log = open(abspath+"/everyday.log","a")  
   log.write(text)
   log.close()


if __name__ == '__main__':
   today = str(datetime.date.today()-datetime.timedelta(days=1))[0:10]
   #print today
   time.sleep(random.randint(5,7200))
   #for day in range(1,23):
   #   today1= "2016-05-%s" % day
   #   getitv.readitv(today1)
   #   print today1
   getitv.readitv(today)
   logprint(datetime.datetime.now().strftime("%y-%m-%d %I:%M:%S %p")+"\t\t运行成功\n" )
   #readitv(day)





