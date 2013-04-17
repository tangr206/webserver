#coding=utf8

ctrl_user = 'args_user'
ctrl_db = 'args_manage'
ctrl_host = '10.11.18.146'
ctrl_pw = 'args_pwd'
ctrl_dbn = 'mysql'
ctrl_port = 3306
#grant all on args_manage.* to 'args_user'@'%' identified by 'args_pwd'

email_sender = 'ad.report@renren-inc.com'
email_sender_user = 'ad.report'
email_sender_pwd = 'AdEngine9999'
email_server = '10.7.2.18' #mail.renren-inc.com
email_server_port = 587


oper_type = {
             'regin' : '0',
             'login' : '1',
             'getTable' : '2',
             'changeArgs' : '3',
             'deleteArgs' : '4',
             'addArgs' : '5',
             'changeUserRoles' : '6'
             }
oper_type_ch = {
             '0' : '注册',
             '1' : '登录',
             '2' : '查看',
             '3' : '修改参数',
             '4' : '删除参数',
             '5' : '添加参数',
             '6' : '修改用户权限'
             }