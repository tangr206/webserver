<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<div id="daddy">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>新鲜事数据平台 </title>

<!--tangr highchart-->

<script src="/jquery.js"></script>
<script src="/jquery.scrollto.js"></script>
<!--script src="/jquery.min.js"></script-->
<script src="/Highcharts-2.2.5/js/highcharts.js"></script>
<!-- Additional files for the Highslide popup effect -->
<script type="text/javascript" src="/highslide-full.min.js"></script>
<script type="text/javascript" src="/highslide.config.js" charset="utf-8"></script>
<link rel="stylesheet" type="text/css" href="/highslide.css"/> 
<!--script type="text/javascript" src="http://www.highcharts.com/highslide/highslide-full.min.js"></script>
<script type="text/javascript" src="http://www.highcharts.com/highslide/highslide.config.js" charset="utf-8"></script>
<link rel="stylesheet" type="text/css" href="http://www.highcharts.com/highslide/highslide.css" /-->
<link rel="stylesheet" href="/css/date_input.css" type="text/css"></link>
	<!--header-->
	<div class="headerbox" style="background-color:#28004D">
		<div class="header">
			<h1 class="logobox"><img src="logo.png" alt="人人网数据平台" height="42" width="202"></h1>
			<h2 class="page-title"><a href="/stat-detail" style= " font-family: 'Open Sans',Arial,Helvetica,sans-serif;   color: #FFFFFF;    font-size: 20px;    padding: 5px 10px;    text-shadow: 0 3px 0 #0000FF, 1px 2px 2px #AAAAAA;">新鲜事数据平台</a></h2>
			</div>
		</div>
	</div>
	<!-- end -->

<script type="text/javascript">

		  
	var qushi = 0;
	var stypeDesc = new Array();
	function clone(myObj){
	  if(typeof(myObj) != 'object') return myObj;
	  if(myObj == null) return myObj;
	  
	  var myNewObj = new Object();
	  
	  for(var i in myObj)
	     myNewObj[i] = clone(myObj[i]);
	  
	  return myNewObj;
	}	

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
	      alert('Get Stype Desc 加载出错,请重新刷新页面');
	    }
	  });
	}	
	
    	function goto(id, k) {
        	$("#" + id).ScrollTo(1000 + 500*k);
   	}


	function getYesterday(time){    
	    var date = new Date(time)  
	    var yesterday_milliseconds=date.getTime()-1000*60*60*24;       
	    var yesterday = new Date();       
	        yesterday.setTime(yesterday_milliseconds);       
	        
	    var strYear = yesterday.getFullYear();    
	    var strDay = yesterday.getDate();    
	    var strMonth = yesterday.getMonth()+1;  
	    if(strMonth<10)    
	    {    
	        strMonth="0"+strMonth;    
	    }    
	    if(strDay<10)    
	    {    
	        strDay="0"+strDay;    
	    }    
	    datastr = strYear+"-"+strMonth+"-"+strDay;  
	    return datastr;  
	  } 
	
	  
	  function lookPro(obj){
        	ob=eval(obj);
        	var Property="";
        	for(var i in ob){
        		Property+= i +"  |  </br>";
        		document.getElementById("myp").innerHTML=Property;
        	}
          }

  	function Abs(x) {
		return x>0?x:-x;
	}

	function mysort(A, B) {
		return Abs(B.data0 - B.data1) - Abs(A.data0 - A.data1);
	}// smaller ....
	
	var serdis = [
			{name : "", data : []}, 
			{name : "", data : []}, 
			{name : "差值", data : []}
	 ]		
	var catedis = [];

	function getTop(qushi, data) {
		serdis[0].data = []
		serdis[1].data = []
		serdis[2].data = []
		catedis = []
		var Dis = {
			 cate : 0,
			 data0 : 0,
			 data1 : 0,
		}
		var DisVec = []

		for (var i = 0, cnt = 0; i < 10000; ++i) {
			if ( typeof(data[0][i]) == "undefined" ||  typeof(data[1][i]) == "undefined") continue;
			if (qushi * (data[0][i] - data[1][i]) < 0) continue;			
	
			Dis.data0 = data[1][i]//yesterday
			Dis.data1 = data[0][i]
			Dis.cate = i	
			DisVec.push(clone(Dis));
		}
	
		DisVec.sort(mysort);
		//lookPro(DisVec)

		for (var i = 0 ; i < 10 && i < DisVec.length-1; ++i) {
			catedis.push( stypeDesc[DisVec[i].cate] );
			serdis[0].data.push( DisVec[i].data0 )	
			serdis[1].data.push( DisVec[i].data1 )	
			serdis[2].data.push( Abs(DisVec[i].data0-DisVec[i].data1) )	
		}
	}

	// ====================================================================================================
	//  chart style   dis, click, reply, total
	var chart_dispatch = {
            chart: {
                renderTo: 'container_checkout_dispatch',
                type: 'column',
	    	events: {
                            click: function() {
				goto("daddy" , 0)	;
				//document.getElementById("container_checkout_dispatch").style.display="none";
			    }	    
		}
	    },
            title: {
                text: '分发量dispatch 可能的变化原因 (<font color="red">变化大于1万的类型)</font>',
			style: {
				color: 'red',
				fontSize: '20px'
			}
            },
            xAxis: {
		title: {
			text: '类型'
		},
        //        labels: {
	//	    rotation: -45,
        //            formatter: function() {
        //                return this.value; // clean, unformatted number for year
        //            }
        //        }
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
		shared: true,
                crosshairs: true,
            },
	    plotOptions: {
                series: {
                    cursor: 'pointer',
                    point: {
//                        events: {
//                            click: function() {
//		                hs.htmlExpand(null, {
//                                    pageOrigin: {
//                                        x: this.pageX,
//                                        y: this.pageY
//                                    },
//                                    headingText: this.series.name,
//                                    maincontentText: ' 数量: '+ this.y
//                         				+'<br/> 类型:  '+ (stypeDesc[this.category] ? stypeDesc[this.category]: this.category)
//							+ " <br/>日期："+ this.series.name
//                            	});
//                           }
//                        },
                    	marker: {
                        	lineWidth: 1
                    	}
                   }//point
	        }//series
            },
            series: []
        };// var char_taotal

	//!!!!!!!!!!!!!!!!!!
       var chart_total = {
            chart: {
                renderTo: 'container_total',
                type: 'line',
	    },
            title: {
                text: '新鲜事变化总趋势(可点击日期点分类型查看)',
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
                series: {
                    cursor: 'pointer',
		    point: {
                        events: {
                            click: function() {
								
				checkout(this.category, this.series.name);	
//				alert(this.category)
//				lookPro(this.category);			
//                                hs.htmlExpand(null, {
//                                    pageOrigin: {
//                                        x: this.pageX,
//                                        y: this.pageY
//                                    },
//                                    headingText: this.series.name,
//                                    maincontentText:  this.category +':<br/> '+
//                                        this.y +' hits',
//                                   
//                                });
                            }
                        }
                    },
                    marker: {
                        lineWidth: 1
                    }
                }
            },
            series: []
        };// var char_taotal
