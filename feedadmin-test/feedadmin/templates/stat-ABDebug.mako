<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link rel="shortcut icon" href="favicon-rr.ico" type="image/x-icon"> 

<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>
<title>content</title>
<script type="text/javascript" src="/jquery.js"></script>
<script type="text/javascript" src="/AB-debug.js"></script>
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

  <li><a href="#" >实验平台</a>
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


</head>

<body>
<br>
<br>
<div id="content" >
	<div id="right">
		<fieldset>
		<legend>CONDITION</legend>


<form method="get" name="show_checkbox" style="margin: 10px 10px 10px 10px">
 <div class="t1" style="color:#ff0;  font-size:20px">查看项</div>
  <input value="1" name="pv" id="feed_sum" type="checkbox">  			<label for="pv">曝光量</label>
  <input value="1" name="dispatch" id="dispatch_cnt" type="checkbox">  		<label for="dispatch">分发量</label>
  <br>
  <input value="1" name="reply" id="reply_sum" checked="checked" type="checkbox">  <label for="reply">回复量</label>
  <input value="1" name="reply" id="reply_rate" type="checkbox">  	<label for="rr">回复率(回复量/曝光量)</label>
  <br>
  <input value="1" name="click" id="click_sum" checked="checked" type="checkbox">  <label for="click">点击量</label>
  <input value="1" name="click" id="click_rate" type="checkbox">  	<label for="ctr">点击率(点击量/曝光量)</label>
  <br>
  <input value="1" name="index" id="position_show"  type="checkbox">  	<label for="index">展示位置</label>
  <input value="1" name="fin" id="position_clk"  type="checkbox">  	<label for="fin">点击位置</label>
  <br>
 ================== 
 <br>
 <br>
<div class="t1" style="color:#ff0;  font-size:20px">查看方式</div>
<input id="hour" type="radio" value="0" name="day"> 	<label for="hour">按小时</label>
<input id="day" type="radio" checked="" value="1" name="day"> 		<label for="day">按天</label>
  <br>
---------------------
  <br>
<div class="t1" style="color:#ff0; font-size:20px">类型</div>(eg：all 或者 502)
  <input id="stype" value="all" type="text" style="width:100px;">
  <br>
---------------------
  <br>
<div class="t1" style="color:#ff0;  font-size:20px">目标尾号</div>(空格隔开 eg：04 50)
  <input id="include_uid" value="10 30" type="text" style="width:100px;">
<div class="t1" style="color:#ff0;  font-size:20px">过滤尾号</div>
  <input id="exclude_uid" value="none" type="text" style="width:100px;">
  <br>
---------------------
  <br>
<div class="t1" style="color:#ff0;  font-size:20px">展示形式</div>
  <input value="1" name="line" id="line" checked="checked" type="checkbox">  	<label id="line">变化趋势</label>
  <input value="1" name="column" id="column" type="checkbox">  			<label for="column">差异率</label>
 <br>
---------------------
 <br>
  <input value="GO" style="float:right" type="button" onclick="go_fun()"></div>
 </form>

		</fieldset>
	</div>

	<div id="left">
		<div>
			<fieldset>
	<div id="loading"  style="width:100px; height:100px;background:url(/loading/loading45.gif) no-repeat; margin: 100px 10px 10px 500px ; " > </div>
			<legend id="cc">result</legend>
	<div id="container1" style="min-width: 1000px; height: 500px; background-color:cliver ; margin: 10px 5px 10px 10px ; "></div>
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

function has(Arr, num ) {
	var deb=arguments[2]==-1?0:1
	for (a in Arr) {
		//if(deb) alert("has: " + Arr[a] + " : "+ num)
		if (Arr[a] == num) return true
	}
	return false
}

        //------------------------------------
        function clone(myObj){
          if(typeof(myObj) != 'object') return myObj;
          if(myObj == null) return myObj;
          var myNewObj = new Object();
          for(var i in myObj)
             myNewObj[i] = clone(myObj[i]);
          return myNewObj;
        }       

        var currentData = new Array();
        var map = new Array();
        var ABData  = new Array(100);
        var tmp_date = new Array();


