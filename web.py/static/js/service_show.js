var show_type = '';
var picRefreshEvent = null;
var noTicks_ = 7;
var minorTickFreq_ = 5;
var labelsAngle_ = 0;

function findPicData(){
	var t = $('#picStartTime').val().split(" ");
	var t1 = t[0].split("-");
	var t2 = t[1].split(":"); 
	var now_min = (new Date()).getTime() / 60000;
	
	var start = (new Date(t1[0], t1[1] - 1, t1[2], t2[0], t2[1], t2[2])).getTime() / 60000;
	var points = now_min -start;
	
	var end = -1;
	if (! $('#picRefreshBtn').is(':checked')){
		t = $('#picEndTime').val().split(" ");
		t1 = t[0].split("-");
		t2 = t[1].split(":"); 
		end = (new Date(t1[0], t1[1] - 1, t1[2], t2[0], t2[1], t2[2])).getTime() / 60000;
		end = now_min - end;
	}
	if ((end > 0)&&(end < points)){
		alert('结束时间必须晚于开始时间！');
		return ;
	}
	var service = $('#service_name').text();
	$.ajax({
		url: '/monitor/'+service+'/'+start+'/'+end+'/'+show_type,
		cache: false,
		type: 'GET',
		async: false,
		dataType: 'json',
		success: function(data, substat){
			if (data.stat == 1){
				$('#views').empty();
				
			}else{
				alert('查询失败 没有该日期对应的数据');
			}
		},
		error: function(err){
			alert('查询失败 网络错误' + err.status)
		}
	});
}
function setPicRefresh(){
	if ($('#picRefreshBtn').is(':checked')){
		$('#picEndTime').val('').attr('disabled','disabled');
		$('#picRefreshTick').removeAttr('disabled');
		if (picRefreshEvent){
			window.clearInterval(picRefreshEvent);
		}
		picRefreshEvent = window.setInterval(findPicData, parseInt($('#picRefreshTick').val()) * 1000);
	}else{
		$('#picEndTime').removeAttr('disabled');
		var now = new Date();
		$('#picEndTime').val(now.pattern('yyyy-MM-dd HH:mm:ss'));
		$('#picRefreshTick').attr('disabled','disabled');
		if (picRefreshEvent){
			window.clearInterval(picRefreshEvent);
			picRefreshEvent = null;
		}
	}
}
function closeView(){
	if (picRefreshEvent){
		window.clearInterval(picRefreshEvent);
		picRefreshEvent = null;
	}
	$('#views').empty();
	$('#service_show').hide().siblings().show();
}
function initView(){
	$('#views').empty();
	$('#service_show').show().siblings().hide();
	$('#quickMenu .qBtn').unbind('click').click(function(e){
		var subT = parseInt($(this).attr('tick')) * 1000;
		var now = (new Date()).getTime();
		subT = new Date(now - subT);
		$('#picStartTime').val(subT.pattern('yyyy-MM-dd HH:mm:ss'));
		$('#picRefreshBtn').attr('checked', 'checked');
		findPicData();
		setPicRefresh();
		$(this).addClass('on').siblings().removeClass('on');
	}).first().trigger('click');
}
