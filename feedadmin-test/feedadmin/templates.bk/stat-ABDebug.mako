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
<link rel="stylesheet" href="/css/date_input2.css" type="text/css"></link>
<style type="text/css">
a{ text-decoration:none;}
a:hover{ text-decoration:underline;}
</style>
<title>stat-ABDebug</title>

	<!--header-->
	<div class="headerbox" style="background-color:#28004D">
		<div class="header">
			<h1 class="logobox"><img src="logo.png" alt="人人网数据平台" height="42" width="202"></h1>
			<h2 class="page-title"><a href="/stat-detail" style= " font-family: 'Open Sans',Arial,Helvetica,sans-serif;   color: #FFFFFF;    font-size: 20px;    padding: 5px 10px;    text-shadow: 0 3px 0 #0000FF, 1px 2px 2px #AAAAAA;">  新鲜事数据平台-ABDebug</a></h2>
			</div>
		</div>
	</div>
	<!-- end -->


<script type="text/javascript">
	
	var AVE_click = new Array()
	var AVE_reply = new Array()
	var AVE_dispatch = new Array()
	var AVE_view = new Array()
	
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

	//---------------------------	
       	var chart_AB_click = {
            chart: {
                renderTo: 'container_click_userid',
                type: 'line',
	    },
            title: {
                text: '特定尾号与平均值的变化趋势',
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
                        return this.value ;
                   }
                }
            },
            tooltip: {                
		//shared: true,
                crosshairs: true,
                formatter: function() {
			if(this.series.name!="average") {
                    		return this.series.name +'  <b>'+ this.y + '</b><br/>与平均比较:<b>' + ((this.y - AVE_click[this.point.x]))
					+'</b><br/> date:  '+ this.x

			}
                    return this.series.name +'  <b>'+
                        this.y +'</b><br/> date:  '+ this.x //+ "   index:" + series.data[this.point.x - 1];
                }
            },
	    plotOptions: {
            },
            series: []
        };// var char_taotal

	//---------------------------	
       	var chart_AB_reply = {
            chart: {
                renderTo: 'container_reply_userid',
                type: 'line',
	    },
            title: {
                text: '特定尾号与平均值的变化趋势',
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
                        return this.value ;
                   }
                }
            },
            tooltip: {                
		//shared: true,
                crosshairs: true,
                formatter: function() {
			if(this.series.name!="average") {
                    		return this.series.name +'  <b>'+ this.y + '</b><br/>与平均比较:<b>' + ((this.y - AVE_reply[this.point.x]))
					+'</b><br/> date:  '+ this.x
			}
                    return this.series.name +'  <b>'+
                        this.y +'</b><br/> date:  '+ this.x //+ "   index:" + series.data[this.point.x - 1];
                }
            },
	    plotOptions: {
            },
            series: []
        };// var char_taotal

	//---------------------------	
       	var chart_AB_dispatch = {
            chart: {
                renderTo: 'container_dispatch_userid',
                type: 'line',
	    },
            title: {
                text: '特定尾号与平均值的变化趋势',
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
                        return this.value ;
                   }
                }
            },
            tooltip: {                
		//shared: true,
                crosshairs: true,
                formatter: function() {
			if(this.series.name!="average") {
                    		return this.series.name +'  <b>'+ this.y + '</b><br/>与平均比较:<b>' + ((this.y - AVE_dispatch[this.point.x]))
					+'</b><br/> date:  '+ this.x
			}
                    return this.series.name +'  <b>'+
                        this.y +'</b><br/> date:  '+ this.x //+ "   index:" + series.data[this.point.x - 1];
                }
            },
	    plotOptions: {
            },
            series: []
        };// var char_taotal


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

	var tmp_click = new Array();//date-->total_click
	var tmp_reply = new Array();
	var tmp_dispatch = new Array();
	var tmp_date = new Array();

</script>

</head>

<body>


