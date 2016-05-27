import web
import os
import sys
import MySQLdb as mdb
import datetime

sys.path.append(os.path.dirname(__file__))
import config

render = web.template.render(os.path.dirname(__file__))

urls = (
      '/.*', 'hello',
      )

def readitv(sdate):
    conn = mdb.connect(config.DBHOST,config.DBUSER,config.DBPASS,config.DBNAME,config.DBPORT)
    cur = conn.cursor()
    cur.execute("select * from itvday where fday = %s order by ac+0",(sdate,))
    return cur.fetchall()

class hello:
   
   def GET(self):
          sdate = str(datetime.date.today()-datetime.timedelta(days=2))[0:10]
          # sdate="2016-05-21"
          results = readitv(sdate)
          output = render.mailitv(results)
          return output

application = web.application(urls, globals()).wsgifunc()