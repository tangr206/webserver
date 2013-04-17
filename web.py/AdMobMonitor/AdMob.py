import sys
sys.path.append('AdMobMonitor/IcePy-3.3.0/python')
import traceback, Ice, time
import random
import config
Ice.loadSlice("AdMobMonitor/AdMob.ice")
from xce.ad import *

ip = config.ip
port = config.port

status = 0
ic = None
try:
  ic =  Ice.initialize(["--Ice.Default.Locator=AdMob/Locator:default -h "+ip+" -p "+port, "--Ice.Trace.Network=0"])
  proxy = AdMobMonitorPrx.checkedCast(ic.stringToProxy("B@AdMobEngine0"))

  #print proxy

  input = AdMobTargetInput()

  input.type = int(sys.argv[1])
  input.zoneid = long(sys.argv[2])
  input.age = int(sys.argv[3])
  input.gender = int(sys.argv[4])
  input.stage = int(sys.argv[5])
  input.grade = int(sys.argv[6])
  input.school = sys.argv[7]
  input.ipArea = sys.argv[8]
  input.currentArea = sys.argv[9]
  input.screenSize = sys.argv[10]
  input.model = sys.argv[11]
  input.osVersion = sys.argv[12]
  input.netStatus = sys.argv[13]
  input.lbsx = float(sys.argv[14])
  input.lbsy = float(sys.argv[15])
  input.uid = int(sys.argv[16])

  result = proxy.GetTargetGroups(input)

  adm_vec = []
  for adv in result:
	adm_info = {}
	adm_info['groupID'] = adv.groupID
	adm_info['memberID'] = adv.memberID
	adm_info['campaignID'] = adv.campaignID
	adm_info['bidUnitID'] = adv.bidUnitID
	adm_info['transType'] = adv.transType
	adm_info['memberCategory'] = adv.memberCategory
	adm_vec.append(adm_info)
  print adm_vec

except Exception, e:
  print "catch exception: " + str(e)
  traceback.print_exc()
  status = 1
if ic:
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1
sys.exit(status)

