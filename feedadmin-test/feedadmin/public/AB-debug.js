var name
	var YA =[{ // Secondary yAxis
		                gridLineWidth: 0,
		                title: {
		                    text: '点击,回复,分发量',
		                    style: {
		                        color: '#4572A7'
		                    }
		                },
		                labels: {
		                    formatter: function() {
		                        return this.value/1000000 +' M';
		                    },
		                    style: {
		                        color: '#4572A7'
		                    }
		                }
		    
		            },{ // Primary yAxis
		                labels: {
		                    formatter: function() {
		                        return this.value/1000000 +'M';
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
		    
		            } ,{ // Primary yAxis
		                labels: {
		                    formatter: function() {
		                        return this.value ;
		                    },
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		                title: {
		                    text: '点击率,回复率',
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		    
		            } ,{ // Primary yAxis
		                labels: {
		                    formatter: function() {
		                        return this.value ;
		                    },
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		                title: {
		                    text: '曝光,点击位置',
		                    style: {
		                        color: '#89A54E'
		                    }
		                },
		    
		            } ] 




