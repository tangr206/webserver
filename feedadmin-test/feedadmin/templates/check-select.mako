<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 

"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>

<head>

<title>Navigation Effect Using jQuery</title>
<link rel="shortcut icon" href="favicon-rr.ico" type="image/x-icon"> 

<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<link rel="stylesheet" href="/css/stat.css" type="text/css"></link>
<title>content</title>
<script type="text/javascript" src="/jquery.js"></script>
<script src="/Highcharts-2.2.5/js/highcharts.js"></script>

<script type="text/javascript" src="sliding_effect.js"></script>






<script type=text/javascript>
$(function(){
	$('#mobanwang_com li').hover(function(){
		$(this).children('ul').stop(true,true).show('slow');
	},function(){
		$(this).children('ul').stop(true,true).hide('slow');
	});

});

</script>

<div id="wrapper" style=" z-index:1000;">
<ul id="mobanwang_com" class="first-menu">
  <li><a href="stat" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>

  <li><a href="#" target="self">实验平台</a>
    <ul id="subNews" class="second-menu">
      <li><a href="experi-select" target="_self" style="z-index:1000;">实验登记查看</a></li>
      <li><a href="stat-ABDebug" target="_self" style="z-index:1000;">选择尾号查看</a></li>
    </ul>
  </li>
  <li><a href="http://feed.d.xiaonei.com/stat-detail" target="_blank">详细信息</a>
    <ul id="subNews" class="second-menu">
      <li><a href="check-plat" target="_self" style="z-index:1000;">选择平台查看</a></li>
      <li><a href="check-stype" target="_self" style="z-index:1000;">选择类型查看</a></li>
    </ul>
  </li>
</ul>
</div>


</head>

<body>

<div id="navigation-block"> <img src="background.jpg" id="hide" />


  <ul id="sliding-navigation">

    <li class="sliding-element">

      <h3>选择平台</h3>

    </li>

    <li class="sliding-element"><a href="/check-plat?view=all">所有</a></li>

    <li class="sliding-element"><a href="/check-plat?view=view0" >WEB</a></li>

    <li class="sliding-element"><a href="/check-plat?view=view2" >手机</a></li>

    <li class="sliding-element"><a  href="/check-plat?view=view3">实时化</a></li>
    <li class="sliding-element"><a href="/check-plat?view=view4" >开放平台</a></li>
    <li class="sliding-element"><a href="/check-plat?view=view6" >TimeLine</a></li>

  </ul>

</div>



</body>

</html>
