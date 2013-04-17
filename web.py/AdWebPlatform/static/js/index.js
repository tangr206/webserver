var startMenu = null;

$(function(){
	startMenu = new StartMenu($('#menu'));
	
	
	$('.group span').bind('mouseover',function(e){
		$('.group ul').hide(300);
		$(this).next('ul').stop(true).show(300);
		_cancelDefault(e);
		_cancelBubble(e);
		return false;
	});
	$('.group li').bind('click',function(e){
		window.open($(this).attr('gto'));
		$(this).parent('ul').hide(300);
	});
	$('#navi').bind('mouseover',function(e){
		_cancelDefault(e);
		_cancelBubble(e);
		return false;
	});
	$('#mainContainer').bind('click',function(e){
		$('.group ul').hide(300);
	});
	$('#mainContainer').bind('mouseover',function(e){
		$('.group ul').hide(300);
	});
});