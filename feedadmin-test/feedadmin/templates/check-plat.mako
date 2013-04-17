<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link rel="shortcut icon" href="favicon-rr.ico" type="image/x-icon"> 

<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>
<title>content</title>

<script type="text/javascript" src="/stat.mako.js"></script>
<script type="text/javascript" src="/jquery.js"></script>
<script src="/Highcharts-2.2.5/js/highcharts.js"></script>
<!-- Additional files for the Highslide popup effect -->
<script type="text/javascript" src="/gray.js"></script>
<script type="text/javascript" src="/highslide-full.min.js"></script>
<script type="text/javascript" src="/highslide.config.js" charset="utf-8"></script>
<link rel="stylesheet" type="text/css" href="/highslide.css"/> 
<script type="text/javascript" src="sliding_effect.js"></script>


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

  <li><a href="#" target="self">实验平台</a>
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


<h1> <a href="check-plat" target="_self" >按平台查看 </a></h1>

</head>




<body>

<div id="content" >
	<div id="right">
		<fieldset>
		<legend> ---&nbsp选择查看项&nbsp--- </legend>

<form method="get" name="show_checkbox"  style="margin: 10px 10px 10px 10px">
  
  <input value="1" name="c2" id="uv" type="checkbox" checked="checked" onchange="go_change('bb')">
  <label for="uv">访问人数(UV)</label>
  <br>
  <input value="1" name="c2" id="rv" type="checkbox" onchange="go_change('bb')">
  <label for="rv">取新鲜事操作(RV)</label>
  <br>
  <input value="1" name="c2" id="pv" type="checkbox" onchange="go_change('bb')">
  <label for="pv">曝光量(PV)</label>
  <br>
  <input value="1" name="c2" id="session_cnt" type="checkbox" onchange="go_change('bb')">
  <label for="session_cnt">活跃次数</label>
  <br>
  <input value="1" name="c2" id="session_sum" type="checkbox" onchange="go_change('bb')">
  <label for="session_sum">活跃时长</label>
  <br>
 ================== 
 <br>
<input id="hour" type="radio" checked="" value="0" name="day" onchange="go_data('bb')"> 	<label for="hour">按小时</label>
<input id="day" type="radio" value="1" name="day" onchange="go_data('bb')"> 		<label for="day">按天</label>
  <br>
 <!--div class="t1">查看项</div>
  <label for="uv">访问人数(UV)</label>
  <br>
  <label for="rv">取新鲜事操作(RV)</label>
  <br>
  <label for="pv">曝光量(PV)</label>
  <br>
  <label for="session_cnt">活跃次数</label>
  <br>
  <label for="session_sum">活跃时长</label>
  <br-->
  
</form>
		</fieldset>

		<fieldset>
		<legend >选择平台</legend>
<div id="navigation-block"> <!--img src="background.jpg" id="hide" /-->


  <ul id="sliding-navigation">

    <li class="sliding-element">

      <h3>选择平台</h3>

    </li>

    <li class="sliding-element"><a href="/check-plat?view=all">所有</a></li>

    <li class="sliding-element"><a href="/check-plat?view=view0" >WEB</a></li>

    <li class="sliding-element"><a href="/check-plat?view=view2" >手机</a></li>

    <li class="sliding-element"><a  href="/check-plat?view=view3">实时化</a></li>
    <li class="sliding-element"><a href="/check-plat?view=view4" >开放平台</a></li>
    <li class="sliding-element"><a href="/check-plat?view=view6" >TimeLine</a></li>

  </ul>

</div>
		</fieldset>
	</div> <!-- left  -->

<!--- -------------------------------------------- -->
      <div id="left">
		<div id="div_viewa">
			<fieldset>
			<legend id="legendid">ALL</legend>
	<div id="container_plat" style="min-width: 400px; min-height: 525px; background-color:white ; margin: 10px 5px 10px 10px ; "></div>
			</fieldset>
		</div>
      </div> <!-- left -->
</div>
</body>



<script type="text/javascript">
	var name
	var chart_all = {
			chart : {
				renderTo : 'container_plat',
				//type: 'column',
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
		     	   }, {
		     	       type: 'all',
		     	       text: 'All'
		     	   }],
		     	   selected: 1
		   	},
	               tooltip: {
            		}, 
			title : {
				text : 'DATA'
			},
			series : []
		};

function test(id) {
        return document.getElementById(id).checked
}


