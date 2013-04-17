# -*- coding: utf-8 -*-

import web, os

import json
import re
from StringIO import StringIO
import Dao

urls = (
    '/adInfo','AdInfo',
    '/adConfig','ConfigInfo',
    '/zoneIndex','ZoneIndexInfo',
    '/campaignCompete','CampaignInfo',
    '/adedmdiscount','EdmDiscount',
    '/adRequest','AdRequest',
    '/frequencyrestric','FrequencyRestric',
)
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates/adedmsender_monitor/history/', base='base', globals=t_globals)

PYTHON_BIN = '/usr/bin/python'
PYTHON_BIN = '/data/xce/python_client/python_2_4_3/bin/python'
#CMD_PATH = '/data/xce/MONITOR/webserver/python_client/'
CMD_PATH = '/data/xce/MONITOR/webserver/AdWebPlatform/AdEdmSenderMonitor/history/bin/'

app = web.application(urls, locals())

class AdInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSenderMonitor.py'
              
    def GET(self):
        return render.adinfo()

    def POST(self):
        flag = web.input().flag
        date = web.input().datedata
        if flag == '0':
          cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintMembers', date)
        elif flag == '1':
          cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintCampaigns', date)
        elif flag == '2':
          cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintGroups', date)
        elif flag == '3':
          cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintAdLeftBlackList', date)
        elif flag == '4':
          cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintPlatForm', date)
        print cmd
        res = {
                'stat' : 1,
                'res' : '',
                'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res = re.sub(re.compile(r',\n'), '', str_res)
            #print str_res
            res['list'] = str_res.split(',')
            #print res
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    
class ConfigInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSenderMonitor.py'

    def GET(self):
        return render.adconfig() 

    def POST(self):
        date = web.input().datedata
        cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintConfigInfo', date)
        print cmd
        res = {
               'stat' : 1,
               'res' : '',
               'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res = re.sub(re.compile(r'\n'), '', str_res)
            res['list'] = str_res.split(',')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)

class ZoneIndexInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSenderMonitor.py'

    def GET(self):
	return render.zoneindex()

    def POST(self):
        data = web.input()
        date = data.datedata
        adZoneId = long(data.adZoneId)
        adIndex = (data.adIndex)
	cmd = "%s %s %s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintZoneIndex', date, adZoneId, adIndex)
        print cmd
	res = {
		'stat' : 1,
		'res' : '',
		'list': []
	      }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res = re.sub(re.compile(r':\n'), ':;', str_res)
            #print "===>", str_res
            if str_res == '' or str_res =="NULL":
              return Dao.json_encode(res)
            str_res = str_res.replace(',;', ';')
            str_res = str_res[0:len(str_res)-1]
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)


class EdmDiscount:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSenderMonitor.py'

    def GET(self):
        return render.adedmdiscount()

    def POST(self):
        date = web.input().datedata
        cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintEdmDiscount', date)
        print cmd
        res = {
               'stat' : 1,
               'res' : '',
               'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)

class FrequencyRestric:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSenderMonitor.py'

    def GET(self):
        return render.adFrequencyRestric()

    def POST(self):
        date = web.input().datedata
        cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintFrequencyRestric', date)
        print cmd
        res = {
               'stat' : 1,
               'res' : '',
               'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res = str_res.replace(',', ';')
            print str_res
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)

if __name__ == '__main__':
    app.run()
