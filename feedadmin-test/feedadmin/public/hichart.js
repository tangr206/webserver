
<script type="text/javascript">

	var chart_dispatch = {
            chart: {
                renderTo: 'container_checkout_dispatch',
                type: 'column',
	    	events: {
                            click: function() {
				goto("container_total")	;
			    }	    
		}
	    },
            title: {
                text: 'dispatch 可能的变化原因 (变化大于50万的类型)'
            },
            xAxis: {
		title: {
			text: '类型'
		},
                labels: {
		    rotation: -45,
                    formatter: function() {
                        return this.value; // clean, unformatted number for year
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
		shared: true,
                crosshairs: true,
            },
	    plotOptions: {
                series: {
                    cursor: 'pointer',
                    point: {
                        events: {
                            click: function() {
				goto("container_total")	;
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

	var chart_click = {
            chart: {
                renderTo: 'container_checkout_click',
                type: 'column',
	    	events: {
                            click: function() {
				goto("container_total")	;
			    }	    
		}
	    },
            title: {
                text: 'click 可能的变化原因 (变化大于50万的类型)'
            },
            xAxis: {
		title: {
			text: '日期'
		},
                labels: {
		    rotation: -45,
                    formatter: function() {
                        return this.value; // clean, unformatted number for year
                    }
                }
            },
            yAxis: {
                title: {
                    text: '类型'
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
                        events: {
                            click: function() {
				goto("container_total")	;
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

	

	var chart_reply = {
            chart: {
                renderTo: 'container_checkout_reply',
                type: 'column',
	    	events: {
                            click: function() {
				goto("container_total")	;
			    }	    
		}
	    },
            title: {
                text: 'reply 可能的变化原因 (变化大于50万的类型)'
            },
            xAxis: {
		title: {
			text: '类型'
		},
                labels: {
		    rotation: -45,
                    formatter: function() {
                        return this.value; // clean, unformatted number for year
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
		shared: true,
                crosshairs: true,
            },
	    plotOptions: {
                series: {
                    cursor: 'pointer',
                    point: {
                        events: {
                            click: function() {
				goto("container_total")	;
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

</script>


