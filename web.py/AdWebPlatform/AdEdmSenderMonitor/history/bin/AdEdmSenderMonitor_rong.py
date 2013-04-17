#! /usr/bin/env python
import sys
sys.path.append('/data/xce')
sys.path.append('/data/xce/IcePy-3.3.0/python')
import traceback, Ice, time
import random
Ice.loadSlice("-I. --all ./Util.ice  ./AdEdmSender.ice")
#from xce.ad import *
import xce.ad
import MyUtil
import time
import re

TIMES = 2000000

ic = None
status=0
try:

  
  ic =  Ice.initialize(["--Ice.Default.Locator=Edm/Locator:default -h 10.3.23.75 -p 14810", "--Ice.Trace.Network=0"])
  #ic =  Ice.initialize(["--Ice.Default.Locator=Edm/Locator:default -h 10.3.22.26 -p 14810", "--Ice.Trace.Network=0"])
  serviceName = "MONITOR@AdEdmSender0";
  prx = xce.ad.AdEdmSenderMonitorPrx.checkedCast( ic.stringToProxy(serviceName) )
  #print prx

  print "[OP]:PrintConfigInfo"
  result2 = prx.PrintEngineParametersCache()
  result2 = result2 + prx.PrintEngineConfig()
  print result2


  for i in range(1,8):
    for j in range(0, 11):
      print "[OP]:PrintZoneIndex:%d:%d"%(i,j)
      print prx.PrintEdmInvertedIndex(i, j);


  print "[OP]:PrintMembers"
  print prx.PrintMemberId();

  print "[OP]:PrintCampaigns"
  print prx.PrintCampaignId(); 

  print "[OP]:PrintGroups"
  print prx.PrintGroupId();
  
  print "[OP]:PrintAdLeftBlackList"
  print prx.PrintAdLeftBlackList();
  
  print "[OP]:PrintPlatForm"
  print prx.PrintPlatformMap();
  
  print "[OP]:PrintEdmDiscount"
  print prx.PrintEdmDiscount();
  
  print "[OP]:PrintFrequencyRestric"
  print prx.PrintFrequencyRestric();



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
#/*                                                       
# * IntIndexPtr gender_index_; 0                          
# * IntIndexPtr stage_index_;  1                          
# * IntIndexPtr grade_index_;  2                          
# * IntIndexPtr age_index_;    3                          
# * UInt64IndexPtr area_index_;          4                
# * UInt64IndexPtr school_index_;        5                
# * UInt64IndexPtr school_area_index_;   6                
# *                                                       
# * UInt64IndexPtr company_index_;       7                
# * UInt64IndexPtr interest_index_;      8                
# * UInt64IndexPtr platform_index_;      9                
# * LBSIndexPtr lbs_index_;              10               
# *                                                       
# * */                                                    
#


