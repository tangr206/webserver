# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1307621172.5467789
_template_filename='/data/xce/pylons-dev/feedadmin/feedadmin/templates/apply-new-version-list.mako'
_template_uri='/apply-new-version-list.mako'
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
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>\n<script src="/jquery.js" type="text/javascript"></script>\n<script src="/feed-admin.js" type="text/javascript"></script>\n<title>\u5217\u8868 - \u65b0\u9c9c\u4e8b\u7ba1\u7406</title>\n</head>\n<body>\n<table id="apply-version-list-table" width="1200" border="1" class="t1">\n  <tr>\n    <th width="5">\u7533\u8bf7id</th>\n    <th width="60">\u4ea7\u54c1\u4eba\u5458</th>\n    <th width="300">\u4fee\u6539\u539f\u56e0\u63cf\u8ff0<br/></th>\n    <th width="5">\u72b6\u6001</th>\n    <th width="50">\u64cd\u4f5c</th>\n  </tr>\n</table>\n</body>\n\n<script type="text/javascript">\n$(document).ready(\n  function() {\n    $.ajax(\'/get-apply-version-list\', {\n      \'success\' : function(text){\n        var v = $.parseJSON(text);\n        var table = $(\'#apply-version-list-table\');\n        var yes = \'<span style="color:green;">\u5df2\u7ecf\u5904\u7406</span>\';\n        var no = \'<span style="color:red;">\u672a\u5904\u7406</span>\';\n        for(var i = 0; i < v.length; ++i) {\n          var o = v[i];\n          var html = \'<tr><td>\' + o.apply_id + \'</td>\'\n                   + \'<td>\' + o.pm_names + \'</td>\'\n                   + \'<td>\' + o.version_desc + \'</td>\'\n                   + \'<td>\' + (o.status ?  yes : no) + \'</td>\'\n                   + \'<td><a target="_blank" href="/feed-config-edit?stype=\' + o.stype_id + \'&from_version_id=\' + o.from_version_id + \'&apply_id=\' + o.apply_id + \'">\u521b\u5efa\u65b0\u7684\u5b57\u6bb5\u7248\u672c</a> <a href="#nogo">\u5220\u9664\u7533\u8bf7</a></td>\';\n\n           table.append($(html));\n        }\n      },\n      \'error\' : function(){\n        alert(\'\u52a0\u8f7d\u51fa\u9519\');\n      }\n    });\n  }\n);\n</script>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


