# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1347364587.853653
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/plat-all.mako'
_template_uri='/plat-all.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />\n<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>\n<title>content</title>\n<script type="text/javascript" src="/jquery.js"></script>\n<script src="/Highcharts-2.2.5/js/highcharts.js"></script>\n<!-- Additional files for the Highslide popup effect -->\n<script type="text/javascript" src="/highslide-full.min.js"></script>\n<script type="text/javascript" src="/highslide.config.js" charset="utf-8"></script>\n<link rel="stylesheet" type="text/css" href="/highslide.css"/> \n\n\n<script type=text/javascript>\n$(function(){\n\t$(\'#mobanwang_com li\').hover(function(){\n\t\t$(this).children(\'ul\').stop(true,true).show(\'slow\');\n\t},function(){\n\t\t$(this).children(\'ul\').stop(true,true).hide(\'slow\');\n\t});\n\n});\n\n</script>\n\n<div id="wrapper" style=" z-index:1000;">\n<ul id="mobanwang_com" class="first-menu">\n  <li><a href="#" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>\n\n  <li><a href="stat" target="_blank">\u5b9e\u9a8c\u5e73\u53f0</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="experi-signin" target="_self" style="z-index:1000;">\u5b9e\u9a8c\u767b\u8bb0</a></li>\n      <li><a href="experi-select" target="_self" style="z-index:1000;">\u9009\u62e9\u5b9e\u9a8c\u67e5\u770b</a></li>\n      <li><a href="http://feed.d.xiaonei.com/stat-ABDebug" target="_self" style="z-index:1000;">\u9009\u62e9\u5c3e\u53f7\u67e5\u770b</a></li>\n    </ul>\n  </li>\n  <li><a href="http://feed.d.xiaonei.com/stat-detail" target="_blank">\u8be6\u7ec6\u4fe1\u606f</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="check-plat" target="_self" style="z-index:1000;">\u9009\u62e9\u5e73\u53f0\u67e5\u770b</a></li>\n      <li><a href="check-stype" target="_self" style="z-index:1000;">\u9009\u62e9\u7c7b\u578b\u67e5\u770b</a></li>\n    </ul>\n  </li>\n  <li><a href="http://feed.d.xiaonei.com/quota" target="_blank">\u914d\u989d\u7cfb\u7edf</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="#" target="_self" style="z-index:1000;">\u67e5\u770b</a></li>\n    </ul>\n  </li>\n</ul>\n</div>\n\n<!--div id="wrapper">\n    <ul id="nav">\n        <li><a href="experiment-rout">\u5b9e\u9a8c\u5e73\u53f0</a></li>\n        <li><a href="detail-rout">\u8be6\u7ec6\u4fe1\u606f</a></li>\n        <li><a href="www.feed.d.xiaonei.com">feed</a></li>\n        <li><a href="http://feed.d.xiaonei.com/stat-ABDebug">AB</a></li>\n    </ul>\n</div-->\n\n\n<h1> <a href="check-plat" target="_self" >\u6309\u5e73\u53f0\u67e5\u770b </a></h1>\n\n</head>\n\n<script type="text/javascript">\n\tvar name\n\tvar chart_all = {\n\n\t    chart: {\n                renderTo: \'container\',\n                type: \'line\',\n\t\tzoomType: \'xy\',\n            },\n            title: {\n                text: name+\'\u5e73\u53f0\u7684\u5404\u9879\u6307\u6807\',\n                x: -20 //center\n            },\n            subtitle: {\n                text: \'Source: WorldClimate.com\',\n                x: -20\n            },\n            xAxis: {\n            },\n            yAxis: {\n                title: {\n                    text: \'\u6570\u91cf\'\n                },\n           },\n            tooltip: {\n\t\tshared: true,\n                crosshairs: true,\n                //formatter: function() {\n                //        return \'<b>\'+ this.series.name +\' \'+\n                 //       this.x +\': \'+ this.y ;\n                //}\n            },\n            legend: {\n            },\n            series: []\n        };\n\n\nfunction div(number1,number2){\n       var num1 = Math.round(number1);\n       var num2 = Math.round(number2);\n       var result = num1/num2;\n       if(result >=0){\n           result = Math.floor(result);\n       }else{\n           result = Math.ceil(result);\n       }\n       return result;\n    }\n\n$(document).ready(function() {\n  $.ajax({\n    type: \'POST\',\n    url: \'/view-day-list\',\n    async: false,\n    data:"view=" + ')
        # SOURCE LINE 121
        __M_writer(escape(c.name))
        __M_writer(u',\n    success : function(text){\n\tname = "HH"\n\tswitch(')
        # SOURCE LINE 124
        __M_writer(escape(c.name))
        __M_writer(u')\n\t   \u3000\u3000{\n\t\u3000\u3000   case -1:\n\t\t name = "ALL"\n\t \u3000\u3000    break\n\t\u3000\u3000   case 0:\n\t\t name = "WEB"\n\t \u3000\u3000    break\n\t\u3000\u3000   case 2:\n\t\t name = "\u624b\u673a"\n\t \u3000\u3000    break\n\t\u3000\u3000   case 3:\n\t\t name = "\u5b9e\u65f6\u5316"\n\t \u3000\u3000    break\n\t\u3000\u3000   case 4:\n\t\t name = "\u5f00\u653e\u5e73\u53f0"\n\t \u3000\u3000    break\n\t\u3000\u3000   case 6:\n\t\t name = "TimeLine"\n\t \u3000\u3000    break\n\t\u3000\u3000   default:\n\t\t name = "NONE"\n\t\u3000\u3000   }\n\t      $("#legendid").html("----->" + name + "<-----");\n\n\n\t      \t\tif(!text || text.length <= 0) return;\n\t\t      \tcurrentData = eval(\'(\' + text + \')\');\n\n\t      var html = \'<option value="\' + 0 + \'">\' + \'\u9009\u62e9\u65e5\u671f</option>\';\n\t      var set = {}\n\t      for(var i = currentData.length-2; i >=0 ; --i) {\n\t\tdd = currentData[i]["date"]\n\t\tif ( !set[dd] ) {\n\t        \thtml += \'<option value="\' + currentData[i]["date"].toString() + \'">\' + currentData[i]["date"].toString() + \'</option>\';\n\t\t\tset[dd] = true;\n\t\t}\n\t      }\n\t      $("select[name=st_date]").html(html);\n\t      $("select[name=ed_date]").html(html);\n\n\n//------------------------------------------\n\n\t\t      var series = [\n\t\t\t\t{name : \'\u8bbf\u95ee\u4eba\u6570\', data : []}, \n\t\t\t\t{name : \'\u53d6\u65b0\u9c9c\u4e8b\u64cd\u4f5c\', data : []}, \n\t\t\t\t{name : \'\u66dd\u5149\u91cf\', data : []}, \n\t\t\t\t{name : \'\u6d3b\u8dc3\u6b21\u6570\', data : []}, \n\t\t\t\t{name : \'\u6d3b\u8dc3\u65f6\u957f\', data : []}, \n\t\t\t\t{name : \'\u53ef\u70b9\u51fb\u5404\u9879 \u786e\u5b9a\u662f\u5426\u663e\u793a\', data : []}, \n\t\t      ]\t\n/*\nmysql> select date, sum(uv) , sum(rv), sum(session_cnt), sum(session_sum), sum(feed_sum) from view_day_stat2 group by date;\n+----------+----------+-----------+------------------+------------------+---------------+\n| date     | sum(uv)  | sum(rv)   | sum(session_cnt) | sum(session_sum) | sum(feed_sum) |\n+----------+----------+-----------+------------------+------------------+---------------+\n| 20120830 | 16361264 | 203752577 |         72039390 |       7440978761 |    3871198126 | \n| 20120831 | 16243919 | 200855746 |         70687944 |       7370880721 |    3835647670 | \n+----------+----------+-----------+------------------+------------------+---------------+\ni\n[{"date":20120830, "uv":16361264, "rv":203752577, "feed_sum":3871198126, "secnt":72039390, "sesum":7440978761},{"date":20120831, "uv":16243919, "rv":200855746, "feed_sum":3835647670, "secnt":70687944, "sesum":7370880721},{}]*/\n\t\tvar date = new Array(currentData.length);\n\t\tfor(var i = 0, j = 0; i < currentData.length -1 && i<30 ;  ++i) {\n\t\t\t//index = div(i, 5)\n\t\t\tindex = i \n\t\t\tdate[index] = currentData[index]["date"]\n\t\t\tseries[0].data[index] = currentData[i]["uv"] \n\t\t\tseries[1].data[index] = currentData[i]["rv"] \n\t\t\tseries[2].data[index] = currentData[i]["feed_sum"] \n\t\t\tseries[3].data[index] = currentData[i]["secnt"] \n\t\t\tseries[4].data[index] = currentData[i]["sesum"] \n\t\t}\n\n                \tchart_all.title.text =  name+\'\u5e73\u53f0\u7684\u5404\u9879\u6307\u6807\',\n\t\t\t\n\t\t      chart_all.series = []\n\t\t      chart_all.series.push(series[0]);\n\t\t      chart_all.series.push(series[1]);\n\t\t      chart_all.series.push(series[2]);\n\t\t      chart_all.series.push(series[3]);\n\t\t      chart_all.series.push(series[4]);\n\t\t      chart_all.series.push(series[5]);\n\t\t      chart_all.xAxis.categories = date;\n\n\t\t      chart1 = new Highcharts.Chart(chart_all)\n\n\n      //$("#data").append(html);\n    },\n    error : function(){\n      alert(\'ready \u52a0\u8f7d\u51fa\u9519\');\n    }\n  });\n});\n</script>\n\n\n\n\n\n<body>\n\n<div id="content" >\n\t<div id="right">\n\t\t<fieldset>\n\t\t<legend> ---&nbspCondition&nbsp--- </legend>\n\n<form method="get" name="show_checkbox"  style="margin: 10px 10px 10px 10px">\n  <div class="t1">\u65f6\u95f4</div>\n  \u8d77\u59cb:\n  <select id="st_date" name="st_date">\n  </select>\n  </br>\n  </br>\n  \u7ec8\u6b62:\n  <select id="ed_date" name="ed_date">\n  </select>\n--------------------------------\n  <br>\n  <!--input name="day" value="0" id="hour" checked="checked" type="radio">\n  <label for="hour">\u6309\u5c0f\u65f6</label>\n  <input name="day" value="1" id="day" type="radio"-->\n  <label for="day">\u6309\u5929\u5c55\u793a<br>(\u70b9\u51fb\u5404\u8282\u70b9\u53ef\u6309\u5c0f\u65f6\u67e5\u770b)</label>\n  \n--------------------------------\n  \n<!--div class="t1">\u67e5\u770b\u9879</div>\n  <input value="1" name="c2" id="uv" type="checkbox" checked="checked">\n  <label for="uv">\u8bbf\u95ee\u4eba\u6570(UV)</label>\n  <br>\n  <input value="1" name="c2" id="rv" type="checkbox">\n  <label for="rv">\u53d6\u65b0\u9c9c\u4e8b\u64cd\u4f5c(RV)</label>\n  <br>\n  <input value="1" name="c2" id="pv" type="checkbox">\n  <label for="pv">\u66dd\u5149\u91cf(PV)</label>\n  <br>\n  <input value="1" name="c2" id="session_cnt" type="checkbox">\n  <label for="session_cnt">\u6d3b\u8dc3\u6b21\u6570</label>\n  <br>\n  <input value="1" name="c2" id="session_sum" type="checkbox">\n  <label for="session_sum">\u6d3b\u8dc3\u65f6\u957f</label>\n  <br-->\n <div class="t1">\u67e5\u770b\u9879</div>\n  <label for="uv">\u8bbf\u95ee\u4eba\u6570(UV)</label>\n  <br>\n  <label for="rv">\u53d6\u65b0\u9c9c\u4e8b\u64cd\u4f5c(RV)</label>\n  <br>\n  <label for="pv">\u66dd\u5149\u91cf(PV)</label>\n  <br>\n  <label for="session_cnt">\u6d3b\u8dc3\u6b21\u6570</label>\n  <br>\n  <label for="session_sum">\u6d3b\u8dc3\u65f6\u957f</label>\n  <br>\n  \n</form>\n\t\t</fieldset>\n\t</div>\n\n<!--- -------------------------------------------- -->\n      <div id="left">\n\t\t<div id="div_viewa">\n\t\t\t<fieldset>\n\t\t\t<legend id="legendid">ALL</legend>\n\t<div id="container" style="min-width: 400px; height: 400px; background-color:white ; margin: 10px 5px 10px 10px ; "></div>\n\t\t\t</fieldset>\n\t\t</div>\n      </div> <!-- left -->\n</div>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


