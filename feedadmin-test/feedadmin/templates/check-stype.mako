<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link rel="shortcut icon" href="favicon-rr.ico" type="image/x-icon"> 

<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>
<title>FD 按类型查看</title>
<script type="text/javascript" src="/AB-debug.js"></script>
<script type="text/javascript" src="/jquery.js"></script>
<script src="/Highcharts-2.2.5/js/highcharts.js"></script>

<script src="/Highstock-1.2.2/js/highstock.js"></script>
<script src="/Highstock-1.2.2/js/modules/exporting.js"></script>
<script src="/Highstock-1.2.2/js/themes/gray.js"></script>

<script type=text/javascript>
$(function(){
	$('#mobanwang_com li').hover(function(){
		$(this).children('ul').stop(true,true).show('slow');
	},function(){
		$(this).children('ul').stop(true,true).hide('slow');
	});

});

</script>

<div id="wrapper" style=" z-index:1000;">
<ul id="mobanwang_com" class="first-menu">
  <li><a href="stat" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>

  <li><a href="#">实验平台</a>
    <ul id="subNews" class="second-menu">
      <li><a href="experi-select" target="_self" style="z-index:1000;">实验登记查看</a></li>
      <li><a href="stat-ABDebug" target="_self" style="z-index:1000;">选择尾号查看</a></li>
    </ul>
  </li>
  <li><a href="http://feed.d.xiaonei.com/stat-detail" target="_blank">详细信息</a>
    <ul id="subNews" class="second-menu">
      <li><a href="check-plat" target="_self" style="z-index:1000;">选择平台查看</a></li>
      <li><a href="check-stype" target="_self" style="z-index:1000;">选择类型查看</a></li>
    </ul>
  </li>
</ul>
</div>



<h1> 按类型查看 </h1>


</head>

<body>

<div id="content" >
	<div id="right">
		<fieldset>
		<legend>CONDITION (WEB端数据)</legend>

<form method="get" name="show_checkbox" style="margin: 10px 10px 10px 10px">
 <br>
<input id="hour" type="radio" checked="" value="0" name="day"> 	<label for="hour">按小时</label>
<input id="day" type="radio" value="1" name="day"> 		<label for="day">按天</label>
  <br>
 ================== 
<div class="t1">查看项</div>
  <input value="1" name="pv" id="feed_sum" type="checkbox">  			<label for="pv">曝光量</label>
  <input value="1" name="dispatch" id="dispatch_cnt" type="checkbox">  		<label for="dispatch">分发量</label>
  <br>
  <input value="1" name="reply" id="reply_sum" checked="checked" type="checkbox">  <label for="reply">回复量</label>
  <input value="1" name="click" id="click_sum" checked="checked" type="checkbox">  <label for="click">点击量</label>
  <br>
  <input value="1" name="rr" id="reply_rate" type="checkbox">  		<label for="rr">回复率</label>
  <input value="1" name="ctr" id="click_rate" type="checkbox">  	<label for="ctr">点击率</label>
  <br>
  <input value="1" name="index" id="position_clk" type="checkbox"> 	 <label for="index">展示位置</label>
  <input value="1" name="fin" id="position_show" type="checkbox">		 <label for="fin">点击位置</label>
  <br>
 ================== 
<div class="t1">类型（空格隔开)
	<br> 
  (例如：all 或者 102 502)
  <input id="stype" value="all" type="text" style="width:100px">
  <input value="GO" style="float:right" type="button" onclick="go_fun()"></div>
</form>
  <br><br>

		</fieldset>
	</div>

	<div id="left">
		<div>
			<fieldset>
	<div id="loading"  style="width:100px; height:100px;background:url(/loading/loading45.gif) no-repeat; margin: 100px 10px 10px 500px ; " > </div>
			<legend>CONTAINER1</legend>
	<div id="container1" style="min-width: 400px; height: 500px; background-color:cliver ; margin: 10px 5px 10px 10px ; "></div>
			</fieldset>
		</div>
	</div>
</div>

</body>



<script type="text/javascript">

	var chart_all1 = {
			chart : {
				renderTo : 'container1',
				zoomType: 'xy',
			},
		rangeSelector: {
		     	   buttons: [{
		     	       type: 'day',
		     	       count: 1,
		     	       text: 'd'
		     	   }, {
		     	       type: 'week',
		     	       count: 1,
		     	       text: '1w'
		     	   }, {
		     	       type: 'month',
		     	       count: 1,
		     	       text: '1m'
		     	   },  {
		     	       type: 'year',
		     	       count: 1,
		     	       text: '1y'
		     	   }, {
		     	       type: 'all',
		     	       text: 'All'
		     	   }],
		     	   selected: 1
		   	},
	               tooltip: {
            		}, 
			title : {
				text : '分发,曝光/100,点击量,回复量'
			},
			series : []
		};

