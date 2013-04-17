<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>
<script src="/jquery.js" type="text/javascript"></script>
<script type="text/javascript">
var g_user_right = ${user_right};
var g_list_filter = ${list_filter};
if (g_user_right <= 0) {
  var f = window.location.href;
  window.location = 'https://passport.no.opi-corp.com/login.php?forward=' + escape(f);
}
</script>
<script src="/feed-admin.js" type="text/javascript"></script>
<title>新鲜事类型列表</title>
</head>
<body>
<div class="alignCenter">
<div class="admin-only hidden">
  <table width="1200" border="1" class="t1">
    <tr>
      <th align="left"><a href="/feed-config-create">新建新鲜事类型</a> &nbsp; <a href="/user-apply-list">处理申请</a> &nbsp; <a class="reloadtest" href="#nogo">测试环境重新加载</a> &nbsp; <a class="reloaddist hidden" href="#nogo">线上环境重新加载</a></th>
    </tr>
  </table>
</div>
<div class="user-only hidden">
  <table width="1200" border="1" class="t1">
    <tr>
      <th align="left"><a target="_blank" href="/user-apply">申请新鲜事创建及修改</a> &nbsp; <a class="reloadtest" href="#nogo">测试环境重新加载</a></th>
    </tr>
  </table>
</div>
<br/>
<table width="1200" border="0">
  <tr>
    <th align="left" width="20%">
      <b style="font-size:120%;">新鲜事类型列表
          <select id="feed-list-filter">
             <option value="0">所有</option>
             <option value="1">禁用</option>
             <option value="2">测试</option>
             <option value="3">线上所有</option>
             <option value="4">线上只读</option>
             <option value="5">线上可发送</option>
          </select></b> &nbsp; &nbsp; 
    </th>
    <th align="left" width="20%">
      <a href="/old-feed-list.htm">查看老版本列表</a>
    </th>
    <th align="right" width="60%">
      <b style="font-size:120%;">注意:新鲜事模板更新时间——工作日每天16:00</b>&nbsp; &nbsp;
    </th>
</tr>
</table>
<table id="stype-list-table" width="1200" border="1" class="t1">
  <tr>
    <th width="28" class="admin-only hidden" rowspan="2">删除</td>
    <!-- <th width="25" rowspan="2">类型(type)</th> -->
    <th width="48" rowspan="2">小类型(stype)<br/></th>
    <th width="34" rowspan="2">持久化本体</th>
    <th width="34" rowspan="2">持久化<br/>FeedDB</th>
    <th colspan="2">合并策略</th>

    <th width="150" rowspan="2">推送策略</th>
    <th width="34" rowspan="2">权重</th>
    <!-- <th width="40" rowspan="2">保留时长<br />（天）</th> -->
    <th width="350" rowspan="2">类型介绍</th>
    <th width="50" rowspan="2">可发送版本号</th>
    <th width="32" rowspan="2">操作</th>
  </tr>
  <tr>
    <th width="30">News</th>
    <th width="30">Mini</th>
  </tr>
</table>
</div>
</body>

<script type="text/javascript">
function GetPushHtml(txt, b) {
  var color = b ? 'green' : 'red';
  if (!b) {
    return '';
  }
  return '<span style="color:' + color + ';">' + txt + '</span> &nbsp; ';
}
$('a.reloadtest').click(
  function() {
    $.ajax('/reloadtest', {
      success : function(text){
        alert(text);
      },
      error : function() {
        alert("测试环境重新加载失败");
      }
    });
  }
);

$('a.reloaddist').click(
  function() {
    if (!confirm('该操作会影响到线上服务，确定继续吗？')) {
      return;
    }
    $.ajax('/reloaddist', {
      success : function(text){
        alert(text);
      },
      error : function() {
        alert("线上环境重新加载失败");
      }
    });
  }
);

$(document).ready(
  function() {
    $('#feed-list-filter').val(${list_filter});
    $('#feed-list-filter').change(
      function() {
        window.location = "/feed-list?filter=" + $(this).val();
      }
    );
    if (g_user_right >= 2) {
      $('.admin-only').removeClass('hidden');
      $('.admin-only').attr('disabled', false);
      if (g_user_right > 2) {
        $('a.reloaddist').removeClass('hidden');
      }
    } else {
      $('.user-only').removeClass('hidden');
    }
    $.ajax('/get-stype-list?filter=${list_filter}', {
      'success' : function(text){
        var tv = $.parseJSON(text);
        var text_yes = '<span style="color:green;">Yes</span>';
        var text_no = '<span style="color:red;">No</span>';
        for(var i = 0; i < tv.length; ++i) {
          var o = tv[i];
          var html = '<tr style="background:' + (i % 2 ? "#e9edff" : "#f9e9ed") + '">'
                   + (g_user_right >= 2 ? '<td><a id="remove_stype" href="#nogo">删除</a></td>' : '')
                   //+ '<td>' + (o.stype - o.stype % 100) + '</td>'
                   + '<td>' + o.stype  + '</td>'
                   + '<td>' + (o.persist_body ? text_yes : text_no) + '</td>'
                   + '<td>' + (o.persist_feeddb ? text_yes : text_no) + '</td>';
           if (o.news_merge_type == 1) {
             html += '<td>replace</td>';
           } else if(o.news_merge_type == 2) {
             html += '<td>append</td>';
           } else {
             html += '<td><span style="color:red;">error</span></td>';
           }

           if (o.mini_merge_type == 1) {
             html += '<td>replace</td>';
           } else if(o.mini_merge_type == 2) {
             html += '<td>append</td>';
           } else {
             html += '<td><span style="color:red;">error</span></td>';
           }

           html += '<td>'
                + GetPushHtml('Newsfeed', o.push_feed_flags & F_PUSH_NEWS) 
                + GetPushHtml('Minifeed', o.push_feed_flags & F_PUSH_MINI) 
                + GetPushHtml('IM ', o.push_feed_flags & F_PUSH_IM) 
                + GetPushHtml('Class ', o.push_feed_flags & F_PUSH_CLASS) 
                + GetPushHtml('Minigroup ', o.push_feed_flags & F_PUSH_MINI_GROUP) + '</td>';

           html += '<td>' + o.weight + '</td>';
           //html += '<td>' + o.lifetime + '</td>';
           html += '<td>' + o.description + '</td>';
           html += '<td>' + (o.dispatching_ver > 0 ? ('<span style="color:green;">版本 ' + o.dispatching_ver + '</span>')
                           : '<span style="color:red;">不可发送</span>')
                   + '</td>';
           html += '<td><a href="/feed-config-edit?stype=' + o.stype + '">编辑</a> '
                   + '</td>';
           html += '</tr>';
           var node = $(html);
           $('#remove_stype', node).click(
             function() {
               var stype_id = o.stype;
               return function() {
                 if (!confirm('确定要删除新鲜事类型 ' + stype_id + ' 吗?')) {
                   return;
                 }
                 $.ajax('/remove-stype?stype_id=' + stype_id, {
                   success : function(text) {
                     alert(text);
                   },
                   error : function() {
                     alert('删除类型 ' + stype_id + ' 失败');
                   }
                 });
               };
             }()
           );
           $('#stype-list-table').append(node);
        }
      },
      'error' : function(){
        alert('加载出错');
      }
    });
  }
);
</script>
</html>

