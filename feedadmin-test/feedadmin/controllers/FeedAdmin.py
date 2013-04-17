# -*- coding: utf8 -*-
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from feedadmin.lib.base import BaseController, render

from feedadmin.model.stypeconfig import StypeConfig
from feedadmin.model.dataversion import DataVersion
from feedadmin.model.versiontplmapping import VersionTplMapping
from feedadmin.model.tplview import TplView

from feedadmin.model.userapply import UserApply

from feedadmin.model.applynew import ApplyNewFeed
from feedadmin.model.applyversion import ApplyNewVersion
from feedadmin.model.applytpl import ApplyNewTpl
from feedadmin.model.applyrollback import ApplyRollback
from feedadmin.model.applypublish import ApplyPublish

from feedadmin.model.feed_stat_total import FeedStatTotal
from feedadmin.model.feed_stat_stype import FeedStatStype
from feedadmin.model.feed_stat_stype_balance import FeedStatStypeBalance
from feedadmin.model.feed_stat_type_balance import FeedStatTypeBalance
from feedadmin.model.feed_stat_userid_stype import FeedStatUseridStype



from feedadmin.model.v1.feed_experi_stat import ExperiStat
from feedadmin.model.v1.web_stype_day_stat import WebStypeDayStat
from feedadmin.model.v1.web_stype_stat import WebStypeStat
from feedadmin.model.v1.view_stat import ViewStat
from feedadmin.model.v1.view_day_stat import ViewDayStat



from feedadmin.lib.base import Session
from sqlalchemy import func, distinct

import sqlalchemy as sa
import sys
# sys.path.append("/usr/lib/python2.6/site-packages/")
sys.path.append("/usr/lib/python2.6/site-packages/site-packages/")
sys.path.append("/data/xce/pylons-dev/ice/")
import feed_admin_reload
import feed_admin_reload_dist

import neo_cgi
import neo_util
import neo_cs
import urllib2
import time
import smtplib

log = logging.getLogger(__name__)

class FeedadminController(BaseController):
  def __before__(self):
    # self.sessions_ = {}

    self.stype_config_ = Session.query(StypeConfig)
    self.version_tpl_mapping_ = Session.query(VersionTplMapping)
    self.data_version_ = Session.query(DataVersion)
    self.tpl_views_ = Session.query(TplView)

    self.apply_feeds_ = Session.query(ApplyNewFeed)
    self.apply_versions_ = Session.query(ApplyNewVersion)
    self.apply_tpls_ = Session.query(ApplyNewTpl)
    self.apply_rollbacks_ = Session.query(ApplyRollback)
    self.apply_publishs_ = Session.query(ApplyPublish)

    self.user_applies_ = Session.query(UserApply)

    self.feed_stat_total_ = Session.query(FeedStatTotal)
    self.feed_stat_stype_ = Session.query(FeedStatStype)








  def ExperiSignin(self):
    return render('/experi-signin.mako');

  def ExperiSelect(self):
    return render('/experi-select.mako');

  def ExperiList(self):
      if 1 == 1:
      	ret = ''
      	feed_stat = Session.query(ExperiStat.number.label('number'),\
                    	ExperiStat.begin.label('begin'), \
                    	ExperiStat.end.label('end'), \
                    	ExperiStat.tail.label('tail'), \
                    	ExperiStat.describ.label('describ'), \
                    	ExperiStat.contact.label('contact'), \
                    	ExperiStat.summary.label('summary'), \
                    ).order_by(ExperiStat.begin.desc())
        ret = '['
        if feed_stat:
          for o in feed_stat:
            ret += '{'
            
            if o.number:              ret += '"number":' + str(o.number) 
            else:                   ret += '"number":-1'
            if o.begin:              ret += ', "begin":' + str(o.begin)
            else:              		ret += ', "begin":0'
            if o.end:              ret += ', "end":' + str(o.end)
            else:              	      ret += ', "end":0'
            if o.tail:              ret += ', "tail":"' + str(o.tail) + '"'
            else:              	     ret += ', "tail":"NULL"'
            if o.describ:              ret += ', "describ":"' + str(o.describ) + '"'
            else:                    ret += ', "describ":"NULL"'
            if o.contact:              ret += ', "contact":"' + str(o.contact) + '"'
            else:                    ret += ', "contact":"NULL"'
            if o.summary:              ret += ', "summary":"' + str(o.summary) + '"'
            else:                    ret += ', "summary":"NULL"'
            
            ret += '},'
        ret += ']'
        return ret;

  def ExperiInsert(self):
      begin = (request.params.get('begin'))
      end = (request.params.get('end'))
      tail = request.params.get('tail')
      describ = request.params.get('describ')
      contact = request.params.get('contact')
      item = ExperiStat(begin, end, tail, describ, contact)
      Session.add(item)
      Session.commit()
      return contact


#select date, sum(uv), sum(feed_cnt) from  view_stat where view=0 group by date;
#select date,   sum(click) from web_stype_stat group by date;
  def StatWebData(self): # stat.mako
      if 1 == 1:
      	ret = ''
      	feed_stat = Session.query(ViewDayStat.date.label('date'),\
                    	ViewDayStat.view.label('view'), \
                    	func.sum(ViewDayStat.uv).label('uv'), \
                    	func.sum(ViewDayStat.feed_sum).label('feed_sum'), \
                    ).filter_by(view="0").group_by(ViewDayStat.date)

       	feed_stat2 = Session.query(WebStypeDayStat.date.label('date'),\
                    	func.sum(WebStypeDayStat.click_sum).label('click_sum'), \
                    	#func.sum(WebStypeStat.reply_sum).label('reply_sum'), \
                    ).filter_by(stype="all").group_by(WebStypeDayStat.date)
        ret = '['
        if feed_stat:
          #for o,k in feed_stat,feed_stat2:
          for o in feed_stat:
            tm = []
            ret += '{'
           
            if o.date: tdate=int(o.date)
            else : tdate = 0
            tm.extend([tdate/10000, tdate/100%100, tdate%100]) 

            #if o.time: ttime=int(o.time)
            #else: ttime=0
            #tm.extend([ttime, 0, 0, 0, 0, 0])           
            tm.extend([0, 0, 0, 0, 0, 0])           

            restime = time.mktime(tm)
            ret += '"date":' + str(int(restime*1000)) 
            
            #if o.date:              ret += '"date":' + str(o.date) 
            #else:                   ret += '"date":-1'
            if o.uv:              ret += ', "uv":' + str(o.uv)
            else:              		ret += ', "uv":0'
            if o.feed_sum:              ret += ', "feed_sum":' + str(o.feed_sum)
            else:              	      ret += ', "feed_sum":0'
           
            f=0
            cnt = 0
            for k in feed_stat2:
              cnt = cnt + 1
              if k.date == o.date:
                f = 1
                ret += ', "click_sum":' + str(k.click_sum) 
                #ret += ', "reply_sum":' + str(k.reply_sum) 
            if f ==0 :
              ret += ', "click_sum":' + str(o.date)
              #ret += ', "reply_sum":0'

            ret += '},'
        ret+='{}'
        ret += ']'
        return ret;

  def StatAllData(self): # stat.mako  TODO
      if 1 == 1:
      	ret = ''
      	feed_stat = Session.query(ViewStat.date.label('date'),\
                    	func.sum(ViewStat.uv).label('uv'), \
                    	func.sum(ViewStat.feed_sum).label('feed_sum'), \
                    	ViewStat.view.label('view'), \
                    ).filter_by(view="0").group_by(ViewStat.date)

       	feed_stat2 = Session.query(WebStypeStat.date.label('date'),\
                    	func.sum(WebStypeStat.click_sum).label('click_sum'), \
                    	#func.sum(WebStypeStat.reply_sum).label('reply_sum'), \
                    ).filter_by(stype="all").group_by(WebStypeStat.date)
        ret = '['
        if feed_stat:
          #for o,k in feed_stat,feed_stat2:
          for o in feed_stat:
            ret += '{'
            
            if o.date:              ret += '"date":' + str(o.date) 
            else:                   ret += '"date":-1'
            if o.uv:              ret += ', "uv":' + str(o.uv)
            else:              		ret += ', "uv":0'
            if o.feed_sum:              ret += ', "feed_sum":' + str(o.feed_sum)
            else:              	      ret += ', "feed_sum":0'
           
            f=0
            for k in feed_stat2:
              if k.date == o.date:
                f = 1
                ret += ', "click_sum":' + str(k.click_sum) 
                #ret += ', "reply_sum":' + str(k.reply_sum) 
            if f ==0 :
              ret += ', "click_sum":0'
              #ret += ', "reply_sum":0'

            ret += '},'
        ret+='{}'
        ret += ']'
        return ret;


  def ABDebug(self):
    return render('/stat-ABDebug.mako');

  def ABDebugData(self):
      day = int(request.params.get('day'))
      mstype = request.params.get('stype')
      if 1 == 1:
        if day == 0:
