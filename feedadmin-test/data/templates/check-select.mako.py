# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1348646456.503448
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/check-select.mako'
_template_uri='/check-select.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" \n\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n\n<html>\n\n<head>\n\n<title>Navigation Effect Using jQuery</title>\n\n<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />\n<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>\n<title>content</title>\n<script type="text/javascript" src="/jquery.js"></script>\n<script src="/Highcharts-2.2.5/js/highcharts.js"></script>\n\n<script type="text/javascript" src="sliding_effect.js"></script>\n\n\n\n\n\n\n<script type=text/javascript>\n$(function(){\n\t$(\'#mobanwang_com li\').hover(function(){\n\t\t$(this).children(\'ul\').stop(true,true).show(\'slow\');\n\t},function(){\n\t\t$(this).children(\'ul\').stop(true,true).hide(\'slow\');\n\t});\n\n});\n\n</script>\n\n<div id="wrapper" style=" z-index:1000;">\n<ul id="mobanwang_com" class="first-menu">\n  <li><a href="stat" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>\n\n  <li><a href="#" target="_self">\u5b9e\u9a8c\u5e73\u53f0</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="experi-signin" target="_self" style="z-index:1000;">\u5b9e\u9a8c\u767b\u8bb0</a></li>\n      <li><a href="experi-select" target="_self" style="z-index:1000;">\u9009\u62e9\u5b9e\u9a8c\u67e5\u770b</a></li>\n      <li><a href="stat-ABDebug" target="_self" style="z-index:1000;">\u9009\u62e9\u5c3e\u53f7\u67e5\u770b</a></li>\n    </ul>\n  </li>\n  <li><a href="http://feed.d.xiaonei.com/stat-detail" target="_blank">\u8be6\u7ec6\u4fe1\u606f</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="check-plat" target="_self" style="z-index:1000;">\u9009\u62e9\u5e73\u53f0\u67e5\u770b</a></li>\n      <li><a href="check-stype" target="_self" style="z-index:1000;">\u9009\u62e9\u7c7b\u578b\u67e5\u770b</a></li>\n    </ul>\n  </li>\n  <!--li><a href="http://feed.d.xiaonei.com/quota" target="_blank">\u914d\u989d\u7cfb\u7edf</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="#" target="_self" style="z-index:1000;">\u67e5\u770b</a></li>\n    </ul>\n  </li-->\n</ul>\n</div>\n\n\n\n</head>\n\n<body>\n\n<div id="navigation-block"> <img src="background.jpg" id="hide" />\n\n\n  <ul id="sliding-navigation">\n\n    <li class="sliding-element">\n\n      <h3>\u9009\u62e9\u5e73\u53f0</h3>\n\n    </li>\n\n    <li class="sliding-element"><a href="/check-plat?view=all">\u6240\u6709</a></li>\n\n    <li class="sliding-element"><a href="/check-plat?view=view0" >WEB</a></li>\n\n    <li class="sliding-element"><a href="/check-plat?view=view2" >\u624b\u673a</a></li>\n\n    <li class="sliding-element"><a  href="/check-plat?view=view3">\u5b9e\u65f6\u5316</a></li>\n    <li class="sliding-element"><a href="/check-plat?view=view4" >\u5f00\u653e\u5e73\u53f0</a></li>\n    <li class="sliding-element"><a href="/check-plat?view=view6" >TimeLine</a></li>\n\n  </ul>\n\n</div>\n\n\n\n</body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


