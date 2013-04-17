<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>
<script type="text/javascript" src="/jquery.min.js"></script>
<script type="text/javascript" src="/old-feed-list.js"></script>
<script type="text/javascript" src="/jquery.date_input.js"></script>
<script type="text/javascript">$($.date_input.initialize);</script>
<link rel="stylesheet" href="/css/date_input.css" type="text/css"></link>
<style type="text/css">
a{ text-decoration:none;}
a:hover{ text-decoration:underline;}
</style>
<title>stat-detail</title>
	<!--header-->
	<div class="headerbox" style="background-color:#28004D">
		<div class="header">
			<h1 class="logobox"><img src="logo.png" alt="人人网数据平台" height="42" width="202"></h1>
			<h2 class="page-title"><a href="/stat-detail" style= " font-family: 'Open Sans',Arial,Helvetica,sans-serif;   color: #FFFFFF;    font-size: 20px;    padding: 5px 10px;    text-shadow: 0 3px 0 #0000FF, 1px 2px 2px #AAAAAA;">  新鲜事数据平台-详细信息</a></h2>
			</div>
		</div>
	</div>
	<!-- end -->
</head>
<body>
<div> <!-- style="position:absolute;left:50%;margin-left:-600px;width:1200px;" -->
<div>
  <table id="option" width="1200" border="1" class="t1">
    <tr>
      <th align="left">
        stype:&nbsp;<select name="stype"></select>&nbsp;&nbsp;
        date:&nbsp;<input type="text" name="date" class="date_input" size="11">&nbsp;&nbsp;
        <!-- origin_url:&nbsp;<select name="origin_url"></select>&nbsp;&nbsp; -->
      </th>
    </tr>
  </table>
</div>
<br/>

<table id="data" width="1400" border="1" class="t1" style="text-align:center;" cellspacing="1%">
  <tr>
    <th><a id="title_stype_home" href="#nogo">类型</a></th>
    <th><a id="title_date_home" href="#nogo" href="#nogo">日期↓</a></th>
    <th><a id="title_dispatch_home" href="#nogo">发送量</a></th>
    <th><a id="title_tosize_home" href="#nogo">分发量</a></th>
    <th><a id="title_dispatch_user_home" href="#nogo">发送用户数</a></th>
    <th><a id="title_view_home" href="#nogo">曝光条次</a></th>
    <th><a id="title_view_pos_home" href="#nogo">平均曝光位置</a></th>
    <th><a id="title_view_user_home" href="#nogo">取新鲜事的用户数</a></th>
    <th><a id="title_viewed_user_home" href="#nogo">被曝光的用户数</a></th>
    <th><a id="title_reply_home" href="#nogo">回复数</a></th>
    <th><a id="title_reply_user_home" href="#nogo">产生回复的用户数</a></th>
    <th><a id="title_click_home" href="#nogo">点击量</a></th>
    <th><a id="title_click_pos_home" href="#nogo">平均点击位置</a></th>
    <th><a id="title_click_user_home" href="#nogo">产生点击的用户数</a></th>
    <th><a id="title_clicked_user_home" href="#nogo">被点击的用户数</a></th>
  </tr>
</table>
</div>
<table id="loading" width="1200" style="display:none;" border="1" class="t1">
  <tr>
    <th style="font-size:110%;font-weight:bold;text-align:left;">数据读取中...</th>
  </tr>
</table>

<div id="toolBackTo" class="back-to" style="display:none;">
<a class="backtotop" onclick="window.scrollTo(0,0);return false;" href="#top">
返回顶部
<img class="back-tip" src="http://a.xnimg.cn/imgpro/button/back-tip.png">
</a>
</div>
<script>
$("#toolBackTo").css("left", (document.body.scrollWidth-70).toString() + "px");
$(window).scroll(function(){
  if(document.documentElement.scrollTop > 30){
    $("#toolBackTo").show();
  }else{
    $("#toolBackTo").hide();
  }
});
</script>
</body>

