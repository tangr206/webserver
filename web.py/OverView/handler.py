# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: 阳健
'''
import web
import Dao
import time
import math
import re


urls = (
        '/','Index',
        '/getTable', 'GetTable',
        '/getData', 'GetData',
        )
t_globals = {
    'datestr': web.datestr
}
app = web.application(urls, globals())
render = web.template.render('templates/over_view/', base='', globals=t_globals)

mem_ = ["KB", "MB", "GB", "TB"]
def mem_change(mem):
    i = 0
    while mem > 1000:
        mem /= 1000
        i += 1
    return ("%.2f" % mem) + mem_[i]

class MethodInfo:
    def __init__(self, method):
        self.service_name = str(method["server_name"])
        self.method_name = str(method["method_name"])
        self._99 = float(method["time_nn"])
        self.avg = float(method["time_avg"])
        self.sd = float(method["time_std_deviation"])
        self.req = '-'
        
class ServiceInfo:
    def __init__(self, service):
        self.service_name = str(service["service_name"])
        self.node = str(service["node"])
        self.cpu_rate = float(service["cpu_rate"])
        self.des_rate = float(service["des_rate"])
        self.memory = float(service["memory"])
        self.threads = float(service["threads"])
        
class MethodHistory:
    def __init__(self, service_name, method_name, start_time, end_time):
        self.method_name = method_name
        self.response_time = []
        self.request_num = []
        start_time = time.strftime("%Y%m%d%H%M%S", time.localtime(start_time))
        if end_time > 0:
            end_time = time.strftime("%Y%m%d%H%M%S", time.localtime(end_time))
        self.getMethodHistory(service_name, start_time, end_time)
        
    def getMethodHistory(self, service_name, start_time, end_time):
        res_db = Dao.GetMethodHistoryByService_Method(service_name, self.method_name, start_time, end_time)
        for record in res_db:
            updatetime = time.strptime(str(record["updatetime"]), "%Y%m%d%H%M%S")
            updatetime = time.mktime(updatetime) * 1000
            self.response_time.append([updatetime, record["responsetime"]])
            self.request_num.append([updatetime, record["require_num"]])

class ServiceHistory:
    def __init__(self, service_name):
        self.service_name = service_name
        self.cpu_rate = []
        self.des_rate = []
        self.memory = []
        self.threads = []
        self.methods = []
        #self.getResoucesHistory(start_time, end_time)#use seconds
        #self.getMethodsHistory(start_time, end_time)#use pattern yyyyMMddHHmmss
    
    def getResoucesHistory(self, start_time, end_time):
        res_db = Dao.GetResoucesHistoryByService(self.service_name, start_time, end_time)
        
        for res in res_db:
            updatetime = int(res["update_time"])*1000

            self.cpu_rate.append([updatetime, res["cpu_rate"]])
            self.des_rate.append([updatetime, res["des_rate"]])
            self.memory.append([updatetime, res["memory"]])
            self.threads.append([updatetime, res["threads"]])
            
    def getCpu_rateHistory(self, start_time, end_time):
        res_db = Dao.GetCpu_rateHistoryByService(self.service_name, start_time, end_time)
        
        for res in res_db:
            updatetime = int(res["update_time"])*1000

            self.cpu_rate.append([updatetime, res["cpu_rate"]])
            
    def getDes_rateHistory(self, start_time, end_time):
        res_db = Dao.GetDes_rateHistoryByService(self.service_name, start_time, end_time)
        
        for res in res_db:
            updatetime = int(res["update_time"])*1000

            self.des_rate.append([updatetime, res["des_rate"]])
            
    def getMemoryHistory(self, start_time, end_time):
        res_db = Dao.GetMemoryHistoryByService(self.service_name, start_time, end_time)
        
        for res in res_db:
            updatetime = int(res["update_time"])*1000

            self.memory.append([updatetime, res["memory"]])
            
    def getThreadsHistory(self, start_time, end_time):
        res_db = Dao.GetThreadsHistoryByService(self.service_name, start_time, end_time)
        
        for res in res_db:
            updatetime = int(res["update_time"])*1000

            self.threads.append([updatetime, res["threads"]])
            
    def getMethods(self):
        methods_db = Dao.GetMethodsByService(self.service_name)
        methods = []
        #use pattern yyyyMMddHHmmss
        #start_time = time.strftime("%Y%m%d%H%M%S", time.localtime(start_time))
        #if end_time > 0:
        #    end_time = time.strftime("%Y%m%d%H%M%S", time.localtime(end_time))
        
        for method in methods_db:
            methods.append(method["method_name"])
        return methods
        
class ServiceInfo:
    def __init__(self, service):
        self.service_name = str(service["service_name"])
        self.node = str(service["node"])
        self.cpu_rate = float(service["cpu_rate"])
        self.des_rate = float(service["des_rate"])
        self.memory = float(service["memory"])
        self.threads = float(service["threads"])
                
class StatusShow:
    
    def POST(self):
        data = web.input()
        service_name = data.serviceName
        start_time = long(data.startTime) #seconds
        end_time = long(data.endTime) #seconds
        show_type = data.showType
        serviceHistory = ServiceHistory(service_name)
        if show_type == 'all':
            serviceHistory.getResoucesHistory(start_time, end_time)
            methods = serviceHistory.getMethods()
            for method_name in methods:
                serviceHistory.methods.append(MethodHistory(service_name, method_name, start_time, end_time))
        elif show_type == 'cpu_rate':
            serviceHistory.getCpu_rateHistory(start_time, end_time)
        elif show_type == 'des_rate':
            serviceHistory.getDes_rateHistory(start_time, end_time)
        elif show_type == 'memory':
            serviceHistory.getMemoryHistory(start_time, end_time)
        elif show_type == 'threads':
            serviceHistory.getThreadsHistory(start_time, end_time)
        else:
            serviceHistory.methods.append(MethodHistory(service_name, show_type, start_time, end_time))
        
                
        res = {
               'stat': 1,
               'res': '',
               #"service_name": serviceHistory.service_name,
               "cpu_rate": {
                            "title": "cpu使用率",
                            "unit": '%',
                            "data": serviceHistory.cpu_rate,
                            "upper": 5
                            },
               "des_rate": {
                            "title": "句柄使用率",
                            "unit": '%',
                            "data": serviceHistory.des_rate,
                            "upper": 5
                            },
               "memory": {
                            "title": "内存使用量",
                            "unit": '',
                            "sepe":'mem',
                            "data": serviceHistory.memory,
                            "upper": 100000
                            },
               "threads": {
                            "title": "线程使用数",
                            "unit": '个',
                            "data": serviceHistory.threads,
                            "upper": 20
                            },
               "methods": []
               }
        
        for method in serviceHistory.methods:
            met = {
                   "method_name": method.method_name,
                   "response_time": {
                            "title": "响应时间",
                            "unit": 'ms',
                            "data": method.response_time,
                            "upper": 2
                            },
                   "request_num": {
                            "title": "请求数",
                            "unit": '次',
                            "data": method.request_num,
                            "upper": 200
                            }                   
                   }
            res["methods"].append(met)
        
        return Dao.json_encode(res)
    
class Status:
    def GET(self):
        allServices = []
        services = Dao.GetAllServices()
        services.sort()
        for service in services:
            allServices.append(ServiceInfo(service))
        res = {
               "services":[]
               }
        for service in allServices:
            res_service = {
                           "service_name" : service.service_name,
                           "node" : service.node,
                           "cpu_rate" : service.cpu_rate,
                           "des_rate" : service.des_rate,
                           "memory" : service.memory,
                           "threads" : service.threads,
                           "methods":[]
                           }
            for method in service.methods:
                res_method = {
                              "method_name" : method.method_name,
                              "_99" : method._99,
                              "avg" : method.avg,
                              "sd" : method.sd,
                              "req" : method.req,
                              }
                res_service["methods"].append(res_method)
            res["services"].append(res_service)
        return Dao.json_encode(res)



#=============================

class GetTable:
    def GET(self):
        
        now = time.time()
        last_min = now - 60
        last_day = now - 86400
        last_2day = now - 172800
        last_7day = now - 604800
        
        last_min_db = Dao.GetResourcesInfoByTime(last_min)
        last_day_db = Dao.GetResourcesInfoByTime(last_day)
        last_7day_db = Dao.GetResourcesInfoByTime(last_7day)
        
        allServices = [{},{},{}]
        for service in last_min_db:
            allServices[0][str(service["service_name"])] = ServiceInfo(service)
                
        for service in last_day_db:
            allServices[1][str(service["service_name"])] = ServiceInfo(service)
                
        for service in last_7day_db:
            allServices[2][str(service["service_name"])] = ServiceInfo(service)
                
        last_day_db = Dao.Get_99ByTime(time.strftime('%Y%m%d120000', time.localtime(last_day)))
        last_2day_db = Dao.Get_99ByTime(time.strftime('%Y%m%d120000', time.localtime(last_2day)))
        last_7day_db = Dao.Get_99ByTime(time.strftime('%Y%m%d120000', time.localtime(last_7day)))
        
        allMethods = [{},{},{}]
        for method in last_day_db:
            n_key = str(method["server_name"]) + '__' + str(method["method_name"])
            allMethods[0][n_key] = MethodInfo(method)
                
        for method in last_2day_db:
            n_key = str(method["server_name"]) + '__' + str(method["method_name"])
            allMethods[1][n_key] = MethodInfo(method)
                
        for method in last_7day_db:
            n_key = str(method["server_name"]) + '__' + str(method["method_name"])
            allMethods[2][n_key] = MethodInfo(method)
                
        last_min_db = Dao.GetRequestNumByTime(time.strftime('%Y%m%d%H%M%S', time.localtime(last_min - 40)), time.strftime('%Y%m%d%H%M%S', time.localtime(last_min + 40)))
        last_day_db = Dao.GetRequestNumByTime(time.strftime('%Y%m%d%H%M%S', time.localtime(last_day - 40)), time.strftime('%Y%m%d%H%M%S', time.localtime(last_day + 40)))
        last_7day_db = Dao.GetRequestNumByTime(time.strftime('%Y%m%d%H%M%S', time.localtime(last_7day - 40)), time.strftime('%Y%m%d%H%M%S', time.localtime(last_7day + 40)))
        
        for request in last_min_db:
            n_key = str(request["server_name"]) + '__' + str(request["method_name"])
            if n_key in allMethods[0]:
                allMethods[0][n_key].req = request["require_num"]
                
        for request in last_day_db:
            n_key = str(request["server_name"]) + '__' + str(request["method_name"])
            if n_key in allMethods[1]:
                allMethods[1][n_key].req = request["require_num"]
                
        for request in last_7day_db:
            n_key = str(request["server_name"]) + '__' + str(request["method_name"])
            if n_key in allMethods[2]:
                allMethods[2][n_key].req = request["require_num"]
                
        allServices_ = {}
        for s_name in allServices[0]:
            service0 = allServices[0][s_name]
            res_service = {
                           "service_name" : service0.service_name,
                           "node" : service0.node,
                           "cpu_rate" : ["%.2f" % service0.cpu_rate],
                           "des_rate" : [service0.des_rate],
                           "memory" : [mem_change(service0.memory)],
                           "threads" : [service0.threads],
                           "methods":[]
                           }
                           
            for i in range(1, 3):
                if s_name in allServices[i]:
                    servicei = allServices[i][s_name]
                    res_service["cpu_rate"].append("%.2f" % (service0.cpu_rate - servicei.cpu_rate))
                    res_service["des_rate"].append(service0.des_rate - servicei.des_rate)
                    res_service["memory"].append(mem_change(service0.memory - servicei.memory))
                    res_service["threads"].append(service0.threads - servicei.threads)
                else:
                    res_service["cpu_rate"].append('-')
                    res_service["des_rate"].append('-')
                    res_service["memory"].append('-')
                    res_service["threads"].append('-')
                    
            allServices_[s_name] = res_service
            
        for n_key in allMethods[0]:
            s_name = n_key.split('__')[0]
            if s_name not in allServices_:
                allServices_[s_name] = {
                           "service_name" : s_name,
                           "node" : '-',
                           "cpu_rate" : ['-', '-', '-'],
                           "des_rate" : ['-', '-', '-'],
                           "memory" : ['-', '-', '-'],
                           "threads" : ['-', '-', '-'],
                           "methods":[]
                           }
            method0 = allMethods[0][n_key]
            res_method = {
                          "method_name" : method0.method_name,
                          "_99" : [("%.2f" % method0._99)],
                          "avg" : [("%.2f" % method0.avg)],
                          "sd" : [("%.2f" % method0.sd)],
                          "req" : [method0.req],
                          }
            for i in range(1, 3):
                if n_key in allMethods[i]:
                    methodi = allMethods[i][n_key]
                    res_method["_99"].append("%.2f" % (method0._99 - methodi._99))
                    res_method["avg"].append("%.2f" % (method0.avg - methodi.avg))
                    res_method["sd"].append("%.2f" % (method0.sd - methodi.sd))
                    if (method0.req != '-') and (methodi.req != '-'):
                        res_method["req"].append(method0.req - methodi.req)
                    else:
                        res_method["req"].append('-')
                else:
                    res_method["_99"].append("-")
                    res_method["avg"].append("-")
                    res_method["sd"].append("-")
                    res_method["req"].append("-")
                    
            allServices_[s_name]["methods"].append(res_method)
                    
            
        res = {
               "services":[]
               }
        for s_name in allServices_:
            if len(allServices_[s_name]["methods"]) == 0:
                res_method = {
                          "method_name" : '-',
                          "_99" : ['-','-','-'],
                          "avg" : ['-','-','-'],
                          "sd" : ['-','-','-'],
                          "req" : ['-','-','-'],
                          }
                allServices_[s_name]["methods"].append(res_method)
                
            res["services"].append(allServices_[s_name])
            
        res["services"].sort(key=lambda service : service["service_name"])
        return Dao.json_encode(res)

class GetData:

  def POST(self):
    data = web.input()
    service_name = data.servername
    cate = data.cate

    if (cate == 'service_status'): #service_status
      res = Dao.GetResourcesInfoByService(service_name) 
      data = []
      #{'update_time': 1365600391.0, 'memory': 508272.0, 'threads': 82.0, 'des_rate': 73.0, 'cpu_rate': 0.1}
      for meta in res:
        dic = {}
        for i in meta:
          dic[i] = int(float(meta[i]))
        data.append(dic)
      return Dao.json_encode(data)
    else:
      res = Dao.GetResourcesInfoByService2(service_name, 20130409000000) 
      data = []
      print res[0]
    #{'method_name': 'Click', 'updatetime': 20130409000007L, 
    #'require_num': 4L, 'responsetime': '0.25'}>
      #for i in xrange(0, len(res), 2):
      cnt = 0
      for meta in res:
        if cnt == 0:
          cnt = 1
          dic = {}
          a = time.strptime(str(meta["updatetime"]), "%Y%m%d%H%M%S")
          dic["update_time"] = int(time.mktime(a))

          dic[meta["method_name"] + " require_num"] = int(meta["require_num"])
          dic[meta["method_name"] + " responsetime"] = float(meta["responsetime"])
          data.append(dic)
        else:
          cnt = 0
          dic = data[-1]
          dic[meta["method_name"] + " require_num"] = int(meta["require_num"])
          dic[meta["method_name"] + " responsetime"] = float(meta["responsetime"])
        #print data[-1]
      return Dao.json_encode(data)
 

class Index:
    def GET(self):
        data = web.input()
        service_name = data.serviceName
        cate = data.cate
  
        if (cate == 'service_status'): #service_status
          res = Dao.GetItemByService(service_name) 
          item = []
          if(len(res) != 0):
            for i in res[0]:
              item.append(i)
          return render.index(service_name, cate, item)
        else: # server_ping_info  or default
          #responsetime, require_num

          match = re.search("(^\w*?)(\d*$)",service_name)
          if not match:
            match = re.search("(^\w*?)(-\d*$)",service_name)

          if match:
            res = Dao.GetItemByService2( match.group(1) ) 
            item = []
            if(len(res) != 0):
              for i in res:
                item.append(i["method_name"] + " responsetime")
                item.append(i["method_name"] + " require_num")
            return render.index(service_name, cate, item)
 


if __name__ == '__main__':
    app.run()
