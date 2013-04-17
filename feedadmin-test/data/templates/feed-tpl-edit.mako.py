# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333687672.0290101
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/feed-tpl-edit.mako'
_template_uri='/feed-tpl-edit.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user_right = context.get('user_right', UNDEFINED)
        version = context.get('version', UNDEFINED)
        tpl_using = context.get('tpl_using', UNDEFINED)
        tpl_id = context.get('tpl_id', UNDEFINED)
        stype = context.get('stype', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\r\n<title>\u65b0\u9c9c\u4e8b\u6a21\u677fview\u7f16\u8f91</title>\r\n<link href="/css/new-style.css" rel="stylesheet" type="text/css" />\r\n<script src="/jquery.js" type="text/javascript"></script>\r\n<script type="text/javascript" src="/feed-admin.js"></script>\r\n<script type="text/javascript">\r\nvar g_user_right = ')
        # SOURCE LINE 10
        __M_writer(escape(user_right))
        __M_writer(u';\r\nvar g_tpl_using = ')
        # SOURCE LINE 11
        __M_writer(escape(tpl_using))
        __M_writer(u';\r\nvar g_stype = ')
        # SOURCE LINE 12
        __M_writer(escape(stype))
        __M_writer(u';\r\nvar g_version = ')
        # SOURCE LINE 13
        __M_writer(escape(version))
        __M_writer(u';\r\nvar g_tpl_id = ')
        # SOURCE LINE 14
        __M_writer(escape(tpl_id))
        __M_writer(u';\r\n\r\nif (g_user_right <= 0) {\r\n  var f = window.location.href;\r\n  window.location = \'https://passport.no.opi-corp.com/login.php?forward=\' + escape(f);\r\n}\r\n</script>\r\n</head>\r\n<body>\r\n<div><a href="/feed-list">\u5168\u90e8\u7c7b\u578b\u5217\u8868</a> &gt; <a href="/feed-config-edit?stype=')
        # SOURCE LINE 23
        __M_writer(escape(stype))
        __M_writer(u'">\u7c7b\u578b')
        __M_writer(escape(stype))
        __M_writer(u'</a>\r\n&gt; <a href="/feed-keys-edit?stype=')
        # SOURCE LINE 24
        __M_writer(escape(stype))
        __M_writer(u'&version=')
        __M_writer(escape(version))
        __M_writer(u'">\u6570\u636e\u7248\u672c')
        __M_writer(escape(version))
        __M_writer(u'</a>\r\n&gt; <a href="/feed-tpl-edit?stype=')
        # SOURCE LINE 25
        __M_writer(escape(stype))
        __M_writer(u'&version=')
        __M_writer(escape(version))
        __M_writer(u'&tpl_id=')
        __M_writer(escape(tpl_id))
        __M_writer(u'">\u6a21\u677f\u5e8f\u53f7')
        __M_writer(escape(tpl_id))
        __M_writer(u'</a>\r\n</div>\r\n<table width="1000" border="0" class="t1">\r\n  <tbody><tr>\r\n      <th colspan="5">stype <span style="color:red;font-weight:bold;">')
        # SOURCE LINE 29
        __M_writer(escape(stype))
        __M_writer(u'</span> \r\n        verion <span style="color:red;font-weight:bold;">')
        # SOURCE LINE 30
        __M_writer(escape(version))
        __M_writer(u'</span> \r\n        \u5e8f\u53f7 <span style="color:red;font-weight:bold;">')
        # SOURCE LINE 31
        __M_writer(escape(tpl_id))
        __M_writer(u'</span> \r\n        Feed \u6a21\u677f\u5217\u8868\u7f16\u8f91. </th>\r\n  </tr>\r\n</tbody></table>\r\n<div id="feed-key-view"></div>\r\n<br/>\r\n<span><a href="#nogo" id="add-template">\u65b0\u5efa\u6a21\u677f</a>(\u7c7b\u578b=<select id="add-template-view"><option></option>\r\n        <option value="0">0 \u7f51\u7ad9 Home&amp;Profile</option>\r\n        <option value="1">1 IM</option>\r\n        <option value="2">2 Wap</option>\r\n        <option value="3">3 \u5b9e\u65f6\u5316</option>\r\n        <option value="4">4 \u5f00\u653e\u5e73\u53f0</option>\r\n        <option value="5">5 \u5c0f\u7ad9</option>\r\n</select>)</span>\r\n<table width="1000" id="tpl-list"></table>\r\n</body>\r\n\r\n<script type="text/javascript">\r\n$(\'#add-template\').click(\r\n  function() {\r\n    var view = $(\'#add-template-view\').val();\r\n    if(view.length <= 0) {\r\n      alert(\'\u8bf7\u6307\u5b9a\u6a21\u677fview\u7c7b\u578b\');\r\n      return;\r\n    }\r\n    var view_desc = $(\'option[value=\' + view + \']\', $(\'#add-template-view\')).text();\r\n    var tpl = new TplListItem(view, 0, view_desc, \'empty\');\r\n    alert(\'\u65b0\u5efa\u6210\u529f\uff0c\u5237\u65b0\u9875\u9762\u524d\u8bf7\u6ce8\u610f\u4fdd\u5b58\');\r\n    tpl.AddToList();\r\n  }\r\n);\r\n$(document).ready(\r\n  function() {\r\n    var view = new FeedKeyView(g_stype, g_version, g_tpl_id, -1, 0, true);\r\n    view.AppendToNode($(\'#feed-key-view\'));\r\n    view.HideAllPanel();\r\n \r\n    $.ajax(\'/get-tpls?tpl_id=\' + g_tpl_id, {\r\n      success : function(text) {\r\n        var tpl_list = eval(\'(\' + text + \')\');\r\n        for(var i = 0; i < tpl_list.length; ++i) {\r\n          var view = tpl_list[i][\'view\'];\r\n          var view_desc = $(\'option[value=\' + view + \']\', $(\'#add-template-view\')).text();\r\n          var tpl = new TplListItem(view, tpl_list[i][\'status\'], view_desc, tpl_list[i][\'template\'], g_user_right, g_stype, g_version);\r\n          tpl.AddToList();\r\n          if (g_user_right < 2) {\r\n            tpl.HideEditStatus();\r\n          }\r\n          // \u7ebf\u4e0a\u6a21\u677f\uff0c\u5373\u4f7f\u8d85\u7ea7\u7ba1\u7406\u5458\u4e5f\u4e0d\u80fd\u4fee\u6539, \u5fc5\u987b\u5148\u884c\u4e0b\u7ebf\r\n          if(g_tpl_using && (tpl_list[i][\'status\'] > 0)) {\r\n            tpl.Readonly();\r\n          }\r\n        }\r\n      },\r\n      error : function() {\r\n        alert(\'\u52a0\u8f7d\u6a21\u677f\u5931\u8d25, \u8bf7\u5237\u65b0\u9875\u9762\');\r\n      }\r\n    });\r\n  }\r\n);\r\n$(\'#add-template-view\').attr(\'disabled\', false);\r\n</script>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


