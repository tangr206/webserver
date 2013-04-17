#! /usr/bin/env python
import sys
sys.path.append('AdMobMonitor/IcePy-3.3.0/python')
import traceback, Ice, time
import random
import datetime
import os
import config
Ice.loadSlice("AdMobMonitor/AdMob.ice")
from xce.ad import *

def send_warn_msg(warnMsg):
  #phone_book="18600574510  18600883672  18210295797  18600276158   18610489065  13811401320  13718813681 18810750484  15110171906"
  phone_book = [18210295797, 18811154233]
  for i in phone_book:
    cmd = 'wget -q -O /dev/null "http://10.22.198.81:2000/receiver?number='+str(i)+'&message='+warnMsg+'"'
    os.system(cmd)
    #pipe = os.popen(cmd)

ip = config.ip
port = config.port

status = 0
ic = None
try:
  ic =  Ice.initialize(["--Ice.Default.Locator=AdMob/Locator:default -h "+ip+" -p "+port, "--Ice.Trace.Network=0"])

  proxy = AdMobPrx.checkedCast(ic.stringToProxy("M@AdMobEngine0"))

  para = AdMobReqPara()
  para.uid = 438127289
  para.requestTime = 20120427101010
  para.appid = "198733"
  para.sid = "11111"
  para.adzoneId = 100000000103
  para.client.screenSize="486X0"
  para.lastGroupIds = [ 10000505720001 ]
  para.ipArea="0086110000000000"
  para.client.osVersion="iPhone OS4.1"
  result = proxy.GetAds(para)
  if result.adgroupId == -1 :
    print "-----------Get No Ad-----------------"
    time1 = time.strftime('%Y-%m-%d %X', time.localtime())
    print time1
    print result
    print "-------------------------------------"
    #send_warn_msg('Get No Mobile Ad @'+time1)
  print result

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
