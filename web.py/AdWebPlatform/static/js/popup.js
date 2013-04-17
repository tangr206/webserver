// JavaScript Document
function _cancelDefault(e){ if(e.preventDefault) e.preventDefault(); else e.returnValue=false;}
function _cancelBubble(e){ if(e.stopPropagation) e.stopPropagation();  else e.cancelBubble=true;}
var PopUp ={
	view : null,
	P : { x:-1 , y:-1 },
	makeDialog : function(title,inner){
		var $self = $("<div><div class='bgFilter'></div><div class='popup'><div class='popup_title_bar'><span class='popup_title_txt'>"+title+"</span><div class='popup_btn_close'></div></div><div class='popup_content'><table class='layout' id='inputTable'>"+inner+"</table><table class='controls'><tr><td align='center' valign='middle'><span class='confirmBtn popupBtn'>确 定</span><span class='cancleBtn popupBtn'>取 消</span></td></tr></table></div></div></div>");
		$self.appendTo('body').hide().fadeIn(200);
		var $pop = $self.find(".popup");
		$pop.css({left:($(window).width() -$pop.width())/2,top:($(window).height() - $pop.height())/2}).find('.popup_title_bar').mousedown(function(e){
			PopUp.P.x = e.clientX;
			PopUp.P.y = e.clientY;
			_cancelDefault(e);
			_cancelBubble(e);
		}).mousemove(function(e){
			if (PopUp.P.x > 0){
				var cx = e.clientX > PopUp.P.x ? '+=' + (e.clientX - PopUp.P.x) + 'px' : '-='+ (PopUp.P.x - e.clientX) + 'px';
				var cy = e.clientY > PopUp.P.y ? '+=' + (e.clientY - PopUp.P.y) + 'px' : '-='+ (PopUp.P.y - e.clientY) + 'px';
				$pop.css({left:cx,top:cy})
				PopUp.P.x = e.clientX;
				PopUp.P.y = e.clientY;
			}
		}).mouseup(function(e){
			PopUp.P.x = -1;
			PopUp.P.y = -1;
		});
		$self.find(".bgFilter").click(function(e) {
			var $pop = $self.find(".popup");
			var tx = Math.max(0,Math.min(($(window).width() -$pop.outerWidth()),e.clientX - 150));
			var ty = Math.max(0,Math.min(($(window).height() -$pop.outerHeight()),e.clientY - 80));
			$pop.animate({left:tx,top:ty},600,function(){
				$('.confirmBtn',this)[0].focus();
			});
		}).mouseup(function(){
			PopUp.P.x = -1;
			PopUp.P.y = -1;
		});
		$self.find('.cancleBtn , .popup_btn_close').click(function(){PopUp.hide($self);});
		return $self;
	},
	makeTextInput:function(id, val){
		return '<input id="'+id+'" value="'+val+'" type="text" x-webkit-speech />';
	},
	makePwdInput:function(id){
		return '<input id="'+id+'" value="" type="password" x-webkit-speech />';
	},
	makeSelect:function(id, vals, selected){
		var sel = '<select id="'+id+'">';
		for (var i in vals){
			if (selected == vals[i]){
				sel += '<option selected="selected">'+vals[i]+'</option>';
			}else{
				sel += '<option>'+vals[i]+'</option>';
			}
		}
		sel += '</select>';
		return sel;
	},
	showInput:function (title,innerBody,callBack){
		callBack == null ? callBack = function(){} : null;
		var innerHtml = '';
		for (var i = 0 ; i < innerBody.length ;i++){
			var input = '';
			switch (innerBody[i][2]){
				case 'select':
					input = PopUp.makeSelect('i_'+i, innerBody[i][1], innerBody[i][3]);
					break;
				case 'password':
					input = PopUp.makePwdInput('i_'+i);
					break;
				case 'text':
				default:
					input = PopUp.makeTextInput('i_'+i, innerBody[i][1]);
					break;
			}
			innerHtml +='<tr><td align="right">'+innerBody[i][0]+':</td><td align="left">'+input+'<font color="#FF0000">*</font></td></tr>';
		}
		var $dialog = PopUp.makeDialog(title,innerHtml);
		$dialog.find(".confirmBtn").click(function(){callBack($dialog);});
		$dialog.find('input').each(function(i,e){
			$(this).val(innerBody[i][1]);
		});
		$dialog.find('input').keyup(function(e){
			if(!e) e = window.event;//火狐中是 window.event
			var keyCode = (e.keyCode || e.which);
			if(keyCode == 13){
				$('.confirmBtn').trigger('click');
				return false;
			}
		})[0].focus();
	},
	hide:function($dialog){
		$dialog.fadeOut(200,function(){$(this).remove();});
	}		
}