//==============================================================

</script>



<script type="text/javascript">
	flag = 0;
	var Date2Data = new Object();
	
        var series = [
  		{name : 'name', data : []}, 
  		{name : 'name', data : []}, 
  		{name : 'name', data : []}, 
  		{name : 'name', data : []}, 
  	]	
  

	function get_checkout_data(datetime) {//change the series data
		$.ajax({
		    type: 'POST',
		    url: '/get-stat-data',
		    async: false,
		    data: "date="+datetime,
		    success : function(text){
			      if(!text || text.length <= 0) return;
			      var currentData = eval('(' + text + ')');

			      series[0].name = "发送量" 
			      series[1].name = "点击数"
			      series[2].name = "回复数" 

			      series[0].data[10000] = 0
			      series[1].data[10000] = 0
			      series[2].data[10000] = 0
				
			      for(var i = currentData.length - 1, j = 0; i >= 0;  --i, ++j) {
	        		  //date[j] = currentData[i]["date"]
	         		  stype = currentData[i]["stype"]
				  if (stype >= 10000) continue;
				  series[0].data[stype] = currentData[i]["dispatch"]
	         		  series[1].data[stype] = currentData[i]["click"]
	         		  series[2].data[stype] = currentData[i]["reply"]
			      }
		    },// sucess
		    error : function(){
        	      alert('get_checkout_data : 加载出错, 请重新刷新页面 date:' + time);
        	    }
        
    	  });//ajax
	}//get_checkout_data

	function checkout(time, idname) {
//	        year = Date().getYear();	
//		time =  "2012-"+time
		chart_dispatch.chart.renderTo = 'container_checkout_dispatch'
		//$("#container_detail").ScrollTo(800);
		//$.ScrollTo("#container_detail",800);
  		//goto("container_checkout_click");  
		var time2 = getYesterday(time)	
		var time1 = time
		//Date2Data  ::  date  dispatch,click,reply
		if (idname == "发送量") {
			chart_dispatch.title.text = idname + '[dispatch]' + " 变化幅度 top10"
			qushi = Date2Data[time][0] > Date2Data[time2][0] ? 1 : -1
		}
		else if (idname == "点击数") {
			chart_dispatch.title.text = idname + '[click]' + " 变化幅度 top10"
			qushi = Date2Data[time][1] > Date2Data[time2][1] ? 1 : -1
		}	
		else if (idname == "回复数") {
			chart_dispatch.title.text = idname + '[reply]' + " 变化幅度top10"
			qushi = Date2Data[time][2] > Date2Data[time2][2] ? 1 : -1

		}	
  		//idname = "container_checkout_dispatch"
		document.getElementById("container_checkout_dispatch").style.display="block";
		goto("container_checkout_dispatch", 0); 
		
		var dis = []
		var click = []
		var reply = []

	      	get_checkout_data(time);		

		dis[0] = series[0].data
		click[0] = series[1].data
		reply[0] = series[2].data

		series[0].data = []
		series[1].data = []
		series[2].data = []

	      	get_checkout_data(time2);		
		dis[1] = series[0].data
		click[1] = series[1].data
		reply[1] = series[2].data

		var Dis = {
			 cate : 0,
			 data0 : 0,
			 data1 : 0,
		}
		var DisVec = []

	
		//function getTop(qushi, data, serdis, catedis) {
		if(idname == "发送量") {
		//dispatch
			getTop(qushi, dis);
		}

		if(idname == "点击数") {
			getTop(qushi, click)
		}

		if(idname == "回复数") {
			getTop(qushi, reply)	
		}

		serdis[0].name = time2;
		serdis[1].name = time1;
		if (flag++) {
			chart_dispatch.xAxis.categories = catedis;
			chart_dispatch.series = [] ;
			chart_dispatch.series.push( serdis[0] ) ;
			chart_dispatch.series.push( serdis[1] ) ;
			chart_dispatch.series.push( serdis[2] ) ;

		} else {
			chart_dispatch.xAxis.categories = catedis;
			chart_dispatch.series.push( serdis[0] ) ;
			chart_dispatch.series.push( serdis[1] ) ;
			chart_dispatch.series.push( serdis[2] ) ;

		}

		chart2 = new Highcharts.Chart(chart_dispatch)

	}