#select date,time,uid, sum(feed_sum), sum(dispatch_cnt), sum(reply_sum), sum(click_sum), avg(position_clk) from web_stype_stat where stype="all" group by  date, time, uid;
        	ret = ''
        	feed_stat = Session.query(\
  			WebStypeStat.date.label('date'),\
  			WebStypeStat.time.label('time'),\
  			WebStypeStat.uid.label('uid'),\
                      	func.sum(WebStypeStat.feed_sum).label('feed_sum'), \
                      	func.sum(WebStypeStat.dispatch_cnt).label('dispatch_cnt'), \
                      	func.sum(WebStypeStat.reply_sum).label('reply_sum'), \
                      	func.sum(WebStypeStat.click_sum).label('click_sum'), \
                      	func.avg(WebStypeStat.position_clk).label('position_clk'), \
                      	func.avg(WebStypeStat.position_show).label('position_show'), \
                      ).filter_by(stype=mstype).group_by(WebStypeStat.date).group_by(WebStypeStat.time).group_by(WebStypeStat.uid)
        if day == 1: 
        	ret = ''
  #select date,time, sum(feed_sum), sum(dispatch_cnt), sum(reply_sum), sum(click_sum), avg(position_clk) from web_stype_stat where stype=="all" group by  date, time;
        	feed_stat = Session.query(\
  			WebStypeDayStat.date.label('date'),\
  			WebStypeDayStat.uid.label('uid'),\
                      	func.sum(WebStypeDayStat.feed_sum).label('feed_sum'), \
                      	func.sum(WebStypeDayStat.dispatch_cnt).label('dispatch_cnt'), \
                      	func.sum(WebStypeDayStat.reply_sum).label('reply_sum'), \
                      	func.sum(WebStypeDayStat.click_sum).label('click_sum'), \
                      	func.avg(WebStypeDayStat.position_clk).label('position_clk'), \
                      	func.avg(WebStypeDayStat.position_show).label('position_show'), \
                      ).filter_by(stype=mstype).group_by(WebStypeDayStat.date).group_by(WebStypeDayStat.uid)

        tdate = 0
        ttime = 0
        restime = 0

        ret = '['
        if feed_stat:
          #for o,k in feed_stat,feed_stat2:
          for o in feed_stat:
            tm = []
            ret += '{'

            if o.date: tdate=int(o.date)
            else : tdate = 0
            tm.extend([tdate/10000, tdate/100%100, tdate%100]) 

            if day==0 and o.time: ttime=int(o.time)
            else: ttime=0
            tm.extend([ttime, 0, 0, 0, 0, 0])           

            restime = time.mktime(tm)
            ret += '"date":' + str(int(restime*1000)) 
            #ret += '"date":' + str(int(tdate*100) + ttime) 
            if o.uid:              ret += ', "uid":' + str(o.uid)
            else:              		ret += ', "uid":0'
            if o.feed_sum:              ret += ', "feed_sum":' + str(o.feed_sum)
            else:              		ret += ', "feed_sum":0'
            if o.dispatch_cnt:              ret += ', "dispatch_cnt":' + str(o.dispatch_cnt)
            else:              		ret += ', "dispatch_cnt":0'
            if o.reply_sum:              ret += ', "reply_sum":' + str(o.reply_sum)
            else:              	      ret += ', "reply_sum":0'
            if o.click_sum:              ret += ', "click_sum":' + str(o.click_sum)
            else:              		ret += ', "click_sum":0'
            if o.position_clk:              ret += ', "position_clk":' + str(o.position_clk)
            else:              		ret += ', "position_clk":0'
            if o.position_show:              ret += ', "position_show":' + str(o.position_show)
            else:              		ret += ', "position_show":0'
           
            ret += '},'
        ret+='{}'
        ret += ']'
        return ret;


  def CheckPlat(self): # check-select.mako
    view = (request.params.get('view'))
    if view == "all" :
      c.name = -1
      return render('/check-plat.mako');
    if view == "view0" :
      c.name = 0
      return render('/check-plat.mako');
    if view == "view2" :
      c.name = 2
      return render('/check-plat.mako');
    if view == "view3" :
      c.name = 3
      return render('/check-plat.mako');
    if view == "view4" :
      c.name = 4
      return render('/check-plat.mako');
    if view == "view6" :
      c.name = 6
      return render('/check-plat.mako');
    #return render('/check-select.mako');
    c.name = -1
    return render('/check-plat.mako');

  def ViewDayList(self): # check-plat.mako
      day = int(request.params.get('day'))
      view = int(request.params.get('view'))
      if day==1:
        if view == -1: # ALL
        	ret = ''
  #mysql> select date,sum(uv), sum(feed_sum) from  view_day_stat where view="all" group by date;
  
        	feed_stat = Session.query(ViewDayStat.date.label('date'),\
                      	func.sum(ViewDayStat.uv).label('uv'), \
                      	func.sum(ViewDayStat.rv).label('rv'), \
                      	func.sum(ViewDayStat.session_cnt).label('secnt'), \
                      	func.sum(ViewDayStat.session_sum).label('sesum'), \
                      	func.sum(ViewDayStat.feed_sum).label('feed_sum'), \
                      ).filter_by(view="all").group_by(ViewDayStat.date)
        if view != -1:
        	ret = ''
        	feed_stat = Session.query(ViewDayStat.date.label('date'),\
                      	func.sum(ViewDayStat.uv).label('uv'), \
                      	func.sum(ViewDayStat.rv).label('rv'), \
                      	func.sum(ViewDayStat.session_cnt).label('secnt'), \
                      	func.sum(ViewDayStat.session_sum).label('sesum'), \
                      	func.sum(ViewDayStat.feed_sum).label('feed_sum'), \
                      ).filter_by(view=str(view)).group_by(ViewDayStat.date)
        ret = '['
        if feed_stat:
          #for o,k in feed_stat,feed_stat2:
          for o in feed_stat:
            tm = []
            ret += '{'
            
            if o.date: tdate=int(o.date)
            else : tdate = 0
            tm.extend([tdate/10000, tdate/100%100, tdate%100]) 
  
            #if o.time: ttime=int(o.time)
            #else: ttime=0
            #tm.extend([ttime, 0, 0, 0, 0, 0])           
            tm.extend([0, 0, 0, 0, 0, 0])           
  
            restime = time.mktime(tm)
            ret += '"date":' + str(int(restime*1000)) 
            #if o.date:              ret += '"date":' + str(o.date) 
            #else:                   ret += '"date":-1'
            if o.uv:              ret += ', "uv":' + str(o.uv)
            else:              		ret += ', "uv":0'
            if o.rv:              ret += ', "rv":' + str(o.rv)
            else:              		ret += ', "rv":0'
            if o.feed_sum:              ret += ', "feed_sum":' + str(o.feed_sum)
            else:              	      ret += ', "feed_sum":0'
            if o.secnt:              ret += ', "secnt":' + str(o.secnt)
            else:              		ret += ', "secnt":0'
            if o.sesum:              ret += ', "sesum":' + str(o.sesum)
            else:              		ret += ', "sesum":0'
           
            ret += '},'
        ret+='{}'
        ret += ']'
        return ret;


      if day==0:
        if view == -1: # ALL
        	ret = ''
        	feed_stat = Session.query(ViewStat.date.label('date'),\
                        ViewStat.time.label('time'),\
                      	func.sum(ViewStat.uv).label('uv'), \
                      	func.sum(ViewStat.rv).label('rv'), \
                      	func.sum(ViewStat.session_cnt).label('secnt'), \
                      	func.sum(ViewStat.session_sum).label('sesum'), \
                      	func.sum(ViewStat.feed_sum).label('feed_sum'), \
                      ).filter_by(view="all").group_by(ViewStat.date).group_by(ViewStat.time)
        if view != -1:
        	ret = ''
        	feed_stat = Session.query(ViewStat.date.label('date'),\
                        ViewStat.time.label('time'),\
                      	func.sum(ViewStat.uv).label('uv'), \
                      	func.sum(ViewStat.rv).label('rv'), \
                      	func.sum(ViewStat.session_cnt).label('secnt'), \
                      	func.sum(ViewStat.session_sum).label('sesum'), \
                      	func.sum(ViewStat.feed_sum).label('feed_sum'), \
                      ).filter_by(view=str(view)).group_by(ViewStat.date).group_by(ViewStat.time)
  
      ret = '['
      if feed_stat:
        #for o,k in feed_stat,feed_stat2:
        for o in feed_stat:
          tm = []
          ret += '{'
          
          if o.date: tdate=int(o.date)
          else : tdate = 0
          tm.extend([tdate/10000, tdate/100%100, tdate%100]) 

          if o.time: ttime=int(o.time)
          else: ttime=0
          tm.extend([ttime, 0, 0, 0, 0, 0])           
          #tm.extend([0, 0, 0, 0, 0, 0])           

          restime = time.mktime(tm)
          ret += '"date":' + str(int(restime*1000)) 
          #if o.date:              ret += '"date":' + str(o.date) 
          #else:                   ret += '"date":-1'
          if o.uv:              ret += ', "uv":' + str(o.uv)
          else:              		ret += ', "uv":0'
          if o.rv:              ret += ', "rv":' + str(o.rv)
          else:              		ret += ', "rv":0'
          if o.feed_sum:              ret += ', "feed_sum":' + str(o.feed_sum)
          else:              	      ret += ', "feed_sum":0'
          if o.secnt:              ret += ', "secnt":' + str(o.secnt)
          else:              		ret += ', "secnt":0'
          if o.sesum:              ret += ', "sesum":' + str(o.sesum)
          else:              		ret += ', "sesum":0'
         
          ret += '},'
      ret+='{}'
      ret += ']'
      return ret;

  def CheckStype(self):
    return render('/check-stype.mako');

  def WebStypeList(self):
      day = int(request.params.get('day'))
      mstype = request.params.get('stype')
      if 1 == 1:
        if day == 0:
        	ret = ''
  #select date,time, sum(feed_sum), sum(dispatch_cnt), sum(reply_sum), sum(click_sum), avg(position_clk) from web_stype_stat where stype=="all" group by  date, time;
        	feed_stat = Session.query(\
  			WebStypeStat.date.label('date'),\
  			WebStypeStat.time.label('time'),\
                      	func.sum(WebStypeStat.feed_sum).label('feed_sum'), \
                      	func.sum(WebStypeStat.dispatch_cnt).label('dispatch_cnt'), \
                      	func.sum(WebStypeStat.reply_sum).label('reply_sum'), \
                      	func.sum(WebStypeStat.click_sum).label('click_sum'), \
                      	func.avg(WebStypeStat.position_clk).label('position_clk'), \
                      	func.avg(WebStypeStat.position_show).label('position_show'), \
                      ).filter_by(stype=mstype).group_by(WebStypeStat.date).group_by(WebStypeStat.time)
        if day == 1: 
        	ret = ''
  #select date,time, sum(feed_sum), sum(dispatch_cnt), sum(reply_sum), sum(click_sum), avg(position_clk) from web_stype_stat where stype=="all" group by  date;
        	feed_stat = Session.query(\
  			WebStypeDayStat.date.label('date'),\
                      	func.sum(WebStypeDayStat.feed_sum).label('feed_sum'), \
                      	func.sum(WebStypeDayStat.dispatch_cnt).label('dispatch_cnt'), \
                      	func.sum(WebStypeDayStat.reply_sum).label('reply_sum'), \
                      	func.sum(WebStypeDayStat.click_sum).label('click_sum'), \
                      	func.avg(WebStypeDayStat.position_clk).label('position_clk'), \
                      	func.avg(WebStypeDayStat.position_show).label('position_show'), \
                      ).filter_by(stype=mstype).group_by(WebStypeDayStat.date)
 

        tdate = 0
        ttime = 0
        restime = 0

        ret = '['
        if feed_stat:
          #for o,k in feed_stat,feed_stat2:
          for o in feed_stat:
            tm = []
            ret += '{'

            if o.date: tdate=int(o.date)
            else : tdate = 0
            tm.extend([tdate/10000, tdate/100%100, tdate%100]) 

            try:
              if o.time: ttime=int(o.time)
              else: ttime=0
            except:
             ttime=0
            tm.extend([ttime, 0, 0, 0, 0, 0])           

            restime = time.mktime(tm)
            ret += '"date":' + str(int(restime*1000)) 
            #ret += '"date":' + str(int(tdate*100) + ttime) 
            if o.feed_sum:              ret += ', "feed_sum":' + str(o.feed_sum)
            else:              		ret += ', "feed_sum":0'
            if o.dispatch_cnt:              ret += ', "dispatch_cnt":' + str(o.dispatch_cnt)
            else:              		ret += ', "dispatch_cnt":0'
            if o.reply_sum:              ret += ', "reply_sum":' + str(o.reply_sum)
            else:              	      ret += ', "reply_sum":0'
            if o.click_sum:              ret += ', "click_sum":' + str(o.click_sum)
            else:              		ret += ', "click_sum":0'
            if o.position_clk:              ret += ', "position_clk":' + str(o.position_clk)
            else:              		ret += ', "position_clk":0'
            if o.position_show:              ret += ', "position_show":' + str(o.position_show)
            else:              		ret += ', "position_show":0'
           
            ret += '},'
        ret+='{}'
        ret += ']'
        return ret;

 

