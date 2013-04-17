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
    '/frequencycache','FrequencyCache',
)
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates/adedmsender_monitor/', base='base', globals=t_globals)

PYTHON_BIN = '/data/xce/python_client/python_2_4_3/bin/python'
CMD_PATH = '/data/xce/MONITOR/webserver/python_client/'

app = web.application(urls, locals())

class AdInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSenderMonitor.py'
              
    def GET(self):
        return render.adinfo()

    def POST(self):
        flag = web.input().flag
        if flag == '0':
          cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintMembers')
        elif flag == '1':
          cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintCampaigns')
        elif flag == '2':
          cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintGroups')
        elif flag == '3':
          cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintAdLeftBlackList')
        elif flag == '4':
          cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintPlatForm')
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
        cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintConfigInfo')
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
        return render.adconfig(res) 

class ZoneIndexInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSenderMonitor.py'

    def GET(self):
	return render.zoneindex()

    def POST(self):
        data = web.input()
        adZoneId = long(data.adZoneId)
        adIndex = (data.adIndex)
	cmd = "%s %s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintZoneIndex', adZoneId, adIndex)
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
            print "===>", str_res
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
        cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintEdmDiscount')
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
        return render.adedmdiscount(res)

class FrequencyRestric:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSenderMonitor.py'

    def GET(self):
        cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintFrequencyRestric')
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
        return render.adFrequencyRestric(res)

class FrequencyCache:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSenderMonitor.py'

    def GET(self):
	return render.adFrequencyCache()
    
    def POST(self):
	uid = web.input().uid
	cmd = PYTHON_BIN + ' ' + self.CMD + ' PrintFrequencyCache ' + uid 
	print cmd
        res = {
               'stat' : 1,
               'res' : '',
               'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res =re.sub(r':\n', ':;', str_res)
            str_res =re.sub(r',', ';', str_res)
            print str_res
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)


class AdRequest:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEngineBMonitor.py'

    def GET(self):
	return render.requestad()
    
    def POST(self):
	uid = web.input().uid
	refer = web.input().refer
 	rotate_index = web.input().rotateIndex
	cmd = PYTHON_BIN + ' ' + self.CMD + ' PrintResult ' + uid + ' \'' + refer + '\' ' + rotate_index
	print cmd
        res = {
               'stat' : 1,
               'res' : '',
               'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res =re.sub(r'\n', '', str_res)
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)

if __name__ == '__main__':
    app.run()
