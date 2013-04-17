# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

'''

import web
import json
import datetime

#ping_db. server_ping_info ：存储服务方法每分钟的平均响应时间、请求数等数据
#ping_db. server_ping_stat：存储服务方法的平均响应时间、.99相应时间、.90响应时间、标准差等数据

ping_user = 'work@RR'
ping_db = 'fb'
ping_host = '10.3.20.37'
ping_pw = 'Geeker4ZolZ'
ping_dbn = 'mysql'
ping_port = 3306

#mysql --default-character-set=utf8  -h10.3.20.37 -uwork@RR -pGeeker4ZolZ -Dfb

# ping_user = 'ad'
# ping_db = 'adn'
# ping_host = '10.3.20.38'
# ping_pw = 'adjb###'
# ping_dbn = 'mysql'
# ping_port = 3306

service_user = 'work@RR'
service_db = 'ad_monitor'
service_host = '10.11.18.146'
service_pw = 'Geeker4ZolZ'
service_dbn = 'mysql'
service_port = 3306
#service_status ：存储服务所在node、cpu、内存、线程数、句柄数等数据

#mysql --default-character-set=utf8  -h10.11.18.146 -uwork@RR -pGeeker4ZolZ -Dad_monitor

#service_status | CREATE TABLE `service_status` (
#    `id` bigint(20) unsigned NOT NULL auto_increment,
#    `service_name` varchar(150) collate utf8_bin NOT NULL,
#    `cpu_rate` varchar(10) collate utf8_bin NOT NULL,
#    `des_rate` varchar(10) collate utf8_bin NOT NULL,
#    `node` varchar(200) collate utf8_bin NOT NULL,
#    `update_time` bigint(20) unsigned NOT NULL default '0',
#    `memory` varchar(10) collate utf8_bin NOT NULL default '0',
#    `threads` varchar(10) collate utf8_bin NOT NULL default '0',
#    PRIMARY KEY  (`id`),
#    KEY `IND_server_status_update_time` (`update_time`),
#    KEY `IND_service_status_service_name` (`service_name`)
#    ) ENGINE=MyISAM AUTO_INCREMENT=25227083 DEFAULT CHARSET=utf8 COLLATE=utf8_bin

ping_db = web.database(dbn=ping_dbn, db=ping_db, user=ping_user, pw=ping_pw, host=ping_host, port=ping_port)
service_db = web.database(dbn=service_dbn, db=service_db, user=service_user, pw=service_pw, host=service_host, port=service_port)


class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return super(JSONDateTimeEncoder,self).default(obj)
        
def json_encode(data):
    return json.dumps(data,cls=JSONDateTimeEncoder)

def GetAllServices():
    sql = "select distinct service_name from service_status"
    s_services = service_db.query(sql)
    sql = "select distinct server_name from server_ping_stat"
    p_services = ping_db.query(sql)
    services = []
    for service in s_services:
        services.append(service["service_name"])
    for service in p_services:
        if service["server_name"] not in services:
            services.append(service["server_name"])
    return services

#===================================

def GetItemByService(service_name):
    sql = "select cpu_rate, des_rate, memory, threads from service_status where service_name = '" + \
        service_name + "' order by id desc limit 1"
    return service_db.query(sql)

def GetResourcesInfoByService(service_name):
    sql = "select cpu_rate, des_rate,  memory, threads, update_time from service_status where service_name = '" + \
        service_name + "' order by id  "
    print sql
    return service_db.query(sql)

def GetResourcesInfoByService_Time(service_name, time):
    sql = "select cpu_rate, des_rate, node, memory, threads from service_status where service_name = '" + \
        service_name + "' and update_time between " + str(time - 60) + " and " + str(time + 60) + " order by id desc limit 1"
    return service_db.query(sql)

def GetResourcesInfoByTime(time):
    sql = "select service_name, cpu_rate, des_rate, node, memory, threads from service_status where update_time between " + \
        str(time - 40) + " and " + str(time + 40)
    return service_db.query(sql)
    
#===================================


def GetItemByService2(service_name):
    sql = "select method_name from server_ping_config where server_name ='" + service_name + "'";
    return ping_db.query(sql)

def GetResourcesInfoByService2(service_name, time):
    sql = "select method_name, responsetime, require_num, updatetime from server_ping_info \
        where updatetime>" + str(time) + "  and server_name='" + service_name + "'"
    print sql
    return ping_db.query(sql)

def GetMethodsByService(service_name):
    sql = "select distinct method_name from server_ping_info where server_name = '" + service_name + "'"
    return ping_db.query(sql)
    
def Get_99(service_name, method_name, time):
    sql = "select time_nn, time_avg, time_std_deviation from server_ping_stat where server_name = '" + \
        service_name + "' and method_name = '" + method_name +"' " + \
        "and end_time like '" + str(time) + "______' order by id desc LIMIT 1"
    return ping_db.query(sql)

def Get_99ByTime(time):
    sql = "select server_name, method_name, time_nn, time_avg, time_std_deviation from server_ping_stat where " + \
        " begin_time < " + str(time) + " and end_time > " + str(time) + " order by server_name, method_name;"
    return ping_db.query(sql)
    
def GetRequestNumByService_Method(service_name, method_name, start, end):
    sql = "select require_num from server_ping_info where server_name = '" + \
        service_name + "' and method_name = '" + method_name + "' and updatetime > " + str(start) + \
        " and updatetime < " + str(end)
    return ping_db.query(sql)

def GetRequestNumByTime(start, end):
    sql = "select server_name, method_name, require_num from server_ping_info where updatetime > " + str(start) + \
        " and updatetime < " + str(end)
    return ping_db.query(sql)
