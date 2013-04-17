<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>新鲜事模板view编辑</title>
<link href="/css/new-style.css" rel="stylesheet" type="text/css" />
<script src="/jquery.js" type="text/javascript"></script>
<script type="text/javascript" src="/feed-admin.js"></script>
<script type="text/javascript">
var g_user_right = ${user_right};
var g_tpl_using = ${tpl_using};
var g_stype = ${stype};
var g_version = ${version};
var g_tpl_id = ${tpl_id};

if (g_user_right <= 0) {
  var f = window.location.href;
  window.location = 'https://passport.no.opi-corp.com/login.php?forward=' + escape(f);
}
</script>
</head>
<body>
<div><a href="/feed-list">全部类型列表</a> &gt; <a href="/feed-config-edit?stype=${stype}">类型${stype}</a>
&gt; <a href="/feed-keys-edit?stype=${stype}&version=${version}">数据版本${version}</a>
&gt; <a href="/feed-tpl-edit?stype=${stype}&version=${version}&tpl_id=${tpl_id}">模板序号${tpl_id}</a>
</div>
<table width="1000" border="0" class="t1">
  <tbody><tr>
      <th colspan="5">stype <span style="color:red;font-weight:bold;">${stype}</span> 
        verion <span style="color:red;font-weight:bold;">${version}</span> 
        序号 <span style="color:red;font-weight:bold;">${tpl_id}</span> 
        Feed 模板列表编辑. </th>
  </tr>
</tbody></table>
<div id="feed-key-view"></div>
<br/>
<span><a href="#nogo" id="add-template">新建模板</a>(类型=<select id="add-template-view"><option></option>
        <option value="0">0 网站 Home&amp;Profile</option>
        <option value="1">1 IM</option>
        <option value="2">2 Wap</option>
        <option value="3">3 实时化</option>
        <option value="4">4 开放平台</option>
        <option value="5">5 小站</option>
</select>)</span>
<table width="1000" id="tpl-list"></table>
</body>

<script type="text/javascript">
$('#add-template').click(
  function() {
    var view = $('#add-template-view').val();
    if(view.length <= 0) {
      alert('请指定模板view类型');
      return;
    }
    var view_desc = $('option[value=' + view + ']', $('#add-template-view')).text();
    var tpl = new TplListItem(view, 0, view_desc, 'empty');
    alert('新建成功，刷新页面前请注意保存');
    tpl.AddToList();
  }
);
$(document).ready(
  function() {
    var view = new FeedKeyView(g_stype, g_version, g_tpl_id, -1, 0, true);
    view.AppendToNode($('#feed-key-view'));
    view.HideAllPanel();
 
    $.ajax('/get-tpls?tpl_id=' + g_tpl_id, {
      success : function(text) {
        var tpl_list = eval('(' + text + ')');
        for(var i = 0; i < tpl_list.length; ++i) {
          var view = tpl_list[i]['view'];
          var view_desc = $('option[value=' + view + ']', $('#add-template-view')).text();
          var tpl = new TplListItem(view, tpl_list[i]['status'], view_desc, tpl_list[i]['template'], g_user_right, g_stype, g_version);
          tpl.AddToList();
          if (g_user_right < 2) {
            tpl.HideEditStatus();
          }
          // 线上模板，即使超级管理员也不能修改, 必须先行下线
          if(g_tpl_using && (tpl_list[i]['status'] > 0)) {
            tpl.Readonly();
          }
        }
      },
      error : function() {
        alert('加载模板失败, 请刷新页面');
      }
    });
  }
);
$('#add-template-view').attr('disabled', false);
</script>
</html>

