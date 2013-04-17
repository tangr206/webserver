# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1331970745.156481
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/feed-config-edit.mako'
_template_uri='/feed-config-edit.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user_right = context.get('user_right', UNDEFINED)
        from_version_id = context.get('from_version_id', UNDEFINED)
        apply_id = context.get('apply_id', UNDEFINED)
        stype = context.get('stype', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>\n<script src="/jquery.js" type="text/javascript"></script>\n<title>\u5b57\u6bb5\u7f16\u8f91 - \u65b0\u9c9c\u4e8b\u914d\u7f6e\u7ba1\u7406</title>\n<script type="text/javascript" src="/old-feed-list.js"></script>\n<script type="text/javascript" src="/feed-admin.js"></script>\n<script type="text/javascript">\nvar g_user_right = ')
        # SOURCE LINE 11
        __M_writer(escape(user_right))
        __M_writer(u';\nvar g_stype = ')
        # SOURCE LINE 12
        __M_writer(escape(stype))
        __M_writer(u';\nvar g_from_version_id = ')
        # SOURCE LINE 13
        __M_writer(escape(from_version_id))
        __M_writer(u';\nvar g_apply_id = ')
        # SOURCE LINE 14
        __M_writer(escape(apply_id))
        __M_writer(u';\n\nif (g_user_right <= 0) {\n  var f = window.location.href;\n  window.location = \'https://passport.no.opi-corp.com/login.php?forward=\' + escape(f);\n}\n</script>\n</head>\n<body>\n<div><a href="/feed-list">\u5168\u90e8\u7c7b\u578b\u5217\u8868</a> &gt; <a href="/feed-config-edit?stype=')
        # SOURCE LINE 23
        __M_writer(escape(stype))
        __M_writer(u'">\u7c7b\u578b')
        __M_writer(escape(stype))
        __M_writer(u'</a></div>\n<div id="config-placeholder"></div>\n<br/>\n<div id="versions-header">\n<table width="1000" border="0" class="t1">\n  <tbody><tr>\n      <th colspan="5">Feed\u5168\u90e8\u7248\u672c\u5217\u8868(\u5171\u6709 <span id="version_count">?</span> \u4e2a\u7248\u672c) <a id="create_version" style="float:right;" href="#nogo">\u65b0\u5efa\u7248\u672c</a></th>\n  </tr>\n</tbody></table>\n</div>\n</body>\n<script type="text/javascript">\nvar g_max_version = 0;\n$(\'#create_version\').click(\n  function() {\n    var v = 1 + g_max_version;\n    if (!confirm(\'\u786e\u5b9a\u521b\u5efa\u65b0\u7248\u672c \' + v + \' \u5417?\')) {\n      return;\n    }\n    $.ajax(\'/add-stype-version?stype=\' + g_stype, {\n      \'success\' : function(text) {\n        var v = parseInt(text);\n        if (!isNaN(v) && v > 0) {\n          var feed_key = new FeedKeyView(g_stype, v, -1, -1, 1, false);\n          feed_key.AppendToBody();\n           feed_key.ShowMapping(false);\n           feed_key.ShowKeys(false);\n           feed_key.Disable();\n          ++ g_max_version;\n        } else {\n          alert(\'\u521b\u5efa\u65b0\u7248\u672c\u5931\u8d25, \u8bf7\u8054\u7cfb\u7ba1\u7406\u5458\');\n        }\n      },\n      \'error\' : function(text){\n        alert(\'\u521b\u5efa\u65b0\u7248\u672c\u5931\u8d25\');\n      }\n    });\n  }\n);\n\nif (g_apply_id > 0) {\n  $(\'#create_version\').click(\n    function() {\n      $.ajax(\'/version-apply-handled?apply_id=\' + g_apply_id, {\n          success : function(text) {\n          },\n          error : function(){\n          }\n        });\n    }\n  );\n}\n\n$(document).ready(\n  function() {\n    if(g_stype <= 0) {\n      $(\'#versions-header\').css(\'display\', \'none\');\n    } else {\n      $.ajax(\'/get-stype-versions?stype=\' + g_stype, {\n        \'success\' : function(text){\n          var versions = $.parseJSON(text); \n          for(var i = 0; i < versions.length; ++i) {\n            var v = versions[i];\n            var view = new FeedKeyView(g_stype, v.version, \n                v.using_tpl_id, v.test_tpl_id, v.status, true);\n            view.AppendToBody();\n            view.ShowMapping(false);\n            view.ShowKeys(false);\n            if (g_max_version < v.version) {\n              g_max_version = v.version;\n            }\n          }\n          $(\'#version_count\').html(versions.length);\n        },\n        \'error\' : function(){\n        }\n      });\n    }\n\n    var cfg_view = new FeedConfigView(g_stype);\n    cfg_view.Load();\n    cfg_view.AppendToNode($(\'#config-placeholder\'));\n    if (g_user_right < 2) {\n      cfg_view.Disable();\n      $(\'#create_version\').hide();\n    }\n    // cfg_view.HideMapping();\n  }\n);\n</script>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