#-----------------------------------------------------------------------------------------------





  def AddLoginUser(self, user, ticket):
    print 'add session : ', ticket
    if ticket in session:
      session[ticket]["time"] = time.time()
    else:
      session[ticket] = {}
      session[ticket]["user"] = user
      session[ticket]["time"] = time.time()
    session.save()

  def CheckLoginUser(self, ticket):
    if ticket in session:
      if time.time() - session[ticket]["time"] > 1800.0:
        print 'session', ticket, 'timeout'
        del(session[ticket])
        session.save()
        return ''
      session[ticket]["time"] = time.time()
      return session[ticket]["user"]
    print 'session', ticket, 'not found'
    return ''

  def GetUserId(self, req, rsp):
    user = ''

    if "ticket" in req.cookies:
      ticket = str(req.cookies['ticket'])
      print 'cookie session : ', ticket
      user = self.CheckLoginUser(ticket)

    if len(user) <= 0 and 'ticket' in req.params:
      ticket = str(req.params['ticket'])
      #try:
      headers = {'Referer' : ticket}
      httpreq = urllib2.Request('https://passport.no.opi-corp.com/verify.php?t=' + ticket, None, headers)
      c = urllib2.urlopen(httpreq)
      user = c.read()
      if user:
        self.AddLoginUser(user, ticket)
      #except Exception, e:
      # print "error : open url %s failed", str(e)

    if user:
      rsp.set_cookie('ticket', ticket, max_age=1800)
    return user

  def UserRight(self, req, rsp):
    cookies = req.cookies
    user_id = self.GetUserId(req, rsp)
    print 'user id : ------ ', user_id 
    if len(user_id) == 0:
      return 0

    if user_id in ['yuwei.mu']:
      return 3

    if user_id in ['fei.yuan', 'tiean.zhang', 'qun.liu', 'zizhong.zhang', 'tinghai.zhang']:
      return 3
    if user_id in ['fei.yuan', 'yuwei.mu', 'tiean.zhang', 'di.liu', 'qun.liu', 'zizhong.zhang', 'tinghai.zhang']:
      return 2

    return 1

  def FeedListView(self):
    list_filter = 0
    if "filter" in request.params:
      list_filter = int(request.params['filter'])
    return render('/feed-list.mako', {"user_right" : self.UserRight(request, response), "list_filter" : list_filter})

  def FilterByStatus(self, stype, filter):
