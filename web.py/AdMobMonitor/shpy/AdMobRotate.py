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
  
  print "----"+time.strftime('%Y-%m-%d %X',time.localtime())+'----'
  print "Get Rotate Groups:"
  result2 = proxy.GetRotateGroups(long(sys.argv[1]))
  print sys.argv[1]
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

