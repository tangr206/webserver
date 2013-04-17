#! /usr/bin/env python
import sys
sys.path.append('AdMobMonitor/IcePy-3.3.0/python')
import traceback, Ice, time
import random
import datetime
import os
Ice.loadSlice("AdMobMonitor/AdMob.ice")
from xce.ad import *

status = 0
ic = None
try:
  ic =  Ice.initialize(["--Ice.Default.Locator=AdMob/Locator:default -h 10.7.18.58 -p 14880", "--Ice.Trace.Network=0"])

  proxy = AdMobPrx.checkedCast(ic.stringToProxy("M@AdMobEngine0"))

  para = AdMobReqPara()
  para.uid = 438127289
  para.requestTime = 20120427101010
  para.appid = "198733"
  para.sid = "11111"
  para.adzoneId = 100000000103
  para.client.screenSize="486X0"
  para.lastGroupIds = [ 10000505720001 ]
  para.ipArea="0086000000000000"
  para.client.osVersion="iPhone OS4,0\nA\tB\r\n"
  para.res2="202"
  result = proxy.GetAds(para)
  print result
  print result.pageData.clickUrl
  print result.pageData.htmlData
except Exception, e:
    print "MemoryGarden : " + str(e)
    traceback.print_exc()
    status = 1
if ic:
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1
sys.exit(status)