<script type="text/javascript">
$(function(){
  $("#loading").ajaxSend(function(){
    $("#data").hide()
    $(this).show();
  });
  $("#loading").ajaxComplete(function(){
    $("#data").show()
    $(this).hide();
  });
});

var allIds = new Array();
var idsStr = "";
var column = ["stype", "date", "origin", "dispatch", "tosize", \
              "dispatch_user", "view", "view_pos", "view_user", "viewed_user", \
              "reply", "reply_user", "replyed_user", "click", "click_pos", \
              "click_user", "clicked_user"];
var sortOrder = { "home":{"stype":0, "date":0, "origin":0, "dispatch":0, "tosize":0, \
                 "dispatch_user":0, "view":0, "view_pos":0, "view_user":0, "viewed_user":0, \
                 "reply":0, "reply_user":0, "replyed_user":0, "click":0, "click_pos":0, \
                 "click_user":0, "clicked_user":0},
                 "stype":{"stype":0, "date":0, "origin":0, "dispatch":0, "tosize":0, \
                 "dispatch_user":0, "view":0, "view_pos":0, "view_user":0, "viewed_user":0, \
                 "reply":0, "reply_user":0, "replyed_user":0, "click":0, "click_pos":0, \
                 "click_user":0, "clicked_user":0},
                 "date":{"stype":0, "date":0, "origin":0, "dispatch":0, "tosize":0, \
                 "dispatch_user":0, "view":0, "view_pos":0, "view_user":0, "viewed_user":0, \
                 "reply":0, "reply_user":0, "replyed_user":0, "click":0, "click_pos":0, \
                 "click_user":0, "clicked_user":0} };

var currentData = new Array();

