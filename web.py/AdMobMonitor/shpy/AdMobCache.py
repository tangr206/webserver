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

  # [MEMBER, CAMPAIGN, GROUP, ZONE, UserBind, PLATFORM, BRAND3G, RESOLUTION, RESOLUTION_WIDGET]
  x = [1,2,3,4,5,6,7,8,9]
  result = ''  
  for i in x:
    result = result + str(proxy.GetPoolSize(i)) + '\r\n'
    result += proxy.GetPoolAll(i,10000)
    result += "\r\n"
  f = file(ip+'/cache_log/cache_log_'+time.strftime('%Y-%m-%d-%H',time.localtime())+'.log', 'w')
  f.write(result)
  f.close()
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
