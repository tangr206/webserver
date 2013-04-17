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

  proxy = IndexMonitorPrx.checkedCast(ic.stringToProxy("M@IndexService1"))
  
  res = {
    'stat' : 1,
    'res' : ''
  }
  print "[OP]:getAdPoolInfo:0"
  print proxy.GetAdPoolInfo(0)
  print "[OP]:getAdPoolInfo:1"
  print proxy.GetAdPoolInfo(1)
  print "[OP]:getAdPoolInfo:2"
  print proxy.GetAdPoolInfo(2)
    
  print "[OP]:getZoneAdNum"
  print proxy.GetZoneAdNum()
  print "[OP]:getTriggerInfo"
  print proxy.GetTriggerInfo()
  print "[OP]:getGameAdNum"
  print proxy.GetGameAdNum()
  print "[OP]:getGameMemNum"
  print proxy.GetGameMemNum()
  zoneids = [100000000001, 100000000060, 100000000063, 100000000065, 100000000069,\
      100000000070,100000000071,100000000072,100000000073,100000000074,100000000075,\
      100000000091,100000000093,100000000101]
  for i in zoneids:
    for j in range(0, 9):
      print "[OP]:getZoneIndex:%d:%d"%(i,j)
      print proxy.GetZoneIndex(i, j)

  print "[OP]:getClosedAd"
  print proxy.GetClosedAd()
  print "[OP]:getAdZonePrice"
  print proxy.GetAdZonePrice(0)

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

