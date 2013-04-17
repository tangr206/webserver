var MSel = function($lcon, $rcon){
	var self = this;
	
	var bindLClick = function (index, element){
		$(this).unbind('click').click(function(e){
			if (! e.ctrlKey)
				$('span', $lcon).removeClass('sel');
			$(this).addClass('sel');
		});
	}
	var bindRClick = function (index, element){
		$(this).unbind('click').click(function(e){
			if (! e.ctrlKey)
				$('span', $rcon).removeClass('sel');
			$(this).addClass('sel');
		});
	}
	
	$('span', $lcon).each(bindLClick);
	$('span', $rcon).each(bindRClick);
	
	this.mvSel = function(){
		$('span.sel',$lcon).each(function(index, element) {
			var addAble = true;
			var $lSpan = $(this);
			$('span',$rcon).each(function(index, element) {
				var $rSpan = $(this);
				if ($lSpan.attr('id') == $rSpan.attr('id'))
					addAble = false;
			});
			if (addAble){
				$rcon.append($lSpan.clone().each(bindRClick));
			}
		});
	}
	this.mvAll = function(){
		$('span',$lcon).addClass('sel');
		self.mvSel();
	}
	this.delSel = function(){
		$('span.sel',$rcon).remove();
	}
	this.delAll = function(){
		$('span',$rcon).remove();
	}
}