#coding=utf-8
import web, os
import re
import json
import time
import config
from StringIO import StringIO

### Url mappings

urls = (
    '/', 'AdMob', 	
    '/AdMobCache', 'Cache',
    '/AdMob', 'AdMob',
    '/AdMobIndex', 'MonitorIndex',
#    '/login', 'Login',
#    '/logout', 'Logout',
)
### Templates
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates/admob_monitor/', base='base', globals=t_globals)

ip = config.ip
user = config.user
pwd = config.password
pythonpath = config.pythonpath

if os.path.exists('AdMobMonitor/' + ip + '/cache_log') == False :
  os.system('sh AdMobMonitor/makedir.sh')

def session_hook():
  web.ctx.session = session

web.config.debug = False

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'logged_in': False})
app.add_processor(web.loadhook(session_hook))

class Login:
  def GET(self):
    return render.login()
      
  def POST(self):
    login_data = web.input()
    #print login_data
    if login_data.user == user and login_data.passwd == pwd:
      session.logged_in = True
      #print session
      return render.admob()
    else:
      return render.login()

class Logout:
  def GET(self):
    try:
      session.logged_in = False
      return render.login()
    except AttributeError:
      pass
      return render.login()
      
class AdMob:
  def __init__(self):
    self.PYTHON_BIN = pythonpath
    self.CMD = 'AdMobMonitor/AdMob.py'
		  
  def GET(self):
#    try:
#      if session.logged_in == False:
#        raise web.seeother('/login')
#    except AttributeError:
#      pass
#      raise web.seeother('/login')
    return render.admob()
        
  def POST(self):
    parm_dict = {}
    data = web.data()
    for d in data.split('&'):
      pair = d.split('=')
      if len(pair) == 2 :
        parm_dict[pair[0]] = pair[1]
      else:
        return 'Error'
    #print parm_dict


    cmd = "%s %s %s %s %s %s %s %s %s %s %s %s '%s' '%s' %s %s %s %s" % (self.PYTHON_BIN, self.CMD, parm_dict['type'], parm_dict['zoneid'], parm_dict['age'], parm_dict['gender'], parm_dict['stage'], parm_dict['grade'], parm_dict['school'], parm_dict['ipArea'], parm_dict['currentArea'], parm_dict['screenSize'], parm_dict['model'], parm_dict['osVersion'], parm_dict['netStatus'], parm_dict['lbsx'], parm_dict['lbsy'], parm_dict['uid'])

    print cmd
		
    pipe = os.popen(cmd)
    result = eval(pipe.read())

    io = StringIO()	
    json.dump(result, io)
    web.header("Content-Type", "text/plain")
    return io.getvalue()

class Cache:
  def __init__(self):
    self.PYTHON_BIN = pythonpath
    self.CMD = 'AdMobMonitor/AdMobCache.py'

  def GET(self):
#    try:
#      if session.logged_in == False:
#        raise web.seeother('/login')
#    except AttributeError:
#      pass
#      raise web.seeother('/login')
    return render.cache()
  
  #[['123', '456', '789'], ['3', '456', '789']]
  def ProcessLine(self, line):
    line.replace(' ', '')
    p = re.compile('\[\d*\]')
    ids = p.sub('#', line)
    ids = ids[1:]
    arr = re.split('#', ids)
    str = ''
    count = 0
    for a in arr:
      if count % 5 == 0:
        if count != 0:
          str += '</tr>'
        str = str + '<tr>' + '<td>' + a + '</td>'
      else:
        str = str + '<td>' + a + '</td>'
      count += 1
    return str

  def POST(self):
    parm_dict = {}
    data = web.data()
    for d in data.split('&'):
      pair = d.split('=')
      if len(pair) == 2 :
        parm_dict[pair[0]] = pair[1]
      else:
        return 'Error'
    #print parm_dict

    #file no exist, create new file now
    time1 = parm_dict['time']
    path = 'AdMobMonitor/' + ip + '/cache_log/cache_log_' + time1 + '.log'
    flag = 0
    if os.path.exists('AdMobMonitor/' + ip + '/cache_log') == False :
      os.system('sh AdMobMonitor/makedir.sh')
    if os.path.exists(path) == False :
      flag = 1
      cmd = "%s %s" % (self.PYTHON_BIN, self.CMD)
      #pipe = os.popen(cmd)
      os.system(cmd)
      path = 'AdMobMonitor/' + ip + '/cache_log/cache_log_' + time.strftime('%Y-%m-%d-%H', time.localtime()) + '.log' 
    		
    result = ''
    file = open(os.path.abspath(path), 'r')
    lines = file.readlines()
    dict = {'[member pool]:':'广告商', '[campaign pool]:':'广告计划', \
            '[Resolution map]:':'分辨率', '[brand3G map]:':'手机品牌', \
	    '[platform map]:':'OS平台', '[UserBind pool]:':'大客户', \
            '[zone pool]:':'广告位', '[self group pool]:':'自助广告', \
            '[brand group pool]:':'品牌广告'}
    htmldata = ''
    key = ''
    idLines = ''
    num = ''
    if flag == 1:
      htmldata += '时间-' + time1 + '时没有记录缓存，当前缓存' + time.strftime('%Y-%m-%d-%H', time.localtime()) + '如下<br/>'
    for line in lines:
      if -1 == line.find('['):
        num = line.strip()
        if '' != key:
          htmldata = htmldata + self.ProcessLine(idLines) + '</table><br/>'
          key = ''
          idLines = ''
        continue
      if -1 != line.find('[self group pool]:'):
        htmldata = htmldata + self.ProcessLine(idLines) + '</table><br/>'
        idLines = ''
        key = line.strip()
        htmldata += dict[key] + '(' + num + ')' + '<br/><table id="mytable" cellspacing="0" style="margin:auto;">' + \
            '<tr><th>ID</th><th>ID</th><th>ID</th><th>ID</th><th>ID</th></tr>'
        continue
      if -1 != line.find(':'):
        key = line.strip()
        htmldata = htmldata + dict[key] + '(' + num + ')' + \
            '<br/><table id="mytable" cellspacing="0"><tr><th>ID</th><th>ID</th><th>ID</th><th>ID</th><th>ID</th></tr>'
        continue
      idLines += line     
    file.close()  
    
    web.header("Content-Type", "text/plain")
    return htmldata

