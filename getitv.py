#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import getday

import urllib2,httplib
import os,datetime,string
import sys
import re
import time
import MySQLdb as mdb

def load_page(url):
    opener = urllib2.build_opener()
    print url
    f = opener.open(url)
    html = f.read()
    f.close()
    return html

# ??һ????Ԫ?????????ڴ???һ????ITV??չ?? (???ڣ??????ţ??????�����չ?û????????ۼƷ?չ?û??????????û????????ۼƾ????û???)
def parse_itv(html):
    result=[]
    html = re.sub("&#39;","'",html,0)
    html = re.sub("&quot;",'"',html,0)
    html = re.sub("&lt;","<",html,0)
    html = re.sub("&gt;",">",html,0)
    m = re.search(r'<table id="G_SECTION_2_ELEMENT_2".*jsonData=\'{"AREA_ID":\[(".*?)\],'\
                 '"AREA_NAME":\[(.*?)\],'\
                 '"SUM\(MEASURE_1\)":\[(.*?)\],'\
                 '"SUM\(MEASURE_2\)":\[(.*?)\],'\
                 '"SUM\(MEASURE_3\)":\[(.*?)\],'\
                 '"SUM\(MEASURE_4\)":\[(.*?)\],'\
                 '"SUM\(MEASURE_5\)":\[(.*?)\]}.*</table>',html)
    for i in range(1,8):
        result.append(m.group(i).replace('"','').split(','))
    return result

# ??һ????Ԫ?????????ڴ???һ????ITV??չ?? (???ڣ????�����չ?û????????ۼƷ?չ?û??????Ʒ??û???)
def parse_gqitv(html):
    result=[]
    html = re.sub("&#39;","'",html,0)
    html = re.sub("&quot;",'"',html,0)
    html = re.sub("&lt;","<",html,0)
    html = re.sub("&gt;",">",html,0)
    m = re.search(r'<table id="G_SECTION_2_ELEMENT_4".*jsonData=\'{"AREA_ID":\[(".*?)\],'\
                 '"AREA_NAME":\[(.*?)\],'\
                 '"SUM\(MEASURE_1\)":\[(.*?)\],'\
                 '"SUM\(MEASURE_2\)":\[(.*?)\],'\
                 '"SUM\(MEASURE_3\)":\[(.*?)\]}.*</table>',html)
    for i in range(1,6):
        result.append(m.group(i).replace('"','').split(','))
    return result


def write2db(sdate,myInfo,gqitv):
    conn = mdb.connect(config.DBHOST,config.DBUSER,config.DBPASS,config.DBNAME,config.DBPORT)
    cur = conn.cursor()
    for i in range(0,10):
        cur.execute("INSERT INTO itvday VALUES \
            (%s,%s,%s,%s,%s,%s,%s,%s)",
            (sdate,myInfo[0][i],myInfo[1][i].decode("gb2312"),\
             myInfo[2][i],myInfo[3][i],\
             myInfo[4][i],myInfo[5][i],myInfo[6][i]))

#        cur.execute("INSERT INTO itvday VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" % \
#                     (sdate,myInfo[0][i],myInfo[1][i].decode("gb2312"),myInfo[2][i],myInfo[3][i],\
#                    myInfo[4][i],myInfo[5][i],myInfo[6][i]))

        cur.execute("INSERT INTO gqitvday VALUES \
           (%s,%s,%s,%s,%s,%s)",
           (sdate,gqitv[0][i],gqitv[1][i].decode("gb2312"),gqitv[2][i],gqitv[3][i],gqitv[4][i]))
    conn.commit()
    conn.close()

def readitv(sdate):
    itvurl=config.ITVURL % sdate
    mhtml=load_page(itvurl)
    itv_num = parse_itv(mhtml)
    gqitv_num = parse_gqitv(mhtml)
    print itv_num[1]
    write2db(sdate,itv_num,gqitv_num)

if __name__ == '__main__':
    for day in getday.getDays("2017-03-14","2017-03-14"):
        readitv(day)
#    for day in range(19,20):
#        readitv("2016-01-%02d" % day)

