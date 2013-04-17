<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>
<script src="/jquery.js" type="text/javascript"></script>
<title>创建新鲜事类型 - 新鲜事配置管理</title>
<script type="text/javascript" src="/old-feed-list.js"></script>
<script type="text/javascript" src="/feed-admin.js"></script>
</head>
<body>
<div><a href="/feed-list">全部类型列表</a> &gt; <a href="#nogo">新建类型</a></div>
<div id="stype-apply-placeholder"></div>
<br/>
<div id="config-placeholder"></div>
<br/>
<input id="config-submit" style="margin-left:570px;font-weight:bold;" type="button" value="完成"/>
<div style="display:block;margin:0 auto;">
</div>
</body>
<script type="text/javascript">
var g_apply_id = ${apply_id};
var cfg_view = new FeedConfigView(-1);
$('#config-submit').click(
  function() {
    // cfg_view.Save(true, g_apply_id);
    cfg_view.Save(true, g_apply_id, true);
  }
);

$(document).ready(
  function() {
    cfg_view.Load();
    cfg_view.AppendToNode($('#config-placeholder'));
    // cfg_view.Disable();
    cfg_view.HideSave();

    if (g_apply_id > 0) {
      var v = new StypeApplyView(g_apply_id); 
      v.AppendToNode($('#stype-apply-placeholder'));
      v.Disable();
    }
  }
);
</script>
</html>

