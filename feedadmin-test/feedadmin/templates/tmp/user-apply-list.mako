<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>
<script src="/jquery.js" type="text/javascript"></script>
<script src="/feed-admin.js" type="text/javascript"></script>
<title>列表 - 新鲜事管理</title>
</head>
<body>
<div><a href="/feed-list">全部类型列表</a> &gt; <a href="#nogo">新鲜事创建以及修改申请列表</a></div>
<table id="apply-feed-list-table" width="1200" border="1" class="t1">
  <tr>
    <th width="5">申请id</th>
    <th width="5">新鲜事类型id</th>
    <th width="300">新鲜事类型描述<br/></th>
    <th width="60">产品人员</th>
    <th width="5">状态</th>
    <th width="50">操作</th>
  </tr>
</table>
</body>

<script type="text/javascript">
$(document).ready(
  function() {
    $.ajax('/get-user-apply-list', {
      'success' : function(text){
        var applies = $.parseJSON(text);
        var table = $('#apply-feed-list-table');
        var yes = '<span style="color:green;">已经处理</span>';
        var no = '<span style="color:red;">未处理</span>';
        for(var i = 0; i < applies.length; ++i) {
          var o = applies[i];
          var node = $('<tr><td><span id="toggle-span" class="toggle-span folded"></span>' + o.apply_id + '</td>'
                   + '<td>' + o.feed_stype + '</td>'
                   + '<td>' + o.feed_desc + '</td>'
                   + '<td>' + o.pm_names + '</td>'
                   + '<td id="apply_status">' + (o.status ?  yes : no) + '</td>'
                   + '<td>' + (o.status == 0 ? '<a id="set_handled" href="#nogo">设为已处理</a>' : '') + ' <a id="remove_apply" href="#nogo">删除申请</a></td></tr>'
                   + '<tr style="display:none;"><td colspan="6"><span id="view_box"></span></td></tr>');
          table.append(node);

          $('#set_handled', node).click(
            function() {
              var apply_id = o.apply_id;
              var status_node = $('#apply_status', node);
              var set_node = $('#set_handled', node);
              return function() {
                $.ajax('/set-user-apply-handled?apply_id=' + apply_id, {
                  'success' : function(text){
                    alert(text);
                    status_node.html(yes);
                    set_node.remove();
                  },
                  'error' : function(){alert('出错');}
                });
              };
            }()
          );

          $('#remove_apply', node).click(
            function() {
              var apply_id = o.apply_id;
              return function() {
                $.ajax('/remove-user-apply?apply_id=' + apply_id, {
                  'success' : function(text){
                    alert(text);
                  },
                  'error' : function(){alert('删除失败');}
                });
              };
            }()
          );


          $('span.toggle-span', node).click(
            function() {
              var T = node;
              return function() {
                if ($(this).hasClass('folded')) {
                  $('#view_box', T).parent().parent().show();
                  $(this).removeClass('folded').addClass('expanded')
                } else {
                  $('#view_box', T).parent().parent().hide();
                  $(this).removeClass('expanded').addClass('folded')
                }
              };
            }()
          );
          var aid = o.apply_id;
          var apply_view = new UserApplyView(aid);
          apply_view.AppendToNode($('#view_box', node));
          // apply_view.Disable();
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

