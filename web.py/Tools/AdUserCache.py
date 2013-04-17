# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: 阳健
'''

import web, os
import hashlib

import json
from StringIO import StringIO

urls = (
    '/list','AdUserCacheList',
    '/set','AdUserCacheSet',
    '/reset','AdUserCacheReset',
    '/get','AdUserCacheGet',
)

t_globals = {
    'datestr': web.datestr
}

render = web.template.render('templates/ad_user_cache/', base='base', globals = t_globals)

PYTHON_BIN = '/usr/bin/python'
CMD_PATH = '/data/xce/MONITOR/webserver/python_client/'

app = web.application(urls, locals())

class AdUserCacheList:
    def __init__(self):
        self.CMD = CMD_PATH + 'AdUserCacheList.py'
              
    def GET(self):
        
        cmd = "%s %s" %(PYTHON_BIN, self.CMD)

        print cmd
        
        pipe = os.popen(cmd)
        result = eval(pipe.read())

        io = StringIO()    
        json.dump(result, io)
        return web.template.render('templates/ad_user_cache/').ad_user_cache_list(io.getvalue())

class AdUserCacheGet:
    def __init__(self):
#        self.CMD = '/data/xce/Ad/python_client/AdMob.py'
        self.CMD = CMD_PATH + 'AdUserCacheGet.py'
    def POST(self):
        data = web.input()

        print "uid: %s" %(data.uid)
        
    
        cmd = "%s %s '%s'" %(PYTHON_BIN, self.CMD, data.uid)

        print cmd
        
        pipe = os.popen(cmd)
        result = eval(pipe.read())

        io = StringIO()    
        json.dump(result, io)
        return io.getvalue()

class AdUserCacheSet:
    def __init__(self):
#        self.CMD = '/data/xce/Ad/python_client/AdMob.py'
        self.CMD = CMD_PATH + 'AdUserCacheSet.py'
              
    def GET(self):
#        return render.admob()
        return render.ad_user_cache_set()

    def POST(self):
        data = web.input()

        company = data.company.split(',')

        print "company: %s" %(company)
        cp_md5_list = []
        
        for cp in company:
            cp_md5 = hashlib.md5()
            #cp_md5.update(cp.decode('utf-8').encode('gbk'))
            cp_md5.update(cp)
            cp_md5_list.append(cp_md5.hexdigest()[0:16])
            
        print cp_md5_list
    
        cmd = "%s %s %s %s %s %s %s %s %s %s '%s'" %(PYTHON_BIN, self.CMD, data.uid, data.age, data.gender, data.stage, data.grade, data.school, data.currentArea, data.homeArea, ','.join(cp_md5_list))

        print cmd
        
        pipe = os.popen(cmd)
        result = eval(pipe.read())

        io = StringIO()    
        json.dump(result, io)
        return io.getvalue()

class AdUserCacheReset:
    def __init__(self):
#        self.CMD = '/data/xce/Ad/python_client/AdMob.py'
        self.CMD = CMD_PATH + 'AdUserCacheReset.py'
              
    def GET(self):
#        return render.admob()
        return render.ad_user_cache_reset()

    def POST(self):
        data = web.input()

        cmd = "%s %s %s" %(PYTHON_BIN, self.CMD, data.uid)

        print cmd
        
        pipe = os.popen(cmd)
        result = eval(pipe.read())

        io = StringIO()    
        json.dump(result, io)
        return io.getvalue()

if __name__ == '__main__':
    app.run()