<script type="text/javascript">

	function getData() {
	  $.ajax({
	    type: 'POST',
	    url: '/stat-ABDebug-data',
	    success : function(text) {
		if(!text || text.length <= 0) {
			 return;
		}
		currentData = eval('(' + text + ')');
	
		var meta = { name : 'name', data : [] } 
	
		for(var i=0; i<100; ++i) ABData[i] = [];
			
		for(var i = 0; i < currentData.length;  ++i) {

			now = currentData[i]
			if (i%100 ==0)  tmp_date.push(now["date"])

			meta.name = now["date"]
			meta.data = []
			meta.data.push(now["click"])
			meta.data.push(now["reply"])
			meta.data.push(now["dispatch"])
			uid = now["userid"]
			ABData[uid][ now["date"] ] = clone(meta)

			if (!tmp_click[now["date"]])	tmp_click[now["date"]] = 0
			tmp_click[now["date"]] += now["click"]

			if (!tmp_reply[now["date"]])	tmp_reply[now["date"]] = 0
			tmp_reply[now["date"]] += now["reply"]

			if (!tmp_dispatch[now["date"]])	tmp_dispatch[now["date"]] = 0
			tmp_dispatch[now["date"]] += now["dispatch"]
			
		}
		showChartClickUserid()
		showChartReplyUserid()
		showChartDispatchUserid()
	    },
	    error : function(){
	      alert('getData  加载出错, 请重新刷新页面');
	    }
	  });//ajax

	}//getData



//=============================================================================================

	function showChartClickUserid() {
		var meta = { name:0, data:[] }
		var series= [
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
		]

		var marked = []
		for (var i=0, j=1; i<100; ++i ) 
			if(map[i]==1) {
				marked.push(i)
				alert(j)
				series[j].name = i+" 尾号:";
				series[j].data = []
				j++;
		}

		for (var i=0; i<tmp_date.length; ++i) {
			var sum = 0;
			var day = tmp_date[i]
			for(var j=0; j<marked.length; ++j){
				if (! ABData[marked[j]][day]) {
					alert("wrong   uid:"+marked[j]+"  day:"+ day)
					series[j+1].data[i] = 0				
				} else {
					var click = ABData[ marked[j] ][ day ].data[0];
					sum+=click;
					series[j+1].data[i] = click
				}				
			} 
			var ave =  ( tmp_click[day] - sum )/(100-marked.length) 
			AVE_click.push(ave) 
			series[0].data[i] = ave;
		}

		chart_AB_click.title.text ='特定尾号与平均值(去掉选定尾号)的变化趋势 click'  
		chart_AB_click.series = []
		for(var i=0; i<=marked.length; ++i) 
			chart_AB_click.series.push(series[i]);
		chart_AB_click.xAxis.categories = tmp_date
		chart1 = new Highcharts.Chart(chart_AB_click)
	}


	function showChartReplyUserid() {
		var meta = { name:0, data:[] }
		var series= [
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
		]

		var marked = []
		for (var i=0, j=1; i<100; ++i ) 
			if(map[i]==1) {
				marked.push(i)
				alert(j)
				series[j].name = i+" 尾号:";
				series[j].data = []
				j++;
		}

		for (var i=0; i<tmp_date.length; ++i) {
			var sum = 0;
			var day = tmp_date[i]
			for(var j=0; j<marked.length; ++j){
				if (! ABData[marked[j]][day]) {
					alert("wrong   uid:"+marked[j]+"  day:"+ day)
					series[j+1].data[i] = 0				
				} else {
					var reply = ABData[ marked[j] ][ day ].data[1];
					sum+=reply;
					series[j+1].data[i] = reply
				}				
			} 
			var ave =  ( tmp_reply[day] - sum )/(100-marked.length) 
			AVE_reply.push(ave) 
			series[0].data[i] = ave;
		}

		chart_AB_reply.title.text ='特定尾号与平均值(去掉选定尾号)的变化趋势'  
		chart_AB_reply.series = []
		for(var i=0; i<=marked.length; ++i) 
			chart_AB_reply.series.push(series[i]);
		chart_AB_reply.xAxis.categories = tmp_date
		chart1 = new Highcharts.Chart(chart_AB_reply)
	}


	function showChartDispatchUserid() {
		var meta = { name:0, data:[] }
		var series= [
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
			{ name:"average", data:[] },
		]

		var marked = []
		for (var i=0, j=1; i<100; ++i ) 
			if(map[i]==1) {
				marked.push(i)
				series[j].name = i+" 尾号:";
				series[j].data = []
				j++;
		}

		for (var i=0; i<tmp_date.length; ++i) {
			var sum = 0;
			var day = tmp_date[i]
			for(var j=0; j<marked.length; ++j){
				if (! ABData[marked[j]][day]) {
					alert("wrong   uid:"+marked[j]+"  day:"+ day)
					series[j+1].data[i] = 0				
				} else {
					var dispatch = ABData[ marked[j] ][ day ].data[2];
					sum+=dispatch;
					series[j+1].data[i] = dispatch
				}				
			} 
			var ave =  ( tmp_dispatch[day] - sum )/(100-marked.length) 
			AVE_dispatch.push(ave) 
			series[0].data[i] = ave;
		}

		chart_AB_dispatch.title.text ='特定尾号与平均值(去掉选定尾号)的变化趋势'  
		chart_AB_dispatch.series = []
		for(var i=0; i<=marked.length; ++i) 
			chart_AB_dispatch.series.push(series[i]);
		chart_AB_dispatch.xAxis.categories = tmp_date
		chart1 = new Highcharts.Chart(chart_AB_dispatch)
	}