$(document).ready(function() {
  $.ajax({
    type: 'POST',
    url: '/get-stype-ids',
    async: false,
    success : function(text){
      ids = eval('(' + text + ')');
      idsStr = ',' + ids.join(',');
      for(var i = 0; i < ids.length; ++i) {
        allIds[i] = parseInt(ids[i]);
      }
      if (typeof(g_old_feed_list) != 'undefined') {
        for(var id in g_old_feed_list) {
          if(idsStr.indexOf(',' + id + ',') == -1) {
            allIds[allIds.length] = parseInt(id);
          }
        }
      }
      allIds.sort(function(a, b){ return a-b;});
      var html = '<option value="' + 0 + '">' + 'ALL</option>';
      for(var i = 0; i < allIds.length; ++i) {
        html += '<option value="' + allIds[i].toString() + '">' + allIds[i].toString() + '</option>';
      }
 
      $("select[name=stype]").html(html);
    },
    error : function(){
      alert('/加载出错, 请重新刷新页面');
    }
  });

  var today = new Date();
  var todayStr = today.getFullYear().toString() + "-" 
                 + ((today.getMonth()+1).toString().length == 1 ? "0": "") +  (today.getMonth()+1).toString() + "-"
                 + (today.getDate().toString().length == 1 ? "0": "") +  today.getDate().toString();
  $("input[name=date]").val(todayStr);

  $.ajax({
    type: 'POST',
    url: '/stat-list',
    async: false,
    data: "stype=0&date=" + todayStr + "&origin_url=0&limit=10",
    success : function(text){
      if($("#data tr").length > 1) {
        var len = $("#data tr").length;
        for(var i = len-1; i > 0; --i) {
          $("#data tr:eq(" + i.toString() + ")").remove();
        }
      }
      if(!text || text.length <= 0) return;
      currentData = eval('(' + text + ')');
      var html = "";
      for(var i=0; i<currentData.length; ++i) {
        html += "<tr><td>ALL</td>"
            + "<td>" + currentData[i]["date"].toString() + "</td>" + "<td>" + currentData[i]["dispatch"].toString() + "</td>" 
            + "<td>" + currentData[i]["tosize"].toString() + "</td>" + "<td>" + currentData[i]["dispatch_user"].toString() + "</td>"
            + "<td>" + currentData[i]["view"].toString() + "</td>" + "<td>" + currentData[i]["view_pos"].toString() + "</td>" 
            + "<td>" + currentData[i]["view_user"].toString() + "</td>" + "<td>" + currentData[i]["viewed_user"].toString() + "</td>"
            + "<td>" + currentData[i]["reply"].toString() + "</td>" + "<td>" + currentData[i]["reply_user"].toString() + "</td>" 
            + "<td>" + currentData[i]["click"].toString() + "</td>" + "<td>" + currentData[i]["click_pos"].toString() + "</td>"
            + "<td>" + currentData[i]["click_user"].toString() + "</td>" + "<td>" + currentData[i]["clicked_user"].toString() + "</td>";
            + "</tr>";
      }
      $("#data").append(html);
    },
    error : function(){
      alert('/加载出错');
    }
  });

  for(var i = 0; i < column.length; ++i) {
    if($("#title_" + column[i] + "_home")) {
      $("#title_" + column[i] + "_home").click(function(){
        var key = $(this).attr("id").substring(6, $(this).attr("id").lastIndexOf("_home"));
        if($("#data tr").length > 0) {
          var len = $("#data tr").length;
          for(var i = len-1; i >= 1; --i) {
            $("#data tr:eq(" + i.toString() + ")").remove();
          }
        }
        $("#data tr:eq(0) th a").each(function(){
          if($(this).text().match(/[↓↑]/)) {
            $(this).text($(this).text().substring(0, $(this).text().length-1));
          }
        });
        var html = "";
        currentData.sort(function(a, b){
          if(key.match(/^[0-9][0-9]*[0-9]$/)) {
            if(sortOrder["home"][key] == 0) {
              return parseInt(a[key])-parseInt(b[key]);
            } else {
              return parseInt(b[key])-parseInt(a[key]);
            }
          } else {
            if(sortOrder["home"][key] == 0) {
              if(a[key] > b[key]) return 1;
              if(a[key] == b[key]) return 0;
              if(a[key] < b[key]) return -1;
            } else {
              if(b[key] > a[key]) return 1;
              if(b[key] == a[key]) return 0;
              if(b[key] < a[key]) return -1;
            }
          }
        });
        if(sortOrder["home"][key] == 0) {
          $(this).text($(this).text() + "↑");
          sortOrder["home"][key] = 1;
        } else {
          $(this).text($(this).text() + "↓");
          sortOrder["home"][key] = 0;
        }
        for(var i = 0; i < currentData.length; ++i) {
          html += "<tr><td>ALL</td>"
            + "<td>" + currentData[i]["date"].toString() + "</td>" + "<td>" + currentData[i]["dispatch"].toString() + "</td>" 
            + "<td>" + currentData[i]["tosize"].toString() + "</td>" + "<td>" + currentData[i]["dispatch_user"].toString() + "</td>"
            + "<td>" + currentData[i]["view"].toString() + "</td>" + "<td>" + currentData[i]["view_pos"].toString() + "</td>" 
            + "<td>" + currentData[i]["view_user"].toString() + "</td>" + "<td>" + currentData[i]["viewed_user"].toString() + "</td>"
            + "<td>" + currentData[i]["reply"].toString() + "</td>" + "<td>" + currentData[i]["reply_user"].toString() + "</td>" 
            + "<td>" + currentData[i]["click"].toString() + "</td>" + "<td>" + currentData[i]["click_pos"].toString() + "</td>"
            + "<td>" + currentData[i]["click_user"].toString() + "</td>" + "<td>" + currentData[i]["clicked_user"].toString() + "</td>";
            + "</tr>";
        }
        $("#data").append(html);
      });
    }
  }

});

$.extend(DateInput.DEFAULT_OPTS, {
  month_names: ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"],
  short_month_names: ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"],
  short_day_names: ["日", "一", "二", "三", "四", "五", "六"],
  
  start_of_week: 0,

  stringToDate: function(string) {
    var matches;
    if (matches = string.match(/^(\d{4,4})-(\d{2,2})-(\d{2,2})$/)) {
      return new Date(matches[1], matches[2] - 1, matches[3]);
    } else {
      return null;
    };
  },

  dateToString: function(date) {
    var month = (date.getMonth() + 1).toString();
    var dom = date.getDate().toString();
    if (month.length == 1) month = "0" + month;
    if (dom.length == 1) dom = "0" + dom;
    return date.getFullYear() + "-" + month + "-" + dom;
  }
});

