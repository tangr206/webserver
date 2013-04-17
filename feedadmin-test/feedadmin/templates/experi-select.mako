<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link rel="shortcut icon" href="favicon-rr.ico" type="image/x-icon"> 
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<link rel="stylesheet" href="/css/select.css" type="text/css" media="all"></link>
<link rel="stylesheet" href="/css/signin.css" type="text/css" media="all"></link>


<title>Experiment Select</title>
<script type="text/javascript" src="/jquery.js"></script>

<script type=text/javascript>
$(function(){
	$('#mobanwang_com li').hover(function(){
		$(this).children('ul').stop(true,true).show('slow');
	},function(){
		$(this).children('ul').stop(true,true).hide('slow');
	});

        $('#sign').hover(function(){
                $('#sign_in').stop(true,true).show('slow');
        },function(){
                $('#sign_in').stop(true,true).hide('slow');
        });
});

</script>


<div id="wrapper" style=" z-index:1000;">
<ul id="mobanwang_com" class="first-menu">
  <li><a href="stat" style="color:#ff0; background:none; border:none;" target="_self">FEED</a></li>

  <li><a href="#" >实验平台</a>
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



<h1>Experiment Select</h1>

</head>

<script type="text/javascript">
$(document).ready(function() {
  $.ajax({
    type: 'POST',
    url: '/experi-list',
    async: false,
    success : function(text){
      if(!text || text.length <= 0) return;
      currentData = eval('(' + text + ')');
      var html = "";
      for(var i=0; i<currentData.length; ++i) {
	cc = "checked" + i
        html += "<tr><th>"+i+"</th>"
            + "<td>" + currentData[i]["tail"].toString() + "</td>" + "<td>" + currentData[i]["begin"].toString() + "</td>" 
            + "<td>" + currentData[i]["end"].toString() + "</td>" + "<td>" + currentData[i]["describ"].toString() + "</td>"
            + "<td>" + currentData[i]["contact"].toString() + "</td>" + "<td>" + currentData[i]["summary"].toString() + "</td>"
	    + "</td>" + "<td id=\""+cc+"\" onclick=\"alert('" + cc + "')\" >" + cc  + "</td>"
            + "</tr>";
      }
	//alert(html)
      $("#data").append(html);
    },
    error : function(){
      alert('/加载出错');
    }
  });
});
</script>


   
<body>

<div id="content" style="margin: 20px 20px 20px 20px;" >

	<div id="left" style="margin: 20px 20px 20px 20px; " >

<div id="sign" style="margin:10px 0px 10px 0px">
			<fieldset>
			<legend>实验登记</legend>
<div style="min-height:20px;">
<div id="sign_in" style=" margin: 20px 20px 20px 20px;display:none" >

<form class="form">
  <p class="name">
    <label for="name">开始日期</label>
    <input type="text"  id="begin" />
  </p>
</br>
  <p class="email">
    <label for="name">结束日期</label>
    <input type="text"  id="end" />
  </p>
</br>
  <p class="web">
    <label for="name">实验尾号</label>
    <input type="text"  id="tail" />
  </p>
</br>
  <p class="email">
    <label for="email">@联系人 </label>
    <input type="text" id="email" />
  </p>
</br>
   <p class="text">
    <label for="name">实验描述</label>
    <textarea name="text" id="describ"></textarea>
  </p>
<br/>
  <p class="submit" >
    <label onclick="mysubmit()" />提交</label>
  </p>
</form>
</div>
</div>
			</fieldset>
</div>



			<fieldset style="margin:20px 0px 0px 0px">
			<legend>实验列表</legend>
<table id="data" cellspacing="0" cellpadding="0">
      <tr>
        <td>&nbsp;</td>
        <th>实验尾号</th>
        <th>开始日期</th>
        <th>结束日期</th>
        <th>实验描述</th>
        <th>负责人</th>
        <th>实验结论</th>
        <th>点击查看</th>
      </tr>
    </table>
			</fieldset>



	</div>
</div>
</body>

<script type="text/javascript">

        function mysubmit() {
                 begin = $("#begin").val() 
                 end = $("#end").val()
                 tail = $("#tail").val()
                 describ = $("#describ").val()
                 contact = $("#email").val()
                  $.ajax({
                    type: 'POST',
                    url: '/experi-insert',
                    async: false,
                    data: "begin="+begin+"&end="+end+"&tail="+tail+\
                                "&describ="+describ+"&contact="+contact, 
                    success : function(text){
                                updateForm()
                            },
                    error : function(){
                      alert('mysubmit 出错');
                    }
                });

        }

        function updateForm() {
          $.ajax({
            type: 'POST',
            url: '/experi-list',
            async: false,
            success : function(text){
              if(!text || text.length <= 0) return;
              if($("#data tr").length > 1) {
                        var len = $("#data tr").length;
                        for(var i = len-1; i > 0; --i) {
                          $("#data tr:eq(" + i.toString() + ")").remove();
                        }
              }
 currentData = eval('(' + text + ')');
              var html = "";
              for(var i=0; i<currentData.length; ++i) {
                cc = "update" + i
                html += "<tr><th>"+i+"</th>"
                    + "<td>" + currentData[i]["tail"].toString() + "</td>" + "<td>" + currentData[i]["begin"].toString() + "</td>" 
                    + "<td>" + currentData[i]["end"].toString() + "</td>" + "<td>" + currentData[i]["describ"].toString() + "</td>"
                    + "<td>" + currentData[i]["contact"].toString() + "</td>" + "<td>" + currentData[i]["summary"].toString() + "</td>"
                    + "</td>" + "<td id=\""+cc+"\" onclick=\"alert('" + cc + "')\" >" + cc  + "</td>"
                    + "</tr>";
              }
              $("#data").append(html);
            },
            error : function(){
              alert('updateFoem 加载出错');
            }
          });
        }
        

//====================================================================================
</script>


</html>

