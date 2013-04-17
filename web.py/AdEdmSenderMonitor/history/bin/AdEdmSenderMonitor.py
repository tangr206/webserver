#! /usr/bin/env python
#coding=utf-8

import sys
sys.path.append('/data/xce/IcePy-3.3.0/python')
import traceback, Ice, time
import random
#Ice.loadSlice("/data/xce/MONITOR/webserver/python_client/Util.ice /data/xce/MONITOR/webserver/python_client/AdEdmSender.ice")
Ice.loadSlice("-I. --all /data/xce/MONITOR/webserver/python_client/Util.ice  /data/xce/MONITOR/webserver/python_client/AdEdmSender.ice")
from xce.ad import *
#import xce.ad
#import MyUtil
#import time

TIMES = 2000000

def GetData(OpName, date):
  filename = "/data/xce/MONITOR/webserver/AdWebPlatform/AdEdmSenderMonitor/history/data/res."+date
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


def GetData2(OpName, date, zoneid, index):
  filename = "/data/xce/MONITOR/webserver/AdWebPlatform/AdEdmSenderMonitor/history/data/res."+date
  #print filename
  #print OpName
  f = open(filename);
  lines = f.readlines()
  f.close()
  res = ""
  lines_length = len(lines)
  for index1 in range(0, lines_length):
    seq = lines[index1].strip().split(":")
    if (seq[0] == "[OP]" and len(seq) > 2):
      #print seq[1], OpName
      #print type(seq[1]), type(OpName)
      if (seq[1] == OpName and int(seq[2]) == zoneid and int(seq[3]) == index):
        for index2 in range(index1+1, lines_length):
          seq2 = lines[index2].strip().split(":")
          if (seq2[0] == "[OP]"):
            return res
          res = res + lines[index2]
  return res


try:

 
  opType = sys.argv[1]
  date = sys.argv[2]
  if str(opType) == 'PrintZoneIndex':
    zoneId = int(sys.argv[3])
    index = int(sys.argv[4])
    result2 = GetData2('PrintZoneIndex', date, zoneId, index)
  else:
    result2 = GetData(str(opType), date)

  print result2

except Exception, e:
    print "MemoryGarden : " + str(e)
    traceback.print_exc()
    status = 1
sys.exit(0)

