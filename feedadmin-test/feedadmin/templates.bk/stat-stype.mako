<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>
<script type="text/javascript" src="/jquery.min.js"></script>
<script type="text/javascript" src="/old-feed-list.js"></script>
<script type="text/javascript" src="/jquery.date_input.js"></script>
<script src="/Highcharts-2.2.5/js/highcharts.js"></script>
<script type="text/javascript">$($.date_input.initialize);</script>
<link rel="stylesheet" href="/css/date_input.css" type="text/css"></link>
<style type="text/css">
a{ text-decoration:none;}
a:hover{ text-decoration:underline;}
</style>
<title>stat-stype</title>

	<!--header-->
	<div class="headerbox" style="background-color:#28004D">
		<div class="header">
			<h1 class="logobox"><img src="logo.png" alt="人人网数据平台" height="42" width="202"></h1>
			<h2 class="page-title"><a href="/stat-detail" style= " font-family: 'Open Sans',Arial,Helvetica,sans-serif;   color: #FFFFFF;    font-size: 20px;    padding: 5px 10px;    text-shadow: 0 3px 0 #0000FF, 1px 2px 2px #AAAAAA;">  新鲜事数据平台-各类型趋势</a></h2>
			</div>
		</div>
	</div>
	<!-- end -->


<script type="text/javascript">
var allIds = new Array();
var currentData = new Array();

var stypeDesc = new Array();
function getStypeDesc() {
  $.ajax({
    type: 'POST',
    url: '/get-stype-list',
    async: false,
    success : function(text){
      var data = eval('(' + text + ')');
      for(var i=0; i< data.length; ++i) {
        stypeDesc[data[i]["stype"].toString()] = data[i]["description"];
      }
    },
    error : function(){
      alert('getStypeDesc 加载出错,请重新刷新页面');
    }
  });
}

       var chart = {
            chart: {
                renderTo: 'container_stype',
                type: 'line',
	    },
            title: {
                text: '新',
			style: {
				color: 'blue',
				fontSize: '20px'
			}
            },
            xAxis: {
		title: {
			text: '日期'
		},
                labels: {
		    rotation: -45,
                    formatter: function() {
                        //return this.value // clean, unformatted number for year
                        return this.value.slice(5,10); // clean, unformatted number for year
                    }
                }
            },
            yAxis: {
                title: {
                    text: '数量'
                },
                labels: {
                    formatter: function() {
                        return this.value / 10000 + 'w';
                   }
                }
            },
            tooltip: {                
		//shared: true,
                crosshairs: true,
                formatter: function() {
                    return this.series.name +'  <b>'+
                        this.y +'</b><br/> date:  '+ this.x //+ "   index:" + series.data[this.point.x - 1];
                }
            },
	    plotOptions: {
            },
            series: []
        };// var char_taotal



var name = [ "发送量","发送用户数", "取新鲜事的用户数", "回复数", "产生回复的用户数", "点击量", "产生点击的用户数"]

$("select[name=stype]").live('change',	function(){
  if( $("select[name=stype]").val() == "选择类型") {
	document.getElementById("container_stype").style.display="none";
  	return;
  }
  document.getElementById("container_stype").style.display="block";

  $.ajax({
    type: 'POST',
    url: '/stat-list',
    data: "stype=" + $("select[name=stype]").val() ,
    success : function(text){
	  if(!text || text.length <= 0) {
		 return;
	  }
	  currentData = eval('(' + text + ')');

		      var series = [
				{name : 'name', data : []}, 
				{name : 'name', data : []}, 
				{name : 'name', data : []}, 
				{name : 'name', data : []}, 
				{name : 'name', data : []}, 
				{name : 'name', data : []}, 
				{name : 'name', data : []}, 
		      ]	

		for (var i=0; i < name.length; ++i) {
			series[i].name = name[i]
		}	

		var date = new Array(currentData.length);
		for(var i = currentData.length - 1, j = 0; i >= 0;  --i, ++j) {
			date[j] = currentData[i]["date"]
			series[0].data[j] = currentData[i]["dispatch"] 
			series[1].data[j] =  currentData[i]["dispatch_user"]
			series[2].data[j] =  currentData[i]["view_user"]
			series[3].data[j] =  currentData[i]["reply"] 
			series[4].data[j] =  currentData[i]["reply_user"] 
			series[5].data[j] =  currentData[i]["click"]
			series[6].data[j] =  currentData[i]["click_user"]
		}
		

		      chart.title.text = stypeDesc[$("select[name=stype]").val()] + " [" +$("select[name=stype]").val() + "]的变化曲线"
		      chart.series = []
		      chart.series.push(series[0]);
		      //chart.series.push(series[1]);
		      //chart.series.push(series[2]);
		      chart.series.push(series[3]);
		      //chart.series.push(series[4]);
		      chart.series.push(series[5]);
		      chart.xAxis.categories = date;

		      chart1 = new Highcharts.Chart(chart)

    },
    error : function(){
      alert('select stype  加载出错, 请重新刷新页面');
    }
  });
});



$(document).ready(function() {
	document.getElementById("container_stype").style.display="none";
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
	      allIds.sort(function(a, b){ return a-b;});
	      var html = '<option value="' + 0 + '">' + '选择类型</option>';
	      for(var i = 0; i < allIds.length; ++i) {
	        html += '<option value="' + allIds[i].toString() + '">' + allIds[i].toString() + '</option>';
	      }
	 
	      $("select[name=stype]").html(html);
	    },
	    error : function(){
	      alert('/ready  加载出错, 请重新刷新页面');
	    }
	  });
	
	
	getStypeDesc();

}); // ready 




</script>

</head>

<body>
<div> <!-- style="position:absolute;left:50%;margin-left:-600px;width:1200px;" -->
<div>
  <table id="option" width="1200" border="1" class="t1">
    <tr>
      <th align="left">
        stype:&nbsp;<select name="stype"></select>&nbsp;&nbsp;
        <!-- origin_url:&nbsp;<select name="origin_url"></select>&nbsp;&nbsp; -->
      </th>
    </tr>
  </table>
</div>
<div> <!-- style="position:absolute;left:50%;margin-left:-600px;width:1200px;" -->


<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>
<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>
<div id="container_father" style="background-color:silver; margin: 0px 15px 0px 15px">
	<div id="container_stype" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px"></div>
</div>
<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>

<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="97%" color=#987cb9 SIZE=1>
</body>

</html>

