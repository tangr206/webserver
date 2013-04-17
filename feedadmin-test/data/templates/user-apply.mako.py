# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1308207059.2605231
_template_filename='/data/xce/pylons-dev/feedadmin/feedadmin/templates/user-apply.mako'
_template_uri='/user-apply.mako'
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
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>\n<script src="/jquery.js" type="text/javascript"></script>\n<script type="text/javascript" src="/feed-admin.js"></script>\n<style type="text/css">\n</style>\n<title>\u7533\u8bf7\u65b0\u7c7b\u578b\u65b0\u9c9c\u4e8b - \u65b0\u9c9c\u4e8b\u7ba1\u7406</title>\n</head>\n<body>\n<div id="user-apply-container"></div>\n<script type="text/javascript">\n$(document).ready(\n  function() {\n    var v = new UserApplyView(); \n    v.AppendToNode($(\'#user-apply-container\'));\n    // v.Disable();\n  }\n);\n</script>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