var currentData;

var series = [
  	{name : '访问人数', data : [], type: 'spline'}, 
  	{yAxis: 1,name : '取新鲜事操作', data : [], type: 'spline'}, 
  	{yAxis: 2,name : '曝光量', data : [], type: 'spline'}, 
  	{yAxis: 3,name : '活跃次数', data : [], type: 'spline'}, 
  	{yAxis: 4,name : '活跃时长', data : [], type: 'spline'}, 
  	{yAxis: 3,name : '可点击各项 确定是否显示', data : []}, 
]	


function go_change(ff) {

		      chart_all.series = []
			if(test("uv")) {
		      		chart_all.series.push(series[0]);
			}     
			if(test("rv")) {
		      		chart_all.series.push(series[1]);
			}     
			if(test("pv")) {
		      		chart_all.series.push(series[2]);
			}     
			if(test("session_cnt")) {
		      		chart_all.series.push(series[3]);
			}     
			if(test("session_sum")) {
		      		chart_all.series.push(series[4]);
			}     

		try {
		      var chart1 = new Highcharts.StockChart(chart_all)
		} catch (e) {
			alert(e)
		}


}


function go_data(ff) {
	var day = 0
	if (document.getElementById("day").checked)
		day = 1

  $.ajax({
    type: 'POST',
    url: '/view-day-list',
    async: false,
    data:"view=" + ${c.name}+"&day="+day,
    success : function(text){
	name = "HH"
	switch(${c.name})
	   　　{
	　　   case -1:
		 name = "ALL"
	 　　    break
	　　   case 0:
		 name = "WEB"
	 　　    break
	　　   case 2:
		 name = "手机"
	 　　    break
	　　   case 3:
		 name = "实时化"
	 　　    break
	　　   case 4:
		 name = "开放平台"
	 　　    break
	　　   case 6:
		 name = "TimeLine"
	 　　    break
	　　   default:
		 name = "NONE"
	　　   }
	      $("#legendid").html("----->" + name + "<-----");


	      		if(!text || text.length <= 0) return;
		      	currentData = eval('(' + text + ')');

//		      var series = [
//				{name : '访问人数', data : [], type: 'spline'}, 
//				{yAxis: 1,name : '取新鲜事操作', data : [], type: 'spline'}, 
//				{yAxis: 2,name : '曝光量', data : [], type: 'spline'}, 
//				{yAxis: 3,name : '活跃次数', data : [], type: 'spline'}, 
//				{yAxis: 4,name : '活跃时长', data : [], type: 'spline'}, 
//				{yAxis: 3,name : '可点击各项 确定是否显示', data : []}, 
//		      ]	
//
		series[0].data = []
		series[1].data = []
		series[2].data = []
		series[3].data = []
		series[4].data = []
		series[5].data = []
		for(var i = 0, j = 0; i < currentData.length -1 ;  ++i) {
			//index = div(i, 5)
			index = i 
			mtime = currentData[index]["date"] + 8*1000*60*60
			series[0].data[index] = [mtime, currentData[i]["uv"] ] 
			series[1].data[index] = [mtime, currentData[i]["rv"] ]
			series[2].data[index] = [mtime, currentData[i]["feed_sum"] ]
			series[3].data[index] = [mtime, currentData[i]["secnt"] ]
			series[4].data[index] = [mtime, currentData[i]["sesum"] ]
		}

                	chart_all.title.text =  name+'平台的各项指标',
			chart_all.yAxis = YA	
		      chart_all.series = []
			if(test("uv")) {
		      		chart_all.series.push(series[0]);
			}     
			if(test("rv")) {
		      		chart_all.series.push(series[1]);
			}     
			if(test("pv")) {
		      		chart_all.series.push(series[2]);
			}     
			if(test("session_cnt")) {
		      		chart_all.series.push(series[3]);
			}     
			if(test("session_sum")) {
		      		chart_all.series.push(series[4]);
			}     

			if(chart_all.series.length == 0) { document.getElementById("div_viewa").display = "none"; return ;}
			else document.getElementById("div_viewa").display = "block";
try {
		      var chart1 = new Highcharts.StockChart(chart_all)
} catch (e) {
alert(e)
}

      //$("#data").append(html);
    },
    error : function(){
      alert('ready 加载出错');
    }
  });

}

$(document).ready( go_data("dd") );
</script>



</html>





