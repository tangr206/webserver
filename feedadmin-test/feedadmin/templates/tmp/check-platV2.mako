<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>
<title>content</title>
<script type="text/javascript" src="/jquery.js"></script>
<script src="/Highcharts-2.2.5/js/highcharts.js"></script>
<!-- Additional files for the Highslide popup effect -->
<script type="text/javascript" src="/highslide-full.min.js"></script>
<script type="text/javascript" src="/highslide.config.js" charset="utf-8"></script>
<link rel="stylesheet" type="text/css" href="/highslide.css"/> 


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
  <li><a href="#" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>

  <li><a href="stat" target="_blank">实验平台</a>
    <ul id="subNews" class="second-menu">
      <li><a href="experi-signin" target="_self" style="z-index:1000;">实验登记</a></li>
      <li><a href="experi-select" target="_self" style="z-index:1000;">选择实验查看</a></li>
      <li><a href="http://feed.d.xiaonei.com/stat-ABDebug" target="_self" style="z-index:1000;">选择尾号查看</a></li>
    </ul>
  </li>
  <li><a href="http://feed.d.xiaonei.com/stat-detail" target="_blank">详细信息</a>
    <ul id="subNews" class="second-menu">
      <li><a href="check-plat" target="_self" style="z-index:1000;">选择平台查看</a></li>
      <li><a href="check-stype" target="_self" style="z-index:1000;">选择类型查看</a></li>
    </ul>
  </li>
  <li><a href="http://feed.d.xiaonei.com/quota" target="_blank">配额系统</a>
    <ul id="subNews" class="second-menu">
      <li><a href="#" target="_self" style="z-index:1000;">查看</a></li>
    </ul>
  </li>
</ul>
</div>

<!--div id="wrapper">
    <ul id="nav">
        <li><a href="experiment-rout">实验平台</a></li>
        <li><a href="detail-rout">详细信息</a></li>
        <li><a href="www.feed.d.xiaonei.com">feed</a></li>
        <li><a href="http://feed.d.xiaonei.com/stat-ABDebug">AB</a></li>
    </ul>
</div-->

<h1> 按平台查看 </h1>

</head>

<script type="text/javascript">



	var chart_all = {
            chart: {
                renderTo: 'container_viewa',
               	zoomType: 'xy',
                type: 'column'
            },
            title: {
                text: '各个平台的登录人数'
            },
            xAxis: {
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'uv'
                },

            },
            tooltip: {
                formatter: function() {
                    return '<b>'+ this.x +'</b><br/>'+
                        this.series.name +': '+ this.y +'<br/>'+
                        'Total: '+ this.point.stackTotal;
                }
            },
            plotOptions: {
                column: {
                    stacking: 'normal',
                    dataLabels: {
                        enabled: true,
                        color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white'
                    }
                }
            },
            series: []
        };



function div(number1,number2){
       var num1 = Math.round(number1);
       var num2 = Math.round(number2);
       var result = num1/num2;
       if(result >=0){
           result = Math.floor(result);
       }else{
           result = Math.ceil(result);
       }
       return result;
    }


function getViewDataByPlate( view) {



}


function show_fun(id, flag) {
	id = "container_" + id
	alert(id)
	if (flag) {
		document.getElementById(id).style.display="block";
	} else {
		document.getElementById(id).style.display="none";
	}
}

function go_fun() {
	var input = document.getElementsByName("c2");
	alert(input[0].checked)

}

$(document).ready(function() {
  $.ajax({
    type: 'POST',
    url: '/view-day-list',
    async: false,
    data:"date=0",
    success : function(text){
      if(!text || text.length <= 0) return;
      currentData = eval('(' + text + ')');

	      var html = '<option value="' + 0 + '">' + '选择日期</option>';
	      var set = {}
	      for(var i = 0; i < currentData.length-1; ++i) {
		dd = currentData[i]["date"]
		if ( !set[dd] ) {
	        	html += '<option value="' + currentData[i]["date"].toString() + '">' + currentData[i]["date"].toString() + '</option>';
			set[dd] = true;
		}
	      }
	      $("select[name=st_date]").html(html);
	      $("select[name=ed_date]").html(html);

	       html = '';
		for(var i = 0; i < 24; ++i) {
	        	html += '<option value="' + i.toString() + '">' + i.toString() + '</option>';
		}
	      $("select[name=st_hour]").html(html);
	      $("select[name=ed_hour]").html(html);


		      var series = [
				{name : 'web', data : []}, 
				{name : '手机', data : []}, 
				{name : '实时化', data : []}, 
				{name : '开放平台', data : []}, 
				{name : 'Timeline', data : []}, 
				{name : 'name', data : []}, 
				{name : 'name', data : []}, 
		      ]	

		var date = new Array(currentData.length);
		for(var i = 0, j = 0; i < currentData.length -1 ;  ++i) {
			if (i%5 ==0 ) j = 0
			else j++
			index = div(i, 5)
			date[index] = currentData[i]["date"]
			series[j].data[index] = currentData[i]["uv"] 
		}
		
		      chart_all.series = []
		      chart_all.series.push(series[0]);
		      chart_all.series.push(series[1]);
		      chart_all.series.push(series[2]);
		      chart_all.series.push(series[3]);
		      chart_all.series.push(series[4]);
		      chart_all.xAxis.categories = date;

		      chart1 = new Highcharts.Chart(chart_all)


      //$("#data").append(html);
    },
    error : function(){
      alert('ready 加载出错');
    }
  });
});
</script>





