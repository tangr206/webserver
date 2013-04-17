# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1313661736.2238979
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/feed-keys-edit.mako'
_template_uri='/feed-keys-edit.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        is_user = context.get('is_user', UNDEFINED)
        from_tpl_id = context.get('from_tpl_id', UNDEFINED)
        user_right = context.get('user_right', UNDEFINED)
        version = context.get('version', UNDEFINED)
        apply_id = context.get('apply_id', UNDEFINED)
        stype = context.get('stype', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>\n<script src="/jquery.js" type="text/javascript"></script>\n<title>\u5b57\u6bb5\u7f16\u8f91 - \u65b0\u9c9c\u4e8b\u914d\u7f6e\u7ba1\u7406</title>\n<script type="text/javascript" src="/feed-admin.js"></script>\n<script type="text/javascript">\nvar g_user_right = ')
        # SOURCE LINE 10
        __M_writer(escape(user_right))
        __M_writer(u';\nvar g_stype = ')
        # SOURCE LINE 11
        __M_writer(escape(stype))
        __M_writer(u';\nvar g_version = ')
        # SOURCE LINE 12
        __M_writer(escape(version))
        __M_writer(u';\nvar g_from_tpl_id = ')
        # SOURCE LINE 13
        __M_writer(escape(from_tpl_id))
        __M_writer(u';\nvar g_apply_id = ')
        # SOURCE LINE 14
        __M_writer(escape(apply_id))
        __M_writer(u';\nvar g_is_user = ')
        # SOURCE LINE 15
        __M_writer(escape(is_user))
        __M_writer(u';\nif (g_user_right <= 0) {\n  var f = window.location.href;\n  window.location = \'https://passport.no.opi-corp.com/login.php?forward=\' + escape(f);\n}\n</script>\n</head>\n<body>\n<div><a href="/feed-list">\u5168\u90e8\u7c7b\u578b\u5217\u8868</a> &gt; <a href="/feed-config-edit?stype=')
        # SOURCE LINE 23
        __M_writer(escape(stype))
        __M_writer(u'">\u7c7b\u578b')
        __M_writer(escape(stype))
        __M_writer(u'</a>\n&gt; <a href="/feed-keys-edit?stype=')
        # SOURCE LINE 24
        __M_writer(escape(stype))
        __M_writer(u'&version=')
        __M_writer(escape(version))
        __M_writer(u'">\u6570\u636e\u7248\u672c')
        __M_writer(escape(version))
        __M_writer(u'</a>\n</div>\n<table width="1000" border="0" class="t1">\n  <tbody><tr>\n      <th colspan="5">Feed\u6570\u636e\u5b57\u6bb5\u5b9a\u4e49(stype:<span>')
        # SOURCE LINE 28
        __M_writer(escape(stype))
        __M_writer(u'</span>, \u7248\u672c\u53f7: ')
        __M_writer(escape(version))
        __M_writer(u') \n        <span class="admin-only hidden">&nbsp; \u72b6\u6001 <a id="version-status-edit" href="#nogo">\u4fee\u6539</a> <select id="version-status" disabled="true"><option value="0">disabled</option><option value="1">test</option><option value="2">read only</option><option value="3">dispatching</option></select></span>\n        </th>\n  </tr>\n</tbody></table>\n<div id="feed-key-container"></div>\n<div class="seq-list-container"><div>\u6a21\u677f\u5e8f\u53f7\u7ba1\u7406\uff1a\n<a id="create_seq" href="#nogo">\u65b0\u5efa</a> | \u7ebf\u4e0a\u6a21\u677f\u5e8f\u53f7 <a class="admin-only hidden" id="using-version-id-edit" href="#nogo">\u4fee\u6539</a> <select id="using-version-id" value="" disabled="true"><option>0</option></select> | \u6d4b\u8bd5\u6a21\u677f\u5e8f\u53f7 <a id="test-version-id-edit" href="#nogo">\u4fee\u6539</a> <select id="test-version-id" value="" disabled="true"><option>0</option></select>&nbsp; </div>\n\u5168\u90e8\u5e8f\u53f7\u5217\u8868\uff1a\n</div>\n<br/>\n</body>\n<script type="text/javascript">\n$(\'#create_seq\').click(\n  function() {\n      $.ajax(\'/add-version-seq?stype=\' + g_stype + \'&version=\' + g_version, {\n          success : function(text) {\n            alert(\'\u6210\u529f\u65b0\u5efa\u6a21\u677f\u5e8f\u53f7 : \' + text);\n            var seq_list = $(\'div.seq-list-container\');\n            seq_list.append($(\'<a style="margin-left:10px;" href="/feed-tpl-edit?stype=\' + g_stype \n                + \'&version=\' + g_version + \'&tpl_id=\' + text + \'">\u6a21\u677f\u5e8f\u53f7\' + text + \'</a>\'));\n          },\n          error : function(){\n          }\n        });\n  }\n);\n\nif (g_apply_id > 0) {\n  $(\'#create_seq\').click(\n    function() {\n      $.ajax(\'/seq-apply-handled?apply_id=\' + g_apply_id, {\n          success : function(text) {\n          },\n          error : function(){\n          }\n        });\n    }\n  );\n}\n\n$(\'#using-version-id-edit\').click(\n  function() {\n    if (!confirm("\u8be5\u64cd\u4f5c\u4f1a\u5f71\u54cd\u5230\u7ebf\u4e0a\u65b0\u9c9c\u4e8b\u3002\u786e\u5b9a\u8981" + $(this).html() + "\u5417?")) {\n      return;\n    }\n    if ($(this).html() == \'\u4fdd\u5b58\') {\n      $.ajax(\'/update-stype-version-using-id?stype=\' + g_stype + \'&version=\' + g_version + \'&tpl_id=\' + $(\'#using-version-id\').val(), {\n        \'success\' : function(text){\n          alert(text);\n          $(this).html(\'\u4fee\u6539\');\n          $(\'#using-version-id\').attr(\'disabled\', true);\n        },\n        \'error\' : function() {\n          alert(\'\u4fdd\u5b58\u5931\u8d25\');\n        }\n      });\n    } else {\n      $(this).html(\'\u4fdd\u5b58\');\n      $(\'#using-version-id\').attr(\'disabled\', false);\n    }\n  }\n);\n\n$(\'#version-status-edit\').click(\n  function() {\n    if (!confirm("\u8be5\u64cd\u4f5c\u4f1a\u5f71\u54cd\u5230\u7ebf\u4e0a\u65b0\u9c9c\u4e8b\u3002\u786e\u5b9a\u8981" + $(this).html() + "\u5417?")) {\n      return;\n    }\n    if ($(this).html() == \'\u4fdd\u5b58\') {\n      $.ajax(\'/update-stype-version-status?stype=\' + g_stype + \'&version=\' + g_version + \'&status=\' + $(\'#version-status\').val(), {\n        "context" : $(this),\n        \'success\' : function(text){\n          alert(text);\n          $(this).html(\'\u4fee\u6539\');\n          $(\'#version-status\').attr(\'disabled\', true);\n        },\n        \'error\' : function() {\n          alert(\'\u4fdd\u5b58\u5931\u8d25\');\n        }\n      });\n    } else {\n      $(this).html(\'\u4fdd\u5b58\');\n      $(\'#version-status\').attr(\'disabled\', false);\n    }\n  }\n);\n\n$(\'#test-version-id-edit\').click(\n  function() {\n    if ($(this).html() == \'\u4fdd\u5b58\') {\n      $.ajax(\'/update-stype-version-test-id?stype=\' + g_stype + \'&version=\' + g_version + \'&tpl_id=\' + $(\'#test-version-id\').val(), {\n        \'success\' : function(text){\n          alert(text);\n          $(this).html(\'\u4fee\u6539\');\n          $(\'#test-version-id\').attr(\'disabled\', true);\n        },\n        \'error\' : function() {\n          alert(\'\u4fdd\u5b58\u5931\u8d25\');\n        }\n      });\n    } else {\n      $(this).html(\'\u4fdd\u5b58\');\n      $(\'#test-version-id\').attr(\'disabled\', false);\n    }\n  }\n);\n\n$(document).ready(\n  function() {\n    if (g_user_right >= 2) {\n      $(\'.admin-only\').removeClass(\'hidden\');\n    }\n\n    if(g_stype <= 0) {\n      return;\n    }\n    $.ajax(\'/get-stype-version-seqs?stype=\' + g_stype + \'&version=\' + g_version, {\n      \'success\' : function(text){\n        var seqs = $.parseJSON(text); \n        for(var i = 0; i < seqs.length; ++i) {\n          // var view = new FeedKeyView(g_stype, g_version, seqs[i]);\n          // view.AppendToBody();\n          var seq_list = $(\'div.seq-list-container\');\n          if (seq_list.length <= 0) {\n            seq_list = $(\'<div class="seq-list-container"> \u6a21\u677f\u5e8f\u53f7\u5217\u8868(\u70b9\u51fb\u7f16\u8f91\u6a21\u677f): </div>\');\n            $(document.body).append(seq_list);\n          }\n          seq_list.append($(\'<a id="seq_entrance_\' + seqs[i] + \'" style="margin-left:10px;" href="/feed-tpl-edit?stype=\' + g_stype \n              + \'&version=\' + g_version + \'&tpl_id=\' + seqs[i] + \'">\u6a21\u677f\u5e8f\u53f7\' + seqs[i] + \'</a>\'));\n          \n          $(\'#test-version-id\').append($(\'<option value=\' + seqs[i] + \'>\' + seqs[i] + \'</option>\'));\n          $(\'#using-version-id\').append($(\'<option value=\' + seqs[i] + \'>\' + seqs[i] + \'</option>\'));\n        }\n        $.ajax(\'/get-stype-version-info?stype=\' + g_stype + \'&version=\' + g_version, {\n           \'success\' : function(text) {\n             var o = $.parseJSON(text);\n             $(\'#test-version-id\').val(o.test_id);\n             $(\'#seq_entrance_\' + o.test_id).html(\'\u6a21\u677f\u5e8f\u53f7\' + o.test_id + \'(\u6b63\u5728\u6d4b\u8bd5)\').css(\'color\', \'green\');\n             \n             $(\'#using-version-id\').val(o.using_id);\n             $(\'#seq_entrance_\' + o.using_id).html(\'\u6a21\u677f\u5e8f\u53f7\' + o.using_id + \'(\u7ebf\u4e0a\u751f\u6548)\').css(\'color\', \'red\');\n\n             $(\'#version-status\').val(o.status);\n             var readonly = (o.status > 1 && g_user_right < 2);\n\n             var view = new FeedKeyView(g_stype, g_version, o.using_id, o.test_id, o.status, readonly);\n             view.AppendToNode($(\'#feed-key-container\'));\n             view.HideVersion();\n             view.HideStatus();\n             view.HideSeqs();\n             view.HideToggle();\n           },\n           \'error\' : function() {\n             alert(\'\u52a0\u8f7did\u51fa\u9519\');\n           }\n        });\n      },\n      \'error\' : function(text){\n      }\n    });\n  }\n);\n</script>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


