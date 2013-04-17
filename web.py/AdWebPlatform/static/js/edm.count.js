var colors;
//var map_EN_CH = {'商业广告':'bussness', '自助广告':'self', '特殊用户广告':'special'};
//var map_CH_EN = {'bussness':'商业广告', 'self':'自助广告', 'special':'特殊用户广告'};
function closeView(id){
	$('#' + id).hide(300);
}
function getData(){
	$.ajax({
		url: '/edmAdCount/getAdDaily/' + $('#date').val(),
		cache: false,
		type: 'GET',
		async: false,
		dataType: 'json',
		success: function(data, substat){
			if (data.stat == 'ok'){
				res = data;
				setAdSin();
				$('#ctrlPanel a').first().trigger('click');
			}else{
				alert('查询失败 没有该日期对应的数据');
			}
		},
		error: function(err){
			alert('查询失败 网络错误' + err.status)
		}
	});
}
function setAdSin(){
	$('#res5 tbody').empty();
	for(var i = 0; i < res.single_ad.length; i++){
		$('#res5 tbody').append('<tr><td>' + res.single_ad[i][0] +
								'</td><td>' + res.single_ad[i][1] +
								'</td><td>' + res.single_ad[i][2] +
								'</td><td>' + res.single_ad[i][3] + '</td></tr>');
	}	
}
function par(fl){
	return parseInt(fl * 10000)/100;
}
function drawSend(){
	$('#res12').empty();
	var total = res.request.bussness + res.request.self + res.request.special;
	var categories = ['商业广告', '自助广告', '特殊用户广告'],
		data = [{
				y: par(res.request.bussness / total),
				color: colors[0],
				drilldown: {
					name: '商业广告发送情况',
					categories: ['实际发送', '无广告源丢失', '其他丢失'],
					data: [par(res.actual_send.bussness / total), par(res.no_source.bussness / total), par((res.request.bussness - res.actual_send.bussness - res.no_source.bussness) / total)],
					color: colors[0]
				}
			}, {
				y: par(res.request.self / total),
				color: colors[1],
				drilldown: {
					name: '自助广告发送情况',
					categories: ['实际发送', '无广告源丢失', '其他丢失'],
					data: [par(res.actual_send.self / total), par(res.no_source.self / total), par((res.request.self - res.actual_send.self - res.no_source.self) / total)],
					color: colors[1]
				}
			}, {
				y: par(res.request.special / total),
				color: colors[2],
				drilldown: {
					name: '特殊用户广告发送情况',
					categories: ['实际发送', '无广告源丢失', '其他丢失'],
					data: [par(res.actual_send.special / total), par(res.no_source.special / total), par((res.request.special - res.actual_send.special - res.no_source.special) / total)],
					color: colors[2]
				}
			}];


	// Build the data arrays
	var adTypeData = [];
	var adSendedData = [];
	for (var i = 0; i < data.length; i++) {

		// add browser data
		adTypeData.push({
			name: categories[i],
			y: data[i].y,
			color: data[i].color
		});

		// add version data
		for (var j = 0; j < data[i].drilldown.data.length; j++) {
			var brightness = 0.2 - (j / data[i].drilldown.data.length) / 5 ;
			adSendedData.push({
				name: data[i].drilldown.categories[j],
				y: data[i].drilldown.data[j],
				color: Highcharts.Color(data[i].color).brighten(brightness).get()
			});
		}
	}

	// Create the chart
	var chart12 = new Highcharts.Chart({
		chart: {
			renderTo: 'res12',
			type: 'pie'
		},
		title: {
			text: 'Edm广告发送情况统计'
		},
		plotOptions: {
			pie: {
				shadow: true,
				cursor: 'pointer',
				events: {
					click: function(e){
						var poName = '';
						switch(e.point.name){
							case '商业广告':
								poName = 'bussness';
								break;
							case '自助广告':
								poName = 'self';
								break;
							case '特殊用户广告':
								poName = 'special';
								break;
							default :
								return ;
						}
						drawSingV(poName, e.point.name);
					}
				}
			}
		},
		tooltip: {
			formatter: function() {
				return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
			}
		},
		credits: {
			enabled: true,
			text: 'renren.ad',
			href: 'http://adsys3.xce.n.xiaonei.com:8022/',
			position: {
				align: 'right',
				x: -10,
				verticalAlign: 'bottom',
				y: -5
			},
			style: {
				cursor: 'pointer',
				color: '#909090',
				fontSize: '10px'
			}
		},
		series: [{
			name: '广告类型',
			data: adTypeData,
			size: '60%',
			dataLabels: {
				formatter: function() {
					return this.y > 5 ? this.point.name : null;
				},
				color: 'white',
				distance: -30
			}
		}, {
			name: '发送情况',
			data: adSendedData,
			innerSize: '60%',
			dataLabels: {
				formatter: function() {
					// display only if larger than 1
					return this.y > 1 ? '<b>'+ this.point.name +':</b> '+ this.y +'%'  : null;
				}
			}
		}]
	});
	
	$('#res12').append(getTable());
	
	
}
function getTable(){
	var $tab = $('<table border="1" cellspacing="0" cellpadding="4" style="margin:auto;"><thead><tr><th>类别</th><th>用户请求数</th><th>广告发送量</th><th>无广告源丢失</th></thead></table>');
	$tab.append('<tr><td>商业广告</td><td>' + res.request.bussness + '</td><td>' + res.actual_send.bussness + '</td><td>' + res.no_source.bussness + '</td></tr>');
	$tab.append('<tr><td>自助广告</td><td>' + res.request.self + '</td><td>' + res.actual_send.self + '</td><td>' + res.no_source.self + '</td></tr>');
	$tab.append('<tr><td>特殊用户广告</td><td>' + res.request.special + '</td><td>' + res.actual_send.special + '</td><td>' + res.no_source.special + '</td></tr>');
	$tab.append('<tr><td>总计</td><td>' + res.request.total + '</td><td>' + res.actual_send.total + '</td><td>' + res.no_source.total + '</td></tr>');
	return $tab;
}
function getCtrlTable(){
	var $tab = $('<table border="1" cellspacing="0" cellpadding="4" style="margin:auto;"><thead><tr><th>类别</th><th>不发送数</th></thead></table>');
	$tab.append('<tr><td>商业广告</td><td>' + res.beyond_budget.bussness + '</td></tr>');
	$tab.append('<tr><td>自助广告</td><td>' + res.beyond_budget.self + '</td></tr>');
	$tab.append('<tr><td>特殊用户广告</td><td>' + res.beyond_budget.special + '</td></tr>');
	$tab.append('<tr><td>总计</td><td>' + res.beyond_budget.total + '</td></tr>');
	return $tab;
}
function drawLowerCtrl(){
	$('#res4').empty();
	var total = res.beyond_budget.bussness + res.beyond_budget.self + res.beyond_budget.special;
	var chart = new Highcharts.Chart({
            chart: {
                renderTo: 'res4',
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false
            },
            title: {
                text: '超预算导致用户不发送'
            },
            tooltip: {
                formatter: function() {
                    return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
                }
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        color: '#000000',
                        connectorColor: '#000000',
                        formatter: function() {
                            return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
                        }
                    }
                }
            },
			credits: {
				enabled: true,
				text: 'renren.ad',
				href: 'http://adsys3.xce.n.xiaonei.com:8022/',
				position: {
					align: 'right',
					x: -10,
					verticalAlign: 'bottom',
					y: -5
				},
				style: {
					cursor: 'pointer',
					color: '#909090',
					fontSize: '10px'
				}
			},
            series: [{
                type: 'pie',
                name: '超预算控制情况',
                data: [
                    {
                        name: '商业广告',
                        y: par(res.beyond_budget.bussness / total),
                        sliced: true,
                        selected: true
                    },
                    ['自助广告', par(res.beyond_budget.self / total)],
                    ['特殊用户广告', par(res.beyond_budget.special / total)],
                ]
            }]
        });
    $('#res4').append(getCtrlTable());
}
function drawSingV(id, name){
	$('#sinView').show().find('#closer').siblings().remove();
	var chart = new Highcharts.Chart({
            chart: {
                renderTo: 'sinView',
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false
            },
            title: {
                text: '<strong>' + name + '</strong>' + '发送情况'
            },
            tooltip: {
                formatter: function() {
                    return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
                }
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        color: '#000000',
                        connectorColor: '#000000',
                        formatter: function() {
                            return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
                        }
                    }
                }
            },
			credits: {
				enabled: true,
				text: 'renren.ad',
				href: 'http://adsys3.xce.n.xiaonei.com:8022/',
				position: {
					align: 'right',
					x: -10,
					verticalAlign: 'bottom',
					y: -5
				},
				style: {
					cursor: 'pointer',
					color: '#909090',
					fontSize: '10px'
				}
			},
            series: [{
                type: 'pie',
                name: name+'发送情况',
                data: [
                    ['无广告源丢失', par(res.no_source[id] / res.request[id])],
                    {
                        name: '正常发送',
                        y: par(res.actual_send[id] / res.request[id]),
                        sliced: true,
                        selected: true
                    },
                    ['其他丢失', par((res.request[id] - res.no_source[id] - res.actual_send[id]) / res.request[id])],
                ]
            }]
        });
    $('#sinView').append(getTable()).append('<span class="btn closeBtn" onClick="closeView(\'sinView\')">关闭</span>');
}
$(function(){
	$('#date').val(res.date);
	setAdSin();
	
	colors = Highcharts.getOptions().colors = $.map(Highcharts.getOptions().colors, function(color) {
		return {
			radialGradient: { cx: 0.5, cy: 0.3, r: 0.7 },
			stops: [
				[0, color],
				[1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
			]
		};
	});
	
	$('#ctrlPanel a').click(function(){
		if (res.stat == 'ok'){
			$('.res').hide();
			var comm = parseInt($(this).attr('sv'));
			$('#res' + comm).show(300,function(){
				switch (comm){
					case 12:
						drawSend();
						break;
					case 4:
						drawLowerCtrl();
						break;
				}
			});
		}else{
			alert('没有所选日期的数据，请重试');
			$('#date').focus();
		}
	}).first().trigger('click');
});