<body>

<div id="content" >
	<div id="right">
		<fieldset>
		<legend> ---&nbspCondition&nbsp--- </legend>

<form method="get" name="show_checkbox"  style="margin: 10px 10px 10px 10px">
  <div class="t1">时间</div>
  起始:
  <select id="st_date" name="st_date">
  </select>
  <select id="st_hour" name="st_hour">
  </select>
  </br>
  </br>
  终止:
  <select id="ed_date" name="ed_date">
  </select>
  <select id="ed_hour" name="ed_hour">
    <option value="23" selected="selected">23</option>
  </select>
--------------------------------
  <br>
  <!--input name="day" value="0" id="hour" checked="checked" type="radio">
  <label for="hour">按小时</label>
  <input name="day" value="1" id="day" type="radio"-->
  <label for="day">按天<br>(点击各节点可按小时查看)</label>
  
--------------------------------
  
<div class="t1">类型</div>
  <input value="1" name="c1" id="viewa" type="checkbox" checked="checked" onclick="show_fun(id, checked)">
  <label for="viewa">All</label>
  <br>
  <input value="1" name="c1" id="view0" type="checkbox"  onclick="show_fun(id, checked)">
  <label for="view0">Web</label>
  <br>
  <input value="1" name="c1" id="view2" type="checkbox"  onclick="show_fun(id, checked)">
  <label for="view2">手机</label>
  <br>
  <input value="1" name="c1" id="view3" type="checkbox"  onclick="show_fun(id, checked)">
  <label for="view3">实时化</label>
  <br>
  <input value="1" name="c1" id="view4" type="checkbox"  onclick="show_fun(id, checked)">
  <label for="view4">开放平台</label>
  <br>
  <input value="1" name="c1" id="view6" type="checkbox"  onclick="show_fun(id, checked)">
  <label for="view0">Timeline</label>
--------------------------------
  
<div class="t1">查看项</div>
  <input value="1" name="c2" id="uv" type="checkbox" checked="checked">
  <label for="uv">访问人数(UV)</label>
  <br>
  <input value="1" name="c2" id="rv" type="checkbox">
  <label for="rv">取新鲜事操作(RV)</label>
  <br>
  <input value="1" name="c2" id="pv" type="checkbox">
  <label for="pv">曝光量(PV)</label>
  <br>
  <input value="1" name="c2" id="session_cnt" type="checkbox">
  <label for="session_cnt">活跃次数</label>
  <input value="1" name="c2" id="session_sum" type="checkbox">
  <label for="session_sum">活跃时长</label>
  <br>
  
==================
  <div class="t1"><input value="搞定" style="float:right" type="submit" onclick="go_fun()"></div>
</form>
		</fieldset>
	</div>

<!--- -------------------------------------------- -->
	<div id="left">
		<div id="div_viewa">
			<fieldset>
			<legend>ALL</legend>
	<div id="container_viewa" style="min-width: 400px; height: 400px; background-color:white ; margin: 10px 5px 10px 10px ; "></div>
			</fieldset>
		</div>
		<div id="div_viwe0">
			<fieldset>
			<legend>WEB</legend>
	<div id="container_view0" style="min-width: 400px; height: 500px; background-color:white ; margin: 10px 5px 10px 10px ; display:none; "></div>
			</fieldset>
		</div>
		<div id="div_viwe2">
			<fieldset>
			<legend>手机</legend>
	<div id="container_view2" style="min-width: 400px; height: 500px; background-color:white ; margin: 10px 5px 10px 10px ; display:none; "></div>
			</fieldset>
		</div>
		<div id="div_viwe3">
			<fieldset>
			<legend>实时化</legend>
	<div id="container_view3" style="min-width: 400px; height: 500px; background-color:white ; margin: 10px 5px 10px 10px ; display:none; "></div>
			</fieldset>
		</div>
		<div id="div_viwe4">
			<fieldset>
			<legend>开放平台</legend>
	<div id="container_view4" style="min-width: 400px; height: 500px; background-color:white ; margin: 10px 5px 10px 10px ; display:none; "></div>
			</fieldset>
		</div>
		<div id="div_viwe6">
			<fieldset>
			<legend>TimeLine</legend>
	<div id="container_view6" style="min-width: 400px; height: 500px; background-color:white ; margin: 10px 5px 10px 10px ; display:none; "></div>
			</fieldset>
		</div>
	</div>
</div>
</body>
</html>

