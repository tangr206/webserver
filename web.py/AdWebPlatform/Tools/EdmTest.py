# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: 阳健
'''
import web
import os
import json
from StringIO import StringIO

urls = (
    '/','EdmTest',
    '/set','EdmTest',
)

render = web.template.render('templates/edm_sender/')

PYTHON_BIN = '/usr/bin/python'
CMD_PATH = '/data/xce/MONITOR/webserver/python_client/'

app = web.application(urls, locals())

class EdmTest:
    '''
    classdocs
    '''
    def __init__(self):
        self.CMD = CMD_PATH + 'AdEdmSender.py'
        
    def GET(self):
        return render.index()
    
    def POST(self):
        data = web.input()
        print "user_list:" + str(data.user_list)
        print "user_status:" + str(data.user_status)
        print "edm_type:" + str(data.edm_type)
        
        #cmd = "%s %s %s %s" %(PYTHON_BIN, self.CMD, data.user_status, data.user_list)
        cmd = "%s %s %s %s %s" %(PYTHON_BIN, self.CMD, data.user_status, data.user_list,data.edm_type)

        print cmd
        
        pipe = os.popen(cmd)
        result = eval(pipe.read())

        io = StringIO()    
        json.dump(result, io)
        return io.getvalue()
    
if __name__ == '__main__':
    app.run()      
