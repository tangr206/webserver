# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1348890791.6610849
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/experi-select.mako'
_template_uri='/experi-select.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<link rel="shortcut icon" href="favicon-rr.ico" type="image/x-icon"> \n<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />\n<link rel="stylesheet" href="/css/select.css" type="text/css" media="all"></link>\n<link rel="stylesheet" href="/css/signin.css" type="text/css" media="all"></link>\n\n\n<title>Experiment Select</title>\n<script type="text/javascript" src="/jquery.js"></script>\n\n<script type=text/javascript>\n$(function(){\n\t$(\'#mobanwang_com li\').hover(function(){\n\t\t$(this).children(\'ul\').stop(true,true).show(\'slow\');\n\t},function(){\n\t\t$(this).children(\'ul\').stop(true,true).hide(\'slow\');\n\t});\n\n        $(\'#sign\').hover(function(){\n                $(\'#sign_in\').stop(true,true).show(\'slow\');\n        },function(){\n                $(\'#sign_in\').stop(true,true).hide(\'slow\');\n        });\n});\n\n</script>\n\n\n<div id="wrapper" style=" z-index:1000;">\n<ul id="mobanwang_com" class="first-menu">\n  <li><a href="stat" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>\n\n  <li><a href="#" >\u5b9e\u9a8c\u5e73\u53f0</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="experi-select" target="_self" style="z-index:1000;">\u5b9e\u9a8c\u767b\u8bb0\u67e5\u770b</a></li>\n      <li><a href="stat-ABDebug" target="_self" style="z-index:1000;">\u9009\u62e9\u5c3e\u53f7\u67e5\u770b</a></li>\n    </ul>\n  </li>\n  <li><a href="http://feed.d.xiaonei.com/stat-detail" target="_blank">\u8be6\u7ec6\u4fe1\u606f</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="check-plat" target="_self" style="z-index:1000;">\u9009\u62e9\u5e73\u53f0\u67e5\u770b</a></li>\n      <li><a href="check-stype" target="_self" style="z-index:1000;">\u9009\u62e9\u7c7b\u578b\u67e5\u770b</a></li>\n    </ul>\n  </li>\n</ul>\n</div>\n\n\n\n<h1>Experiment Select</h1>\n\n</head>\n\n<script type="text/javascript">\n$(document).ready(function() {\n  $.ajax({\n    type: \'POST\',\n    url: \'/experi-list\',\n    async: false,\n    success : function(text){\n      if(!text || text.length <= 0) return;\n      currentData = eval(\'(\' + text + \')\');\n      var html = "";\n      for(var i=0; i<currentData.length; ++i) {\n\tcc = "checked" + i\n        html += "<tr><th>"+i+"</th>"\n            + "<td>" + currentData[i]["tail"].toString() + "</td>" + "<td>" + currentData[i]["begin"].toString() + "</td>" \n            + "<td>" + currentData[i]["end"].toString() + "</td>" + "<td>" + currentData[i]["describ"].toString() + "</td>"\n            + "<td>" + currentData[i]["contact"].toString() + "</td>" + "<td>" + currentData[i]["summary"].toString() + "</td>"\n\t    + "</td>" + "<td id=\\""+cc+"\\" onclick=\\"alert(\'" + cc + "\')\\" >" + cc  + "</td>"\n            + "</tr>";\n      }\n\t//alert(html)\n      $("#data").append(html);\n    },\n    error : function(){\n      alert(\'/\u52a0\u8f7d\u51fa\u9519\');\n    }\n  });\n});\n</script>\n\n\n   \n<body>\n\n<div id="content" style="margin: 20px 20px 20px 20px;" >\n\n\t<div id="left" style="margin: 20px 20px 20px 20px; " >\n\n<div id="sign" style="margin:10px 0px 10px 0px">\n\t\t\t<fieldset>\n\t\t\t<legend>\u5b9e\u9a8c\u767b\u8bb0</legend>\n<div style="min-height:20px;">\n<div id="sign_in" style=" margin: 20px 20px 20px 20px;display:none" >\n\n<form class="form">\n  <p class="name">\n    <label for="name">\u5f00\u59cb\u65e5\u671f</label>\n    <input type="text"  id="begin" />\n  </p>\n</br>\n  <p class="email">\n    <label for="name">\u7ed3\u675f\u65e5\u671f</label>\n    <input type="text"  id="end" />\n  </p>\n</br>\n  <p class="web">\n    <label for="name">\u5b9e\u9a8c\u5c3e\u53f7</label>\n    <input type="text"  id="tail" />\n  </p>\n</br>\n  <p class="email">\n    <label for="email">@\u8054\u7cfb\u4eba </label>\n    <input type="text" id="email" />\n  </p>\n</br>\n   <p class="text">\n    <label for="name">\u5b9e\u9a8c\u63cf\u8ff0</label>\n    <textarea name="text" id="describ"></textarea>\n  </p>\n<br/>\n  <p class="submit" >\n    <label onclick="mysubmit()" />\u63d0\u4ea4</label>\n  </p>\n</form>\n</div>\n</div>\n\t\t\t</fieldset>\n</div>\n\n\n\n\t\t\t<fieldset style="margin:20px 0px 0px 0px">\n\t\t\t<legend>\u5b9e\u9a8c\u5217\u8868</legend>\n<table id="data" cellspacing="0" cellpadding="0">\n      <tr>\n        <td>&nbsp;</td>\n        <th>\u5b9e\u9a8c\u5c3e\u53f7</th>\n        <th>\u5f00\u59cb\u65e5\u671f</th>\n        <th>\u7ed3\u675f\u65e5\u671f</th>\n        <th>\u5b9e\u9a8c\u63cf\u8ff0</th>\n        <th>\u8d1f\u8d23\u4eba</th>\n        <th>\u5b9e\u9a8c\u7ed3\u8bba</th>\n        <th>\u70b9\u51fb\u67e5\u770b</th>\n      </tr>\n    </table>\n\t\t\t</fieldset>\n\n\n\n\t</div>\n</div>\n</body>\n\n<script type="text/javascript">\n\n        function mysubmit() {\n                 begin = $("#begin").val() \n                 end = $("#end").val()\n                 tail = $("#tail").val()\n                 describ = $("#describ").val()\n                 contact = $("#email").val()\n                  $.ajax({\n                    type: \'POST\',\n                    url: \'/experi-insert\',\n                    async: false,\n                    data: "begin="+begin+"&end="+end+"&tail="+tail+')
        # SOURCE LINE 171
        __M_writer(u'                                "&describ="+describ+"&contact="+contact, \n                    success : function(text){\n                                updateForm()\n                            },\n                    error : function(){\n                      alert(\'mysubmit \u51fa\u9519\');\n                    }\n                });\n\n        }\n\n        function updateForm() {\n          $.ajax({\n            type: \'POST\',\n            url: \'/experi-list\',\n            async: false,\n            success : function(text){\n              if(!text || text.length <= 0) return;\n              if($("#data tr").length > 1) {\n                        var len = $("#data tr").length;\n                        for(var i = len-1; i > 0; --i) {\n                          $("#data tr:eq(" + i.toString() + ")").remove();\n                        }\n              }\n currentData = eval(\'(\' + text + \')\');\n              var html = "";\n              for(var i=0; i<currentData.length; ++i) {\n                cc = "update" + i\n                html += "<tr><th>"+i+"</th>"\n                    + "<td>" + currentData[i]["tail"].toString() + "</td>" + "<td>" + currentData[i]["begin"].toString() + "</td>" \n                    + "<td>" + currentData[i]["end"].toString() + "</td>" + "<td>" + currentData[i]["describ"].toString() + "</td>"\n                    + "<td>" + currentData[i]["contact"].toString() + "</td>" + "<td>" + currentData[i]["summary"].toString() + "</td>"\n                    + "</td>" + "<td id=\\""+cc+"\\" onclick=\\"alert(\'" + cc + "\')\\" >" + cc  + "</td>"\n                    + "</tr>";\n              }\n              $("#data").append(html);\n            },\n            error : function(){\n              alert(\'updateFoem \u52a0\u8f7d\u51fa\u9519\');\n            }\n          });\n        }\n        \n\n//====================================================================================\n</script>\n\n\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


