
	//!!!!!!!!!!!!!!!!!!
/*       var chart_web ={
         chart: {
            renderTo: 'container_web',
	    zoomType: 'xy',
            type: 'line'
         },
         title: {
            text: 'WEB'
         },
         xAxis: {
         },
	yAxis: [{ // Primary yAxis
                labels: {
                    formatter: function() {
                        return this.value/10000 +'w';
                    },
                    style: {
                        color: '#89A54E'
                    }
                },
                title: {
                    text: '曝光量',
                    style: {
                        color: '#89A54E'
                    }
                },
                opposite: true
    
            }, { // Secondary yAxis
                gridLineWidth: 0,
                title: {
                    text: '访问人数 和点击数',
                    style: {
                        color: '#4572A7'
                    }
                },
                labels: {
                    formatter: function() {
                        return this.value/10000 +' W';
                    },
                    style: {
                        color: '#4572A7'
                    }
                }
    
            }], // y
            tooltip: {                
		shared: true,
                crosshairs: true,
            },
 	    series: []
      }
*/


	var YA =[{ // Secondary yAxis
		                gridLineWidth: 0,
		                title: {
		                    //text: '访问人数',
		                    style: {
		                        color: '#4572A7'
		                    }
		                },
		                labels: {
		                    formatter: function() {
		                        //return this.value/1000000 +' M';
		                    },
		                    style: {
		                        color: '#4572A7'
		                    }
		                }
		    
		            },{ // Primary yAxis
		                labels: {
		                    formatter: function() {
		                        //return this.value/1000000000 +'G';
		                    },
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		                title: {
		                    //text: '曝光量',
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		    
		            } ,{ // Primary yAxis
		                labels: {
		                    formatter: function() {
		                       // return this.value/1000000 +' M';
		                    },
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		                title: {
		                    //text: '点击量',
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		    
		            } ,{ // Primary yAxis
		                labels: {
		                    formatter: function() {
		                       // return this.value/1000000 +' M';
		                    },
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		                title: {
		                    //text: '点击量',
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		    
		            },{ // Primary yAxis
		                labels: {
		                    formatter: function() {
		                       // return this.value/1000000 +' M';
		                    },
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		                title: {
		                    //text: '点击量',
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		    
		            } ] 