function fillTable(text, tableType) {
  var stypeDescription = new Array();
  $.ajax({
    type: 'POST',
    url: '/get-stype-list',
    async: false,
    success : function(text){
      var data = eval('(' + text + ')');
      for(var i=0; i< data.length; ++i) {
        stypeDescription[data[i]["stype"].toString()] = data[i]["description"];
      }
    },
    error : function(){
      alert('加载出错,请重新刷新页面');
    }
  });

  var html = '<tr>'
           + '<th><a id="title_stype_' + tableType + '" href="#nogo">类型</a></th>'
           + '<th>描述</th>'
           + '<th><a id="title_date_' + tableType + '" href="#nogo">日期</a></th>'
           + '<th><a id="title_dispatch_' + tableType + '" href="#nogo">发送量</a></th>'
           + '<th><a id="title_tosize_' + tableType + '" href="#nogo">分发量</a></th>'
           + '<th><a id="title_dispatch_user_' + tableType + '" href="#nogo">发送用户数</a></th>'
           + '<th><a id="title_view_' + tableType + '" href="#nogo">曝光条次</a></th>'
           + '<th><a id="title_view_pos_' + tableType + '" href="#nogo">平均曝光位置</a></th>'
           + '<th><a id="title_view_user_' + tableType + '" href="#nogo">取新鲜事的用户数</a></th>'
           + '<th><a id="title_reply_' + tableType + '" href="#nogo">回复数</a></th>'
           + '<th><a id="title_reply_user_' + tableType + '" href="#nogo">产生回复的用户数</a></th>'
           + '<th><a id="title_click_' + tableType + '" href="#nogo">点击量</a></th>'
           + '<th><a id="title_click_user_' + tableType + '" href="#nogo">产生点击的用户数</a></th>'
           + '</tr>'
  if(tableType == "stype") {
    html = html.substring(0, html.indexOf("</a>", html.indexOf("日期"))) + "↓" + html.substring(html.indexOf("</a>", html.indexOf("日期")));
  }
  if(tableType == "date") {
    html = html.substring(0, html.indexOf("</a>", html.indexOf("发送量"))) + "↓" + html.substring(html.indexOf("</a>", html.indexOf("发送量")));
  }

  if($("#data tr").length > 0) {
    var len = $("#data tr").length;
    for(var i = len-1; i >= 0; --i) {
      $("#data tr:eq(" + i.toString() + ")").remove();
    }
  }
  if(!text || text.length <= 0) return;
  currentData = eval('(' + text + ')');
  for(var i = 0; i < currentData.length; ++i) {
    html += "<tr>"
          + "<td>" + currentData[i]["stype"] + "</td>" 
          + "<td>" + (stypeDescription[currentData[i]["stype"]] ? stypeDescription[currentData[i]["stype"]]: "&nbsp;")+ "</td>"
          + "<td>" + currentData[i]["date"].toString() + "</td>" 
          + "<td>" + currentData[i]["dispatch"].toString() + "</td>" 
          + "<td>" + currentData[i]["tosize"].toString() + "</td>" 
          + "<td>" + currentData[i]["dispatch_user"].toString() + "</td>"
          + "<td>" + currentData[i]["view"].toString() + "</td>"
          + "<td>" + currentData[i]["view_pos"].toString() + "</td>"
          + "<td>" + currentData[i]["view_user"].toString() + "</td>"
          + "<td>" + currentData[i]["reply"].toString() + "</td>" 
          + "<td>" + currentData[i]["reply_user"].toString() + "</td>" 
          + "<td>" + currentData[i]["click"].toString() + "</td>"
          + "<td>" + currentData[i]["click_user"].toString() + "</td>"
          + "</tr>";
  }
  $("#data").append(html);
  $("#data").attr("width", "1200");

  for(var i = 0; i < column.length; ++i) {
    if($("#title_" + column[i] + "_" + tableType)) {
      $("#title_" + column[i] + "_" + tableType).click(function(){
        var key = $(this).attr("id").substring(6, $(this).attr("id").lastIndexOf("_" + tableType));
        if($("#data tr").length > 0) {
          var len = $("#data tr").length;
          for(var i = len-1; i >= 1; --i) {
            $("#data tr:eq(" + i.toString() + ")").remove();
          }
        }
        $("#data tr:eq(0) th a").each(function(){
          if($(this).text().match(/[↓↑]/)) {
            $(this).text($(this).text().substring(0, $(this).text().length-1));
          }
        });
        var html = "";
        currentData.sort(function(a, b){
          if(key.match(/^[0-9][0-9]*[0-9]$/)) {
            if(sortOrder[tableType][key] == 0) {
              return parseInt(a[key])-parseInt(b[key]);
            } else {
              return parseInt(b[key])-parseInt(a[key]);
            }
          } else {
            if(sortOrder[tableType][key] == 0) {
              if(a[key] > b[key]) return 1;
              if(a[key] == b[key]) return 0;
              if(a[key] < b[key]) return -1;
            } else {
              if(b[key] > a[key]) return 1;
              if(b[key] == a[key]) return 0;
              if(b[key] < a[key]) return -1;
            }
          }
        });
        if(sortOrder[tableType][key] == 0) {
          $(this).text($(this).text() + "↑");
          sortOrder[tableType][key] = 1;
        } else {
          $(this).text($(this).text() + "↓");
          sortOrder[tableType][key] = 0;
        }
        for(var i = 0; i < currentData.length; ++i) {
          html += "<tr>"
               + "<td>" + currentData[i]["stype"] + "</td>" 
               + "<td>" + (stypeDescription[currentData[i]["stype"]] ? stypeDescription[currentData[i]["stype"]]: "&nbsp;")+ "</td>"
               + "<td>" + currentData[i]["date"].toString() + "</td>" 
               + "<td>" + currentData[i]["dispatch"].toString() + "</td>" 
               + "<td>" + currentData[i]["tosize"].toString() + "</td>" 
               + "<td>" + currentData[i]["dispatch_user"].toString() + "</td>"
               + "<td>" + currentData[i]["view"].toString() + "</td>"
               + "<td>" + currentData[i]["view_pos"].toString() + "</td>"
               + "<td>" + currentData[i]["view_user"].toString() + "</td>"
               + "<td>" + currentData[i]["reply"].toString() + "</td>" 
               + "<td>" + currentData[i]["reply_user"].toString() + "</td>" 
               + "<td>" + currentData[i]["click"].toString() + "</td>"
               + "<td>" + currentData[i]["click_user"].toString() + "</td>"
               + "</tr>";
        }
        $("#data").append(html);
      }); 
    }
  }
}

$("select[name=stype]").change(function(){
  $.ajax({
    type: 'POST',
    url: '/stat-list',
    data: "stype=" + $("select[name=stype]").val() + "&date=" + $("input[name=date]").val() + "&origin_url=" + $("select[name=origin_url]").val(),
    success : function(text){
      fillTable(text, 'stype')
    },
    error : function(){
      alert('加载出错, 请重新刷新页面');
    }
  });
});

$("input[name=date]").change(function(){
  if(!$(this).val().match(/^(\d{4,4})-(\d{2,2})-(\d{2,2})$/)){
    alert("输入日期错误: " + $(this).val());
    return ;
  } else {
    $.ajax({
      type: 'POST',
      url: '/stat-list',
      data: "stype=0&date=" + $("input[name=date]").val() + "&origin_url=" + $("select[name=origin_url]").val(),
      success : function(text){
        fillTable(text, 'date');
      },
      error : function(){
        alert('/加载出错, 请重新刷新页面');
      }
    });
  }
});

</script>
</html>

