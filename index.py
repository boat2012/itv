import web
import os
import sys
import MySQLdb as mdb
import datetime

sys.path.append(os.path.dirname(__file__))
import config

render = web.template.render(os.path.dirname(__file__))
web.config.debug = True

urls = (
      '/.*', 'hello',
      )

def readitv(sdate):
    conn = mdb.connect(config.DBHOST,config.DBUSER,config.DBPASS,config.DBNAME,config.DBPORT)
    cur = conn.cursor()
    cur.execute("select an,format(d_yhs,0),format(m_yhs,2),format(jf_yhs,2),format(jz_yhs,0),format(yjz_yhs,0) from itvday where fday = %s order by ac+0",(sdate,))
    returnlist={}
    mylist=cur.fetchall()
    returnlist['itv']=mylist
    cur.execute("select an,format(d_yhs,0),format(m_yhs,0),format(jf_yhs,0) from gqitvday where fday = %s order by ac+0",(sdate,))
    mylist=cur.fetchall()
    returnlist['gqitv']=mylist
    
    conn.close()
    return returnlist

class hello:
   
   def GET(self):
          sdate = str(datetime.date.today()-datetime.timedelta(days=2))[0:10]
          # sdate="2016-05-21"
          results = readitv(sdate)
          output = render.mailitv(sdate,results)
          return output

application = web.application(urls, globals()).wsgifunc()