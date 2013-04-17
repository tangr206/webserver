# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: 阳健
'''

import web
import Dao
import time
import emailSender
import hashlib
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8') 
#def session_hook():
#    web.ctx.session = session

urls = (
    '/','Login',
    '/sys','sLogin',
    '/login','Login',
    '/logout','Logout',
    '/regin','Regin',
    '/logs','Logs',
    
    '/index','Index',
    
    '/args','Args',
    '/table/(.*)','Table',
    
    '/addArgs/(.*)/(.*)','AddArgs',
    '/changeArgs','ChangeArgs',
    '/deleteArgs/(.*)/(.*)','DeleteArgs',
    
    '/self_set','SelfSet',
    '/pwd_set','PWDSet',
    
    '/userMan','UserMan',
    '/user_set','UserSet',
    '/delete_user','DeleteUser',
    
    '/user_info/(.*)','UserInfo',
    '/user_info','UserInfo',
    
    '/roleMan','RoleMan',
    '/role_set','RoleSet',
    '/add_role','AddRole',
    '/delete_role','DeleteRole',
    
    '/role_info/(.*)','RoleInfo',
    '/role_info','RoleInfo',
    
    '/tableMan','TableMan',
    '/table_set','TableSet',
    '/add_table','AddTable',
    '/delete_table','DeleteTable',
    
    '/table_info/(.*)','TableInfo',
    '/table_info','TableInfo',
)

t_globals = {
    'datestr': web.datestr
}
app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'site': 'pro', 'user': False})

#app.add_processor(web.loadhook(session_hook))

AUTH_READ = 0
AUTH_WRITE = 1

def render():
    try:
        if not session.site:
            session.site = 'pro'
    except Exception as why:
        print str(why)
        session.site = 'pro'
    
    return web.template.render('templates/args_manage/', base='base_' + session.site, globals=t_globals)

def validteAdmin():
    try:
        if not session.user:
            return False
        roles = getUserRoles(session.user.user_id)
        for role in roles:
            if role.role_id == 1:
                return True
    except Exception as why:
        print 'exception ' + str(why)
    return False

def mod_test(mods_str):
    if len(mods_str) == 0:
        return True
    if (mods_str.lower() == 'all') or (mods_str.lower() == 'all'):
        return True
    for i in range(0, len(mods_str)):
        if (mods_str[i] != ',') and (mods_str[i] != '~') and (mods_str[i] != '-') and ((mods_str[i] < '0') or (mods_str[i] > '9')):
            return False
        if (mods_str[i] == '-') and (i > 0) and (mods_str[i-1] != ',') and (mods_str[i-1] != '~'):
            return False
    mods_str = mods_str.split(',')
    for mod_str in mods_str:
        if mod_str == '':
            return False
        elif mod_str == '-':
            return False
        elif mod_str.find('~') > -1:
            mod_start = mod_str.split('~')[0]
            mod_end = mod_str.split('~')[1]
            if (mod_start == '') or (mod_end == '') or (int(mod_end) < int(mod_start)):
                return False
    return True
    
def validateTable(table_id, auth):
    tables = getUserTables(session.user.user_id)
    for table in tables :
        if (str(table.table_id) == str(table_id)) and (table.auth >= auth):
            return True
    return False

def getDBSourceInfo(db_source):
    res = {'stat':False}
    try:
        res_db = Dao.getDBInfo(db_source)
        if len(res_db) > 0:
            res_db = res_db[0]
            res['stat'] = True
            res['ip'] = res_db['ip']
            res['port'] = res_db['port']
            res['db_name'] = res_db['db_name']
            res['user'] = res_db['user']
            res['password'] = res_db['password']
            res['type'] = res_db['type']
            
    except Exception as why:
        print 'exception ' + str(why)
    return res

def tableRepeatTest(table_name, db_source):
    try:
        tab = Dao.GetTableInCtrl(table_name, db_source)
        if len(tab) == 0 :
            return True
    except Exception as why:
        print 'exception ' + str(why)
        return False
    return False

def tableTest(table_name, db_source):
    try:
#        tab = Dao.GetTableInCtrl(table_name)
#        if len(tab) == 0 :
#            return False
        db_source_info = getDBSourceInfo(db_source)
        if db_source_info['stat']:
            cols = Dao.GetTableCols(table_name, db_source_info)
            if len(cols) == 0 :
                return False
        else:
            return False
    except Exception as why:
        print 'exception ' + str(why)
        return False
    return True

def getUserTables(user_id):
    tables = []
    tables_db = Dao.GetUserTables(user_id);
    if len(tables_db) > 0:
        for table in tables_db:
            tables.append(table);
    return tables

def getUserRoles(user_id):
    roles = []
            
    roles_db = Dao.GetUserRoles(user_id)
    
    if len(roles_db) > 0:
        for role in roles_db:
            roles.append(role)
            
    return roles
    

class RoleInfo:
    def GET(self, role_id):
        res = {
               'stat' : 1,
               'res' : '',
               'users' : [],
               'tables' : [],
               'all_users' : []
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有权限查看用户信息'
            return Dao.json_encode(res)
        
        users_db = Dao.GetRoleUsers(role_id)
        for user in users_db:
            res['users'].append(user)
            
        tables_db = Dao.GetRoleTables(role_id);
        for table in tables_db:
#            addAble = True
#            for addedTable in res['tablse']:
#                if addedTable.table_id == table.table_id:
#                    addAble = False
#                    if table.auth > addedTable.auth:
#                        addedTable.auth = table.auth
#                    break
#            if addAble:
            res['tables'].append(table);
            
        all_users_db = Dao.GetAllUsers()
        for user in all_users_db:
#            addAble = True
#            for added_role in res['roles']:
#                if added_role.role_id == role.role_id:
#                    addAble = False
#                    break
#            if addAble:
            res['all_users'].append(user)
            
        other_tables_db = Dao.GetOtherTables(role_id)
        
        for table in other_tables_db:
            res['tables'].append(table)
    
        return Dao.json_encode(res)
    
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有权限查看用户信息'
            return Dao.json_encode(res)
        data = web.input()
        role_id = data.role_id
        user_ids = data.users
        if len(user_ids) > 0:
            user_ids = user_ids.split('&')
        else:
            user_ids = []
        
        tables = data.tables
        if len(tables) > 0:
            tables = tables.split('&')
        else:
            tables = []
        table_ids = []
        auths = []
        
        for table in tables:
            table_ids.append(table.split('=')[0])
            auths.append(table.split('=')[1])

        try:
            Dao.SetRoleProfs(role_id, user_ids, table_ids, auths)
            
            return self.GET(role_id)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)
    
class TableInfo:
    def GET(self, table_id):
        res = {
               'stat' : 1,
               'res' : '',
               'roles' : [],
               'users' : []
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有权限查看参数表信息'
            return Dao.json_encode(res)
        
        roles_db = Dao.GetTableRoles(table_id)
        for role in roles_db:
            res['roles'].append(role)
            
        users_db = Dao.GetTableUsers(table_id);
        for user in users_db:
#            addAble = True
#            for addedTable in res['tablse']:
#                if addedTable.table_id == table.table_id:
#                    addAble = False
#                    if table.auth > addedTable.auth:
#                        addedTable.auth = table.auth
#                    break
#            if addAble:
            res['users'].append(user);
        return Dao.json_encode(res)
    
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有权限修改参数表信息'
            return Dao.json_encode(res)
        data = web.input()
        table_id = data.table_id
        roles = data.roles
        
        if len(roles) > 0:
            roles = roles.split('&')
        else:
            roles = []
        
        role_ids = []
        auths = []
        
        for role in roles:
            role_ids.append(role.split('=')[0])
            auths.append(role.split('=')[1])
        
        try:
            Dao.SetTableRoles(table_id, role_ids, auths)
            return self.GET(table_id)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)

class UserInfo:
    def GET(self, user_id):
        res = {
               'stat' : 1,
               'res' : '',
               'roles' : [],
               'tables' : [],
               'other_roles' : []
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有权限查看用户信息'
            return Dao.json_encode(res)
        
        roles_db = Dao.GetUserRoles(user_id)
        for role in roles_db:
            res['roles'].append(role)
            
        tables_db = Dao.GetUserTables(user_id);
        for table in tables_db:
#            addAble = True
#            for addedTable in res['tablse']:
#                if addedTable.table_id == table.table_id:
#                    addAble = False
#                    if table.auth > addedTable.auth:
#                        addedTable.auth = table.auth
#                    break
#            if addAble:
            res['tables'].append(table);
            
        other_roles_db = Dao.GetOtherRoles(user_id)
        for role in other_roles_db:
#            addAble = True
#            for added_role in res['roles']:
#                if added_role.role_id == role.role_id:
#                    addAble = False
#                    break
#            if addAble:
            res['other_roles'].append(role)
        
        return Dao.json_encode(res)
    
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有权限修改用户信息'
            return Dao.json_encode(res)
        data = web.input()
        role_ids = data.roles
        user_id = data.user_id
        
        if len(role_ids) > 0:
            role_ids = role_ids.split('&')
        else:
            role_ids = []
        
        
        try:
            Dao.SetUserRoles(user_id, role_ids)
            return self.GET(user_id)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)

class UserMan:
    def GET(self):
        if not validteAdmin():
            return render().login('')
        users_db = Dao.GetAllUsers()
        users = []
        for user in users_db:
            users.append(user)
        
        return render().user_man(getUserRoles(session.user.user_id), users)
    
class RoleMan:
    def GET(self):
        if not validteAdmin():
            return render().login('')
        roles_db = Dao.GetAllRoles2Users()
        roles = []
        for role in roles_db:
            roles.append(role)
        
        return render().role_man(getUserRoles(session.user.user_id), roles)
    
class TableMan:
    def GET(self):
        if not validteAdmin():
            return render().login('')
        tables_db = Dao.GetAllTables()
        tables = []
        for table in tables_db:
            tables.append(table)
        db_sources_db = Dao.GetAllDBSources()
        db_sources = []
        for db_source in db_sources_db:
            db_sources.append(db_source["source_name"])
        
        return render().table_man(getUserRoles(session.user.user_id), tables, db_sources)
    
class AddTable:
    def POST(self):
        res = {
               'stat' : 1,
               'res' : '',
               'table_id' : 0
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有添加参数表的权限'
            return Dao.json_encode(res)
        data = web.input()
        table_name = data.table_name
        table_dis = data.table_dis
        db_source = data.db_source
        try:
            if tableTest(table_name, db_source):
                if tableRepeatTest(table_name, db_source):
                    res['table_id'] = Dao.AddTable(table_name, table_dis, db_source)[0].id
                else:
                    res['stat'] = 0
                    res['res'] = '表 '+table_name + '已添加'
            else:
                res['stat'] = 0
                res['res'] = '在数据源 '+db_source+' 中找不到表 '+table_name
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)

class AddRole:
    def POST(self):
        res = {
               'stat' : 1,
               'res' : '',
               'role_id' : 0
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有添加角色的权限'
            return Dao.json_encode(res)
        data = web.input()
        role_name = data.role_name
        try:
            res['role_id'] = Dao.AddRole(role_name)[0].id
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    
class DeleteTable:
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有删除参数表的权限'
            return Dao.json_encode(res)
        data = web.input()
        table_id = data.table_id
        try:
            Dao.DeleteTable(table_id)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    
class DeleteRole:    
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有删除角色的权限'
            return Dao.json_encode(res)
        data = web.input()
        role_id = data.role_id
        try:
            Dao.DeleteRole(role_id)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
class DeleteUser:
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有删除用户的权限'
            return Dao.json_encode(res)
        data = web.input()
        user_id = data.user_id
        try:
            Dao.DeleteUser(user_id)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
class RoleSet:
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有修改角色信息的权限'
            return Dao.json_encode(res)
        
        data = web.input()
        role_name = data.role_name
        role_id = data.role_id
        try:
            Dao.ChangeRoleName(role_id, role_name)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    
class TableSet:
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有修改参数表的权限'
            return Dao.json_encode(res)
        
        data = web.input()
        table_name = data.table_name
        table_dis = data.table_dis
        db_source = data.db_source
        table_id = data.table_id
        try:
            if tableTest(table_name, db_source):
                Dao.ChangeTableProf(table_id, table_name, table_dis, db_source)
            else:
                res['stat'] = 0
                res['res'] = '在数据源 '+db_source+' 中找不到表 '+table_name
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    
class UserSet:
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validteAdmin():
            res['stat'] = 0
            res['res'] = '您没有修改用户信息的权限'
            return Dao.json_encode(res)
        
        data = web.input()
        name = data.name
        email = data.email
        user_id = data.user_id
        try:
            Dao.ChangeUserProf(user_id, name, email)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    
class SelfSet:
    def GET(self):
        if not session.user :
            return render().login('');
        return render().self_set(getUserRoles(session.user.user_id), session.user);
    
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not session.user:
            res['stat'] = 0
            res['res'] = '您尚未登陆'
            return Dao.json_encode(res)
        data = web.input()
        name = data.name
        email = data.email
        try:
            Dao.ChangeUserProf(session.user.user_id, name, email)
            session.user.name = name
            session.user.email = email
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        
        return Dao.json_encode(res)

class PWDSet:
    def POST(self):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not session.user:
            res['stat'] = 0
            res['res'] = '您尚未登陆'
            return Dao.json_encode(res)
        data = web.input()
        prePWD = data.prePWD
        newPWD = data.newPWD
        if len(newPWD) < 6 or len(newPWD) > 16:
            res['stat'] = 0
            res['res'] = '新密码长度不合法'
        else:
            try:
                if session.user.user_pwd == hashlib.md5(prePWD).hexdigest():
                    Dao.ChangePWD(session.user.user_id, newPWD)
                else:
                    res['stat'] = 0
                    res['res'] = '原密码不正确'
            except Exception as why:
                print 'exception ' + str(why)
                res['stat'] = 0
                res['res'] = str(why)
            
        return Dao.json_encode(res)
#Dao.SetAdmin();
class Table:
    def GET(self, table_id):
        #validate
        res = {
               'stat' : 1,
               'res' : '',
               'cols' : [],
               'rows' : []
            }
        if not validateTable(table_id, AUTH_READ):
            res['stat'] = 0
            res['res'] = '您无权查询此参数表'
            return Dao.json_encode(res)
        try:
            table_info = Dao.GetTableById(table_id)[0]
            table_name = table_info.table_name
            db_source_info = getDBSourceInfo(table_info.db_source)
            
            cols_db = Dao.GetTableCols(table_name, db_source_info)
            
            for col in cols_db:
                res['cols'].append(str(col.Field))
            rows_db = Dao.GetTableRows(table_name, db_source_info)
            for row in rows_db:
		row_r = {}
		for col in res['cols']:
			row_r[col] = str(row[col])
                res['rows'].append(row_r)
                #res['rows'].append(row)
            #Dao.KeepLog(session.user.user_id, 'getTable', table_name)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
	#print res
        return Dao.json_encode(res)
    
class AddArgs:
    def GET(self, table_id, args):
        print args
        
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validateTable(table_id, AUTH_WRITE):
            res['stat'] = 0
            res['res'] = '您无权修改此参数表'
            return Dao.json_encode(res)
        log_args = args
        args = args.split('&')
        args_cols = []
        args_data = []
        for arg in args:
            args_cols.append(arg.split('=')[0])
            args_data.append(arg.split('=')[1])
            
        try:
            table_info = Dao.GetTableById(table_id)[0]
            table_name = table_info.table_name
            
            ############### for table module_status ##################
            if (table_name == 'module_status') and (not mod_test(args_data[1])):
                res['stat'] = 0
                res['res'] = '降级参数格式不正确'
                return Dao.json_encode(res)
            ############### for table module_status ##################
            
            db_source_info = getDBSourceInfo(table_info.db_source)
            Dao.SaveArgs(table_name, args_cols, args_data, db_source_info)
            Dao.KeepLog(session.user.user_id, 'addArgs', table_info.db_source+'.'+table_name + '::' + log_args)
            
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
        
class ChangeArgs:
    def POST(self):
        
        data = web.input()
        table_id = data.tabId
        pArgs = data.pArgs
        nArgs = data.nArgs
        
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validateTable(table_id, AUTH_WRITE):
            res['stat'] = 0
            res['res'] = '您无权修改此参数表'
            return Dao.json_encode(res)
        log_pArgs = pArgs
        pArgs = pArgs.split('&')
        args_cols = []
        pArgs_data = []
        for arg in pArgs:
            args_cols.append(arg.split('=')[0])
            pArgs_data.append(arg.split('=')[1])
        log_nArgs = nArgs
        nArgs = nArgs.split('&')
        nArgs_data = []
        for arg in nArgs:
            nArgs_data.append(arg.split('=')[1])
            
        try:
            table_info = Dao.GetTableById(table_id)[0]
            table_name = table_info.table_name
            ############### for table module_status ##################
            if (table_name == 'module_status') and (not mod_test(nArgs_data[1])):
                res['stat'] = 0
                res['res'] = '降级参数格式不正确'
                return Dao.json_encode(res)
            ############### for table module_status ##################
            db_source_info = getDBSourceInfo(table_info.db_source)
            Dao.ChangeArgs(table_name, args_cols, nArgs_data, pArgs_data, db_source_info)
            Dao.KeepLog(session.user.user_id, 'changeArgs', table_info.db_source+'.'+table_name + '::' + log_pArgs + '->' + log_nArgs)
            
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        
        return Dao.json_encode(res)
    
class DeleteArgs:
    def GET(self, table_id, args):
        res = {
               'stat' : 1,
               'res' : ''
               }
        if not validateTable(table_id, AUTH_WRITE):
            res['stat'] = 0
            res['res'] = '您无权修改此参数表'
            return Dao.json_encode(res)
        log_args = args
        args = args.split('&')
        args_cols = []
        args_data = []
        for arg in args:
            args_cols.append(arg.split('=')[0])
            args_data.append(arg.split('=')[1])
            
        try:
            table_info = Dao.GetTableById(table_id)[0]
            table_name = table_info.table_name
            db_source_info = getDBSourceInfo(table_info.db_source)
            Dao.RemoveArgs(table_name, args_cols, args_data, db_source_info)
            Dao.KeepLog(session.user.user_id, 'deleteArgs', table_info.db_source+'.'+table_name + '::' + log_args)
        except Exception as why:
            print 'exception ' + str(why)
            res['stat'] = 0
            res['res'] = str(why)
        return Dao.json_encode(res)
    
class sLogin:
    def GET(self):
        session.site = 'sys'
        return render().login('')
    
class Login:
    def GET(self):
        session.site = 'pro'
        return render().login('')
    
    def POST(self):
        login_data = web.input()
        try:
            user_db = Dao.Login(login_data.username, login_data.password)
            
            if len(user_db) == 0:
                return render().login('用户名或密码错误')
            
            user = user_db[0]
                
            session.user = user;
            
            return render().index(getUserRoles(session.user.user_id), session.user)
        
        except Exception as why:
            print 'exception ' + str(why)
            return render().login('数据库错误')

class Regin:
    def GET(self):
        return render().regin('')
    
    def POST(self):
        regin_data = web.input()
        
        username = regin_data.username
        password = regin_data.password
        re_password = regin_data.re_password
        
        if len(username) > 32:
            return render().regin('账号长度不合法')
        if len(password) > 16:
            return render().regin('密码长度不合法')
        if not password == re_password:
            return render().regin('两次密码输入不一致')
        
        user = Dao.CheckUser(username)
        if len(user) > 0:
            return render().regin('账号已被注册')
        # check emial && name??
        try:
            Dao.Regin(username, password, regin_data.name, regin_data.email)
            #Dao.KeepLog(user_id, 'regin')
            
            admins = Dao.getAdmins()
            emails = []
            
            for admin in admins:
                emails.append(admin.email)
            #emails = '; '.join(emails)
            context = '用户 ' + regin_data.name + ': ' + username + '\n' + \
                    '邮箱地址: ' + regin_data.email + '\n' + \
                    '于 ' + time.strftime('%Y-%m-%d %X', time.localtime()) + ' ' + \
                    '注册了参数平台。'
            subject = '有新人注册系统参数平台'
            emailSender.sendEmail(emails, context, subject)
            return render().login('')
        except Exception as why:
            print 'exception ' + str(why)
            return render().regin(str(why))
    
class Index:
    def GET(self):
        if not session.user:
            return render().login('')
        
        return render().index(getUserRoles(session.user.user_id), session.user)

class Args:
    def GET(self):
        if not session.user:
            return render().login('')
        else:
            return render().tables(getUserTables(session.user.user_id), getUserRoles(session.user.user_id))
    
class Logout:
    def GET(self):
        try:
            session.kill()
        except Exception as why:
            print 'exception ' + str(why)
        return render().login('')

class Logs:
    def GET(self):
        if not validteAdmin():
            return render().login('您没有查看日志的权限')
        
        try:
            res = Dao.GetLogs()
            return render().logs(getUserRoles(session.user.user_id), res)
        except Exception as why:
            print 'Exception ' + str(why)
            return render().login(str(why))
        #print Dao.json_encode(res)


if __name__ == '__main__':
    app.run()
    
