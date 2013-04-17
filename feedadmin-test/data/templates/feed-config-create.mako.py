# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1334220090.223603
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/feed-config-create.mako'
_template_uri='/feed-config-create.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        apply_id = context.get('apply_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>\n<script src="/jquery.js" type="text/javascript"></script>\n<title>\u521b\u5efa\u65b0\u9c9c\u4e8b\u7c7b\u578b - \u65b0\u9c9c\u4e8b\u914d\u7f6e\u7ba1\u7406</title>\n<script type="text/javascript" src="/old-feed-list.js"></script>\n<script type="text/javascript" src="/feed-admin.js"></script>\n</head>\n<body>\n<div><a href="/feed-list">\u5168\u90e8\u7c7b\u578b\u5217\u8868</a> &gt; <a href="#nogo">\u65b0\u5efa\u7c7b\u578b</a></div>\n<div id="stype-apply-placeholder"></div>\n<br/>\n<div id="config-placeholder"></div>\n<br/>\n<input id="config-submit" style="margin-left:570px;font-weight:bold;" type="button" value="\u5b8c\u6210"/>\n<div style="display:block;margin:0 auto;">\n</div>\n</body>\n<script type="text/javascript">\nvar g_apply_id = ')
        # SOURCE LINE 22
        __M_writer(escape(apply_id))
        __M_writer(u";\nvar cfg_view = new FeedConfigView(-1);\n$('#config-submit').click(\n  function() {\n    // cfg_view.Save(true, g_apply_id);\n    cfg_view.Save(true, g_apply_id, true);\n  }\n);\n\n$(document).ready(\n  function() {\n    cfg_view.Load();\n    cfg_view.AppendToNode($('#config-placeholder'));\n    // cfg_view.Disable();\n    cfg_view.HideSave();\n\n    if (g_apply_id > 0) {\n      var v = new StypeApplyView(g_apply_id); \n      v.AppendToNode($('#stype-apply-placeholder'));\n      v.Disable();\n    }\n  }\n);\n</script>\n</html>\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