function get_data(stype) {
	//str = "1 45 3645 12341"
	//alert(str.split(" ").length)
	var instr = document.getElementById("include_uid").value
	var exstr = document.getElementById("exclude_uid").value
	var inArr = instr.split(" ")
	var exArr = exstr.split(" ")

	var day = 0
	if (document.getElementById("day").checked)
		day = 1

	document.getElementById("loading").style.display="block";
	document.getElementById("container1").innerHTML =  "";

  $.ajax({
    type: 'POST',
    url: '/stat-ABDebug-data',
    //url: '/web-stype-list',
    async: true,
    data:"stype="+stype+"&day="+day ,
    success : function(text){

	      	if(!text || text.length <= 0) return;
		currentData = eval('(' + text + ')');
  
		var meta = { name : 'name', data :{"feed_sum":0, "dispatch_cnt":0, "reply_sum":0, "click_sum":0, "position_show":0, "position_clk":0} } 
        
                for(var i=0; i<100; ++i) ABData[i] = [];
                        
                for(var i = 0; i < currentData.length-1;  ++i) {

                        now = currentData[i]
                        if (has(tmp_date, now["date"] , -1) == false)  tmp_date.push(now["date"])

                        meta.name = now["date"]
                        meta.data = []
                        meta.data["feed_sum"] = (now["feed_sum"])
                        meta.data["dispatch_cnt"] = (now["dispatch_cnt"])
                        meta.data["reply_sum"] = (now["reply_sum"])
                        meta.data["click_sum"] = (now["click_sum"])
                        meta.data["position_show"] = (now["position_show"])
                        meta.data["position_clk"] = (now["position_clk"])
                        uid = now["uid"]
                        ABData[uid][ now["date"] ] = clone(meta)
                }
		//alert(tmp_date)
		var meta_z = {time:0, data:{"feed_sum":0, "dispatch_cnt":0, "reply_sum":0, "click_sum":0, "reply_ave":0, "click_ave":0, "position_show":0, "position_clk":0}}
		var mmeta = clone(meta_z), mmeta_ex=clone(meta_z)
		var inData=new Array(), exData=new Array()
		index = 0
		aveindex = 0
		//alert(inArr)
		//alert(exArr)
		for (i in tmp_date) {
			mmeta = clone(meta_z), mmeta_ex=clone(meta_z)
			for(var j = 0; j < 100 ;  ++j) {
				var mtime = tmp_date[i]
				var userid = j

				if (has(inArr, userid)) {	
					//alert("1"+userid)
					if (!ABData[userid][mtime]) { alert("wrong!!" + mtime + " uid:"+userid); continue}
					var mdata = ABData[userid][mtime].data

					mmeta.time = mtime
					mmeta.data["feed_sum"] += mdata["feed_sum"]
					mmeta.data["dispatch_cnt"] += mdata["dispatch_cnt"]
					mmeta.data["reply_sum"] += mdata["reply_sum"]
					mmeta.data["click_sum"] += mdata["click_sum"]
					mmeta.data["reply_ave"] += mdata["reply_sum"]/ mdata["feed_sum"]
					mmeta.data["click_ave"] += mdata["click_sum"]/ mdata["feed_sum"]
					mmeta.data["position_show"] += mdata["position_show"]
					mmeta.data["position_clk"] += mdata["position_clk"]
					continue;
				}
				
				if (has(exArr, userid)) {
					//alert("2"+ userid)
					continue
				}

					//alert("3"+ userid)
				if (!ABData[userid][mtime]) { alert("wrong2!!" + mtime + " uid:"+userid); continue}

					var mdata = ABData[userid][mtime].data
					mmeta_ex.time = mtime
					mmeta_ex.data["feed_sum"] += mdata["feed_sum"]
					mmeta_ex.data["dispatch_cnt"] += mdata["dispatch_cnt"]
					mmeta_ex.data["reply_sum"] += mdata["reply_sum"]
					mmeta_ex.data["click_sum"] += mdata["click_sum"]
					mmeta_ex.data["reply_ave"] += mdata["reply_sum"]/ mdata["feed_sum"]
					mmeta_ex.data["click_ave"] += mdata["click_sum"]/ mdata["feed_sum"]
					mmeta_ex.data["position_show"] += mdata["position_show"]
					mmeta_ex.data["position_clk"] += mdata["position_clk"]
	
			}		
			inData.push(clone(mmeta))
			exData.push(clone(mmeta_ex))
			//alert(mtime+" in:"+ inData[inData.length-1].data["reply_sum"] + "  ex:"+ exData[exData.length-1].data["reply_sum"]   )
		}



		//===========================================================================
		      var series = [
				{yAxis: 1, name : instr+ '曝光量', data : [], type: 'spline'}, 
				{name : instr+ '分发量', data : [], type: 'spline'}, 
				{name : instr+ '回复量', data : [], type: 'spline'}, 
				{name : instr+ '点击量', data : [], type: 'spline'}, 
				{yAxis: 2, name : instr+ '回复率', data : [], type: 'spline'}, 
				{yAxis: 2,name : instr+ '点击率', data : [], type: 'spline'}, 
				{yAxis: 3,name : instr+ '展示位置', data : [], type: 'spline'}, 
				{yAxis: 3,name : instr+ '点击位置', data : [], type: 'spline'}, 
				{name : '可点击各项 确定是否显示', data : [], type: 'spline'}, 
		      ]	
			for( i in  inData) {
				var mtime = inData[i].time + 8*1000*60*60 
				var mdata = inData[i].data
				series[0].data[i] = [mtime, mdata["feed_sum"]/inArr.length ]
				series[1].data[i] = [mtime, mdata["dispatch_cnt"]/inArr.length ]
				series[2].data[i] = [mtime, mdata["reply_sum"]/inArr.length ]
				series[3].data[i] = [mtime, mdata["click_sum"]/inArr.length ]
				series[4].data[i] = [mtime, mdata["reply_ave"]/inArr.length ]
				series[5].data[i] = [mtime, mdata["click_ave"]/inArr.length ]
				series[6].data[i] = [mtime, mdata["position_show"]/inArr.length ]
				series[7].data[i] = [mtime, mdata["position_clk"]/inArr.length ]
			}  


		      var seriesAVE = [
				{yAxis: 1, name : 'others曝光量', data : [], type: 'spline'}, 
				{name : 'others分发量', data : [], type: 'spline'}, 
				{name : 'others回复量', data : [], type: 'spline'}, 
				{name : 'others点击量', data : [], type: 'spline'}, 
				{yAxis: 2, name : 'others回复率', data : [], type: 'spline'}, 
				{yAxis: 2,name : 'others点击率', data : [], type: 'spline'}, 
				{yAxis: 3,name : 'others展示位置', data : [], type: 'spline'}, 
				{yAxis: 3,name : 'others点击位置', data : [], type: 'spline'}, 
				{name : '可点击各项 确定是否显示', data : [], type: 'spline'}, 
		      ]	
			var len = 0
			if(exArr[0] == "none") len = 0
			else len = exArr.length
			for( i in  exData) {
				var mtime = exData[i].time + 8*1000*60*60
				var mdata = exData[i].data
				seriesAVE[0].data[i] = [mtime, mdata["feed_sum"]/(100-inArr.length-len) ]
				seriesAVE[1].data[i] = [mtime, mdata["dispatch_cnt"]/(100-inArr.length-len) ]
				seriesAVE[2].data[i] = [mtime, mdata["reply_sum"]/(100-inArr.length-len) ]
				seriesAVE[3].data[i] = [mtime, mdata["click_sum"]/(100-inArr.length-len) ]
				//alert(mdata["reply_ave"]+"  "+ (100-inArr.length-len))
				seriesAVE[4].data[i] = [mtime, mdata["reply_ave"]/(100-inArr.length-len) ]
				//alert(seriesAVE[4].data[i][1])
				seriesAVE[5].data[i] = [mtime, mdata["click_ave"]/(100-inArr.length-len) ]
				seriesAVE[6].data[i] = [mtime, mdata["position_show"]/(100-inArr.length-len) ]
				seriesAVE[7].data[i] = [mtime, mdata["position_clk"]/(100-inArr.length-len) ]
			}  



			//alert(series[0].data)
			chart_all1.title.text = stype+'类型的各项信息'
			//chart_all2.title.text = stype+'类型的 点击率,回复率'
			chart_all1.series = [{
				type : 'flags',
				data : [{
					x : Date.UTC(2012, 8, 14),
					title : 'A',
					text : 'Shape: "squarepin"'
				}, {
					x : Date.UTC(2012, 8, 18),
					title : 'A',
					text : 'Shape: "squarepin"'
				}],
				onSeries : 'dataseries',
				shape : 'squarepin',
				width : 16
			}, {
				type : 'flags',
				data : [{
					x : Date.UTC(2012, 8, 1),
					title : 'B',
					text : 'Shape: "circlepin"'
				}, {
					x : Date.UTC(2012, 8, 2),
					title : 'B',
					text : 'Shape: "circlepin"'
				}],
				shape : 'circlepin',
				width : 16
			}, {
				type : 'flags',
				data : [{
					x : Date.UTC(2012, 8, 10),
					title : 'C',
					text : 'Shape: "flag"'
				}, {
					x : Date.UTC(2012, 8, 11),
					title : 'C',
					text : 'Shape: "flag"'
				}],
				color : '#5F86B3',
				fillColor : '#5F86B3',
				onSeries : 'dataseries',
				width : 16,
				style : {// text style
					color : 'white'
				},
				states : {
					hover : {
						fillColor : '#395C84' // darker
					}
				}
			}]
			chart_all1.yAxis = YA 
			//chart_all2.series = []
			if (test("feed_sum")) { 
				chart_all1.series.push(series[0])
				chart_all1.series.push(seriesAVE[0])
			}
			else chart_all1.yAxis[1].title.text = ""

			var tt = 0
			if (test("dispatch_cnt")) {
				chart_all1.series.push(series[1])
				chart_all1.series.push(seriesAVE[1])
			}
			else tt = tt+1
			if (test("reply_sum")) { 
				chart_all1.series.push(series[2])
				chart_all1.series.push(seriesAVE[2])
			}
			else tt = tt+1
			if (test("click_sum")) {
				chart_all1.series.push(series[3])
				chart_all1.series.push(seriesAVE[3])
			}
			else tt = tt+1
			if (tt == 3) chart_all1.yAxis[0].title.text = ""

			var tt = 0
			if (test("reply_rate")) {
				chart_all1.series.push(series[4])
				chart_all1.series.push(seriesAVE[4])
			}
			else tt = tt+1
			if (test("click_rate")) {
				chart_all1.series.push(series[5])
				chart_all1.series.push(seriesAVE[5])
			}
			else tt = tt+1
			if (tt == 2) chart_all1.yAxis[2].title.text = ""

			tt = 0
			if (test("position_show")) {
				chart_all1.series.push(series[6])
				chart_all1.series.push(seriesAVE[6])
			}
			else tt = tt + 1
			if (test("position_clk")) {
				chart_all1.series.push(series[7])
				chart_all1.series.push(seriesAVE[7])
			}
			else tt = tt + 1
			if (tt == 2) chart_all1.yAxis[3].title.text = ""
			
			//alert(chart_all1.series[0].data[1])
		      var chart1 = new Highcharts.StockChart(chart_all1)
		      //var chart2 = new Highcharts.StockChart(chart_all2)

			document.getElementById("loading").style.display="none";
			document.getElementById("cc").style.display="block";

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














