#-*-coding:utf-8-*-  
import datetime, calendar  

def strtodatetime(datestr,format):      
    return datetime.datetime.strptime(datestr,format)  

def datetostr(date):    
    return   str(date)[0:10]  

def datediff(beginDate,endDate):  
    format="%Y-%m-%d";  
    bd=strtodatetime(beginDate,format)  
    ed=strtodatetime(endDate,format)      
    oneday=datetime.timedelta(days=1)  
    count=0
    while bd!=ed:  
        ed=ed-oneday  
        count+=1
    return count  

def getDays(beginDate,endDate):  
    format="%Y-%m-%d";  
    bd=strtodatetime(beginDate,format)  
    ed=strtodatetime(endDate,format)  
    oneday=datetime.timedelta(days=1)   
    num=datediff(beginDate,endDate)+1   
    li=[]  
    for i in range(0,num):   
        li.append(datetostr(ed))  
        ed=ed-oneday  
    return li 

#for day in getDays("2015-12-10","2016-01-20"):
#     print day
