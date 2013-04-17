import sys
sys.path.append('IcePy-3.3.0/python')
import traceback, Ice, time
import random
import config
Ice.loadSlice("AdMob.ice")
from xce.ad import *

ip = config.ip
port = config.port

status = 0
ic = None
try:
  ic =  Ice.initialize(["--Ice.Default.Locator=AdMob/Locator:default -h "+ip+" -p "+port, "--Ice.Trace.Network=0"])

  proxy = AdMobMonitorPrx.checkedCast(ic.stringToProxy("B@AdMobEngine0"))
  x = [ 1,2,3,4,5,6,7,8,9,10,11,12]
  y = [ "NONE", "GENDER", "STAGE", "AGE", "GRADE", "SCHOOL", "AREA", "SCHOOLAREA", "PLATFORM", "NETWORK", "BRAND3G", "RESOLUTION", "LBS", "MAX" ]
 
  print "----"+time.strftime('%Y-%m-%d %X',time.localtime())+'----'
  print "Get Self Index All Groups:"
  for i in x:
    result2 = proxy.GetSelfIndexInfo(i, int(sys.argv[1]))
    print y[i]
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