#   <option value="0">所有</option>
#   <option value="1">禁用</option>
#   <option value="2">测试</option>
#   <option value="3">线上所有</option>
#   <option value="4">线上只读</option>
#   <option value="5">线上可发送</option>
    if filter == 0:
      return True
    if filter == 1:
      ver = self.data_version_.filter_by(stype = stype, status = 0).first()
      return ver != None
    if filter == 2:
      ver = self.data_version_.filter_by(stype = stype, status = 1).first()
      return ver != None
    if filter == 3:
      ver = self.data_version_.filter_by(stype = stype, status = 2).first()
      if not ver:
        ver = self.data_version_.filter_by(stype = stype, status = 3).first()
      return ver != None
    if filter == 4:
      ver = self.data_version_.filter_by(stype = stype, status = 2).first()
      return ver != None
    if filter == 5:
      ver = self.data_version_.filter_by(stype = stype, status = 3).first()
      return ver != None
    return False;

  def GetStypeList(self):
    list_filter = 0
    if "filter" in request.params:
      list_filter = int(request.params['filter'])

    rsp = '['
    count = 0
    for o in self.stype_config_.all():
      if not self.FilterByStatus(o.stype, list_filter):
        continue

      if count > 0:
        rsp += ','
      
      rsp += '{"stype":' + str(o.stype) 
      rsp += ', "persist_body":' + str(o.is_persist_content)
      rsp += ', "persist_feeddb":' + str(o.is_persist_feeddb)
      rsp += ', "news_merge_type":' + str(o.news_merge_type)
      rsp += ', "mini_merge_type":' + str(o.mini_merge_type)
      rsp += ', "push_feed_flags":' + str(o.push_flag)
      rsp += ', "weight":' + str(o.weight)
      rsp += ', "lifetime":' + str(o.lifetime)
      rsp += ', "description":"' + o.description + '"'
      ver = self.data_version_.filter_by(stype = o.stype, status = 3).first()
      if (ver):
         rsp += ', "dispatching_ver":' + str(ver.version)
      else:
         rsp += ', "dispatching_ver":0'
      rsp += '}'

      count += 1
    rsp += ']'
    return rsp

  def GetStypeIds(self):
    ids = Session.query(StypeConfig.stype)
    rsp = '['
    count = 0
    for o in ids:
      if count > 0:
        rsp += ','
      rsp += str(o[0])
      count += 1
    rsp += ']'
    return rsp

  def UpdateStypeVersionUsingId(self):
    if self.UserRight(request, response) < 2:
      return '"没有操作权限, 请确保管理员帐号登录"'

    stype = int(request.params['stype'])
    version = int(request.params['version'])
    tpl_id = int(request.params['tpl_id'])
    if stype > 0 and version > 0 and tpl_id >= 0:
      ver = self.data_version_.filter_by(stype = stype, version = version).first()
      if ver:
        ver.using_tpl_id = tpl_id
      else:
        ver = DataVersion(stype, version, 0, tpl_id, 0)
        Session.add(ver)
      Session.commit()
      return '保存成功' + str(ver.using_tpl_id)
    return '参数有错误'

  def GetStypeVersionInfo(self):
    stype = int(request.params['stype'])
    version = int(request.params['version'])

    if stype > 0 and version > 0:
      ver = self.data_version_.filter_by(stype = stype, version = version).first()
      cfg = self.stype_config_.filter_by(stype=stype).first()
      if ver:
        keys_escaped = ver.keys_xml.replace('"', '\\"');
        return '{"status":' + str(ver.status) + \
            ',"using_id":' + str(ver.using_tpl_id) + \
            ',"test_id":' + str(ver.test_tpl_id) + \
            ',"news_merge_by":"' + str(ver.news_merge_by) + '"' + \
            ',"mini_merge_by":"' + str(ver.mini_merge_by) + '"' + \
            ',"source_by":"' + str(ver.source_by) + '"' + \
            ',"psource_by":"' + str(ver.psource_by) + '"' + \
            ',"actor_by":"' + str(ver.actor_by) + '"' + \
            ',"togroup_by":"' + str(ver.togroup_by) + '"' + \
            ',"dispatch_expr":"' + urllib2.quote(str(ver.dispatch_expr)) + '"' + \
            ',"is_custom_expr":' + str(cfg.is_custom_expr) + \
            ',"stype_comment":"' + str(cfg.description) + '"' + \
            ',"keys_xml":"' + keys_escaped + '"' + \
            '}'
    return '{"status":0, "using_id":-1,"test_id":-1, "news_merge_by":"", "mini_merge_by":"", "source_by":"", "psource_by":"", "actor_by":"", "dispatch_expr":""}'

  def UpdateStypeVersionTestId(self):
    stype = int(request.params['stype'])
    version = int(request.params['version'])
    tpl_id = int(request.params['tpl_id'])
    if stype > 0 and version > 0 and tpl_id >= 0:
      ver = self.data_version_.filter_by(stype = stype, version = version).first()
      if ver:
        ver.test_tpl_id = tpl_id
      else:
        ver = DataVersion(stype, version, tpl_id, 0)
        Session.add(ver)
      Session.commit()
      return '保存成功' + str(ver.test_tpl_id)
    return '参数有错误'

  def UpdateStypeVersionStatus(self):
    if self.UserRight(request, response) < 2:
      return '"没有操作权限, 请确保管理员帐号登录"'

    stype = int(request.params['stype'])
    version = int(request.params['version'])
    status = int(request.params['status'])

    if status >= 2 and self.UserRight(request, response) < 3:
      return '您没有上线权限'

    if stype > 0 and version > 0:
      ver = self.data_version_.filter_by(stype = stype, version = version).first()
      if ver:
        ver.status = status
        Session.commit()
        return '保存成功' + str(ver.status)
      else:
        return '版本 ' + str(version) + '不存在'
    return '参数有错误'

  def UpdateTplViewStatus(self):
    if self.UserRight(request, response) < 2:
      return '没有操作权限, 请确保管理员帐号登录'

    tpl_id = int(request.params['tpl_id'])
    view = int(request.params['view'])
    status = int(request.params['status'])

    if tpl_id > 0:
      tpl = self.tpl_views_.filter_by(tpl_id = tpl_id, view = view).first()
      if tpl:
        tpl.status = status
        Session.commit()
        return '成功保存状态为 : ' + str(tpl.status)
      else:
        return '视图 ' + str(view) + '不存在'
    return '参数有错误'


  def GetStypeVersions(self):
    stype = -1
    if "stype" in request.params:
      stype = int(request.params['stype'])
    versions = self.data_version_.filter_by(stype = int(request.params['stype']))
    ret = '['
    count = 0
    for v in versions:
      if count > 0:
        ret += ','
      ret += '{"version":' + str(v.version)
      ret += ',"test_tpl_id":' + str(v.test_tpl_id)
      ret += ',"using_tpl_id":' + str(v.using_tpl_id)
      ret += ',"status":' + str(v.status) + '}'
      count += 1
    ret += ']'
    return ret

  def GetStypeVersionTpls(self):
    stype = -1
    version = -1
    if "stype" in request.params:
      stype = int(request.params['stype'])
      if "version" in request.params:
        version = int(request.params['version'])

    tpls = self.version_tpl_mapping_.filter_by(stype = stype, version = version)
    ret = '['
    count = 0
    for v in tpls:
      if count > 0:
        ret += ','
      ret += str(v.tpl_id)
      count += 1
    ret += ']'
    return ret
  def Hello(self):
    # return render('/hello.mako', {"hello" : ("你好").decode('utf-8')})
    print '------------' + request.params['t'] + '---------'
    return ''

  def StypeConfigEdit(self):
    stype = -1
    from_version_id = 0
    apply_id = 0
    uid = 0
    if "id" in request.cookies:
      uid = int(request.cookies['id'])

    if "stype" in request.params:
      stype = int(request.params['stype'])
      if "apply_id" in request.params and "from_version_id" in request.params:
        apply_id = int(request.params['apply_id'])
        from_version_id = int(request.params['from_version_id'])

    return render('/feed-config-edit.mako', {"stype" : stype, 
        "user_right" : self.UserRight(request, response), 
        "apply_id" : apply_id, 
        "from_version_id" : from_version_id})

  def StypeConfigCreate(self):
    apply_id = 0
    if "apply_id" in request.params:
      apply_id = int(request.params['apply_id'])

    return render('/feed-config-create.mako', {"apply_id" : apply_id})

  def UserApply(self):
    return render('/user-apply.mako')

  def UserApplyList(self):
    return render('/user-apply-list.mako')

  def SetUserApplyHandled(self):
    if self.UserRight(request, response) < 2:
      return '"没有操作权限, 请确保管理员帐号登录"'

    apply_id = int(request.params['apply_id'])
    if apply_id > 0:
      apply = self.user_applies_.filter_by(apply_id = apply_id).first()
      if apply:
        apply.status = 1
        Session.commit()
        return "设置成功"
      else:
        return '该申请不存在'
    return "apply_id参数错误"

  def RemoveUserApply(self):
    apply_id = request.params['apply_id']
    a = self.user_applies_.filter_by(apply_id = apply_id).first()
    Session.delete(a)
    Session.commit()
    return '删除成功'
 

  def GetUserApplyItem(self):
    apply_id = request.params['apply_id']
    a = self.user_applies_.filter_by(apply_id = apply_id).first()

    if a:
      ret = '{"apply_id":' + str(a.apply_id)
      ret += ',"pm_names":"' + a.pm_names.replace('"', '\\"') + '"'
      ret += ',"pm_emails":"' + a.pm_emails + '"'
      ret += ',"dev_names":"' + a.dev_names.replace('"', '\\"') + '"'
      ret += ',"dev_emails":"' + a.dev_emails + '"'
      ret += ',"feed_stype":' + str(a.feed_stype)
      ret += ',"feed_desc":"' + a.feed_desc.replace('"', '\\"') + '"'
      ret += ',"apply_type":' + str(a.apply_type)
      ret += ',"apply_desc":"' + a.apply_desc.replace('"', '\\"') + '"'
      ret += ',"push_news":' + str(a.push_news)
      ret += ',"push_mini":' + str(a.push_mini)
      ret += ',"news_merge_desc":"' + a.news_merge_desc.replace('"', '\\"') + '"'
      ret += ',"mini_merge_desc":"' + a.mini_merge_desc.replace('"', '\\"') + '"'
      ret += ',"status":' + str(a.status)
      ret += '}'
      return ret
    return '{}'


  def GetUserApplyList(self):
    applies = self.user_applies_.all()
    count = 0
    ret = '['
    for a in applies:
      if count > 0:
        ret += ','
      ret += '{"apply_id":' + str(a.apply_id)
      ret += ',"pm_names":"' + a.pm_names.replace('"', '\\"') + '"'
      ret += ',"feed_stype":' + str(a.feed_stype)
      ret += ',"feed_desc":"' + a.feed_desc.replace('"', '\\"') + '"'
      ret += ',"status":' + str(a.status)
      ret += '}'
      count += 1
    ret += ']'
    return ret

  def UserApplySubmit(self):
    pm_emails = request.params['pm_emails']
    pm_names = request.params['pm_names']
    feed_desc = request.params['feed_desc']
    apply_id = 0
    if "apply_id" in request.params:
      apply_id = int(request.params['apply_id'])

    print "apply_id", apply_id

    if "apply_id" in request.params:
      a = self.user_applies_.filter_by(apply_id = apply_id).first()
      if a:
        a.pm_names = pm_names
        a.pm_emails = pm_emails
        a.dev_names = request.params['dev_names']
        a.dev_emails = request.params['dev_emails']
        a.feed_stype = int(request.params['feed_stype'])
        a.feed_desc = feed_desc
        a.apply_type = int(request.params['apply_type'])
        a.apply_desc = request.params['apply_desc']
        a.push_news = int(request.params['push_news'])
        a.push_mini = int(request.params['push_mini'])
        a.news_merge_desc = request.params['news_merge_desc']
        a.mini_merge_desc = request.params['mini_merge_desc']
        a.status = 0
        a.apply_time = int(time.time())
      else:
        return '申请id不群在'
    else:
      max_id = Session.query(func.max(UserApply.apply_id)).scalar() or 0
      a = UserApply(max_id + 1,
          pm_names = pm_names, 
          pm_emails = pm_emails, 
          dev_names = request.params['dev_names'], 
          dev_emails = request.params['dev_emails'], 
          feed_stype = int(request.params['feed_stype']), 
          feed_desc = feed_desc, 
          apply_type = int(request.params['apply_type']), 
          apply_desc = request.params['apply_desc'], 
          push_news = int(request.params['push_news']), 
          push_mini = int(request.params['push_mini']), 
          news_merge_desc = request.params['news_merge_desc'], 
          mini_merge_desc = request.params['mini_merge_desc'], 
          status = 0,
          apply_time = int(time.time())
          )
      Session.add(a)
    Session.commit()

    # self.SendMail('yuwei.mu@renren-inc.com', pm_emails, '申请创建新鲜事类型', pm_names + ':' + stype_desc)
    return '申请保存成功'

  def ApplyNewFeed(self):
    return render('/apply-new-feed.mako')

  def ApplyNewVersion(self):
    return render('/apply-new-version.mako')

  def ApplyNewTpl(self):
    return render('/apply-new-tpl.mako')

  def ApplyRollback(self):
    return render('/apply-rollback.mako')

  def ApplyPublish(self):
    return render('/apply-publish.mako')

  def FeedKeysEdit(self):
    stype = -1
    version = -1
    is_user = 0 
    apply_id = 0 

    from_tpl_id = 0
    if "stype" in request.params:
      stype = int(request.params['stype'])
      if "version" in request.params:
        version = int(request.params['version'])
        if "apply_id" in request.params and "from_tpl_id" in request.params:
          apply_id = int(request.params['apply_id'])
          from_tpl_id = int(request.params['from_tpl_id'])

    if "is_user" in request.params:
      is_user = int(request.params['version'])

    return render('/feed-keys-edit.mako', 
        {"stype" : stype, 
         "user_right" : self.UserRight(request, response),
         "version" : version, 
         "from_tpl_id" : from_tpl_id, 
         "apply_id" : apply_id, 
         "is_user" : is_user})

  def FeedTplEdit(self):
    stype = -1
    version = -1
    tpl_id = -1
    if "stype" in request.params:
      stype = int(request.params['stype'])
    if "version" in request.params:
      version = int(request.params['version'])
    if "tpl_id" in request.params:
      tpl_id = int(request.params['tpl_id'])

    ver = self.data_version_.filter_by(stype = stype, version = version).first()
    if not ver:
      return "参数错误"
    tpl_using = 0
    if tpl_id > 0 and tpl_id == ver.using_tpl_id:
      tpl_using = 1

    return render('/feed-tpl-edit.mako', {"stype" : stype, 
        "version" : version, "tpl_id" : tpl_id, "tpl_using" : tpl_using,
        "user_right" : self.UserRight(request, response)})

  def GetStypeConfig(self):
    cfg = self.stype_config_.filter_by(stype=int(request.params['stype'])).first()
    if not cfg:
      cfg = StypeConfig(stype = int(request.params['stype']), 
          weight = 1, 
          type = int(request.params['stype']) / 100, 
          ptype = 0, 
          description = '', 
          push_feed_flags = 0, 
          news_merge_type = 0,
          mini_merge_type = 0,
          update_time_on_merge = 0,
          custom_expr = 0,
          persist_body = 0,
          persist_feeddb = 0,
          lifetime = 0,
          daily_quota = 0,
         
          news_merge_by = '', 
          mini_merge_by = '', 
          source_by = '', 
          psource_by = '', 
          actor_by = '', 
          dispatch_expr = '')
    print cfg.description
    return render('/feed-config.mako', {
        "stype" : cfg.stype, 
        "type" : cfg.type,
        "weight" : cfg.weight,
        "desc" : cfg.description.decode('utf-8'),
        "ptype" : cfg.ptype,
        "save_content" : cfg.is_persist_content,
        "save_feed_db" : cfg.is_persist_feeddb,
        "news_merge_type" : cfg.news_merge_type,
        "mini_merge_type" : cfg.mini_merge_type,
        "push_flags" : cfg.push_flag,
        "custom_expr" : cfg.is_custom_expr,
        "update_time_on_merge" : cfg.is_update_time,
        "lifetime" : cfg.lifetime,
        "daily_quota" : cfg.daily_quota
       }
    )

  def SaveStypeConfig(self):
    if self.UserRight(request, response) < 2:
      return '{"status":1, "desc":"没有操作权限, 请确保管理员帐号登录"}'

    cfg = self.stype_config_.filter_by(stype=int(request.params['stype'])).first()
    if not cfg:
      cfg = StypeConfig(stype = int(request.params['stype']), 
          weight = int(request.params['weight']), 
          type = int(request.params['type']), 
          ptype = int(request.params['ptype']), 
          description = request.params['title'], 
          push_feed_flags = int(request.params['push_flags']), 
          news_merge_type = int(request.params['news_merge_type']),
          mini_merge_type = int(request.params['mini_merge_type']),
          is_update_time_on_merge = int(request.params['update_time_on_merge']),
          is_custom_expr = int(request.params['custom_expr']),
          persist_body = int(request.params['save_content']),
          persist_feeddb = int(request.params['save_feed_db']),
          lifetime = int(request.params['lifetime']),
          daily_quota = int(request.params['daily_quota']))

      Session.add(cfg)
      if 'apply_id' in request.params:
        apply_id = int(request.params['apply_id'])
        self.FeedApplyHandled(apply_id)
    else:
      if int(request.params['is_new']) > 0:
        return '{"status":1, "desc":"新建子类型保存失败(已经存在)"}'

      print cfg.is_update_time, cfg.is_custom_expr
      cfg.is_persist_content = int(request.params['save_content'])
      cfg.ptype = int(request.params['ptype'])
      cfg.description = request.params['title']
      cfg.push_flag = int(request.params['push_flags'])
      cfg.news_merge_type  = int(request.params['news_merge_type'])
      cfg.mini_merge_type = int(request.params['mini_merge_type'])
      cfg.is_update_time = int(request.params['update_time_on_merge'])
      cfg.is_custom_expr = int(request.params['custom_expr'])
      cfg.is_persist_content = int(request.params['save_content'])
      cfg.is_persist_feeddb = int(request.params['save_feed_db'])
      cfg.lifetime = int(request.params['lifetime'])
      cfg.daily_quota = int(request.params['daily_quota'])
      cfg.weight = request.params['weight'] 

    Session.commit()
    return '{"status":0, "desc":"保存成功"}'

  def RemoveStype(self):
    if self.UserRight(request, response) < 2:
      return '"没有操作权限, 请确保管理员帐号登录"'

    stype_id = int(request.params['stype_id'])
    if stype_id <= 0:
      return '参数错误'

    # 删除stype 
    stype_cfg = self.stype_config_.filter_by(stype = stype_id).first()
    Session.delete(stype_cfg)
 
    # 删除数据格式定义
    schemas = self.data_version_.filter_by(stype = stype_id).first()
    Session.delete(schemas)

    # TODO : 删除模板

    Session.commit()

    return '成功删除新鲜事类型' + str(stype_id)

  def AddStypeVersion(self):
    stype = int(request.params['stype'])
    max_ver = Session.query(func.max(DataVersion.version)).filter_by(stype = stype).scalar() or 0
    vc = DataVersion(stype, max_ver + 1, 0, 0)
    Session.add(vc)
    Session.commit()
    return str(max_ver + 1)
    
  def AddVersionTpl(self):
    max_id = Session.query(func.max(VersionTplMapping.tpl_id)).scalar() or 1
    tpl_id = max_id + 1
    feed_key = VersionTplMapping(tpl_id = tpl_id,
        stype = request.params['stype'],
        version = request.params['version'])
    Session.add(feed_key)

    Session.commit()
    return str(tpl_id)

  def SaveVersionKeys(self):
    stype = int(request.params['stype'])
    version = int(request.params['version'])

    if stype <= 0 or version <= 0:
      return "参数错误"
    o = self.data_version_.filter_by(stype=stype, version=version).first()
    if o:
      o.keys_xml = request.params['kl']
      o.news_merge_by = request.params['news_merge_by']
      o.mini_merge_by = request.params['mini_merge_by']
      o.source_by = request.params['source_by']
      o.psource_by = request.params['psource_by']
      o.actor_by = request.params['actor_by']
      o.togroup_by = request.params['togroup_by']
      o.dispatch_expr = urllib2.unquote(str(request.params['dispatch_expr']))
      Session.commit()
      return '保存成功'
    else:
      return '该版本不存在'

  def RemoveDataVersion(self):
    stype = int(request.params['stype'])
    version = int(request.params['version'])

    if stype <= 0 or version <= 0:
      return "参数错误"
    o = self.data_version_.filter_by(stype=stype, version=version).first()

    Session.delete(o)
    Session.commit()
    return '成功删除版本' + str(version)

  def GetFeedKeys(self):
    tpl_id = int(request.params['id'])
    if tpl_id > 0:
      o = self.data_version_.filter_by(tpl_id = tpl_id, stype=int(request.params['stype']), version=int(request.params['version'])).first()
      return o.keys_xml
    else:
      return ''

  def GetVersionKeys(self):
    stype = int(request.params['stype'])
    version = int(request.params['version'])

    if stype > 0 and version > 0:
      o = self.data_version_.filter_by(stype=stype, version=version).first()
      return o.keys_xml
    else:
      return ''

  def SaveTemplate(self):
    sk = TplView(request.params['tpl_id'], 
        view = request.params['view'],
        status = 0,
        template = urllib2.unquote(str(request.params['tpl'])))
    Session.merge(sk)
    Session.commit()
    return '保存模板成功'

  def RemoveTemplate(self):
    if self.UserRight(request, response) < 2:
      return '"没有操作权限, 请确保管理员帐号登录"'

    tpl_id = int(request.params['tpl_id'])
    view = int(request.params['view'])
    if tpl_id <= 0 or view < 0:
      return '参数错误'

    tpl = self.tpl_views_.filter_by(tpl_id = tpl_id, view = view).first()

    Session.delete(tpl)
    Session.commit()

    return '删除模板成功'

  def GetTemplates(self):
    tpl_id = int(request.params['tpl_id'])
    if tpl_id <= 0:
      return '参数错误'

    tpls = self.tpl_views_.filter_by(tpl_id = tpl_id)

    count = 0
    rsp = '['
    for o in tpls:
      print '------------------', o.view, o.template
      if count > 0:
        rsp += ','
      rsp += '{"view":' + str(o.view) + ', "status":' + str(o.status) + ', "template":"' + urllib2.quote(o.template) + '"}'
      count += 1
    rsp += ']'
    return rsp

  def ValidateTemplate(self):
    tpl = request.params['tpl']
    # tpl = urllib2.unquote(str(request.params['tpl'])))
    res = feed_admin_reload.CheckTpl(urllib2.unquote(tpl))
    if res.code == 0:
      return "语法检查通过. code=0"
    return "语法错误:" + str(res.reason) + ". code=" + str(res.code)

  def ApplyNewFeedSubmit(self):
    max_id = Session.query(func.max(ApplyNewFeed.apply_id)).scalar() or 0

    pm_emails = request.params['pm_emails']
    pm_names = request.params['pm_names']
    stype_desc = request.params['stype_desc']
    a = ApplyNewFeed(max_id + 1,
        pm_names = pm_names, 
        pm_emails = pm_emails, 
        dev_names = request.params['dev_names'], 
        dev_emails = request.params['dev_emails'], 
        stype_desc = stype_desc, 
        stype_text = request.params['stype_text'], 
        push_news = int(request.params['push_news']), 
        push_mini = int(request.params['push_mini']), 
        news_merge_desc = request.params['news_merge_desc'], 
        mini_merge_desc = request.params['mini_merge_desc'], 
        lifetime = int(request.params['lifetime']), 
        status = 0,
        apply_time = int(time.time())
        )
    Session.add(a)
    Session.commit()

    self.SendMail('yuwei.mu@renren-inc.com', pm_emails, '申请创建新鲜事类型', pm_names + ':' + stype_desc)
    return '申请保存成功'

  def SendMail(self, sender, receivers, title, body):
    try:
      message = 'From: ' + sender + '\r\n'
      message += 'To: ' + receivers + '\r\n'
      message += 'MIME-Version: 1.0\r\n'
      message += 'Content-type: text/html; charset=UTF-8\r\n'
      message += 'Subject: ' + title + '\r\n'
      message += '\r\n'
      message += body

      smtpObj = smtplib.SMTP('smtp.renren-inc.com')
      smtpObj.sendmail(sender, receivers, message)         
      print "Successfully sent email"
    except SMTPException:
      print "Error: unable to send email"

  def ApplyNewFeedList(self):
    return render('/apply-new-feed-list.mako')

  def GetApplyFeedItem(self):
    apply_id = request.params['apply_id']
    a = self.apply_feeds_.filter_by(apply_id = apply_id).first()

    if a:
      ret = '{"apply_id":' + str(a.apply_id)
      ret += ',"pm_names":"' + a.pm_names.replace('"', '\\"') + '"'
      ret += ',"pm_emails":"' + a.pm_emails + '"'
      ret += ',"dev_names":"' + a.dev_names.replace('"', '\\"') + '"'
      ret += ',"dev_emails":"' + a.dev_emails + '"'
      ret += ',"stype_desc":"' + a.stype_desc.replace('"', '\\"') + '"'
      ret += ',"stype_text":"' + a.stype_text.replace('"', '\\"') + '"'
      ret += ',"push_news":' + str(a.push_news)
      ret += ',"push_mini":' + str(a.push_mini)
      ret += ',"news_merge_desc":"' + a.news_merge_desc.replace('"', '\\"') + '"'
      ret += ',"mini_merge_desc":"' + a.mini_merge_desc.replace('"', '\\"') + '"'
      ret += ',"lifetime":' + str(a.lifetime)
      ret += ',"status":' + str(a.status)
      ret += '}'
      return ret
    return '{}'

  def FeedApplyHandled(self, apply_id):
    a = self.apply_feeds_.filter_by(apply_id = apply_id).first()
    if a:
      a.status = 1
      Session.commit()

  def GetApplyFeedList(self):
    applies = self.apply_feeds_.all()
    count = 0
    ret = '['
    for a in applies:
      if count > 0:
        ret += ','
      ret += '{"apply_id":' + str(a.apply_id)
      ret += ',"pm_names":"' + a.pm_names.replace('"', '\\"') + '"'
      ret += ',"stype_desc":"' + a.stype_desc.replace('"', '\\"') + '"'
      ret += ',"status":' + str(a.status)
      ret += '}'
      count += 1
    ret += ']'
    return ret

  def ApplyNewVersionSubmit(self):
    max_id = Session.query(func.max(ApplyNewVersion.apply_id)).scalar() or 0

    pm_emails = request.params['pm_emails']
    pm_names = request.params['pm_names']
    version_desc = request.params['version_desc']
    a = ApplyNewVersion(max_id + 1,
        stype_id = int(request.params['stype_id']),
        from_version_id = int(request.params['from_version_id']),
        pm_names = pm_names, 
        pm_emails = pm_emails, 
        dev_names = request.params['dev_names'], 
        dev_emails = request.params['dev_emails'], 
        version_desc = version_desc, 
        version_text = request.params['version_text'], 
        status = 0,
        apply_time = int(time.time())
        )
    Session.add(a)
    Session.commit()

    # self.SendMail('yuwei.mu@renren-inc.com', pm_emails, '申请创建新鲜事类型', pm_names + ':' + stype_desc)
    return '申请保存成功'

  def ApplyNewVersionList(self):
    return render('/apply-new-version-list.mako')

  def GetApplyVersionList(self):
    applies = self.apply_versions_.all()
    count = 0
    ret = '['
    for a in applies:
      if count > 0:
        ret += ','
      ret += '{"apply_id":' + str(a.apply_id)
      ret += ',"stype_id":' + str(a.stype_id)
      ret += ',"from_version_id":' + str(a.from_version_id)
      ret += ',"pm_names":"' + a.pm_names.replace('"', '\\"') + '"'
      ret += ',"version_desc":"' + a.version_desc.replace('"', '\\"') + '"'
      ret += ',"status":' + str(a.status)
      ret += '}'
      count += 1
    ret += ']'
    return ret

  def VersionApplyHandled(self):
    a = self.apply_versions_.filter_by(apply_id = int(request.params['apply_id'])).first()
    if a:
      a.status = 1
      Session.commit()

    return ''

  def ApplyNewTplSubmit(self):
    max_id = Session.query(func.max(ApplyNewTpl.apply_id)).scalar() or 0

    pm_emails = request.params['pm_emails']
    pm_names = request.params['pm_names']
    tpl_desc = request.params['tpl_desc']
    a = ApplyNewTpl(max_id + 1,
        stype_id = int(request.params['stype_id']),
        version = int(request.params['version']),
        from_tpl_id = int(request.params['from_tpl_id']),
        pm_names = pm_names, 
        pm_emails = pm_emails, 
        dev_names = request.params['dev_names'],
        dev_emails = request.params['dev_emails'],
        tpl_desc = tpl_desc,
        tpl_text = request.params['tpl_text'],
        status = 0,
        apply_time = int(time.time())
        )
    Session.add(a)
    Session.commit()

    # self.SendMail('yuwei.mu@renren-inc.com', pm_emails, '申请创建新鲜事类型', pm_names + ':' + stype_desc)
    return '申请保存成功'

  def ApplyNewTplList(self):
    return render('/apply-new-tpl-list.mako')
  
  def GetApplyTplList(self):
    applies = self.apply_tpls_.all()
    count = 0
    ret = '['
    for a in applies:
      if count > 0:
        ret += ','
      ret += '{"apply_id":' + str(a.apply_id)
      ret += ',"stype_id":' + str(a.stype_id)
      ret += ',"version":' + str(a.version)
      ret += ',"from_tpl_id":' + str(a.from_tpl_id)
      ret += ',"pm_names":"' + a.pm_names.replace('"', '\\"') + '"'
      ret += ',"tpl_desc":"' + a.tpl_desc.replace('"', '\\"') + '"'
      ret += ',"status":' + str(a.status)
      ret += '}'
      count += 1
    ret += ']'
    return ret

  def TplApplyHandled(self):
    a = self.apply_tpls_.filter_by(apply_id = int(request.params['apply_id'])).first()
    if a:
      a.status = 1
      Session.commit()

    return ''

  def ApplyRollbackList(self):
    return render('/apply-rollback-list.mako')

  def GetApplyRollbackList(self):
    applies = self.apply_rollbacks_.all()
    count = 0
    ret = '['
    for a in applies:
      if count > 0:
        ret += ','
      ret += '{"apply_id":' + str(a.apply_id)
      ret += ',"stype_id":' + str(a.stype_id)
      ret += ',"version":' + str(a.version)
      ret += ',"pm_names":"' + a.pm_names.replace('"', '\\"') + '"'
      ret += ',"rollback_desc":"' + a.rollback_desc.replace('"', '\\"') + '"'
      ret += ',"status":' + str(a.status)
      ret += '}'
      count += 1
    ret += ']'
    return ret

  def ApplyRollbackSubmit(self):
    max_id = Session.query(func.max(ApplyRollback.apply_id)).scalar() or 0

    pm_emails = request.params['pm_emails']
    pm_names = request.params['pm_names']
    rollback_desc = request.params['rollback_desc']
    a = ApplyRollback(max_id + 1,
        stype_id = int(request.params['stype_id']),
        version = int(request.params['version']),
        tpl_id = int(request.params['tpl_id']),
        pm_names = pm_names, 
        pm_emails = pm_emails, 
        dev_names = request.params['dev_names'], 
        dev_emails = request.params['dev_emails'], 
        rollback_desc = rollback_desc, 
        status = 0,
        apply_time = int(time.time())
        )
    Session.add(a)
    Session.commit()

    # self.SendMail('yuwei.mu@renren-inc.com', pm_emails, '申请创建新鲜事类型', pm_names + ':' + stype_desc)
    return '申请保存成功'


  def ApplyPublishList(self):
    return render('/apply-publish-list.mako')

  def GetApplyPublishList(self):
    applies = self.apply_publishs_.all()
    count = 0
    ret = '['
    for a in applies:
      if count > 0:
        ret += ','
      ret += '{"apply_id":' + str(a.apply_id)
      ret += ',"stype_id":' + str(a.stype_id)
      ret += ',"version":' + str(a.version)
      ret += ',"pm_names":"' + a.pm_names.replace('"', '\\"') + '"'
      ret += ',"publish_desc":"' + a.publish_desc.replace('"', '\\"') + '"'
      ret += ',"status":' + str(a.status)
      ret += '}'
      count += 1
    ret += ']'
    return ret

  def ReloadTest(self):
    res = feed_admin_reload.Reload()
    if res == 0:
      return "测试环境reload成功"
    return "测试环境reload失败. code=" + str(res)

  def ReloadDist(self):
    if self.UserRight(request, response) < 3:
      return '没有操作权限, 请确保超级管理员帐号登录'

    res = feed_admin_reload_dist.Reload()
    if res == 0:
      return "线上环境reload成功"
    return "线上环境reload失败. code=" + str(res)

  def ApplyPublishSubmit(self):
    max_id = Session.query(func.max(ApplyPublish.apply_id)).scalar() or 0

    pm_emails = request.params['pm_emails']
    pm_names = request.params['pm_names']
    publish_desc = request.params['publish_desc']
    a = ApplyPublish(max_id + 1,
        stype_id = int(request.params['stype_id']),
        version = int(request.params['version']),
        tpl_id = int(request.params['tpl_id']),
        pm_names = pm_names, 
        pm_emails = pm_emails, 
        dev_names = request.params['dev_names'], 
        dev_emails = request.params['dev_emails'], 
        publish_desc = publish_desc, 
        status = 0,
        apply_time = int(time.time())
        )
    Session.add(a)
    Session.commit()

    # self.SendMail('yuwei.mu@renren-inc.com', pm_emails, '申请创建新鲜事类型', pm_names + ':' + stype_desc)
    return '申请保存成功'

  def GenerateCode(self):
    items = urllib2.unquote(request.params['hdf']).split(';')
    # .split(';')
    hdf = neo_util.HDF() 
    print items
    for item in items:
      print item
      v = item.split('=')
      if (len(v) == 2):
        hdf.setValue(v[0], urllib2.unquote(str(v[1])))

    cs = neo_cs.CS(hdf)
    cs.parseFile("./feedadmin/public/feed-java-code.cs") # parse a file from disk
    gen_code = cs.render()


    url_path = '/FeedBuilder_' + request.params['stype'] + '_' + request.params['version'] + '.java'

    f = open("./feedadmin/public" + url_path, "w")

    f.write(gen_code)
    f.close()

    return url_path

  def Stat(self):
    return render('/stat.mako');

  def StatDetail(self):
    return render('/stat-detail.mako');

  def StatStype(self):
    return render('/stat-stype.mako');


  def StatList(self):
    ret = ''
    stype = int(request.params.get('stype'))
    date = request.params.get('date')
    limit = request.params.get('limit')
    if stype == 0:
      if limit and int(limit) == 10:
        feed_stat = Session.query(FeedStatTotal).from_statement("select * from feed_stat_total order by date desc limit 30").all()
        ret = '['
        if feed_stat:
          for o in feed_stat:
            ret += '{'
            if o.date:
              ret += '"date":"' + str(o.date) + '"'
            else:
              ret += '"date":"0"'
            if o.dispatch:
              ret += ', "dispatch":' + str(o.dispatch)
            else:
              ret += ', "dispatch":"0"'
            if o.tosize:
              ret += ', "tosize":' + str(o.tosize)
            else:
              ret += ', "tosize":"0"'
            if o.dispatch_user:
              ret += ', "dispatch_user":' + str(o.dispatch_user)
            else:
              ret += ', "dispatch_user":"0"'
            if o.view:
              ret += ', "view":' + str(o.view)
            else:
              ret += ', "view":"0"'
            if o.view_pos:
              ret += ', "view_pos":' + str(o.view_pos)
            else:
              ret += ', "view_pos":"0"'
            if o.view_user:
              ret += ', "view_user":' + str(o.view_user)
            else:
              ret += ', "view_user":"0"'
            if o.viewed_user:
              ret += ', "viewed_user":' + str(o.viewed_user)
            else:
              ret += ', "viewed_user":"0"'
            if o.reply:
              ret += ', "reply":' + str(o.reply)
            else:
              ret += ', "reply":"0"'
            if o.reply_user:
              ret += ', "reply_user":' + str(o.reply_user)
            else:
              ret += ', "reply_user":"0"'
            if o.click:
              ret += ', "click":' + str(o.click)
            else:
              ret += ', "click":"0"'
            if o.click_pos:
              ret += ', "click_pos":' + str(o.click_pos)
            else:
              ret += ', "click_pos":"0"'
            if o.click_user:
              ret += ', "click_user":' + str(o.click_user)
            else:
              ret += ', "click_user":"0"'
            if o.clicked_user:
              ret += ', "clicked_user":' + str(o.clicked_user)
            else:
              ret += ', "clicked_user":"0"'
            ret += '},'
        ret += ']'
        return ret;
      else: # if limit
        feed_stat = Session.query(FeedStatStype.stype.label('stype'),\
                    FeedStatStype.date.label('date'), \
                    func.sum(FeedStatStype.dispatch).label('dispatch'), \
                    func.sum(FeedStatStype.tosize).label('tosize'), \
                    func.sum(FeedStatStype.dispatch_user).label('dispatch_user'), \
                    func.sum(FeedStatStype.view).label('view'), \
                    func.sum(FeedStatStype.view_pos).label('view_pos'), \
                    func.sum(FeedStatStype.view_user).label('view_user'), \
                    func.sum(FeedStatStype.reply).label('reply'), \
                    func.sum(FeedStatStype.reply_user).label('reply_user'), \
                    func.sum(FeedStatStype.click).label('click'), \
                    func.sum(FeedStatStype.click_user).label('click_user'),\
                    ).filter_by(date=date).\
                    group_by(FeedStatStype.stype).order_by(func.sum(FeedStatStype.dispatch).desc())
        ret = '['
        if feed_stat:
          for o in feed_stat:
            ret += '{"stype":' + str(o.stype) + ','
            ret += '"date":"' + str(o.date) + '", "dispatch":' + str(o.dispatch) + ', "tosize":' + str(o.tosize)
            ret += ', "dispatch_user":' + str(o.dispatch_user) 
            ret += ', "view":' + str(o.view)+ ', "view_pos":' + str(o.view_pos)+ ', "view_user":' + str(o.view_user)
            ret += ', "reply":' + str(o.reply)
            ret += ', "reply_user":' + str(o.reply_user) + ', "click":' + str(o.click)
            ret += ', "click_user":' + str(o.click_user)
            ret += '},'
        ret += ']'
        return ret;
    else: # if stype ==0
      feed_stat = Session.query(FeedStatStype.stype.label('stype'), FeedStatStype.date.label('date'), \
                    func.sum(FeedStatStype.dispatch).label('dispatch'), \
                    func.sum(FeedStatStype.tosize).label('tosize'), \
                    func.sum(FeedStatStype.dispatch_user).label('dispatch_user'), \
                    func.sum(FeedStatStype.view).label('view'), \
                    func.sum(FeedStatStype.view_pos).label('view_pos'), \
                    func.sum(FeedStatStype.view_user).label('view_user'), \
                    func.sum(FeedStatStype.reply).label('reply'), \
                    func.sum(FeedStatStype.reply_user).label('reply_user'), \
                    func.sum(FeedStatStype.click).label('click'), \
                    func.sum(FeedStatStype.click_user).label('click_user'),
                    ).filter_by(stype=stype).group_by(FeedStatStype.date).order_by(FeedStatStype.date.desc()).limit(30)
      ret = '['
      if feed_stat:
        for o in feed_stat:
          ret += '{"stype":' + str(o.stype) + ','
          ret += '"date":"' + str(o.date) + '", "dispatch":' + str(o.dispatch) + ', "tosize":' + str(o.tosize)
          ret += ', "dispatch_user":' + str(o.dispatch_user) + ', "view":' + str(o.view) + ', "view_pos":' + str(o.view_pos) + ', "view_user":' + str(o.view_user)
          ret += ', "reply":' + str(o.reply)
          ret += ', "reply_user":' + str(o.reply_user) + ', "click":' + str(o.click)
          ret += ', "click_user":' + str(o.click_user)
          ret += '},'
      ret += ']'
      return ret;  


  def StatData(self):#  do not modify!!
      date = request.params.get('date')
      if date+"" == "0":
      	ret = ''
      	feed_stat = Session.query(FeedStatTotal).from_statement("select * from feed_stat_total order by date desc  limit 40").all()
        ret = '['
        if feed_stat:
          for o in feed_stat:
            ret += '{'
            
            if o.date:              ret += '"date":"' + str(o.date) + '"'
            else:                   ret += '"date":"0"'
            if o.dispatch:              ret += ', "dispatch":' + str(o.dispatch)
            else:              		ret += ', "dispatch":"0"'
            if o.tosize:              ret += ', "tosize":' + str(o.tosize)
            else:              	      ret += ', "tosize":"0"'
            if o.reply:              ret += ', "reply":' + str(o.reply)
            else:              	     ret += ', "reply":"0"'
            if o.click:              ret += ', "click":' + str(o.click)
            else:                    ret += ', "click":"0"'
            
            ret += '},'
	ret +='{}'
        ret += ']'
        return ret;
      else :
        feed_stat = Session.query(FeedStatStype.stype.label('stype'),\
                    FeedStatStype.date.label('date'), \
                    func.sum(FeedStatStype.dispatch).label('dispatch'), \
                    func.sum(FeedStatStype.tosize).label('tosize'), \
                    func.sum(FeedStatStype.dispatch_user).label('dispatch_user'), \
                    func.sum(FeedStatStype.view).label('view'), \
                    func.sum(FeedStatStype.view_pos).label('view_pos'), \
                    func.sum(FeedStatStype.view_user).label('view_user'), \
                    func.sum(FeedStatStype.reply).label('reply'), \
                    func.sum(FeedStatStype.reply_user).label('reply_user'), \
                    func.sum(FeedStatStype.click).label('click'), \
                    func.sum(FeedStatStype.click_user).label('click_user'),\
                    ).filter_by(date=date).\
                    group_by(FeedStatStype.stype).order_by(FeedStatStype.stype.desc())
        ret = '['
	flag = 0
        if feed_stat:
          for o in feed_stat:
	    if flag == 0 :
              ret += '{'
	      flag = 1
	    else :
              ret +=',{'

            if o.stype:              ret += '"stype":' + str(o.stype) 
            else:                   ret += '"stype":100000'
            if o.date:              ret += ', "date":"' + str(o.date) 
            else:                   ret += ', "date":"0'
            if o.dispatch:              ret += '", "dispatch":' + str(o.dispatch)
            else:              		ret += '", "dispatch":0'
            if o.reply:              ret += ', "reply":' + str(o.reply)
            else:              	     ret += ', "reply":0'
            if o.click:              ret += ', "click":' + str(o.click)
            else:                    ret += ', "click":0'

            ret += '}'
        ret += ']'
        return ret;
 


  def Quota(self):
    return render('/quota.mako');
  
  def QuotaData(self):#  do not modify!!
      date = request.params.get('date')
      isStype = int(request.params.get('isStype'))
      bigtype = int(request.params.get('Bigtype'))
      if isStype == 1:#type date
      	ret = ''
      	feed_stat = Session.query(FeedStatTypeBalance.type.label('type'),\
                    	FeedStatTypeBalance.date.label('date'), \
                    	FeedStatTypeBalance.profit.label('profit'), \
                    	FeedStatTypeBalance.cost.label('cost'), \
                    	FeedStatTypeBalance.balance.label('balance'), \
                    	FeedStatTypeBalance.view.label('view'), \
                    ).filter_by(date=date).order_by(FeedStatTypeBalance.type.desc())
        ret = '['
        if feed_stat:
          for o in feed_stat:
            ret += '{'
            
            if o.date:              ret += '"date":"' + str(o.date) + '"'
            else:                   ret += '"date":"0"'
            if o.type:              ret += ', "type":' + str(o.type)
            else:              		ret += ', "type":"0"'
            if o.profit:              ret += ', "profit":' + str(o.profit)
            else:              	      ret += ', "profit":"0"'
            if o.cost:              ret += ', "cost":' + str(o.cost)
            else:              	     ret += ', "cost":"0"'
            if o.balance:              ret += ', "balance":' + str(o.balance)
            else:                    ret += ', "balance":"0"'
            if o.view:              ret += ', "view":' + str(o.view)
            else:                    ret += ', "view":"0"'
            
            ret += '},'
        ret += ']'
        return ret;
      if isStype == 2:#stype date
      	ret = ''
      	feed_stat = Session.query(FeedStatStypeBalance.stype.label('stype'),\
                    	FeedStatStypeBalance.date.label('date'), \
                    	FeedStatStypeBalance.profit.label('profit'), \
                    	FeedStatStypeBalance.cost.label('cost'), \
                    	FeedStatStypeBalance.balance.label('balance'), \
                    	FeedStatStypeBalance.view.label('view'), \
                    ).filter_by(date=date).order_by(FeedStatStypeBalance.stype.desc())
        ret = '['
        if feed_stat:
          for o in feed_stat:
	    if (o.stype/100*100 != bigtype):
		continue;
            ret += '{'
            
            if o.date:              ret += '"date":"' + str(o.date) + '"'
            else:                   ret += '"date":"0"'
            if o.stype:              ret += ', "stype":' + str(o.stype)
            else:              		ret += ', "stype":"0"'
            if o.profit:              ret += ', "profit":' + str(o.profit)
            else:              	      ret += ', "profit":"0"'
            if o.cost:              ret += ', "cost":' + str(o.cost)
            else:              	     ret += ', "cost":"0"'
            if o.balance:              ret += ', "balance":' + str(o.balance)
            else:                    ret += ', "balance":"0"'
            if o.view:              ret += ', "view":' + str(o.view)
            else:                    ret += ', "view":"0"'
            
            ret += '},'
        ret += ']'
        return ret;
      if isStype == 3:#stype
      	ret = ''
      	feed_stat = Session.query(FeedStatStypeBalance).from_statement("select * from feed_stat_stype_balance_t where stype="+str(bigtype)+" order by date desc  limit 40;").all()
        ret = '['
        if feed_stat:
          for o in feed_stat:
	    if (o.stype/100*100 != bigtype):
		continue;
            ret += '{'
            
            if o.date:              ret += '"date":"' + str(o.date) + '"'
            else:                   ret += '"date":"0"'
            if o.stype:              ret += ', "stype":' + str(o.stype)
            else:              		ret += ', "stype":"0"'
            if o.profit:              ret += ', "profit":' + str(o.profit)
            else:              	      ret += ', "profit":"0"'
            if o.cost:              ret += ', "cost":' + str(o.cost)
            else:              	     ret += ', "cost":"0"'
            if o.balance:              ret += ', "balance":' + str(o.balance)
            else:                    ret += ', "balance":"0"'
            if o.view:              ret += ', "view":' + str(o.view)
            else:                    ret += ', "view":"0"'
            
            ret += '},'
        ret += ']'
        return ret;
      if isStype == 4:#type
      	ret = ''
      	feed_stat = Session.query(FeedStatTypeBalance).from_statement("select * from feed_stat_type_balance_t where type="+str(bigtype)+" order by date desc  limit 40;").all()
        ret = '['
        if feed_stat:
          for o in feed_stat:
	    #if (o.stype/100*100 != bigtype):
		#continue;
            ret += '{'
            
            if o.date:              ret += '"date":"' + str(o.date) + '"'
            else:                   ret += '"date":"0"'
            if o.type:              ret += ', "type":' + str(o.type)
            else:              		ret += ', "type":"0"'
            if o.profit:              ret += ', "profit":' + str(o.profit)
            else:              	      ret += ', "profit":"0"'
            if o.cost:              ret += ', "cost":' + str(o.cost)
            else:              	     ret += ', "cost":"0"'
            if o.balance:              ret += ', "balance":' + str(o.balance)
            else:                    ret += ', "balance":"0"'
            if o.view:              ret += ', "view":' + str(o.view)
            else:                    ret += ', "view":"0"'
            
            ret += '},'
        ret += ']'
        return ret;

      if isStype == 5:
      	ret = ''
      	feed_stat = Session.query(FeedStatTypeBalance).from_statement("select * from feed_stat_type_balance_t where date>'2012-07-01' order by date desc ;").all()
        ret = '['
        if feed_stat:
          for o in feed_stat:
	    #if (o.stype/100*100 != bigtype):
		#continue;
            ret += '{'
            
            if o.date:              ret += '"date":"' + str(o.date) + '"'
            else:                   ret += '"date":"0"'
            if o.type:              ret += ', "type":' + str(o.type)
            else:              		ret += ', "type":"0"'
            if o.profit:              ret += ', "profit":' + str(o.profit)
            else:              	      ret += ', "profit":"0"'
            if o.cost:              ret += ', "cost":' + str(o.cost)
            else:              	     ret += ', "cost":"0"'
            if o.balance:              ret += ', "balance":' + str(o.balance)
            else:                    ret += ', "balance":"0"'
            if o.view:              ret += ', "view":' + str(o.view)
            else:                    ret += ', "view":"0"'
            
            ret += '},'
        ret += ']'
        return ret;


 
