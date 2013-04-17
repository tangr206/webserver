#! /usr/bin/env python
#coding=utf-8

import sys
import MySQLdb
sys.path.append('/data/xce/IcePy-3.3.0/python')
import traceback, Ice, time
import random
import ConfigParser
Ice.loadSlice("/data/xce/MONITOR/webserver/python_client/IndexService.ice")
from xce.ad import *

def GetData(OpName, date):
  filename = "/data/xce/MONITOR/webserver/AdWebPlatform/IndexServiceMonitor/history/data/res."+date
  #print filename
  #print OpName
  f = open(filename);
  lines = f.readlines()
  f.close()
  res = ""
  lines_length = len(lines)
  for index1 in range(0, lines_length):
    seq = lines[index1].strip().split(":")
    if (seq[0] == "[OP]"):
      #print seq[1], OpName
      #print type(seq[1]), type(OpName)
      if (seq[1] == OpName):
        for index2 in range(index1+1, lines_length):
          seq2 = lines[index2].strip().split(":")
          if (seq2[0] == "[OP]"):
            return res
          res = res + lines[index2]
  return res


def GetData1(OpName, date, flag):
  filename = "/data/xce/MONITOR/webserver/AdWebPlatform/IndexServiceMonitor/history/data/res."+date
  #print filename
  #print OpName
  f = open(filename);
  lines = f.readlines()
  f.close()
  res = ""
  lines_length = len(lines)
  for index1 in range(0, lines_length):
    seq = lines[index1].strip().split(":")
    if (seq[0] == "[OP]"):
      #print type(seq[1]), type(OpName)
      if (seq[1] == OpName and int(seq[2]) == int(flag)):
        for index2 in range(index1+1, lines_length):
          seq2 = lines[index2].strip().split(":")
          if (seq2[0] == "[OP]"):
            return res
          res = res + lines[index2]
  return res


def GetData2(OpName, date, adsid, index):
  filename = "/data/xce/MONITOR/webserver/AdWebPlatform/IndexServiceMonitor/history/data/res."+date
  #print filename
  #print OpName
  f = open(filename);
  lines = f.readlines()
  f.close()
  res = ""
  lines_length = len(lines)
  for index1 in range(0, lines_length):
    seq = lines[index1].strip().split(":")
    if (seq[0] == "[OP]"):
      #print seq[1], OpName
      #print type(seq[1]), type(OpName)
      if (seq[1] == OpName):
        for index2 in range(index1+1, lines_length):
          seq2 = lines[index2].strip().split(":")
          if (seq2[0] == "[OP]"):
            return res
          res = res + lines[index2]
  return res


def GetAdzoneId():
  try: 
    conn = MySQldb.connect(host = '10.3.20.38', user = 'ad', passwd = 'adjb###', db = 'adn')
  except:
    print "Could not connect to Mysql server"
    sys.exit(0)

  sql = 'select distinct adzone_id from adzone'
  cursor = conn.cursor()

  try:
    cursor.execute(sql)
  except Exception, e:
    print "getadzoneid execute sql error", e
    sys.exit(0)

  data = cursor.fetchall()
  cursor.close()
  conn.close()
  
  print data
  return data




try:
  
  opType = sys.argv[1]
  date = sys.argv[2]

  if str(opType) == 'getAdPoolInfo':
    flag = int(sys.argv[3])
    result2 = GetData1(str(opType), date, flag)
  elif str(opType) == 'getZoneIndex':
    adsId = int(sys.argv[3])
    index = int(sys.argv[4])
    result2 = GetData2(str(opType), date, adsId, index)
  elif str(opType) == 'GetAdZoneId':
    result2 = GetAdZoneId()
  else:
    result2 = GetData(str(opType), date)

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

