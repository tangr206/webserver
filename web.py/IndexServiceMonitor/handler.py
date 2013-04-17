#encoding= utf-8
'''
Created on 2012-8-28

@author: 阳健
'''

import web, os

import json
import re
from StringIO import StringIO
import Dao
import MySQLdb
import sys

urls = (
    '/request','ISRequest',
    '/adInfo','ISAdInfo',
    '/indexInfo','ISIndexInfo',
    '/compare','ISCompare',
    '/closed','ISClosed',
    '/config','ISConfig',
)
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates/index_service/', base='base', globals=t_globals)

PYTHON_BIN = '/data/xce/python_client/python_2_4_3/bin/python'
CMD_PATH = '../../python_client/'
CMD_PATH = '/data/xce/MONITOR/webserver/python_client/'

app = web.application(urls, locals())

class ISConfig:
    def __init__(self):
        self.CMD = CMD_PATH + 'IndexService.py'
              
    def GET(self):
        return render.config()

    def POST(self):
        opType = int(web.input().opType)
        oper = ['getZoneAdNum', 'getTriggerInfo', 'getGameAdNum', 'getGameMemNum']
        cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, oper[opType])

        print cmd
        res = {
                'stat' : 1,
                'res' : '',
                'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            #print str_res
            
            str_res = re.sub(re.compile(r'\[(\w|\s)*\]|\n'), '', str_res)
            #print str_res
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    

class ISClosed:
    def __init__(self):
        self.CMD = CMD_PATH + 'IndexService.py'

    def GET(self):
        cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'getClosedAd')

        print cmd
        res = {
               'stat' : 1,
               'res' : '',
               'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res = re.sub(re.compile(r'\[|\]|\n'), '', str_res)
            str_res = str_res.replace(',;', ';')
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        
        return render.closed(res)

class ISCompare:
    def __init__(self):
        self.CMD = CMD_PATH + 'IndexService.py'
    def GET(self):
        return render.compare()
    def getPricesFromStr(self, t_str):
        t_str = re.sub(re.compile(r'\[(\w|\s)*\]|\n'), '', t_str)
        return t_str.split(';')
    def POST(self):
        adGroupId = web.input().adGroupId
        cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'getAdZonePrice', adGroupId)

        print cmd
        res = {
               'stat' : 1,
               'res' : '',
               'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            if str(adGroupId) == '0':
                while str_res.find('adgroup:') > -1:
                    group = {}
                    ind = str_res.find('adgroup:') + 8
                    end = str_res.find('\n')
                    group['adgroupId'] = str_res[ind: end]
                    str_res = str_res[end + 1 : len(str_res)]
                    nex = str_res.find('adgroup:')
                    t_str = ''
                    if nex > 0:
                        t_str = str_res[0 : nex]
                        str_res = str_res[nex : len(str_res)]
                    else:
                        t_str = str_res
                    group['prices'] = self.getPricesFromStr(t_str)
                    res['list'].append(group)
            else:
                group = {}
                group['adgroupId'] = adGroupId
                group['prices'] = self.getPricesFromStr(str_res)
                res['list'].append(group)
            
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
class ISIndexInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'IndexService.py'
    def __getAdZoneInfo(self):
       try:
         conn = MySQLdb.connect(host = '10.3.20.38', user = 'ad', passwd = 'adjb###', db = 'adn', charset='utf8')
       except:
         print "Could not connect to Mysql server"
         sys.exit(0)
       sql = 'select adzone_id, adzone_name from adzone where delete_flag = 1 and audit_status = 1 and am_online_status= 1'
       cursor = conn.cursor()
       try:
         cursor.execute(sql)
       except Exception, e:
         print "get adzoneid, adzone_name execute sql error", e
         sys.exit(0)
   
       data = cursor.fetchall()
       cursor.close()
       conn.close()
       return data

    def GET(self):
        data = self.__getAdZoneInfo()
        adzoneids = {
                     'stat' : 1,
                     'res' : '',
                     'list' : [],
                     'dict' : {}
                    }
        try:
          for i in data:
            key = i[0]
            value = i[1]
            adzoneids['list'].append(key)
            adzoneids['dict'][key] = value
        except Exception as why:
          adzoneids['stat'] = 0
          adzoneids['res'] = str(why)
        return render.index_info(adzoneids)

    def POST(self):

        data = web.input()
        adZoneId = data.adZoneId
        adIndex = int(data.adIndex)
        
        cmd = "%s %s %s %s %d" %(PYTHON_BIN, self.CMD, 'getZoneIndex', adZoneId, adIndex)

        print cmd
        res = {
               'stat' : 1,
               'res' : '',
               'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res = str_res.replace(',]',']').replace(',","','","').replace(',"]','"]')
            res['list'] = eval(str_res)
            if int(adZoneId) != 0:
                res['list'] = [res['list']]
            
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)

class ISAdInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'IndexService.py'
              
    def GET(self):
        return render.ad_info()

    def POST(self):
        flag = web.input().flag
        cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'getAdPoolInfo', flag)

        print cmd
        res = {
                'stat' : 1,
                'res' : '',
                'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            #print str_res
            
            str_res = re.sub(re.compile(r'\[(\w|\s)*\]|:|\n'), '', str_res)
            #print str_res
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    
    
class ISRequest:
    def __init__(self):
        self.CMD = CMD_PATH + 'trigger.py'
              
    def GET(self):
        return render.request()

    def POST(self):
        parm_dict = {}
        data = web.data()
        for d in data.split('&'):
            pair = d.split('=')
            if len(pair) == 2 :
                parm_dict[pair[0]] = pair[1]
            else:
                return 'parameter wrong'


        str_zones = parm_dict['zones']    
        str_zone_vector = str_zones.split(',')
        zones = []
        for zone in str_zone_vector:
            if(zone.isdigit()):
                zones.append(long(zone))

        cmd = "%s %s '%s' %s %s %s %s %s %s %s %s" %(PYTHON_BIN, self.CMD, parm_dict['zones'], parm_dict['uid'], parm_dict['age'],
                parm_dict['gender'], parm_dict['stage'], parm_dict['grade'], parm_dict['school'], 
                parm_dict['ipArea'], parm_dict['currentArea'])

        print cmd

        pipe = os.popen(cmd)
        res = pipe.read()
        adv_map = eval(res)

        io = StringIO()    
        json.dump(adv_map, io)
        web.header("Content-Type", "text/plain")
        return io.getvalue()
    
if __name__ == '__main__':
    app.run()
