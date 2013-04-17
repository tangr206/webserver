<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>
<script src="/jquery.js" type="text/javascript"></script>
<script src="/feed-admin.js" type="text/javascript"></script>
<title>版本回退申请列表 - 新鲜事管理</title>
</head>
<body>
  版本回退申请列表 <br/>
<table id="apply-rollback-list-table" width="1200" border="1" class="t1">
  <tr>
    <th width="10">申请id</th>
    <th width="100">产品人员</th>
    <th width="10">stype<br/></th>
    <th width="300">版本回退原因<br/></th>
    <th width="25">处理状态</th>
    <th width="50">操作</th>
  </tr>
</table>
</body>

<script type="text/javascript">
$(document).ready(
  function() {
    $.ajax('/get-apply-rollback-list', {
      'success' : function(text){
        var v = $.parseJSON(text);
        var table = $('#apply-rollback-list-table');
        var yes = '<span style="color:green;">已经处理</span>';
        var no = '<span style="color:red;">未处理</span>';
        for(var i = 0; i < v.length; ++i) {
          var o = v[i];
          var html = '<tr><td>' + o.apply_id + '</td>'
                   + '<td>' + o.pm_names + '</td>'
                   + '<td>' + o.stype_id + '</td>'
                   + '<td>' + o.rollback_desc + '</td>'
                   + '<td>' + (o.status ?  yes : no) + '</td>'
                   + '<td><a target="_blank" href="/feed-keys-edit?stype=' + o.stype_id + '&version=' + o.version + '&from_seq_id=' + o.from_seq_id + '&apply_id=' + o.apply_id + '">创建新的字段版本</a> <a href="#nogo">删除申请</a></td>';

           table.append($(html));
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

