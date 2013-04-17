<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<div id="daddy">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>新鲜事配额系统 </title>

<script src="/jquery.js"></script>
<script src="/jquery.scrollto.js"></script>
<!--script src="/jquery.min.js"></script-->
<script src="/Highcharts-2.2.5/js/highcharts.js"></script>
<!-- Additional files for the Highslide popup effect -->
<script type="text/javascript" src="/highslide-full.min.js"></script>
<script type="text/javascript" src="/highslide.config.js" charset="utf-8"></script>
<script type="text/javascript" src="/jquery.date_input.js"></script>
<script type="text/javascript">$($.date_input.initialize);</script>
<link rel="stylesheet" type="text/css" href="/highslide.css"/> 
<link rel="stylesheet" href="/css/date_input.css" type="text/css"></link>
	<!--header-->
	<div class="headerbox" style="background-color:#28004D">
		<div class="header">
			<h1 class="logobox"><img src="logo.png" alt="人人网数据平台" height="42" width="202"></h1>
			<h2 class="page-title"><a href="/stat-detail" style= " font-family: 'Open Sans',Arial,Helvetica,sans-serif;   color: #FFFFFF;    font-size: 20px;    padding: 5px 10px;    text-shadow: 0 3px 0 #0000FF, 1px 2px 2px #AAAAAA;">  新鲜事业务评估系统</a></h2>
			</div>
		</div>
	</div>
	<!-- end -->


