#! /usr/bin/env python
#coding=utf-8

import sys
sys.path.append('/data/xce/IcePy-3.3.0/python')
import traceback, Ice, time
import random
import ConfigParser
Ice.loadSlice("/data/xce/MONITOR/webserver/python_client/IndexService.ice")
from xce.ad import *

status = 0
ic = None
try:
  ic =  Ice.initialize(["--Ice.Default.Locator=Trigger/Locator:default -h 10.3.23.75 -p 14860", "--Ice.Trace.Network=0"])

  proxy = IndexMonitorPrx.checkedCast(ic.stringToProxy("M@IndexService0"))
  
  opType = sys.argv[1]
  res = {
    'stat' : 1,
    'res' : ''
  }
  #flag = int(sys.argv[2])
  #result2 = proxy.GetAdPoolInfo(flag)
  result2 = proxy.GetAdPoolInfo(1)
    
  if str(opType) == 'getAdPoolInfo':
    result2 = proxy.GetAdPoolInfo(1)
  elif str(opType) == 'getZoneAdNum':
    result2 = proxy.GetZoneAdNum()
  elif str(opType) == 'getTriggerInfo':
    result2 = proxy.GetTriggerInfo()
  elif str(opType) == 'getGameAdNum':
    result2 = proxy.GetGameAdNum()
  elif str(opType) == 'getGameMemNum':
    result2 = proxy.GetGameMemNum()
  elif str(opType) == 'getZoneIndex':
    adsId = int(sys.argv[2])
    index = int(sys.argv[3])
    #print adsId
    result2 = proxy.GetZoneIndex(adsId, index)
    if result2 == '':
      result2 = '{"stat": 0, "res": "不存在此广告位"}'
  elif str(opType) == 'getClosedAd':
    result2 = proxy.GetClosedAd()
  elif str(opType) == 'getAdZonePrice':
    adgId = int(sys.argv[2])
    #print adgId
    result2 = proxy.GetAdZonePrice(adgId)

  #result2 = proxy.GetAdPoolInfo(0); #广告商
  #result2 = proxy.GetAdPoolInfo(1); #广告计划
  #result2 = proxy.GetAdPoolInfo(2); #广告组
  #result2 = proxy.GetZoneAdNum();   #广告位上的广告数
  #result2 = proxy.GetTriggerInfo(); #trigger info
  #result2 = proxy.GetGameAdNum();    #广告位上的游戏数
  #result2 = proxy.GetGameMemNum();   #广告位上的游戏商数
  #result2 = proxy.GetZoneIndex(0);  #广告位上的索引，0是全部
  #result2 = proxy.GetClosedAd();     #关闭广告

  #result2 = proxy.GetAdZonePrice(0); #广告的广告位出价信息，0是全部广告

  print result2

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

