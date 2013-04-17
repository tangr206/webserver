var refreshEvent = null;
var unVis = [];

function getCompare(comp, rows, l_type){
  var trHtml;
  if (comp[0] == '-') {
	  trHtml = '<td id="service_status" rowspan="' + rows + '" class="_link" l_type="' + l_type + '" s_type="' + l_type + '">' + comp[0] + '</td>';
  } else {
	  trHtml = '<td id="service_status" rowspan="' + rows + '" class="link" l_type="' + l_type + '" s_type="' + l_type + '">' + comp[0] + '</td>';
  }

	for (var i = 1; i < comp.length; i++){
		comp[i] = comp[i] + '';
		if (comp[i] == '-'){
			trHtml += '<td id="service_status" rowspan="' + rows + '" class="_link compare_' + i + '" l_type="' + l_type + '" s_type="' + l_type + '">-</td>';
		}else if (comp[i][0] == '-'){
			trHtml += '<td id="service_status" rowspan="' + rows + '" class="link compare_' + i + ' dwd" l_type="' + l_type + '" s_type="' + l_type + '">&darr; ' + comp[i].split('-')[1] + '</td>';
		}else if (parseFloat(comp[i]) == 0){
			trHtml += '<td id="service_status" rowspan="' + rows + '" class="link compare_' + i + ' equ" l_type="' + l_type + '" s_type="' + l_type + '">0</td>';
		}else{
			trHtml += '<td id="service_status" rowspan="' + rows + '" class="link compare_' + i + ' upd" l_type="' + l_type + '" s_type="' + l_type + '">&uarr; ' + comp[i] + '</td>';
		}
	}
	return trHtml;
}

function getMethodCompare(comp, l_type, cla){
  var trHtml;
  if (comp[0] == '-') {
	  trHtml = '<td id="server_ping_info" class="_link" l_type="' + l_type + '" s_type="' + cla + '">' + comp[0] + '</td>';
  } else {
	  trHtml = '<td id="server_ping_info" class="link" l_type="' + l_type + '" s_type="' + cla + '">' + comp[0] + '</td>';
  }
	
  for (var i = 1; i < comp.length; i++){
		comp[i] = comp[i] + '';
		if (comp[i] == '-'){
			trHtml += '<td id="server_ping_info" class="_link compare_' + i + '" l_type="' + l_type + '" s_type="' + cla + '">-</td>';
		}else if (comp[i][0] == '-'){
			trHtml += '<td id="server_ping_info" class="link compare_' + i + ' dwd" l_type="' + l_type + '" s_type="' + cla + '">&darr; ' + comp[i].split('-')[1] + '</td>';
		}else if (parseFloat(comp[i]) == 0){
			trHtml += '<td id="server_ping_info" class="link compare_' + i + ' equ" l_type="' + l_type + '" s_type="' + cla + '">0</td>';
		}else{
			trHtml += '<td id="server_ping_info" class="link compare_' + i + ' upd" l_type="' + l_type + '" s_type="' + cla + '">&uarr; ' + comp[i] + '</td>';
		}
	}
	return trHtml;
}

function findData(){
	$.ajax({
		url: '/serviceStatus/getTable',
		cache: false,
		type: 'GET',
		async: true,
		dataType: 'json',
		success: function(data, substat){
			$('#status tbody').empty();
			for (var i in data.services){
				var service = data.services[i];
				var row_len = service.methods.length;
				var trHtml = '<tr service="' + service.service_name + '">';
				trHtml += '<td id="service_status" rowspan="' + row_len + '" class="link" l_type="all">' + service.service_name + '</td>';
				trHtml += '<td id="service_status" rowspan="' + row_len + '" class="_link" s_type="node">' + service.node + '</td>';
				
				trHtml += getCompare(service.cpu_rate, row_len, 'cpu_rate');
				trHtml += getCompare(service.memory, row_len, 'memory');
				trHtml += getCompare(service.threads, row_len, 'threads');
				trHtml += getCompare(service.des_rate, row_len, 'des_rate');
				
				for (var j = 0; j < row_len; j++){
					method = service.methods[j];
					if (j > 0) trHtml += '<tr service="' + service.service_name + '">';

          if (method.method_name == '-') {
					  trHtml += '<td id="server_ping_info" class="_link" l_type="' + method.method_name + '">' + method.method_name + '</td>';
          } else {
					  trHtml += '<td id="server_ping_info" class="link" l_type="' + method.method_name + '">' + method.method_name + '</td>';
          }
					trHtml += getMethodCompare(method._99, method.method_name, '_99');
					trHtml += getMethodCompare(method.avg, method.method_name, 'avg');
					trHtml += getMethodCompare(method.sd, method.method_name, 'sd');
					trHtml += getMethodCompare(method.req, method.method_name, 'req');
					trHtml += '</tr>';
				}
				$('#status tbody').append(trHtml);
			}
			$('.link').click(function(e){
				//$('#service_name').text();
				//show_type = $(this).attr('l_type');
				initView( $(this).parent().attr('service'), $(this).attr('id') );
				//window.open('/serviceStatus/show/' + $(this).parent().attr('service') + '/' + $(this).attr('l_type'));
			});
			setCompare(1);
			setCompare(2);
		},
		error: function(err){
			alert('查询失败 网络错误' + err.status)
		}
	});
}



function initView(service_name, category){
  for(var i=0; i<service_name.length; ++i) {
    if(service_name[i]>='0' && service_name[i]<='9')
	    window.open('/overview/?serviceName=' + service_name + '&cate=' + category, "_self");
  }
}




function setRefresh(){
	if ($('#refreshBtn').is(':checked')){
		$('#refreshTick').removeAttr('disabled');
		if (refreshEvent){
			window.clearInterval(refreshEvent);
		}
		refreshEvent = window.setInterval(findData, parseInt($('#refreshTick').val()) * 1000);
	}else{
		$('#refreshTick').attr('disabled','disabled');
		if (refreshEvent){
			window.clearInterval(refreshEvent);
			refreshEvent = null;
		}
	}
}

function setCompare(val){
	if ($('#compare' + val + 'Btn').is(':checked')){
		$('#status tbody .compare_' + val).removeClass('nosee');
	}else{
		$('#status tbody .compare_' + val).removeAttr('style').addClass('nosee');
	}
	var nrs = 1 + $('.compBtn:checked').length;
	$('#status thead th').each(function(index, element) {
		if ($(this).attr('colspan')){
			$(this).attr('colspan', nrs);
		}
	});
	$('#status tr').children(':not(.nosee)').each(function(index, element) {
		var visable = true;
		for (var i in unVis){
			if ($(this).attr('s_type') == unVis[i]){
				$(this).hide();
				visable = false;
				break;
			}
		}
		if (visable){
			$(this).show();
		}
    });
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

	$('#visableChoose .show_btn').change(function(e){
		unVis = [];
		$('#visableChoose .show_btn:not(:checked)').each(function(index, element) {
            unVis.push($(this).attr('id'));
        });
		setCompare(1);
		setCompare(2);
	});
});

