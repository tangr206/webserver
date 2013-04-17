# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: 阳健
'''

import web

import Tools.ServiceFinder
import Tools.AdUserCache
import Tools.EdmTest
import IndexServiceMonitor.handler
import IndexServiceMonitor.historyhandler
import ArgsManage.handler
import AdMobMonitor.handler
import AdEngineBMonitor.handler
import AdEdmSenderMonitor.handler
import AdEdmSenderMonitor.historyhandler
#import EdmAdCount.handler
#import PingMonitor.handler
#import ServiceMonitor.handler
import ServiceStatus.handler
import OverView.handler

urls = (
    '/', 'Index',
    '/adUserCache', Tools.AdUserCache.app,
    '/serviceFinder', Tools.ServiceFinder.app,
    '/edmTest', Tools.EdmTest.app,
    '/argsManage', ArgsManage.handler.app,
    '/admobMonitor', AdMobMonitor.handler.app,
    #'/edmAdCount', EdmAdCount.handler.app,
    #'/pingMonitor', PingMonitor.handler.app,
    #'/serviceMonitor', ServiceMonitor.handler.app,
    '/serviceStatus', ServiceStatus.handler.app,
    '/overview', OverView.handler.app,
    '/indexServicehistory', IndexServiceMonitor.historyhandler.app,
    '/indexService', IndexServiceMonitor.handler.app,
    '/adengineb', AdEngineBMonitor.handler.app,
    '/adedmsendermonitorhistory', AdEdmSenderMonitor.historyhandler.app,
    '/adedmsendermonitor', AdEdmSenderMonitor.handler.app,
)

render = web.template.render('templates/')


class Index:
    '''
    classdocs
    '''
    def GET(self):
        return render.Navigate()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