class MonitorIndex:
  def __init__(self):
    self.PYTHON_BIN = pythonpath

  def GET(self):
#    try:
#      if session.logged_in == False:
#        raise web.seeother('/login')
#    except AttributeError:
#      pass
#      raise web.seeother('/login')
    return render.monitor_index()
  
  def ProcessLine(self, line):
    p = re.compile('\[|\]')
    line = p.sub('', line)
    arr = re.split(':', line)
    if len(arr) == 2:
      htmldata = '<tr><th>' + arr[0] + '</th><td>' + arr[1] + '</td></tr>'
    return htmldata
  
  def ProcessBrandSelf(self, path1, zoneid):
    cmd = "%s %s %s" % (self.PYTHON_BIN, path1, zoneid)
    pipe = os.popen(cmd)
    lines = pipe.readlines()
    dict = {'GENDER':'性别', 'STAGE':'人生阶段', 'AGE':'年龄', 'GRADE':'年级', \
           'SCHOOL':'学校', 'AREA':'地区', 'SCHOOLAREA':'学校地区', \
           'PLATFORM':'平台', 'NETWORK':'运营商', 'BRAND3G':'手机品牌', \
           'RESOLUTION':'分辨率', 'LBS':'地理位置'}
    htmldata = ''
    key = ''
    count = 0
    for line in lines:
      count += 1
      if count <= 2 :
        continue
      if '' == line.strip():
        continue
      if -1 == line.find('['):
        if '' != key:
          htmldata += '</table><br/>'
          key = ''
        key = line.strip()
        htmldata += dict[key] + '<br/><table id="mytable" cellspacing="0">' + \
                    '<tr><th>索引</th><td>广告Ids</td></tr>'
        continue
      htmldata += self.ProcessLine(line)
    return htmldata
   
  def ProcessRotate(self, path1, zoneid): 
    cmd = "%s %s %s" % (self.PYTHON_BIN, path1, zoneid)
    pipe = os.popen(cmd)
    lines = pipe.readlines()
    count = 0
    htmldata = ''
    for line in lines:
      if count == 3:
        htmldata += '广告位' + str(zoneid) + '<br/><table id="mytable" cellspacing="0">' + \
                    '<tr><th>广告ID</th><th>轮播数</th></tr>'
      if count == 4:
         arr = re.split(' ', line)
         for a in arr:
           a1 = re.split(':', a)
           if len(a1) == 2:
             htmldata += '<tr><td>' + a1[0] + '</td><td>' + a1[1] + '</td></tr>'
         htmldata += '</table><br/>'
      count += 1
    return htmldata

  def POST(self):
    parm_dict = {}
    data = web.data()
    for d in data.split('&'):
      pair = d.split('=')
      if len(pair) == 2 :
        parm_dict[pair[0]] = pair[1]
      else:
        return 'Error'
    #print parm_dict
      
    type1 = parm_dict['type']
    zoneid = int(parm_dict['zoneid'])
    path1 = ''
    htmldata = ''
    if type1 == 'brand':
      path1 = 'AdMobMonitor/AdMobBrandIndex.py'
      htmldata = self.ProcessBrandSelf(path1, zoneid)
    elif type1 == 'self':
      path1 = 'AdMobMonitor/AdMobSelfIndex.py'
      htmldata = self.ProcessBrandSelf(path1, zoneid)
    else:
      path1 = 'AdMobMonitor/AdMobRotate.py'
      htmldata = self.ProcessRotate(path1, zoneid)
    web.header("Content-Type", "text/plain")
    return htmldata

if __name__ == '__main__':
    app.run()
