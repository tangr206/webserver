# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1348826109.500365
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/stat-ABDebug.mako'
_template_uri='/stat-ABDebug.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<link rel="shortcut icon" href="favicon-rr.ico" type="image/x-icon"> \n\n<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />\n<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>\n<title>content</title>\n<script type="text/javascript" src="/jquery.js"></script>\n<script type="text/javascript" src="/AB-debug.js"></script>\n<script src="/Highcharts-2.2.5/js/highcharts.js"></script>\n\n<script src="/Highstock-1.2.2/js/highstock.js"></script>\n<script src="/Highstock-1.2.2/js/modules/exporting.js"></script>\n<script src="/Highstock-1.2.2/js/themes/gray.js"></script>\n\n\n<script type=text/javascript>\n$(function(){\n\t$(\'#mobanwang_com li\').hover(function(){\n\t\t$(this).children(\'ul\').stop(true,true).show(\'slow\');\n\t},function(){\n\t\t$(this).children(\'ul\').stop(true,true).hide(\'slow\');\n\t});\n\n});\n\n</script>\n\n<div id="wrapper" style=" z-index:1000;">\n<ul id="mobanwang_com" class="first-menu">\n  <li><a href="stat" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>\n\n  <li><a href="#" >\u5b9e\u9a8c\u5e73\u53f0</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="experi-select" target="_self" style="z-index:1000;">\u5b9e\u9a8c\u767b\u8bb0\u67e5\u770b</a></li>\n      <li><a href="stat-ABDebug" target="_self" style="z-index:1000;">\u9009\u62e9\u5c3e\u53f7\u67e5\u770b</a></li>\n    </ul>\n  </li>\n  <li><a href="http://feed.d.xiaonei.com/stat-detail" target="_blank">\u8be6\u7ec6\u4fe1\u606f</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="check-plat" target="_self" style="z-index:1000;">\u9009\u62e9\u5e73\u53f0\u67e5\u770b</a></li>\n      <li><a href="check-stype" target="_self" style="z-index:1000;">\u9009\u62e9\u7c7b\u578b\u67e5\u770b</a></li>\n    </ul>\n  </li>\n</ul>\n</div>\n\n\n</head>\n\n<body>\n<br>\n<br>\n<div id="content" >\n\t<div id="right">\n\t\t<fieldset>\n\t\t<legend>CONDITION</legend>\n\n\n<form method="get" name="show_checkbox" style="margin: 10px 10px 10px 10px">\n <div class="t1" style="color:#ff0;  font-size:20px">\u67e5\u770b\u9879</div>\n  <input value="1" name="pv" id="feed_sum" type="checkbox">  \t\t\t<label for="pv">\u66dd\u5149\u91cf</label>\n  <input value="1" name="dispatch" id="dispatch_cnt" type="checkbox">  \t\t<label for="dispatch">\u5206\u53d1\u91cf</label>\n  <br>\n  <input value="1" name="reply" id="reply_sum" checked="checked" type="checkbox">  <label for="reply">\u56de\u590d\u91cf</label>\n  <input value="1" name="reply" id="reply_rate" type="checkbox">  \t<label for="rr">\u56de\u590d\u7387(\u56de\u590d\u91cf/\u66dd\u5149\u91cf)</label>\n  <br>\n  <input value="1" name="click" id="click_sum" checked="checked" type="checkbox">  <label for="click">\u70b9\u51fb\u91cf</label>\n  <input value="1" name="click" id="click_rate" type="checkbox">  \t<label for="ctr">\u70b9\u51fb\u7387(\u70b9\u51fb\u91cf/\u66dd\u5149\u91cf)</label>\n  <br>\n  <input value="1" name="index" id="position_show"  type="checkbox">  \t<label for="index">\u5c55\u793a\u4f4d\u7f6e</label>\n  <input value="1" name="fin" id="position_clk"  type="checkbox">  \t<label for="fin">\u70b9\u51fb\u4f4d\u7f6e</label>\n  <br>\n ================== \n <br>\n <br>\n<div class="t1" style="color:#ff0;  font-size:20px">\u67e5\u770b\u65b9\u5f0f</div>\n<input id="hour" type="radio" value="0" name="day"> \t<label for="hour">\u6309\u5c0f\u65f6</label>\n<input id="day" type="radio" checked="" value="1" name="day"> \t\t<label for="day">\u6309\u5929</label>\n  <br>\n---------------------\n  <br>\n<div class="t1" style="color:#ff0; font-size:20px">\u7c7b\u578b</div>(eg\uff1aall \u6216\u8005 502)\n  <input id="stype" value="all" type="text" style="width:100px;">\n  <br>\n---------------------\n  <br>\n<div class="t1" style="color:#ff0;  font-size:20px">\u76ee\u6807\u5c3e\u53f7</div>(\u7a7a\u683c\u9694\u5f00 eg\uff1a04 50)\n  <input id="include_uid" value="10 30" type="text" style="width:100px;">\n<div class="t1" style="color:#ff0;  font-size:20px">\u8fc7\u6ee4\u5c3e\u53f7</div>\n  <input id="exclude_uid" value="none" type="text" style="width:100px;">\n  <br>\n---------------------\n  <br>\n<div class="t1" style="color:#ff0;  font-size:20px">\u5c55\u793a\u5f62\u5f0f</div>\n  <input value="1" name="line" id="line" checked="checked" type="checkbox">  \t<label id="line">\u53d8\u5316\u8d8b\u52bf</label>\n  <input value="1" name="column" id="column" type="checkbox">  \t\t\t<label for="column">\u5dee\u5f02\u7387</label>\n <br>\n---------------------\n <br>\n  <input value="GO" style="float:right" type="button" onclick="go_fun()"></div>\n </form>\n\n\t\t</fieldset>\n\t</div>\n\n\t<div id="left">\n\t\t<div>\n\t\t\t<fieldset>\n\t<div id="loading"  style="width:100px; height:100px;background:url(/loading/loading45.gif) no-repeat; margin: 100px 10px 10px 500px ; " > </div>\n\t\t\t<legend id="cc">result</legend>\n\t<div id="container1" style="min-width: 1000px; height: 500px; background-color:cliver ; margin: 10px 5px 10px 10px ; "></div>\n\t\t\t</fieldset>\n\t\t</div>\n\t</div>\n</div>\n</body>\n\n\n\n\n<script type="text/javascript">\n\t\tvar chart_all1 = {\n\t\t\tchart : {\n\t\t\t\trenderTo : \'container1\',\n\t\t\t\tzoomType: \'xy\',\n\t\t\t},\n\t\trangeSelector: {\n\t\t     \t   buttons: [{\n\t\t     \t       type: \'day\',\n\t\t     \t       count: 1,\n\t\t     \t       text: \'d\'\n\t\t     \t   }, {\n\t\t     \t       type: \'week\',\n\t\t     \t       count: 1,\n\t\t     \t       text: \'1w\'\n\t\t     \t   }, {\n\t\t     \t       type: \'month\',\n\t\t     \t       count: 1,\n\t\t     \t       text: \'1m\'\n\t\t     \t   },  {\n\t\t     \t       type: \'year\',\n\t\t     \t       count: 1,\n\t\t     \t       text: \'1y\'\n\t\t     \t   }, {\n\t\t     \t       type: \'all\',\n\t\t     \t       text: \'All\'\n\t\t     \t   }],\n\t\t     \t   selected: 1\n\t\t   \t},\n\t               tooltip: {\n            \t\t}, \n\t\t\ttitle : {\n\t\t\t\ttext : \'\u5206\u53d1,\u66dd\u5149/100,\u70b9\u51fb\u91cf,\u56de\u590d\u91cf\'\n\t\t\t},\n\t\t\tseries : []\n\t\t};\n\n\nfunction test(id) {\n\n\n\treturn document.getElementById(id).checked\n}\n\nfunction has(Arr, num ) {\n\tvar deb=arguments[2]==-1?0:1\n\tfor (a in Arr) {\n\t\t//if(deb) alert("has: " + Arr[a] + " : "+ num)\n\t\tif (Arr[a] == num) return true\n\t}\n\treturn false\n}\n\n        //------------------------------------\n        function clone(myObj){\n          if(typeof(myObj) != \'object\') return myObj;\n          if(myObj == null) return myObj;\n          var myNewObj = new Object();\n          for(var i in myObj)\n             myNewObj[i] = clone(myObj[i]);\n          return myNewObj;\n        }       \n\n        var currentData = new Array();\n        var map = new Array();\n        var ABData  = new Array(100);\n        var tmp_date = new Array();\n\n\nfunction get_data(stype) {\n\t//str = "1 45 3645 12341"\n\t//alert(str.split(" ").length)\n\tvar instr = document.getElementById("include_uid").value\n\tvar exstr = document.getElementById("exclude_uid").value\n\tvar inArr = instr.split(" ")\n\tvar exArr = exstr.split(" ")\n\n\tvar day = 0\n\tif (document.getElementById("day").checked)\n\t\tday = 1\n\n\tdocument.getElementById("loading").style.display="block";\n\tdocument.getElementById("container1").innerHTML =  "";\n\n  $.ajax({\n    type: \'POST\',\n    url: \'/stat-ABDebug-data\',\n    //url: \'/web-stype-list\',\n    async: true,\n    data:"stype="+stype+"&day="+day ,\n    success : function(text){\n\n\t      \tif(!text || text.length <= 0) return;\n\t\tcurrentData = eval(\'(\' + text + \')\');\n  \n\t\tvar meta = { name : \'name\', data :{"feed_sum":0, "dispatch_cnt":0, "reply_sum":0, "click_sum":0, "position_show":0, "position_clk":0} } \n        \n                for(var i=0; i<100; ++i) ABData[i] = [];\n                        \n                for(var i = 0; i < currentData.length-1;  ++i) {\n\n                        now = currentData[i]\n                        if (has(tmp_date, now["date"] , -1) == false)  tmp_date.push(now["date"])\n\n                        meta.name = now["date"]\n                        meta.data = []\n                        meta.data["feed_sum"] = (now["feed_sum"])\n                        meta.data["dispatch_cnt"] = (now["dispatch_cnt"])\n                        meta.data["reply_sum"] = (now["reply_sum"])\n                        meta.data["click_sum"] = (now["click_sum"])\n                        meta.data["position_show"] = (now["position_show"])\n                        meta.data["position_clk"] = (now["position_clk"])\n                        uid = now["uid"]\n                        ABData[uid][ now["date"] ] = clone(meta)\n                }\n\t\t//alert(tmp_date)\n\t\tvar meta_z = {time:0, data:{"feed_sum":0, "dispatch_cnt":0, "reply_sum":0, "click_sum":0, "reply_ave":0, "click_ave":0, "position_show":0, "position_clk":0}}\n\t\tvar mmeta = clone(meta_z), mmeta_ex=clone(meta_z)\n\t\tvar inData=new Array(), exData=new Array()\n\t\tindex = 0\n\t\taveindex = 0\n\t\t//alert(inArr)\n\t\t//alert(exArr)\n\t\tfor (i in tmp_date) {\n\t\t\tmmeta = clone(meta_z), mmeta_ex=clone(meta_z)\n\t\t\tfor(var j = 0; j < 100 ;  ++j) {\n\t\t\t\tvar mtime = tmp_date[i]\n\t\t\t\tvar userid = j\n\n\t\t\t\tif (has(inArr, userid)) {\t\n\t\t\t\t\t//alert("1"+userid)\n\t\t\t\t\tif (!ABData[userid][mtime]) { alert("wrong!!" + mtime + " uid:"+userid); continue}\n\t\t\t\t\tvar mdata = ABData[userid][mtime].data\n\n\t\t\t\t\tmmeta.time = mtime\n\t\t\t\t\tmmeta.data["feed_sum"] += mdata["feed_sum"]\n\t\t\t\t\tmmeta.data["dispatch_cnt"] += mdata["dispatch_cnt"]\n\t\t\t\t\tmmeta.data["reply_sum"] += mdata["reply_sum"]\n\t\t\t\t\tmmeta.data["click_sum"] += mdata["click_sum"]\n\t\t\t\t\tmmeta.data["reply_ave"] += mdata["reply_sum"]/ mdata["feed_sum"]\n\t\t\t\t\tmmeta.data["click_ave"] += mdata["click_sum"]/ mdata["feed_sum"]\n\t\t\t\t\tmmeta.data["position_show"] += mdata["position_show"]\n\t\t\t\t\tmmeta.data["position_clk"] += mdata["position_clk"]\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\t\n\t\t\t\tif (has(exArr, userid)) {\n\t\t\t\t\t//alert("2"+ userid)\n\t\t\t\t\tcontinue\n\t\t\t\t}\n\n\t\t\t\t\t//alert("3"+ userid)\n\t\t\t\tif (!ABData[userid][mtime]) { alert("wrong2!!" + mtime + " uid:"+userid); continue}\n\n\t\t\t\t\tvar mdata = ABData[userid][mtime].data\n\t\t\t\t\tmmeta_ex.time = mtime\n\t\t\t\t\tmmeta_ex.data["feed_sum"] += mdata["feed_sum"]\n\t\t\t\t\tmmeta_ex.data["dispatch_cnt"] += mdata["dispatch_cnt"]\n\t\t\t\t\tmmeta_ex.data["reply_sum"] += mdata["reply_sum"]\n\t\t\t\t\tmmeta_ex.data["click_sum"] += mdata["click_sum"]\n\t\t\t\t\tmmeta_ex.data["reply_ave"] += mdata["reply_sum"]/ mdata["feed_sum"]\n\t\t\t\t\tmmeta_ex.data["click_ave"] += mdata["click_sum"]/ mdata["feed_sum"]\n\t\t\t\t\tmmeta_ex.data["position_show"] += mdata["position_show"]\n\t\t\t\t\tmmeta_ex.data["position_clk"] += mdata["position_clk"]\n\t\n\t\t\t}\t\t\n\t\t\tinData.push(clone(mmeta))\n\t\t\texData.push(clone(mmeta_ex))\n\t\t\t//alert(mtime+" in:"+ inData[inData.length-1].data["reply_sum"] + "  ex:"+ exData[exData.length-1].data["reply_sum"]   )\n\t\t}\n\n\n\n\t\t//===========================================================================\n\t\t      var series = [\n\t\t\t\t{yAxis: 1, name : instr+ \'\u66dd\u5149\u91cf\', data : [], type: \'spline\'}, \n\t\t\t\t{name : instr+ \'\u5206\u53d1\u91cf\', data : [], type: \'spline\'}, \n\t\t\t\t{name : instr+ \'\u56de\u590d\u91cf\', data : [], type: \'spline\'}, \n\t\t\t\t{name : instr+ \'\u70b9\u51fb\u91cf\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 2, name : instr+ \'\u56de\u590d\u7387\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 2,name : instr+ \'\u70b9\u51fb\u7387\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 3,name : instr+ \'\u5c55\u793a\u4f4d\u7f6e\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 3,name : instr+ \'\u70b9\u51fb\u4f4d\u7f6e\', data : [], type: \'spline\'}, \n\t\t\t\t{name : \'\u53ef\u70b9\u51fb\u5404\u9879 \u786e\u5b9a\u662f\u5426\u663e\u793a\', data : [], type: \'spline\'}, \n\t\t      ]\t\n\t\t\tfor( i in  inData) {\n\t\t\t\tvar mtime = inData[i].time + 8*1000*60*60 \n\t\t\t\tvar mdata = inData[i].data\n\t\t\t\tseries[0].data[i] = [mtime, mdata["feed_sum"]/inArr.length ]\n\t\t\t\tseries[1].data[i] = [mtime, mdata["dispatch_cnt"]/inArr.length ]\n\t\t\t\tseries[2].data[i] = [mtime, mdata["reply_sum"]/inArr.length ]\n\t\t\t\tseries[3].data[i] = [mtime, mdata["click_sum"]/inArr.length ]\n\t\t\t\tseries[4].data[i] = [mtime, mdata["reply_ave"]/inArr.length ]\n\t\t\t\tseries[5].data[i] = [mtime, mdata["click_ave"]/inArr.length ]\n\t\t\t\tseries[6].data[i] = [mtime, mdata["position_show"]/inArr.length ]\n\t\t\t\tseries[7].data[i] = [mtime, mdata["position_clk"]/inArr.length ]\n\t\t\t}  \n\n\n\t\t      var seriesAVE = [\n\t\t\t\t{yAxis: 1, name : \'others\u66dd\u5149\u91cf\', data : [], type: \'spline\'}, \n\t\t\t\t{name : \'others\u5206\u53d1\u91cf\', data : [], type: \'spline\'}, \n\t\t\t\t{name : \'others\u56de\u590d\u91cf\', data : [], type: \'spline\'}, \n\t\t\t\t{name : \'others\u70b9\u51fb\u91cf\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 2, name : \'others\u56de\u590d\u7387\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 2,name : \'others\u70b9\u51fb\u7387\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 3,name : \'others\u5c55\u793a\u4f4d\u7f6e\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 3,name : \'others\u70b9\u51fb\u4f4d\u7f6e\', data : [], type: \'spline\'}, \n\t\t\t\t{name : \'\u53ef\u70b9\u51fb\u5404\u9879 \u786e\u5b9a\u662f\u5426\u663e\u793a\', data : [], type: \'spline\'}, \n\t\t      ]\t\n\t\t\tvar len = 0\n\t\t\tif(exArr[0] == "none") len = 0\n\t\t\telse len = exArr.length\n\t\t\tfor( i in  exData) {\n\t\t\t\tvar mtime = exData[i].time + 8*1000*60*60\n\t\t\t\tvar mdata = exData[i].data\n\t\t\t\tseriesAVE[0].data[i] = [mtime, mdata["feed_sum"]/(100-inArr.length-len) ]\n\t\t\t\tseriesAVE[1].data[i] = [mtime, mdata["dispatch_cnt"]/(100-inArr.length-len) ]\n\t\t\t\tseriesAVE[2].data[i] = [mtime, mdata["reply_sum"]/(100-inArr.length-len) ]\n\t\t\t\tseriesAVE[3].data[i] = [mtime, mdata["click_sum"]/(100-inArr.length-len) ]\n\t\t\t\t//alert(mdata["reply_ave"]+"  "+ (100-inArr.length-len))\n\t\t\t\tseriesAVE[4].data[i] = [mtime, mdata["reply_ave"]/(100-inArr.length-len) ]\n\t\t\t\t//alert(seriesAVE[4].data[i][1])\n\t\t\t\tseriesAVE[5].data[i] = [mtime, mdata["click_ave"]/(100-inArr.length-len) ]\n\t\t\t\tseriesAVE[6].data[i] = [mtime, mdata["position_show"]/(100-inArr.length-len) ]\n\t\t\t\tseriesAVE[7].data[i] = [mtime, mdata["position_clk"]/(100-inArr.length-len) ]\n\t\t\t}  \n\n\n\n\t\t\t//alert(series[0].data)\n\t\t\tchart_all1.title.text = stype+\'\u7c7b\u578b\u7684\u5404\u9879\u4fe1\u606f\'\n\t\t\t//chart_all2.title.text = stype+\'\u7c7b\u578b\u7684 \u70b9\u51fb\u7387,\u56de\u590d\u7387\'\n\t\t\tchart_all1.series = [{\n\t\t\t\ttype : \'flags\',\n\t\t\t\tdata : [{\n\t\t\t\t\tx : Date.UTC(2012, 8, 14),\n\t\t\t\t\ttitle : \'A\',\n\t\t\t\t\ttext : \'Shape: "squarepin"\'\n\t\t\t\t}, {\n\t\t\t\t\tx : Date.UTC(2012, 8, 18),\n\t\t\t\t\ttitle : \'A\',\n\t\t\t\t\ttext : \'Shape: "squarepin"\'\n\t\t\t\t}],\n\t\t\t\tonSeries : \'dataseries\',\n\t\t\t\tshape : \'squarepin\',\n\t\t\t\twidth : 16\n\t\t\t}, {\n\t\t\t\ttype : \'flags\',\n\t\t\t\tdata : [{\n\t\t\t\t\tx : Date.UTC(2012, 8, 1),\n\t\t\t\t\ttitle : \'B\',\n\t\t\t\t\ttext : \'Shape: "circlepin"\'\n\t\t\t\t}, {\n\t\t\t\t\tx : Date.UTC(2012, 8, 2),\n\t\t\t\t\ttitle : \'B\',\n\t\t\t\t\ttext : \'Shape: "circlepin"\'\n\t\t\t\t}],\n\t\t\t\tshape : \'circlepin\',\n\t\t\t\twidth : 16\n\t\t\t}, {\n\t\t\t\ttype : \'flags\',\n\t\t\t\tdata : [{\n\t\t\t\t\tx : Date.UTC(2012, 8, 10),\n\t\t\t\t\ttitle : \'C\',\n\t\t\t\t\ttext : \'Shape: "flag"\'\n\t\t\t\t}, {\n\t\t\t\t\tx : Date.UTC(2012, 8, 11),\n\t\t\t\t\ttitle : \'C\',\n\t\t\t\t\ttext : \'Shape: "flag"\'\n\t\t\t\t}],\n\t\t\t\tcolor : \'#5F86B3\',\n\t\t\t\tfillColor : \'#5F86B3\',\n\t\t\t\tonSeries : \'dataseries\',\n\t\t\t\twidth : 16,\n\t\t\t\tstyle : {// text style\n\t\t\t\t\tcolor : \'white\'\n\t\t\t\t},\n\t\t\t\tstates : {\n\t\t\t\t\thover : {\n\t\t\t\t\t\tfillColor : \'#395C84\' // darker\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}]\n\t\t\tchart_all1.yAxis = YA \n\t\t\t//chart_all2.series = []\n\t\t\tif (test("feed_sum")) { \n\t\t\t\tchart_all1.series.push(series[0])\n\t\t\t\tchart_all1.series.push(seriesAVE[0])\n\t\t\t}\n\t\t\telse chart_all1.yAxis[1].title.text = ""\n\n\t\t\tvar tt = 0\n\t\t\tif (test("dispatch_cnt")) {\n\t\t\t\tchart_all1.series.push(series[1])\n\t\t\t\tchart_all1.series.push(seriesAVE[1])\n\t\t\t}\n\t\t\telse tt = tt+1\n\t\t\tif (test("reply_sum")) { \n\t\t\t\tchart_all1.series.push(series[2])\n\t\t\t\tchart_all1.series.push(seriesAVE[2])\n\t\t\t}\n\t\t\telse tt = tt+1\n\t\t\tif (test("click_sum")) {\n\t\t\t\tchart_all1.series.push(series[3])\n\t\t\t\tchart_all1.series.push(seriesAVE[3])\n\t\t\t}\n\t\t\telse tt = tt+1\n\t\t\tif (tt == 3) chart_all1.yAxis[0].title.text = ""\n\n\t\t\tvar tt = 0\n\t\t\tif (test("reply_rate")) {\n\t\t\t\tchart_all1.series.push(series[4])\n\t\t\t\tchart_all1.series.push(seriesAVE[4])\n\t\t\t}\n\t\t\telse tt = tt+1\n\t\t\tif (test("click_rate")) {\n\t\t\t\tchart_all1.series.push(series[5])\n\t\t\t\tchart_all1.series.push(seriesAVE[5])\n\t\t\t}\n\t\t\telse tt = tt+1\n\t\t\tif (tt == 2) chart_all1.yAxis[2].title.text = ""\n\n\t\t\ttt = 0\n\t\t\tif (test("position_show")) {\n\t\t\t\tchart_all1.series.push(series[6])\n\t\t\t\tchart_all1.series.push(seriesAVE[6])\n\t\t\t}\n\t\t\telse tt = tt + 1\n\t\t\tif (test("position_clk")) {\n\t\t\t\tchart_all1.series.push(series[7])\n\t\t\t\tchart_all1.series.push(seriesAVE[7])\n\t\t\t}\n\t\t\telse tt = tt + 1\n\t\t\tif (tt == 2) chart_all1.yAxis[3].title.text = ""\n\t\t\t\n\t\t\t//alert(chart_all1.series[0].data[1])\n\t\t      var chart1 = new Highcharts.StockChart(chart_all1)\n\t\t      //var chart2 = new Highcharts.StockChart(chart_all2)\n\n\t\t\tdocument.getElementById("loading").style.display="none";\n\t\t\tdocument.getElementById("cc").style.display="block";\n\n      //$("#data").append(html);\n    },\n    error : function(){\n      alert(\'ready \u52a0\u8f7d\u51fa\u9519\');\n    }\n  });\n\n}\n\n\nfunction go_fun() {\n\tvar stype = document.getElementById("stype").value\n\tget_data(stype)\n\n}\n\n$(document).ready(get_data("all"));\n\n\n\n\n</script>\n\n\n\n\n</html>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()

