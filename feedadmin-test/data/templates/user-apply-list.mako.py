# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1308558274.977427
_template_filename='/data/xce/pylons-dev/feedadmin/feedadmin/templates/user-apply-list.mako'
_template_uri='/user-apply-list.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>\n<script src="/jquery.js" type="text/javascript"></script>\n<script src="/feed-admin.js" type="text/javascript"></script>\n<title>\u5217\u8868 - \u65b0\u9c9c\u4e8b\u7ba1\u7406</title>\n</head>\n<body>\n<div><a href="/feed-list">\u5168\u90e8\u7c7b\u578b\u5217\u8868</a> &gt; <a href="#nogo">\u65b0\u9c9c\u4e8b\u521b\u5efa\u4ee5\u53ca\u4fee\u6539\u7533\u8bf7\u5217\u8868</a></div>\n<table id="apply-feed-list-table" width="1200" border="1" class="t1">\n  <tr>\n    <th width="5">\u7533\u8bf7id</th>\n    <th width="5">\u65b0\u9c9c\u4e8b\u7c7b\u578bid</th>\n    <th width="300">\u65b0\u9c9c\u4e8b\u7c7b\u578b\u63cf\u8ff0<br/></th>\n    <th width="60">\u4ea7\u54c1\u4eba\u5458</th>\n    <th width="5">\u72b6\u6001</th>\n    <th width="50">\u64cd\u4f5c</th>\n  </tr>\n</table>\n</body>\n\n<script type="text/javascript">\n$(document).ready(\n  function() {\n    $.ajax(\'/get-user-apply-list\', {\n      \'success\' : function(text){\n        var applies = $.parseJSON(text);\n        var table = $(\'#apply-feed-list-table\');\n        var yes = \'<span style="color:green;">\u5df2\u7ecf\u5904\u7406</span>\';\n        var no = \'<span style="color:red;">\u672a\u5904\u7406</span>\';\n        for(var i = 0; i < applies.length; ++i) {\n          var o = applies[i];\n          var node = $(\'<tr><td><span id="toggle-span" class="toggle-span folded"></span>\' + o.apply_id + \'</td>\'\n                   + \'<td>\' + o.feed_stype + \'</td>\'\n                   + \'<td>\' + o.feed_desc + \'</td>\'\n                   + \'<td>\' + o.pm_names + \'</td>\'\n                   + \'<td id="apply_status">\' + (o.status ?  yes : no) + \'</td>\'\n                   + \'<td>\' + (o.status == 0 ? \'<a id="set_handled" href="#nogo">\u8bbe\u4e3a\u5df2\u5904\u7406</a>\' : \'\') + \' <a id="remove_apply" href="#nogo">\u5220\u9664\u7533\u8bf7</a></td></tr>\'\n                   + \'<tr style="display:none;"><td colspan="6"><span id="view_box"></span></td></tr>\');\n          table.append(node);\n\n          $(\'#set_handled\', node).click(\n            function() {\n              var apply_id = o.apply_id;\n              var status_node = $(\'#apply_status\', node);\n              var set_node = $(\'#set_handled\', node);\n              return function() {\n                $.ajax(\'/set-user-apply-handled?apply_id=\' + apply_id, {\n                  \'success\' : function(text){\n                    alert(text);\n                    status_node.html(yes);\n                    set_node.remove();\n                  },\n                  \'error\' : function(){alert(\'\u51fa\u9519\');}\n                });\n              };\n            }()\n          );\n\n          $(\'#remove_apply\', node).click(\n            function() {\n              var apply_id = o.apply_id;\n              return function() {\n                $.ajax(\'/remove-user-apply?apply_id=\' + apply_id, {\n                  \'success\' : function(text){\n                    alert(text);\n                  },\n                  \'error\' : function(){alert(\'\u5220\u9664\u5931\u8d25\');}\n                });\n              };\n            }()\n          );\n\n\n          $(\'span.toggle-span\', node).click(\n            function() {\n              var T = node;\n              return function() {\n                if ($(this).hasClass(\'folded\')) {\n                  $(\'#view_box\', T).parent().parent().show();\n                  $(this).removeClass(\'folded\').addClass(\'expanded\')\n                } else {\n                  $(\'#view_box\', T).parent().parent().hide();\n                  $(this).removeClass(\'expanded\').addClass(\'folded\')\n                }\n              };\n            }()\n          );\n          var aid = o.apply_id;\n          var apply_view = new UserApplyView(aid);\n          apply_view.AppendToNode($(\'#view_box\', node));\n          // apply_view.Disable();\n        }\n      },\n      \'error\' : function(){\n        alert(\'\u52a0\u8f7d\u51fa\u9519\');\n      }\n    });\n  }\n);\n</script>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


