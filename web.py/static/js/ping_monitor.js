var refreshEvent = null;
var noTicks_ = 20;
var labelsAngle_ = 45;
function mouse_drag_all(container, title, das) {
		var options, graph;
	  	var dasmax = -1;
		for (var i in das){
			for (var j in das[i].data){
				das[i].data[j][1] = parseFloat(das[i].data[j][1]);
				if (dasmax < das[i].data[j][1] || dasmax < 0)
					dasmax = das[i].data[j][1];
			}
		}
		
		options = {
		  title : title,
		  xaxis: {
			  mode : 'time',
			  timeFormat: '%m-%d %h:%M',
			  timeMode:'local',
			  labelsAngle: labelsAngle_,
			  noTicks : noTicks_
		  },
		  yaxis:{
			  title: '响应时间(ms)',
			  min:0,
			  max:dasmax + 2
		  },
		  grid:{
			  verticalLines: false,
			  backgroundColor: 'white'
		  },
		  legend: {
			  position: 'nw'
		  },
		  selection : { mode : 'x', fps : 30 },
		  HtmlText : false,
		  mouse : {
			  track           : true, // Enable mouse tracking
			  lineColor       : 'purple',
			  relative        : true,
			  position        : 'ne',
			  sensibility     : 1,
			  trackDecimals   : 2,
			  trackFormatter  : function (o) {
				  var res = new Date(parseInt(o.x)).pattern('yy-MM-dd HH:mm');
				  res = res +' ' + parseFloat(o.y).toFixed(2) + 'ms';
				  return res;
			  }
		  },
		  crosshair : {
			  mode : 'xy'
		  }
		};
		function drawGraph (opts) {
		  var o = Flotr._.extend(Flotr._.clone(options), opts || {});
		  return Flotr.draw(
			container,
			das,
			o
		  );
		}
	  
		graph = drawGraph();
		Flotr.EventAdapter.observe(container, 'flotr:select', function (area) {
		  graph = drawGraph({
			xaxis: {
				min:area.x1,
				max:area.x2,
				mode : 'time',
			  	timeFormat: '%m-%d %h:%M',
			  	timeMode:'local',
			  	labelsAngle: labelsAngle_,
				noTicks : noTicks_
			}
		  });
		});
		Flotr.EventAdapter.observe(container, 'flotr:click', function () { drawGraph(); }); 
}
function get_99(response){
	var _99 = 0, avg = 0, sd = 0;
	if ((response instanceof  Array) && (response.length > 0)){
		response.sort(function (a,b){return b-a;});
		_99 = response[parseInt(response.length/100)].toFixed(2);
		var sum = 0.0;
		for (var i in response){
			sum += response[i];
		}
		avg = sum / response.length;
		sd = 0.0;
		for (var i in response){
			sd += Math.pow(response[i] - avg, 2);
		}
		sd = Math.sqrt(sd/response.length).toFixed(2);
		avg = avg.toFixed(2);
	}
	return '.99响应时间：' + _99 + 'ms 平均响应时间：' + avg + 'ms 标准差：' + sd;
}
function mouse_drag(container, title, das) {
		var options, graph;
		
	  	var dasmax0 = -1;
	  	var dasmax1 = -1;
		var resAll = [];
		for (var j in das[0].data){
			das[0].data[j][1] = parseFloat(das[0].data[j][1]);
			resAll.push(das[0].data[j][1]);
			if (dasmax0 < das[0].data[j][1] || dasmax0 < 0 )
				dasmax0 = das[0].data[j][1];
		}
		for (var j in das[1].data){
			das[1].data[j][1] = parseFloat(das[1].data[j][1]);
			if (dasmax1 < das[1].data[j][1] || dasmax1 < 0)
				dasmax1 = das[1].data[j][1];
		}
	  	var subTitle = get_99(resAll);
		options = {
		  title : title,
		  xaxis: {
			  mode : 'time',
			  timeFormat: '%m-%d %h:%M',
			  timeMode:'local',
			  labelsAngle: labelsAngle_,
			  noTicks : noTicks_
		  },
		  yaxis:{
			  title: '响应时间(ms)',
			  min: 0,
			  max: dasmax0 + 2
		  },
		  y2axis : {
			  color:'#FF0000',
			  title : '请求数(次/分钟)' ,
			  min: 0,
			  max: dasmax1 + 100
		  },
		  grid:{
			  verticalLines: false,
			  backgroundColor: 'white'
		  },
		  legend: {
			  position: 'nw'
		  },
		  selection : { mode : 'x', fps : 30 },
		  HtmlText : false,
		  mouse : {
			  track           : true, // Enable mouse tracking
			  lineColor       : 'purple',
			  relative        : true,
			  position        : 'ne',
			  sensibility     : 1,
			  trackDecimals   : 2,
			  trackFormatter  : function (o) {
				  var res = new Date(parseInt(o.x)).pattern('yy-MM-dd HH:mm');
				  if (o.series.yaxis.n == 1){
					  res = res + ' ' + parseFloat(o.y).toFixed(2) + 'ms';
				  }else if (o.series.yaxis.n == 2){
					  res = res + ' ' + parseFloat(o.y).toFixed(0) + '次';
				  }
				  return res;
			  }
		  },
		  crosshair : {
			  mode : 'xy'
		  }
		};
	  
		function drawGraph (opts) {
	  
		  var o = Flotr._.extend(Flotr._.clone(options), opts || {});
	  
		  return Flotr.draw(
			container,
			das,
			o
		  );
		}
	  
		graph = drawGraph({subtitle : subTitle});
		Flotr.EventAdapter.observe(container, 'flotr:select', function (area) {
		  // Draw graph with new area
		var resN = [];
		for (var j in das[0].data){
			if ((das[0].data[j][0] > area.x1) && (das[0].data[j][0] < area.x2))
				resN.push(das[0].data[j][1]);
		}
	  	var subN = get_99(resN);
		  graph = drawGraph({
			subtitle: subN,
			xaxis: {
				min:area.x1,
				max:area.x2,
				mode : 'time',
			  	timeFormat: '%m-%d %h:%M',
			  	timeMode:'local',
			  	labelsAngle: labelsAngle_,
				noTicks : noTicks_
			}
		  });
		});
		  
		Flotr.EventAdapter.observe(container, 'flotr:click', function () { drawGraph({subtitle : subTitle}); });  
};
function findData(){
	var t = $('#startTime').val().split(" ");
	var t1 = t[0].split("-");
	var t2 = t[1].split(":"); 
	var start = (new Date(t1[0], t1[1] - 1, t1[2], t2[0], t2[1], t2[2])).pattern('yyyyMMddHHmmss');
	
	var end = -1;
	if (! $('#refreshBtn').is(':checked')){
		t = $('#endTime').val().split(" ");
		t1 = t[0].split("-");
		t2 = t[1].split(":"); 
		end = (new Date(t1[0], t1[1] - 1, t1[2], t2[0], t2[1], t2[2])).pattern('yyyyMMddHHmmss');
	}
	var service = $('#serviceName').val();
	var colors = Flotr.defaultOptions.colors;
	$.ajax({
		url: '/pingMonitor/service',
		cache: false,
		type: 'POST',
		data: {serviceName: service, startTime: start, endTime:end},
		async: false,
		dataType: 'json',
		success: function(data, substat){
			if (data.stat == 1){
				var das = [];
				for (var i in data){
					var obj = new Object();
					if ((i == 'stat') || (i == 'res'))
						continue;
					obj.label = i;
					obj.data = data[i].reponse;
					das.push(obj);
				}
				
				$('#views').empty();
				var $container = $('<div id="' + service + '" class="view"></div>').appendTo('#views');
				mouse_drag_all($container[0], service, das);
				
				var col = 0;
				for (var i in das){
					var subData = das[i];
					var method_name = subData.label;
					subData.label = '响应时间';
					
					var subData1 = {yaxis : 2};
					subData1.label = '请求数';
					subData1.data = data[method_name].require;
					
					
					var $container = $('<div id="' + service + '_' + i + '" class="view"></div>').appendTo('#views');
					//subData.lines = {color: colors[i]};
					subData.color = colors[col++];
					subData1.color = '#FF0000';
					mouse_drag($container[0], service + ' - ' + method_name, [subData, subData1]);
				}
			}else{
				alert('查询失败 没有该日期对应的数据');
			}
		},
		error: function(err){
			alert('查询失败 网络错误' + err.status)
		}
	});
}
function setRefresh(){
	if ($('#refreshBtn').is(':checked')){
		$('#endTime').val('').attr('disabled','disabled');
		$('#refreshTick').removeAttr('disabled');
		if (refreshEvent){
			window.clearInterval(refreshEvent);
		}
		refreshEvent = window.setInterval(findData, parseInt($('#refreshTick').val()) * 1000);
	}else{
		$('#endTime').removeAttr('disabled');
		var now = new Date();
		$('#endTime').val(now.pattern('yyyy-MM-dd HH:mm:ss'));
		$('#refreshTick').attr('disabled','disabled');
		if (refreshEvent){
			window.clearInterval(refreshEvent);
			refreshEvent = null;
		}
	}
}
$(function(){
	findData();
	$('#refreshTick').change(function(){
		if ($('#refreshBtn').is(':checked')){
			if (refreshEvent){
				window.clearInterval(refreshEvent);
			}
			refreshEvent = window.setInterval(findData, parseInt($('#refreshTick').val()) * 1000);
		}
	}).trigger('change');
});