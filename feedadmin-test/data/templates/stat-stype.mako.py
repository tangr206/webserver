# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1346932363.431071
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/stat-stype.mako'
_template_uri='/stat-stype.mako'
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
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">\n\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>\n<script type="text/javascript" src="/jquery.min.js"></script>\n<script type="text/javascript" src="/old-feed-list.js"></script>\n<script type="text/javascript" src="/jquery.date_input.js"></script>\n<script src="/Highcharts-2.2.5/js/highcharts.js"></script>\n<script type="text/javascript">$($.date_input.initialize);</script>\n<link rel="stylesheet" href="/css/date_input.css" type="text/css"></link>\n<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>\n<style type="text/css">\na{ text-decoration:none;}\na:hover{ text-decoration:underline;}\n</style>\n<title>stat-stype</title>\n\n\t<!--header-->\n\t<div class="headerbox" style="background-color:#28004D">\n\t\t<div class="header">\n\t\t\t<h1 class="logobox"><img src="logo.png" alt="\u4eba\u4eba\u7f51\u6570\u636e\u5e73\u53f0" height="42" width="202"></h1>\n\t\t\t<h2 class="page-title"><a href="/stat-detail" style= " font-family: \'Open Sans\',Arial,Helvetica,sans-serif;   color: #FFFFFF;    font-size: 20px;    padding: 5px 10px;    text-shadow: 0 3px 0 #0000FF, 1px 2px 2px #AAAAAA;">  \u65b0\u9c9c\u4e8b\u6570\u636e\u5e73\u53f0-\u5404\u7c7b\u578b\u8d8b\u52bf</a></h2>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\t<!-- end -->\n\n\n<script type="text/javascript">\n$(function(){\n\t$(\'#mobanwang_com li\').hover(function(){\n\t\t$(this).children(\'ul\').stop(true,true).show(\'slow\');\n\t},function(){\n\t\t$(this).children(\'ul\').stop(true,true).hide(\'slow\');\n\t});\n});\n\nvar allIds = new Array();\nvar currentData = new Array();\n\nvar stypeDesc = new Array();\nfunction getStypeDesc() {\n  $.ajax({\n    type: \'POST\',\n    url: \'/get-stype-list\',\n    async: false,\n    success : function(text){\n      var data = eval(\'(\' + text + \')\');\n      for(var i=0; i< data.length; ++i) {\n        stypeDesc[data[i]["stype"].toString()] = data[i]["description"];\n      }\n    },\n    error : function(){\n      alert(\'getStypeDesc \u52a0\u8f7d\u51fa\u9519,\u8bf7\u91cd\u65b0\u5237\u65b0\u9875\u9762\');\n    }\n  });\n}\n\n       var chart = {\n            chart: {\n                renderTo: \'container_stype\',\n                type: \'line\',\n\t    },\n            title: {\n                text: \'\u65b0\',\n\t\t\tstyle: {\n\t\t\t\tcolor: \'blue\',\n\t\t\t\tfontSize: \'20px\'\n\t\t\t}\n            },\n            xAxis: {\n\t\ttitle: {\n\t\t\ttext: \'\u65e5\u671f\'\n\t\t},\n                labels: {\n\t\t    rotation: -45,\n                    formatter: function() {\n                        //return this.value // clean, unformatted number for year\n                        return this.value.slice(5,10); // clean, unformatted number for year\n                    }\n                }\n            },\n            yAxis: {\n                title: {\n                    text: \'\u6570\u91cf\'\n                },\n                labels: {\n                    formatter: function() {\n                        return this.value / 10000 + \'w\';\n                   }\n                }\n            },\n            tooltip: {                \n\t\t//shared: true,\n                crosshairs: true,\n                formatter: function() {\n                    return this.series.name +\'  <b>\'+\n                        this.y +\'</b><br/> date:  \'+ this.x //+ "   index:" + series.data[this.point.x - 1];\n                }\n            },\n\t    plotOptions: {\n            },\n            series: []\n        };// var char_taotal\n\n\n\nvar name = [ "\u53d1\u9001\u91cf","\u53d1\u9001\u7528\u6237\u6570", "\u53d6\u65b0\u9c9c\u4e8b\u7684\u7528\u6237\u6570", "\u56de\u590d\u6570", "\u4ea7\u751f\u56de\u590d\u7684\u7528\u6237\u6570", "\u70b9\u51fb\u91cf", "\u4ea7\u751f\u70b9\u51fb\u7684\u7528\u6237\u6570"]\n\n$("select[name=stype]").live(\'change\',\tfunction(){\n  if( $("select[name=stype]").val() == "\u9009\u62e9\u7c7b\u578b") {\n\tdocument.getElementById("container_stype").style.display="none";\n  \treturn;\n  }\n  document.getElementById("container_stype").style.display="block";\n\n  $.ajax({\n    type: \'POST\',\n    url: \'/stat-list\',\n    data: "stype=" + $("select[name=stype]").val() ,\n    success : function(text){\n\t  if(!text || text.length <= 0) {\n\t\t return;\n\t  }\n\t  currentData = eval(\'(\' + text + \')\');\n\n\t\t      var series = [\n\t\t\t\t{name : \'name\', data : []}, \n\t\t\t\t{name : \'name\', data : []}, \n\t\t\t\t{name : \'name\', data : []}, \n\t\t\t\t{name : \'name\', data : []}, \n\t\t\t\t{name : \'name\', data : []}, \n\t\t\t\t{name : \'name\', data : []}, \n\t\t\t\t{name : \'name\', data : []}, \n\t\t      ]\t\n\n\t\tfor (var i=0; i < name.length; ++i) {\n\t\t\tseries[i].name = name[i]\n\t\t}\t\n\n\t\tvar date = new Array(currentData.length);\n\t\tfor(var i = currentData.length - 1, j = 0; i >= 0;  --i, ++j) {\n\t\t\tdate[j] = currentData[i]["date"]\n\t\t\tseries[0].data[j] = currentData[i]["dispatch"] \n\t\t\tseries[1].data[j] =  currentData[i]["dispatch_user"]\n\t\t\tseries[2].data[j] =  currentData[i]["view_user"]\n\t\t\tseries[3].data[j] =  currentData[i]["reply"] \n\t\t\tseries[4].data[j] =  currentData[i]["reply_user"] \n\t\t\tseries[5].data[j] =  currentData[i]["click"]\n\t\t\tseries[6].data[j] =  currentData[i]["click_user"]\n\t\t}\n\t\t\n\n\t\t      chart.title.text = stypeDesc[$("select[name=stype]").val()] + " [" +$("select[name=stype]").val() + "]\u7684\u53d8\u5316\u66f2\u7ebf"\n\t\t      chart.series = []\n\t\t      chart.series.push(series[0]);\n\t\t      //chart.series.push(series[1]);\n\t\t      //chart.series.push(series[2]);\n\t\t      chart.series.push(series[3]);\n\t\t      //chart.series.push(series[4]);\n\t\t      chart.series.push(series[5]);\n\t\t      chart.xAxis.categories = date;\n\n\t\t      chart1 = new Highcharts.Chart(chart)\n\n    },\n    error : function(){\n      alert(\'select stype  \u52a0\u8f7d\u51fa\u9519, \u8bf7\u91cd\u65b0\u5237\u65b0\u9875\u9762\');\n    }\n  });\n});\n\n\n\n$(document).ready(function() {\n\tdocument.getElementById("container_stype").style.display="none";\n\t  $.ajax({\n\t    type: \'POST\',\n\t    url: \'/get-stype-ids\',\n\t    async: false,\n\t    success : function(text){\n\t      ids = eval(\'(\' + text + \')\');\n\t      idsStr = \',\' + ids.join(\',\');\n\t      for(var i = 0; i < ids.length; ++i) {\n\t        allIds[i] = parseInt(ids[i]);\n\t      }\n\t      allIds.sort(function(a, b){ return a-b;});\n\t      var html = \'<option value="\' + 0 + \'">\' + \'\u9009\u62e9\u7c7b\u578b</option>\';\n\t      for(var i = 0; i < allIds.length; ++i) {\n\t        html += \'<option value="\' + allIds[i].toString() + \'">\' + allIds[i].toString() + \'</option>\';\n\t      }\n\t \n\t      $("select[name=stype]").html(html);\n\t    },\n\t    error : function(){\n\t      alert(\'/ready  \u52a0\u8f7d\u51fa\u9519, \u8bf7\u91cd\u65b0\u5237\u65b0\u9875\u9762\');\n\t    }\n\t  });\n\t\n\t\n\tgetStypeDesc();\n\n}); // ready \n\n\n\n\n</script>\n\n</head>\n\n<div id="wrapper" style=" z-index:1000;">\n<ul id="mobanwang_com" class="first-menu">\n  <li><a href="#" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>\n\n  <li><a href="stat" target="_blank">\u5b9e\u9a8c\u5e73\u53f0</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="experi-signin" target="_self" style="z-index:1000;">\u5b9e\u9a8c\u767b\u8bb0</a></li>\n      <li><a href="experi-select" target="_self" style="z-index:1000;">\u9009\u62e9\u5b9e\u9a8c\u67e5\u770b</a></li>\n      <li><a href="http://feed.d.xiaonei.com/stat-ABDebug" target="_self" style="z-index:1000;">\u9009\u62e9\u5c3e\u53f7\u67e5\u770b</a></li>\n    </ul>\n  </li>\n  <li><a href="http://feed.d.xiaonei.com/stat-detail" target="_blank">\u8be6\u7ec6\u4fe1\u606f</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="http://ad43.xce.d.xiaonei.com:9527/wt/feedstat/viewstat.php" target="_self" style="z-index:1000;">\u9009\u62e9\u5e73\u53f0\u67e5\u770b</a></li>\n      <li><a href="http://ad43.xce.d.xiaonei.com:9527/wt/feedstat/stypestat.php" target="_self" style="z-index:1000;">\u9009\u62e9\u7c7b\u578b\u67e5\u770b</a></li>\n    </ul>\n  </li>\n  <li><a href="http://feed.d.xiaonei.com/quota" target="_blank">\u914d\u989d\u7cfb\u7edf</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="#" target="_self" style="z-index:1000;">\u67e5\u770b</a></li>\n    </ul>\n  </li>\n</ul>\n</div>\n\n\n<body>\n<div> <!-- style="position:absolute;left:50%;margin-left:-600px;width:1200px;" -->\n<div>\n  <table id="option" width="1200" border="1" class="t1">\n    <tr>\n      <th align="left">\n        stype:&nbsp;<select name="stype"></select>&nbsp;&nbsp;\n        <!-- origin_url:&nbsp;<select name="origin_url"></select>&nbsp;&nbsp; -->\n      </th>\n    </tr>\n  </table>\n</div>\n<div> <!-- style="position:absolute;left:50%;margin-left:-600px;width:1200px;" -->\n\n\n<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>\n<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>\n<div id="container_father" style="background-color:silver; margin: 0px 15px 0px 15px">\n\t<div id="container_stype" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px"></div>\n</div>\n<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>\n\n<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="97%" color=#987cb9 SIZE=1>\n</body>\n\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