function test(id) {
	return document.getElementById(id).checked
}


function get_data(stype) {

	var day = 0
	if (document.getElementById("day").checked)
		day = 1

	document.getElementById("loading").style.display="block";
	document.getElementById("container1").innerHTML =  "";

  $.ajax({
    type: 'POST',
    url: '/web-stype-list',
    async: true,
    data:"stype="+stype+"&day="+day,
    success : function(text){

	      		if(!text || text.length <= 0) return;
		      	currentData = eval('(' + text + ')');
  
		      var series = [
				{yAxis: 1, name : '曝光量', data : [], type: 'spline'}, 
				{name : '分发量', data : [], type: 'spline'}, 
				{name : '回复量', data : [], type: 'spline'}, 
				{name : '点击量', data : [], type: 'spline'}, 
				{yAxis: 2, name : '回复率', data : [], type: 'spline'}, 
				{yAxis: 2,name : '点击率', data : [], type: 'spline'}, 
				{yAxis: 3,name : '展示位置', data : [], type: 'spline'}, 
				{yAxis: 3,name : '点击位置', data : [], type: 'spline'}, 
				{name : '可点击各项 确定是否显示', data : [], type: 'spline'}, 
		      ]	
		var date = new Array(currentData.length);
                var mtime = 1346428800000 + 8*1000*60*60;
		var tmtime
		for(var i = 0, j = 0; i < currentData.length -1 ;  ++i) {
			//index = div(i, 5)
			index = i 
			mtime = currentData[index]["date"] + 8*1000*60*60
			//if (mtime - tmtime != 3600000) alert(mtime + " : " + tmtime + " I:" + i + "  feed_sum" + currentData[i]["feed_sum"])
			//tmtime = mtime
			//mtime = mtime + 1000*60*60
			series[0].data[index] = [mtime, currentData[i]["feed_sum"] ]
			series[1].data[index] = [mtime, currentData[i]["dispatch_cnt"] ]
			series[2].data[index] = [mtime, currentData[i]["reply_sum"] ]
			series[3].data[index] = [mtime, currentData[i]["click_sum"] ]
			series[4].data[index] = [mtime, currentData[i]["reply_sum"] / currentData[i]["feed_sum"] ]
			series[5].data[index] = [mtime, currentData[i]["click_sum"] / currentData[i]["feed_sum"] ]
			series[6].data[index] = [mtime, currentData[i]["position_show"] ] // ??????????
			series[7].data[index] = [mtime, currentData[i]["position_clk"] ]
		}

			//alert(series[0].data)
			chart_all1.title.text = stype+'类型的各项信息'
			//chart_all2.title.text = stype+'类型的 点击率,回复率'
			chart_all1.series = []
			chart_all1.yAxis = YA 
			//chart_all2.series = []
			if (test("feed_sum")) chart_all1.series.push(series[0])
			else chart_all1.yAxis[1].title.text = ""

			var tt = 0
			if (test("dispatch_cnt")) chart_all1.series.push(series[1])
			else tt = tt+1
			if (test("reply_sum")) chart_all1.series.push(series[2])
			else tt = tt+1
			if (test("click_sum")) chart_all1.series.push(series[3])
			else tt = tt+1
			if (tt == 3) chart_all1.yAxis[0].title.text = ""
 
			var tt = 0
			if (test("reply_rate")) chart_all1.series.push(series[4])
			else tt = tt+1
			if (test("click_rate")) chart_all1.series.push(series[5])
			else tt = tt+1
			if (tt == 2) chart_all1.yAxis[2].title.text = ""
	
			tt = 0
			if (test("position_show")) chart_all1.series.push(series[6])
			else tt = tt + 1
			if (test("position_clk")) chart_all1.series.push(series[7])
			else tt = tt + 1
			if (tt == 2) chart_all1.yAxis[3].title.text = ""
			
		      var chart1 = new Highcharts.StockChart(chart_all1)
		      //var chart2 = new Highcharts.StockChart(chart_all2)

			document.getElementById("loading").style.display="none";

      //$("#data").append(html);
    },
    error : function(){
      alert('ready 加载出错');
    }
  });

}


function go_fun() {
	var stype = document.getElementById("stype").value
	get_data(stype)

}

$(document).ready(get_data("all"));

</script>

</html>











