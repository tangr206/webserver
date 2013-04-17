# -*- coding: utf-8 -*-

import web, os

import json
import re
from StringIO import StringIO
import Dao
import sys
import MySQLdb

urls = (
    '/adInfo','AdInfo',
    '/adConfig','ConfigInfo',
    '/zoneIndex','ZoneIndexInfo',
    '/zoneAd','ZoneAdInfo',
    '/campaignCompete','CampaignInfo',
    '/adRequest','AdRequest',
)
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates/adengineb_monitor/', base='base', globals=t_globals)

PYTHON_BIN = '/usr/bin/python'
PYTHON_BIN = '/data/xce/python_client/python_2_4_3/bin/python'
CMD_PATH = '../../python_client/'
CMD_PATH = '/data/xce/MONITOR/webserver/python_client/'

app = web.application(urls, locals())

class AdInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEngineBMonitor.py'
              
    def GET(self):
        return render.adinfo()

    def POST(self):
        flag = web.input().flag
        if flag == '0':
          cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintMembers')
        elif flag == '1':
          cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintCampaigns')
        else:
          cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintGroups')
        print cmd
        res = {
                'stat' : 1,
                'res' : '',
                'list' : []
               }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res = re.sub(re.compile(r'(\w)*:\n'), '', str_res)
            #print str_res
            res['list'] = str_res.split(',')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    
class ConfigInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEngineBMonitor.py'

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
            #str_res = str_res.replace(',;', ';')
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return render.adconfig(res) 

class ZoneIndexInfo:
    def __init__(self):
      self.CMD = CMD_PATH + 'AdEngineBMonitor.py'

    def __getAdZoneInfo(self):
      try:
        conn = MySQLdb.connect(host = '10.3.20.38', user = 'ad', passwd = 'adjb###', db = 'adn', charset='utf8')
      except Exception, e:
        print "Could not connect to Mysql server", e
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
      print "haha"
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
      return render.zoneindex(adzoneids)

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
            str_res = re.sub(re.compile(r'(\w|\s)*:\n|\n'), '', str_res)
            if str_res == '':
              return Dao.json_encode(res)
            str_res = str_res.replace(',;', ';')
            str_res = str_res[0:len(str_res)-1]
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)

class ZoneAdInfo:
    def __init__(self):
	self.CMD = CMD_PATH + 'AdEngineBMonitor.py'
    def GET(self):
        return render.zonead()
 
    def POST(self):
	zoneid = web.input().zoneid
        cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, 'PrintZoneAds', zoneid)
        print cmd
        res = {
                'stat' : 1,
                'res' : '',
                'list': []
              }
        try:
            pipe = os.popen(cmd)
            str_res = pipe.read()
            str_res = re.sub(re.compile(r'\d*:\n'), '', str_res)
            str_res = re.sub(re.compile(r';\n'), ';', str_res)
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)

class CampaignInfo:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEngineBMonitor.py'

    def GET(self):
        cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, 'PrintCompete')
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
            #str_res = str_res.replace(',;', ';')
            res['list'] = str_res.split(';')
        except Exception as why:
            res['stat'] = 0
            res['res'] = str(why)
        return render.campaigncompete(res)

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