$(function () {
 
    $(document).ready(function() {

	$.ajax({
	    type: 'POST',
	    url: '/get-stat-data',
	    async: false,
	    data: "date=0",
	    success : function(text){
		      if(!text || text.length <= 0) return;
		      currentData = eval('(' + text + ')');
	
		      var series = [
				{name : 'name', data : []}, 
				{name : 'name', data : []}, 
				{name : 'name', data : []}, 
		      ]	
		      series[0].name = "发送量" 
		      series[1].name = "点击数"
		      series[2].name = "回复数" 
			
		      var date = new Array(currentData.length);
		      for(var i = currentData.length - 1, j = 0; i >= 0;  --i, ++j) {
			  date[j] = currentData[i]["date"]
         		  series[0].data[j] = currentData[i]["dispatch"]
         		  series[1].data[j] = currentData[i]["click"]
         		  series[2].data[j] = currentData[i]["reply"]

        		  Date2Data[ date[j] ] = [ series[0].data[j], series[1].data[j], series[2].data[j] ]
		      }

		      chart_total.series.push(series[0]);
		      chart_total.series.push(series[1]);
		      chart_total.series.push(series[2]);
		      chart_total.xAxis.categories = date;

		      chart1 = new Highcharts.Chart(chart_total)
//
//		      chartArray = new Array(chart_checkout, chart_checkout, chart_checkout)
//        	      chart2 = new Highcharts.Chart(chart_checkout)
//        	      chart3 = new Highcharts.Chart(chartArray[0])
//        	      chart4 = new Highcharts.Chart(chartArray[0])
//
	    },// sucess
	    error : function(){
	      alert('chart_total 加载出错, 请重新刷新页面');
	    }

	  });//ajax
	  getStypeDesc();
    });//ready
    
// window.onload = function() {
//	$("#cover").mouseover( function(){
//		document.getElementById("button").style.display="block";
//		document.getElementById("cover").style.display="none";
//		
//	});
//	$("#button").mouseout( function(){
//		document.getElementById("cover").style.display="block";
//		document.getElementById("button").style.display="none";
//		
//	});
//       }	
});
</script>

<!--tangr highchart-->

</head>
    <style>
    a:link,a:visited {font-size:30pxcolor: #ff0000; text-decoration:none;}
    a:hover {font-size:30px;color: #3c5a9a; text-decoration:underline;}
    </style>

<body style="background-color:#FFFFFF">
<SCRIPT type="text/JavaScript">
pos = 15;
TO = null;

</script>


<div>
<span id = "button" style="height:20px; position:relative;margion: 5px 5px 15px 5px;"> 
  <table id="option"  border="0" class="t1" >
    <tr>
      <th align="left" style="width:1000px">
      </th>
      <th align="left">
	<input type=button onclick="window.location.href='/stat-detail'" value="查看详细信息"  >
      </th>
      <th align="left" >
	<input type=button onclick="window.location.href='/stat-stype'" value="查看各类型的趋势" >
      </th>
      <th align="right">
	<input type=button onclick="window.location.href='/stat-ABDebug'" value="A/B Debug"  >
      </th>
    </tr>
  </table>
</span>
</div>

<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>


<div id="container_father" style="background-color:silver; margin: 0px 15px 0px 15px">
	<div id="container_total" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px"></div>
	<div id="container_checkout_click" style="min-width: 400px; height: 500px; background-color:white ; margin: 10px 5px 10px 10px ; display:none"></div>
	<div id="container_checkout_reply" style="min-width: 400px; min-height: 570px;  background-color:white ; margin: 10px 5px 10px 5px; display:none"></div>
	<div id="container_checkout_dispatch" style="min-width: 400px; min-height: 570px; background-color:white ; margin: 10px 5px 10px 5px ; display:none"></div>
</div>
<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>


<div id="myp"> </div>
</body>
<div class="copyright">
<center>feed.renren   &copy;2012</center>
</div>

</div>
</html>
