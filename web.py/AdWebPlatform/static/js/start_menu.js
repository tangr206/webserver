var StartMenu = function($container){
	//init
	var self = this;
	self.$con = $container;
	self.$con.find('ul, li').hide();	
	
	//end init
	
	var makePtn = function ($par){
		self.$con.children('.gtn, .ptn').hide();
		
		var $toolbar = $('<div><span></span><div class="cBtn"></div></div>').addClass('toolbar');
		var $ptn = $('<div></div>').addClass('ptn').append($toolbar);
		
		$toolbar.find('span').text($par.children('li').text());
		
		var $its = $par.children('ul');
		
		$its.each(function(index, element){
			var $it = $(this).children('li');
			
			var $btn = $('<span></span>').addClass('btn');
			$btn.text($it.text());
			
			var $btnD = $('<div></div>').addClass('con').append($btn);
			
			$ptn.append($btnD);
			
			$btnD.attr({'gto': $it.attr('gto')});
			
			$btnD.click(function(e){
				if ($(this).attr('gto') == 'subMenu'){
					makePtn($it.parent());
				}else{
					window.open($(this).attr('gto'));
				}
				cancelDefault_(e); cancelBubble_(e);
			});
		});
		self.$con.append($ptn);
		var top = - $ptn.height() / 2;		
		$ptn.css({top : top});
		if ($its.length == 1){
			$ptn.find('.con').css('float','none');
		}
		
		$toolbar.find('.cBtn').click(function(e){
			$ptn.remove();
			if (self.$con.find('.ptn').length > 0){
				self.$con.children('.ptn').last().show();
			}else{
				self.$con.children('.gtn').show();
			}
		});
	}
	
	var makeGtn = function ($par, $parCon){
		var $gtn = $('<div></div>').addClass('gtn');
		
		$parCon.append($gtn);
		
		var $its = $par.children('ul');
		
		$its.each(function(index, element){
			var $it = $(this).children('li');
			
			var $btn = $('<span></span>').addClass('btn');
			$btn.text($it.text());
			
			var $btnD = $('<div></div>').addClass('con').append($btn);
			
			$gtn.append($btnD);
			
			$btnD.attr({'gto': $it.attr('gto'), 'id': ($parCon.attr('id') + '_' + index)});
			
			$btnD.bind('mouseenter', function(e){
				if ($(this).attr('gto') == 'subMenu'){
					makeGtn($it.parent(), $(this));
				}
				cancelDefault_(e); cancelBubble_(e);
			}).bind('mouseleave', function(e){
				$(this).children('.gtn').remove();
				cancelDefault_(e); cancelBubble_(e);
			}).click(function(e){
				if ($(this).attr('gto') == 'subMenu'){
					makePtn($it.parent());
				}else{
					window.open($(this).attr('gto'));
				}
				cancelDefault_(e); cancelBubble_(e);
			});
		});
			
		var pHeight = $parCon.height();
		var height = $gtn.height();
		
		var left = 5 - $gtn.width() ;
		var top = 0 - (height - pHeight) / 2;
		
		$gtn.css({top: top, left: left});
		
	}
	
	var cancelDefault_ = function (e){
		if (e.preventDefault)
			e.preventDefault();
		else
			e.returnValue=false;
	}
	var cancelBubble_ = function (e){
		if (e.stopPropagation)
			e.stopPropagation();
		else
			e.cancelBubble=true;
	}
	
	
	makeGtn(self.$con, self.$con);
	
}