// ===========================================================================================================


	$(document).ready( function() {
	      var html = '';
	      var k = 0;
	      for(var i = 0; i < 5; ++i) {
		html += '<tr>'
		for(var j = 0; j < 20; ++j) {
	        	html += '<th>' + k + '</th>';
			k++;
	      	}
		html += '</tr>'
	      }
		document.getElementById('op').innerHTML = html	
		getStypeDesc();
		getData();
	}); // ready

	function  setColor() {
		var index = (this.innerHTML)
		if (map[index] == 1) {
			this.style.background = "white"
			map[index] = 0;
		} else {
			this.style.background = "silver"
			map[index] = 1;
		}
		showChartClickUserid()
		showChartReplyUserid()
		showChartDispatchUserid()
	}
	
	window.onload = function() {
	    var table = document.getElementById('op');
	    for (var i = 0; i < table.rows.length; i++) {
	        var row = table.rows[i];
	        for (var j = 0; j < row.cells.length; j++) {
	            row.cells[j].onclick = setColor;
	            //row.cells[j].onmouseover = setColor;
	            //row.cells[j].onmouseout = setColor2;
	        }
	    }
	} 
	
	function func1() {
	 if(document.getElementById("container_click_userid").style.display=="none")
		document.getElementById("container_click_userid").style.display="block";
	 else
		document.getElementById("container_click_userid").style.display="none";
	}
	function func2() {
	 if(document.getElementById("container_reply_userid").style.display=="none")
		document.getElementById("container_reply_userid").style.display="block";
	 else
		document.getElementById("container_reply_userid").style.display="none";
	}
	function func3() {
	 if(document.getElementById("container_dispatch_userid").style.display=="none")
		document.getElementById("container_dispatch_userid").style.display="block";
	 else
		document.getElementById("container_dispatch_userid").style.display="none";
	}

</script>
<div >
<span style="align:center">
<center>dddd</center>
</span>
<span>
  <table align="center" id="op" border="1" width="1000px" >
  </table>
</span>
</div>
<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>



<div id="columns">
    <li class="widget color-blue">
      <div class="widget-head" onclick="func1()">
        <center><h3>点击量</h3></center> 
      </div>
      <div class="widget-content">
	<div id="container_click_userid" style="display:none; min-width: 1275px; height: 500px; margin: 5px 5px 5px 5px"></div>
      </div>
    </li>
<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>

     <li class="widget color-blue">
      <div class="widget-head" onclick="func2()">
        <center><h3>回复量</h3></center> 
      </div>
      <div class="widget-content">
	<div id="container_reply_userid" style="display:none; min-width: 1275px; height: 500px; margin: 5px 5px 5px 5px"></div>
      </div>
    </li>
<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>

     <li class="widget color-blue">
      <div class="widget-head" onclick="func3()">
       <center> <h3>分发量</h3></center> 
      </div>
      <div class="widget-content">
	<div id="container_dispatch_userid" style="display:none; min-width: 1275px; height: 500px; margin: 5px 5px 5px 5px"></div>
      </div>
    </li>
<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>

</div>


<!--div id="container_father" style="background-color:silver; margin: 0px 15px 0px 15px;display:block">
	<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>
	<div id="container_click_userid" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px"></div>
	<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>
	<div id="container_reply_userid" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px"></div>
	<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>
	<div id="container_dispatch_userid" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px"></div>
	<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>
	<div id="container_view_userid" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px"></div>
	<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>
</div-->



</body>

</html>

