# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: 阳健
'''
import settings
import web
import hashlib
import json
import datetime
import time

db = web.database(dbn=settings.ctrl_dbn,
                       db=settings.ctrl_db,
                       user=settings.ctrl_user,
                       pw=settings.ctrl_pw,
                       host=settings.ctrl_host,
                       port=settings.ctrl_port)

def makeDBConn(dbs):
    if dbs['stat']:
        return web.database(dbn=dbs["type"],
                       db=dbs["db_name"],
                       user=dbs["user"],
                       pw=dbs["password"],
                       host=dbs["ip"],
                       port=dbs["port"])
    return None

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return super(JSONDateTimeEncoder,self).default(obj)
        
def json_encode(data):
    return json.dumps(data,cls=JSONDateTimeEncoder)

#def SetAdmin():
#    sql = "update users set user_name = '" + \
#           settings.admin_name + "', " + \
#           "user_pwd = '" + hashlib.md5(settings.admin_pwd).hexdigest() + "', " + \
#           "email = '" + settings.admin_email + "' " + \
#           "where user_id = 1;"
#    return db.query(sql)

def Login(username, password):
    sql = "select * from users where user_name = '" + username + "' " + \
           "and user_pwd = '" + hashlib.md5(password).hexdigest() + "';"
    
    return db.query(sql)

def GetUserRoles(user_id):
    sql = "select roles.* from roles, role2user where role2user.user_id = '" + \
           str(user_id) + "' and roles.role_id = role2user.role_id;"
    return db.query(sql)

def GetRoleUsers(role_id):
    sql = "select users.* from users, role2user where role2user.role_id = '" + \
           str(role_id) + "' and users.user_id = role2user.user_id;"
    return db.query(sql)
    
def SetUserRoles(user_id, role_ids):
    sql = "delete from role2user where user_id = '" + user_id +"';"
    db.query(sql)
    for role_id in role_ids:
        sql = "insert into role2user (role_id, user_id) values ('" + role_id + "', '" + \
            user_id + "');"
        db.query(sql)
        
def SetTableRoles(table_id, role_ids, auths):
    sql = "delete from role2table where table_id = '" + table_id +"';"
    db.query(sql)
    len_role = len(role_ids)
    for i in range(0, len_role):
        sql = "insert into role2table (role_id, table_id, auth) values ('" + role_ids[i] + "', '" + \
            table_id + "', '" + auths[i] + "');"
        db.query(sql)
        
def GetAllRoles2Users():
    sql= "select roles.*, count(role2user.user_id) as u_num from roles left OUTER JOIN role2user on role2user.role_id = roles.role_id group by roles.role_id;"
    return db.query(sql)

def GetTableRoles(table_id):
    sql= "select roles.*, max(role2table.auth) as auth from roles left OUTER JOIN role2table on role2table.role_id = roles.role_id and role2table.table_id = '"+ table_id +"' group by roles.role_id;"
    return db.query(sql)

def GetAllDBSources():
    sql = "select db_source.source_name from db_source;"
    return db.query(sql)
def GetAllTables():
    sql = "select tables.* from tables;"
    return db.query(sql)

def GetOtherRoles(user_id):
    sql = "select roles.* from roles where roles.role_id not in (" + \
            "select role_id from role2user where user_id = '" + \
           str(user_id) + "') ;"
    return db.query(sql)
    
def GetTableUsers(table_id):
    sql = "select users.*, max(role2table.auth) as auth from users, role2user, role2table " + \
            "where users.user_id = role2user.user_id and " + \
            "role2user.role_id = role2table.role_id and " + \
            "role2table.table_id = '" + str(table_id) + "' group by users.user_id;"
    return db.query(sql)

def GetOtherTables(role_id):
    sql = "select tables.* from tables where tables.table_id not in (" + \
            "select table_id from role2table where role_id = '" + \
           str(role_id) + "') ;"
    return db.query(sql)
    
def GetRoleTables(role_id):
    sql = "select tables.*, role2table.auth from tables, role2table where role2table.role_id = '" + \
           str(role_id) + "' and tables.table_id = role2table.table_id;"
    return db.query(sql)

def GetUserTables(user_id):
    sql = "select tables.*, max(role2table.auth) as auth from tables, role2table where tables.table_id = role2table.table_id and " + \
            "role2table.role_id in (select role_id from role2user where user_id = '" + str(user_id) + "') group by tables.table_id;"
    return db.query(sql)


def CheckUser(username):
    sql = "select * from users where user_name = '" + username + "';"
    return db.query(sql)

def getAdmins():
    sql = 'select users.* from users, role2user where role2user.role_id = 1 and role2user.user_id = users.user_id;'
    return db.query(sql)

def Regin(username, password, name, email):
    sql = "insert into users (user_name, user_pwd, name, email) values('" + \
            username + "', '" + \
            hashlib.md5(password).hexdigest() + "', '" + \
            name + "', '" + \
            email + "');"
    return db.query(sql)
    
    #return db.query('select LAST_INSERT_ID() as id')
    
def GetTableById(table_id):
    sql = "select * from tables where table_id = '" + str(table_id) + "';"
    return db.query(sql)

def GetTableCols(table_name, db_source_info):
    args_db = makeDBConn(db_source_info)
    if args_db is None:
        return []
    sql = "desc " + table_name
    return args_db.query(sql)

def GetTableRows(table_name, db_source_info):
    args_db = makeDBConn(db_source_info)
    if args_db is None:
        return []
    return args_db.select(table_name)

def SaveArgs(table_name, args_cols, args_data, db_source_info):
    args_db = makeDBConn(db_source_info)
    if args_db is None:
        return []
    sql = "insert into " + table_name + " ("
    args_cols_len = len(args_cols)
    for i in range(0, args_cols_len):
        sql = sql + table_name + '.' + args_cols[i]
        if i < args_cols_len - 1 :
            sql += ", "
        else:
            sql += ") values ("
            
    for i in range(0, args_cols_len):
        sql += "'" + args_data[i] + "'"
        if i < args_cols_len - 1 :
            sql += ", "
        else:
            sql += ");"
            
    
    return args_db.query(sql)
    
    
def ChangeArgs(table_name, args_cols, nArgs_data, pArgs_data, db_source_info):
    args_db = makeDBConn(db_source_info)
    if args_db is None:
        return []
    sql = "update " + table_name + " set "
    args_cols_len = len(args_cols)
    
    for i in range(0, args_cols_len):
        sql = sql + table_name + '.' + args_cols[i] + " = '" + nArgs_data[i] + "'" 
        if i < args_cols_len - 1 :
            sql += ", "
        else:
            sql += " where "
            
    for i in range(0, args_cols_len):
        sql = sql + table_name + '.' + args_cols[i] + " = '" + pArgs_data[i] + "'" 
        if i < args_cols_len - 1 :
            sql += " and "
        else:
            sql += ";"
    
    return args_db.query(sql)
    
def RemoveArgs(table_name, args_cols, args_data, db_source_info):
    args_db = makeDBConn(db_source_info)
    if args_db is None:
        return []
    sql = "delete from " + table_name + " where "
    
    args_cols_len = len(args_cols)
            
    for i in range(0, args_cols_len):
        sql = sql + table_name + '.' + args_cols[i] + " = '" + args_data[i] + "'" 
        if i < args_cols_len - 1 :
            sql += " and "
        else:
            sql += ";"
    
    return args_db.query(sql)

def KeepLog(user_id, oper_type, oper_con = ''):
    sql = "insert into logs (user_id, oper_type, oper_con, time) values('" + \
            str(user_id) + "', '" + \
            settings.oper_type[oper_type] + "', '" + \
            oper_con + "', '" + \
            time.strftime('%Y-%m-%d %X', time.localtime()) + "');"

    return db.query(sql)
    
def ChangePWD(user_id, newPWD):
    sql = "update users set user_pwd = '" + hashlib.md5(newPWD).hexdigest() + "' " + \
           "where user_id = '" + str(user_id) + "';"
    return db.query(sql)
    
def ChangeUserProf(user_id, name, email):
    sql = "update users set name = '" + name + "', email = '" + \
            email + "' " + \
           "where user_id = '" + str(user_id) + "';"
    return db.query(sql)

def ChangeTableProf(table_id, table_name, table_dis, db_source):
    sql = "update tables set table_name = '" + table_name + "', table_dis = '" + \
            table_dis + "', db_source = '" + db_source + "' " + \
           "where table_id = '" + str(table_id) + "';"
    return db.query(sql)
    
def ChangeRoleName(role_id, role_name):
    sql = "update roles set role_name = '" + role_name + "' " + \
           "where role_id = '" + str(role_id) + "';"
    return db.query(sql)

def GetAllUsers():
    return db.select('users')

def DeleteUser(user_id):
    sql = "delete from role2user where user_id = '" + str(user_id) + "'; "
    db.query(sql)
    sql = "delete from users where user_id = '" + str(user_id) + "';"
    return db.query(sql)

def DeleteTable(table_id):
    sql = "delete from role2table where table_id = '" + str(table_id) + "'; "
    db.query(sql)
    sql = "delete from tables where table_id = '" + str(table_id) + "';"
    return db.query(sql)

def DeleteRole(role_id):
    sql = "delete from role2user where role_id = '" + str(role_id) + "'; "
    db.query(sql)
    sql = "delete from roles where role_id = '" + str(role_id) + "';"
    return db.query(sql)

def AddRole(role_name):
    sql = "insert into roles (role_name) values ('" + role_name + "');"
    db.query(sql)
    sql = "select last_insert_id() as id;"
    return db.query(sql)

def AddTable(table_name, table_dis, db_source):
    sql = "insert into tables (table_name, table_dis, db_source) values ('" + table_name + "', '" + table_dis + "', '" + db_source + "');"
    db.query(sql)
    sql = "select last_insert_id() as id;"
    return db.query(sql)

def SetRoleProfs(role_id, user_ids, table_ids, auths):
    sql = "delete from role2user where role_id = '" + str(role_id) + "'; "
    db.query(sql)
    for user_id in user_ids:
        sql = "insert into role2user (role_id, user_id) values ('" + str(role_id) + "', '" + str(user_id) + "');"
        db.query(sql)
    sql = "delete from role2table where role_id = '" + str(role_id) + "'; "
    db.query(sql)
    
    len_tab = len(table_ids)
    for i in range(0, len_tab):
        sql = "insert into role2table (role_id, table_id, auth) values ('" + str(role_id) + "', '" + str(table_ids[i]) + "', '" + str(auths[i]) + "');"
        db.query(sql)
        
def GetTableInCtrl(table_name, db_source):
    sql = "select * from tables where table_name = '" + table_name + \
        "' and db_source = '" + db_source + "';"
    return db.query(sql)

def getDBInfo(db_source):
    sql = "select * from db_source where source_name = '" + db_source + "'"
    return db.query(sql)

def GetLogs():
    sql = "select users.user_name, users.name, logs.* from logs, users where logs.user_id = users.user_id order by logs.log_id DESC"
    logs_db = db.query(sql)
    logs = []
    for log_db in logs_db:
        log = {
               'log_id' : log_db.log_id,
               'time' : log_db.time,
               'user_name' : log_db.user_name,
               'name' : log_db.name,
               'user_id' : log_db.user_id,
               'oper_type' : str(log_db.oper_type),
               'oper' : settings.oper_type_ch[str(log_db.oper_type)],
               'table_name' : '',
               'before' : '',
               'after' : ''
               }
        oper_con = log_db.oper_con
        log['table_name'] = oper_con.split('::')[0]
        
        oper_con = oper_con.split('::')[1]
        
        if str(log_db.oper_type) == '3':
            log['before'] = oper_con.split('->')[0]
            log['after'] = oper_con.split('->')[1]
        elif str(log_db.oper_type) == '4':
            log['before'] = oper_con
        elif str(log_db.oper_type) == '5':
            log['after'] = oper_con
        logs.append(log)
    return logs
        