<script type="text/javascript">
	var checkeddate;
	var checkedtype;
	function clone(myObj){
	  if(typeof(myObj) != 'object') return myObj;
	  if(myObj == null) return myObj;
	  
	  var myNewObj = new Object();
	  for(var i in myObj)
	     myNewObj[i] = clone(myObj[i]);
	  return myNewObj;
	}	

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
	      alert('Get Stype Desc 加载出错,请重新刷新页面');
	    }
	  });
	}	
	
    	function goto(id, k) {
        	$("#" + id).ScrollTo(1000 + 500*k);
   	}
	  
	function lookPro(obj){
        	ob=eval(obj);
        	var Property="";
        	for(var i in ob){
        		Property+= i +"  |  </br>";
        		document.getElementById("myp").innerHTML=Property;
        	}
        }

  	function Abs(x) {return x>0?x:-x;}

	function mysort(A, B) {
		return Abs(B.data0 - B.data1) - Abs(A.data0 - A.data1);
	}// smaller ....

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
	
	

	// ====================================================================================================
	//  chart style   dis, click, reply, total
	var chart_stype = {
            chart: {
                renderTo: 'container_stype',
                type: 'column',
	    	events: {
                            click: function() {
				goto("daddy" , 0)	;
			    }	    
		}
	    },
            title: {
                text: '小类型的配额分配',
			style: {
				color: 'red',
				fontSize: '20px'
			}
            },
            xAxis: {
		title: {
			text: '类型'
		},
                labels: {
		    rotation: -45,
                }
            },
            yAxis: {
                title: {
                    text: '百分比'
                },
            },
            tooltip: {                
		shared: true,
                crosshairs: true,
            },
            series: []
        };// var char_taotal

       var chart_fangcha = {
            chart: {
                renderTo: 'container_fangcha',
                type: 'line',
	    },
            title: {
                text: '收益方差变化总趋势(可点击日期点查看该日详细情况)',
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
                        return this.value.slice(5,10); // clean, unformatted number for year
                    }
                }
            },
            yAxis: {
                title: {
                    text: '值'
                },
            },
            tooltip: {                
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
				checkeddate = this.category
				getQuotaDate(checkeddate)
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

       var chart_type_date = {
            chart: {
                renderTo: 'container_type',
                type: 'line',
	    	events: {
                            click: function() {
				goto("daddy" , 0)	;
			    }	    
		}
	    },
            title: {
                text: '变化总趋势(可点击日期点查看该类型详细情况)',
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
                    text: '百分比'
                },
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
				checkeddate = this.category
				getQuotaStype(checkedtype);	
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


	//!!!!!!!!!!!!!!!!!!
       var chart_type = {
            chart: {
                renderTo: 'container_type',
                type: 'column',
	    },
            title: {
                text: '配额系统',
			style: {
				color: 'blue',
				fontSize: '20px'
			}
            },
            xAxis: {
		title: {
			text: '类型'
		},
                labels: {
		    rotation: -45,
                    formatter: function() {
                        return this.value // clean, unformatted number for year
                        //return this.value.slice(5,10); // clean, unformatted number for year
                    }
                }
            },
            yAxis: {
                title: {
                    text: '百分比'
                },
                labels: {
                    formatter: function() {
                        return this.value ;
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
                        events: {
                            click: function() {
				getQuotaStype(this.category);	
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
	function getQuotaDate(date) {
		document.getElementById("container_type").style.display="block";
		goto("container_type", 0)
	 	$.ajax({
		    type: 'POST',
		    url: '/get-quota-data',
		    async: false,
		    data: "date="+date+"&isStype=1"+"&Bigtype=0",
		    success : function(text){
		   	 if(!text || text.length <= 0) return;
		   	 currentData = eval('(' + text + ')');
			 if (currentData.length == 0) {
				alert(date + " 这天木有数据  >_< ");
				document.getElementById("container_type").style.display="none";
				return ;
			 }
		   	 var series = [
		   	 	{name : "分发投入", data : []}, 
			    	{name : "曝光投入", data : []}, 
			    	{name : "产出", data : []}, 
			   	{name : "收益（产出 - 分发投入）", data : []},
			   	{name : "收益（产出 - 曝光投入）", data : []}
		   	 ]		
		   	 var cate = [];
		   	
			for(var i = currentData.length - 1, j = 0; i >= 0;  --i) {
				  if (currentData[i]["profit"]==0 || currentData[i]["cost"]==0)
					continue;
				  cate[j] = currentData[i]["type"]
	         		  series[0].data[j] = currentData[i]["cost"]
	         		  series[1].data[j] = currentData[i]["view"]
	         		  series[2].data[j] = currentData[i]["profit"]
	         		  series[3].data[j] = series[2].data[j] - series[0].data[j]//currentData[i]["balance"]
	         		  series[4].data[j] = series[2].data[j] - series[1].data[j]//currentData[i]["balance"]
				  j++;
			}
			 if (cate.length == 0) {
				alert(type + " 木有数据  >_<   OR   数据全为 0.0 ");
				document.getElementById("container_type").style.display="none";
				return ;
			 }
		
			chart_type.series = []
			chart_type.title.text = date + "日 各大类型的评估(可点击查看该详细信息)"
			chart_type.series.push(series[0]);
			chart_type.series.push(series[1]);
		  	chart_type.series.push(series[2]);
		  	chart_type.series.push(series[3]);
		  	chart_type.series.push(series[4]);
		  	chart_type.xAxis.categories = cate;
	
		  	var chart = new Highcharts.Chart(chart_type)
		    },// sucess
		    error : function(){
		      alert('getQuotaDate 加载出错, 请重新刷新页面');
		    }
	
		  });//ajax
	 }

	
	function getQuotaType(type) {
		document.getElementById("container_type").style.display="block";
		goto("container_type", 0)
	 	$.ajax({
		    type: 'POST',
		    url: '/get-quota-data',
		    async: false,
		    data: "date=0&isStype=4"+"&Bigtype="+type,
		    success : function(text){
		   	 if(!text || text.length <= 0) return;
		   	 currentData = eval('(' + text + ')');
		   	 var series = [
		   	 	{name : "分发投入", data : []}, 
			    	{name : "曝光投入", data : []}, 
			    	{name : "产出", data : []}, 
			   	{name : "收益（产出 - 分发投入）", data : []},
			   	{name : "收益（产出 - 曝光投入）", data : []}
		   	 ]		
		   	 var cate = [];
		   	
			for(var i = currentData.length - 1, j = 0; i >= 0;  --i) {
				  if (currentData[i]["profit"]==0 || currentData[i]["cost"]==0)
					continue;
				  cate[j] = currentData[i]["date"]
	         		  series[0].data[j] = currentData[i]["cost"]
	         		  series[1].data[j] = currentData[i]["view"]
	         		  series[2].data[j] = currentData[i]["profit"]
	         		  series[3].data[j] = series[2].data[j] - series[0].data[j]//currentData[i]["balance"]
	         		  series[4].data[j] = series[2].data[j] - series[1].data[j]//currentData[i]["balance"]
				  j++;
			}
			 if (cate.length == 0) {
				alert(type + " 木有数据  >_<   OR   数据全为 0.0 ");
				document.getElementById("container_type").style.display="none";
				return ;
			 }
	
			chart_type_date.series = []
			chart_type_date.title.text = type + "类型的变化曲线(可点击查详细信息)"
			chart_type_date.series.push(series[0]);
			chart_type_date.series.push(series[1]);
		  	chart_type_date.series.push(series[2]);
		  	chart_type_date.series.push(series[3]);
		  	chart_type_date.series.push(series[4]);
		  	chart_type_date.xAxis.categories = cate;
	
		  	chart2 = new Highcharts.Chart(chart_type_date)
		    },// sucess
		    error : function(){
		      alert('getQuotaType 加载出错, 请重新刷新页面');
		    }
	
		  });//ajax
	 }

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
				  series[0].data[stype] = currentData[i]["stype"]
	         		  series[1].data[stype] = currentData[i]["click"]
	         		  series[2].data[stype] = currentData[i]["reply"]
			      }
		    },// sucess
		    error : function(){
        	      alert('get_checkout_data : 加载出错, 请重新刷新页面 date:' + time);
        	    }
        
    	  });//ajax
	}//get_checkout_data

	function getQuotaStype(type) {
		chart_stype.chart.renderTo = 'container_stype',
		document.getElementById("container_stype").style.display="block";
		goto("container_stype", 0); 
		$.ajax({
		    type: 'POST',
		    url: '/get-quota-data',
		    async: false,
		    data: "date="+checkeddate+"&isStype=2"+"&Bigtype="+type,
		    success : function(text){
		   	 if(!text || text.length <= 0) return;
		   	 var currentData = eval('(' + text + ')');
		   	 var series = [
		   	 	{name : "分发投入", data : []}, 
			    	{name : "曝光投入", data : []}, 
			    	{name : "产出", data : []}, 
			   	{name : "收益（产出 - 分发投入）", data : []},
			   	{name : "收益（产出 - 曝光投入）", data : []}
		   	 ]		
		   	 var cate = [];
		   	
			for(var i = currentData.length - 1, j = 0; i >= 0;  --i) {
				  if (currentData[i]["profit"]==0 && currentData[i]["cost"]==0)
					continue;
				  cate[j] = stypeDesc[currentData[i]["stype"]] ? stypeDesc[currentData[i]["stype"]]: currentData[i]["stype"]
	         		  series[0].data[j] = currentData[i]["cost"]
	         		  series[1].data[j] = currentData[i]["view"]
	         		  series[2].data[j] = currentData[i]["profit"]
	         		  series[3].data[j] = series[2].data[j] - series[0].data[j]//currentData[i]["balance"]
	         		  series[4].data[j] = series[2].data[j] - series[1].data[j]//currentData[i]["balance"]
				  j++;
			}
			if (cate.length == 0) {
				alert(checkeddate + " 木有"+type+"类型数据  >_<   OR   数据全为 0.0 ");
				document.getElementById("container_stype").style.display="none";
				return ;
			 }
		
			chart_stype.series = []
			
			chart_stype.title.text = checkeddate + "日 大类型" + type + "下个小类型的评估"	
			chart_stype.series.push(series[0]);
			chart_stype.series.push(series[1]);
		  	chart_stype.series.push(series[2]);
		  	chart_stype.series.push(series[3]);
		  	chart_stype.series.push(series[4]);
		  	chart_stype.xAxis.categories = cate;
	
		  	chart2 = new Highcharts.Chart(chart_stype)
		    },// sucess
		    error : function(){
		      alert('check_out 加载出错, 请重新刷新页面');
		    }
	
		  });//ajax
	}//

    	$(document).ready(function() {
 	      var html = '<option value="' + 0 + '">' + '选择类型</option>';
	      for(var i = 100; i < 10000; i+=100) {
	        html += '<option value="' + i + '">' + i + '</option>';
	      }
	      $("select[name=type]").html(html);
	
  	//select[date]	
	  var today = new Date();
	  var todayStr = today.getFullYear().toString() + "-" 
	                 + ((today.getMonth()+1).toString().length == 1 ? "0": "") +  (today.getMonth()+1).toString() + "-"
	                 + (today.getDate().toString().length == 1 ? "0": "") +  today.getDate().toString();
	//var yesterday="2012-08-19"
	var yesterday=getYesterday(todayStr)
	$("input[name=date]").val( "选择日期");
	//var yesterday=getYesterday(todayStr)
	//getQuotaDate(yesterday)
	getStypeDesc();
		
    });//ready
	
	$.extend(DateInput.DEFAULT_OPTS, {
	  month_names: ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"],
	  short_month_names: ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"],
	  short_day_names: ["一", "二", "三", "四", "五", "六", "日"],
	  
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
	
	$("select[name=type]").live('change', function(){
	     $("input[name=date]").val( "选择日期");
	     checkedtype = $("select[name=type]").val() 
	     getQuotaType(checkedtype)
	});
	
	$("input[name=date]").live('change', function(){
	  if(!$(this).val().match(/^(\d{4,4})-(\d{2,2})-(\d{2,2})$/)){
	    alert("输入日期错误: " + $(this).val());
	    return ;
	  } else {
	     	$("select[name=type]").val( "选择类型");
		checkeddate = $("input[name=date]").val()  
		getQuotaDate(checkeddate)
	  }
	});
	
	
</script>


</head>
    <style>
    a:link,a:visited {font-size:30pxcolor: #ff0000; text-decoration:none;}
    a:hover {font-size:30px;color: #3c5a9a; text-decoration:underline;}
    </style>

<body style="background-color:#FFFFFF">
<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>

<div id="container_father" style="background-color:silver; margin: 0px 15px 0px 15px">
	<div id="container_fangcha" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px; display:none"></div>

<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>
<div > 
  <table id="option"  border="1" class="t1">
    <tr>
      <th align="left" style=" background-color:#FFFFFF">
       &nbsp;&nbsp; 某类型的变化曲线:&nbsp;<select name="type"></select>&nbsp;&nbsp;&nbsp;
      </th>
      <th id="daate" align="right" style=" background-color:#FFFFFF"">
       &nbsp;&nbsp; 某天各大类型的评估:&nbsp;<input type="text"  name="date"  class="date_input" size="11">&nbsp;&nbsp;&nbsp;
      </th>
    </tr>
  </table>
</div>
<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>

	<div id="container_type" style="min-width: 400px; height: 500px; margin: 5px 5px 5px 5px; display:none"></div>
	<div id="container_stype" style="min-width: 400px; min-height: 570px; background-color:white ; margin: 10px 5px 10px 5px ; display:none"></div>
</div>
<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=2)" width="97%" color=silver SIZE=5>

<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#987cb9,direction:145,strength:15)" width="100%" color=#987cb9 SIZE=1>


</body>
<div class="copyright" style="color:white">
<center>feed.renren   &copy;2012</center>
</div>

</div>
</html>















<script type="text/javascript">
//	 	$.ajax({
//		    type: 'POST',
//		    url: '/get-quota-data',
//		    async: true,
//		    data: "date=0&isStype=5"+"&Bigtype=0",
//		    success : function(text){
//		   	 if(!text || text.length <= 0) return;
//		   	 currentData = eval('(' + text + ')');
//			alert(currentData.length)
//			 if (currentData.length == 0) {
//				alert(date + " 木有数据  >_< ");
//				document.getElementById("container_fangcha").style.display="none";
//				return ;
//			 }
//		   	 var series = [
//			   	{name : "收益方差（产出 - 分发投入）", data : []},
//			   	{name : "收益方差（产出 - 曝光投入）", data : []}
//		   	 ]		
//		   	 var cate = [];
//			var dd = currentData[currentData.length - 1]["date"];
//			var data1 = 0, data2 = 0
//			for(var i = currentData.length - 1, j = 0; i >= 0;  --i) {
//				  if (currentData[i]["date"] == dd) {
//					data1 +=(currentData[i]["profit"] - currentData[i]["cost"]) * (currentData[i]["profit"] - currentData[i]["cost"])
//					data2 +=(currentData[i]["profit"] - currentData[i]["view"]) * (currentData[i]["profit"] - currentData[i]["view"])
//				  } else {
//					
//					cate[j] = dd
//					if(data1<1000 && data2<1000) {
//						series[0].data[j] = data1
//						series[1].data[j] = data2
//					} else {
//						alert(dd + " data wrong")
//					}
//
//					dd = currentData[i]["date"]
//					data1 = data2 = 0
//					j++;
//				  }
//			}
//			
//			chart_fangcha.series = []
//			chart_fangcha.series.push(series[0]);
//			chart_fangcha.series.push(series[1]);
//		  	chart_fangcha.xAxis.categories = cate;
//			alert(chart_fangcha.series)	
//		  	chart_fc = new Highcharts.Chart(chart_fangcha)
//			alert(chart_fc)
//		    },// sucess
//		    error : function(){
//		      alert('getFangcha_ready 加载出错, 请重新刷新页面');
//		    }
//	
//		  });//ajax
//
</script>
