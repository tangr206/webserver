# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1348890292.1032529
_template_filename='/data/xce/pylons-dev/feedadmin-test/feedadmin/templates/stat.mako'
_template_uri='/stat.mako'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<link rel="shortcut icon" href="favicon-rr.ico" type="image/x-icon"> \n\n<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />\n<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>\n<title>FD</title>\n<!--script type="text/javascript" src="/stat.mako.js"></script-->\n<script type="text/javascript" src="/stat.mako.js"></script>\n<script type="text/javascript" src="/jquery.js"></script>\n<script src="/Highcharts-2.2.5/js/highcharts.js"></script>\n<!-- Additional files for the Highslide popup effect -->\n<script type="text/javascript" src="/gray.js"></script>\n<script type="text/javascript" src="/highslide-full.min.js"></script>\n<script type="text/javascript" src="/highslide.config.js" charset="utf-8"></script>\n<script type="text/javascript" src="sliding_effect.js"></script>\n\n<script src="/Highstock-1.2.2/js/highstock.js"></script>\n<script src="/Highstock-1.2.2/js/modules/exporting.js"></script>\n<script src="/Highstock-1.2.2/js/themes/gray.js"></script>\n\n\n<link rel="stylesheet" type="text/css" href="/highslide.css"/> \n\n<script type=text/javascript>\n$(function(){\n\t$(\'#mobanwang_com li\').hover(function(){\n\t\t$(this).children(\'ul\').stop(true,true).show(\'slow\');\n\t},function(){\n\t\t$(this).children(\'ul\').stop(true,true).hide(\'slow\');\n\t});\n\n\t$(\'#big_map\').hover(function(){\n\t\t$(\'#map\').stop(true,true).show(\'slow\');\n\t},function(){\n\t\t$(\'#map\').stop(true,true).hide(\'slow\');\n\t});\n\n});\n</script>\n\n<div id="wrapper" style=" z-index:1000;">\n<!--ul id="mobanwang_com" class="first-menu">\n  <li><a href="stat" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>\n\n  <li><a href="#" >\u5b9e\u9a8c\u5e73\u53f0</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="experi-select" target="_self" style="z-index:1000;">\u5b9e\u9a8c\u767b\u8bb0\u67e5\u770b</a></li>\n      <li><a href="stat-ABDebug" target="_self" style="z-index:1000;">\u9009\u62e9\u5c3e\u53f7\u67e5\u770b</a></li>\n    </ul>\n  </li>\n  <li><a href="http://feed.d.xiaonei.com/stat-detail" target="_blank">\u8be6\u7ec6\u4fe1\u606f</a>\n    <ul id="subNews" class="second-menu">\n      <li><a href="check-plat" target="_self" style="z-index:1000;">\u9009\u62e9\u5e73\u53f0\u67e5\u770b</a></li>\n      <li><a href="check-stype" target="_self" style="z-index:1000;">\u9009\u62e9\u7c7b\u578b\u67e5\u770b</a></li>\n    </ul>\n  </li>\n</ul-->\n</div>\n<center><h1>FEED DATA-PLATFORM</h1></center>\n\n</head>\n\n<body>\n\n<div id="content" >\n\t<div id="right">\n\t\t<fieldset>\n\t\t<legend>INSTRUCTION</legend>\n<div id="navigation-block"> <!--img src="background.jpg" id="hide" /-->\n  <ul id="sliding-navigation">\n    <li class="sliding-element"><a href="/experi-select">\u5b9e\u9a8c\u767b\u8bb0\u67e5\u770b</a></li>\n    <li class="sliding-element"><a href="/stat-ABDebug" >\u6307\u5b9a\u5c3e\u53f7\u67e5\u770b</a></li>\n    <li class="sliding-element"><a href="/check-plat" >\u9009\u62e9\u5e73\u53f0\u67e5\u770b</a></li>\n    <li class="sliding-element"><a  href="/check-stype">\u9009\u62e9\u7c7b\u578b\u67e5\u770b</a></li>\n\n  </ul>\n\n</div>\n\n\t\t</fieldset>\n\n\t\t<fieldset id="big_map" style="margin:50px 0px 0px 0px">\n\t\t<legend>VisitMap</legend>\n\t\t\t<div id="map" style="display:none">\n<script type="text/javascript" src="http://jk.revolvermaps.com/r.js"></script><script type="text/javascript">rm_f1st(\'5\',\'220\',\'true\',\'false\',\'000000\',\'ak4h44d83r7\',\'true\',\'ff0000\');</script><noscript><applet codebase="http://rk.revolvermaps.com/j" code="core.RE" width="210" height="210" archive="g.jar"><param name="cabbase" value="g.cab" /><param name="r" value="true" /><param name="n" value="false" /><param name="i" value="ak4h44d83r7" /><param name="m" value="5" /><param name="s" value="220" /><param name="c" value="ff0000" /><param name="v" value="true" /><param name="b" value="000000" /><param name="rfc" value="true" /></applet></noscript>\n\t\t\t</div>\n\t\t</fieldset>\n\n\t</div>\n\n\t<div id="left">\n\t\t<div>\n\t\t\t<fieldset>\n\t<div id="loading"  style="width:100px; height:100px;background:url(/loading/loading45.gif) no-repeat; margin: 100px 10px 10px 500px ; " > </div>\n\t\t\t<legend>WEB</legend>\n\t\t\t\t<div id="container_web" style="min-width: 400px; height: 500px; margin: 10px 5px 10px 10px ; "></div>\n\t\t\t</fieldset>\n\t\t</div>\n\t\t<!--div>\n\t\t\t<fieldset>\n\t\t\t<legend>ALL</legend>\n\t\t\t\t<div id="container_all" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px"></div>\n\t\t\t</fieldset>\n\t\t</div-->\n\t</div>\n</div>\n\n</body>\n\n\n\n\n\n<script type="text/javascript">\n\n\tvar chart_web = {\n\t\t\tchart : {\n\t\t\t\trenderTo : \'container_web\',\n\t\t\t\tzoomType: \'xy\',\n\t\t\t},\n\t\t\ttitle : {\n\t\t\t\ttext: "WEB\u7aef \u70b9\u51fb,\u66dd\u5149,\u8bbf\u95ee\u4eba\u6570"\n\t\t\t},\n\t\t\trangeSelector: {\n\t\t\t\tinputEnabled: false,\n\t\t     \t   buttons: [{\n\t\t     \t       type: \'day\',\n\t\t     \t       count: 1,\n\t\t     \t       text: \'d\'\n\t\t     \t   }, {\n\t\t     \t       type: \'week\',\n\t\t     \t       count: 1,\n\t\t     \t       text: \'1w\'\n\t\t     \t   }, {\n\t\t     \t       type: \'month\',\n\t\t     \t       count: 1,\n\t\t     \t       text: \'1m\'\n\t\t     \t   }, {\n\t\t     \t       type: \'all\',\n\t\t     \t       text: \'All\'\n\t\t     \t   }],\n\t\t     \t   selected: 1\n\t\t   \t},\n\t\t\tseries : []\n\t\t};\n\n\nfunction get_data() {\n\tdocument.getElementById("loading").style.display="block";\n\tdocument.getElementById("container_web").innerHTML =  "";\n\n\n\t$.ajax({\n\t    type: \'POST\',\n\t    url: \'/get-statwebdata\',\n\t    async: false,\n\t    success : function(text){\n\t\t      if(!text || text.length <= 0) return;\n\t\t      currentData = eval(\'(\' + text + \')\');\n\t\t      var series = [\n\t\t\t\t{ name : \'name\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 1,name : \'name\', data : [], type: \'spline\'}, \n\t\t\t\t{yAxis: 2,name : \'name\', data : [], type: \'spline\'}, \n\t\t      ]\t\n\t\t      series[0].name = "\u8bbf\u95ee\u4eba\u6570" \n\t\t      series[1].name = "\u66dd\u5149\u91cf"\n\t\t      series[2].name = "\u70b9\u51fb\u91cf" \n\t\t\t\n\t\t      var date = new Array(currentData.length);\n\t\t\tvar j=0;\n\t\t      for(var i = 0; i < currentData.length - 1;  ++i, ++j) {\n\t\t\t  var mtime = currentData[i]["date"] + 8*1000*60*60\n         \t\t  series[0].data[j] = [mtime, currentData[i]["uv"] ]\n         \t\t  series[1].data[j] = [mtime, currentData[i]["feed_sum"] ]\n         \t\t  series[2].data[j] = [mtime, currentData[i]["click_sum"] ]\n         \t\t  //series[3].data[j] = currentData[i]["reply_sum"]\n\n\t\t      }\n\t\t//alert(series[0].data)\t\n\t\t      chart_web.yAxis = YA \n\t\t      chart_web.series.push(series[0]);\n\t\t      chart_web.series.push(series[1]);\n\t\t      chart_web.series.push(series[2]);\n\t\t\t//alert(chart_web)\n      \t\t      var chart1 = new Highcharts.StockChart(chart_web);\n\t\tdocument.getElementById("loading").style.display="none";\n\t    },// sucess\n\t    error : function(){\n\t      alert(\'chart_web \u52a0\u8f7d\u51fa\u9519, \u8bf7\u91cd\u65b0\u5237\u65b0\u9875\u9762\');\n\t    }\n\n\t  });//ajax\n    }\n\n\n\n\n\n    $(document).ready(get_data() );//ready\n\n</script>\n\n\n \n\n\n\n\n\n\n\n\n\n\n\n\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()

