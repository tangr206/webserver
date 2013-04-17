<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link rel="shortcut icon" href="favicon-rr.ico" type="image/x-icon"> 

<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>
<title>FD</title>
<!--script type="text/javascript" src="/stat.mako.js"></script-->
<script type="text/javascript" src="/stat.mako.js"></script>
<script type="text/javascript" src="/jquery.js"></script>
<script src="/Highcharts-2.2.5/js/highcharts.js"></script>
<!-- Additional files for the Highslide popup effect -->
<script type="text/javascript" src="/gray.js"></script>
<script type="text/javascript" src="/highslide-full.min.js"></script>
<script type="text/javascript" src="/highslide.config.js" charset="utf-8"></script>
<script type="text/javascript" src="sliding_effect.js"></script>

<script src="/Highstock-1.2.2/js/highstock.js"></script>
<script src="/Highstock-1.2.2/js/modules/exporting.js"></script>
<script src="/Highstock-1.2.2/js/themes/gray.js"></script>


<link rel="stylesheet" type="text/css" href="/highslide.css"/> 

<script type=text/javascript>
$(function(){
	$('#mobanwang_com li').hover(function(){
		$(this).children('ul').stop(true,true).show('slow');
	},function(){
		$(this).children('ul').stop(true,true).hide('slow');
	});

	$('#big_map').hover(function(){
		$('#map').stop(true,true).show('slow');
	},function(){
		$('#map').stop(true,true).hide('slow');
	});

});
</script>

<div id="wrapper" style=" z-index:1000;">
<!--ul id="mobanwang_com" class="first-menu">
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
</ul-->
</div>
<center><h1>FEED DATA-PLATFORM</h1></center>

</head>

<body>

<div id="content" >
	<div id="right">
		<fieldset>
		<legend>INSTRUCTION</legend>
<div id="navigation-block"> <!--img src="background.jpg" id="hide" /-->
  <ul id="sliding-navigation">
    <li class="sliding-element"><a href="/experi-select">实验登记查看</a></li>
    <li class="sliding-element"><a href="/stat-ABDebug" >指定尾号查看</a></li>
    <li class="sliding-element"><a href="/check-plat" >选择平台查看</a></li>
    <li class="sliding-element"><a  href="/check-stype">选择类型查看</a></li>

  </ul>

</div>

		</fieldset>

		<fieldset id="big_map" style="margin:50px 0px 0px 0px">
		<legend>VisitMap</legend>
			<div id="map" style="display:none">
<script type="text/javascript" src="http://jk.revolvermaps.com/r.js"></script><script type="text/javascript">rm_f1st('5','220','true','false','000000','ak4h44d83r7','true','ff0000');</script><noscript><applet codebase="http://rk.revolvermaps.com/j" code="core.RE" width="210" height="210" archive="g.jar"><param name="cabbase" value="g.cab" /><param name="r" value="true" /><param name="n" value="false" /><param name="i" value="ak4h44d83r7" /><param name="m" value="5" /><param name="s" value="220" /><param name="c" value="ff0000" /><param name="v" value="true" /><param name="b" value="000000" /><param name="rfc" value="true" /></applet></noscript>
			</div>
		</fieldset>

	</div>

	<div id="left">
		<div>
			<fieldset>
	<div id="loading"  style="width:100px; height:100px;background:url(/loading/loading45.gif) no-repeat; margin: 100px 10px 10px 500px ; " > </div>
			<legend>WEB</legend>
				<div id="container_web" style="min-width: 400px; height: 500px; margin: 10px 5px 10px 10px ; "></div>
			</fieldset>
		</div>
		<!--div>
			<fieldset>
			<legend>ALL</legend>
				<div id="container_all" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px"></div>
			</fieldset>
		</div-->
	</div>
</div>

</body>





<script type="text/javascript">

	var chart_web = {
			chart : {
				renderTo : 'container_web',
				zoomType: 'xy',
			},
			title : {
				text: "WEB端 点击,曝光,访问人数"
			},
			rangeSelector: {
				inputEnabled: false,
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
			series : []
		};


function get_data() {
	document.getElementById("loading").style.display="block";
	document.getElementById("container_web").innerHTML =  "";


	$.ajax({
	    type: 'POST',
	    url: '/get-statwebdata',
	    async: false,
	    success : function(text){
		      if(!text || text.length <= 0) return;
		      currentData = eval('(' + text + ')');
		      var series = [
				{ name : 'name', data : [], type: 'spline'}, 
				{yAxis: 1,name : 'name', data : [], type: 'spline'}, 
				{yAxis: 2,name : 'name', data : [], type: 'spline'}, 
		      ]	
		      series[0].name = "访问人数" 
		      series[1].name = "曝光量"
		      series[2].name = "点击量" 
			
		      var date = new Array(currentData.length);
			var j=0;
		      for(var i = 0; i < currentData.length - 1;  ++i, ++j) {
			  var mtime = currentData[i]["date"] + 8*1000*60*60
         		  series[0].data[j] = [mtime, currentData[i]["uv"] ]
         		  series[1].data[j] = [mtime, currentData[i]["feed_sum"] ]
         		  series[2].data[j] = [mtime, currentData[i]["click_sum"] ]
         		  //series[3].data[j] = currentData[i]["reply_sum"]

		      }
		//alert(series[0].data)	
		      chart_web.yAxis = YA 
		      chart_web.series.push(series[0]);
		      chart_web.series.push(series[1]);
		      chart_web.series.push(series[2]);
			//alert(chart_web)
      		      var chart1 = new Highcharts.StockChart(chart_web);
		document.getElementById("loading").style.display="none";
	    },// sucess
	    error : function(){
	      alert('chart_web 加载出错, 请重新刷新页面');
	    }

	  });//ajax
    }





    $(document).ready(get_data() );//ready

</script>


 












</html>

