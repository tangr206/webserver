<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>
<script src="/jquery.js" type="text/javascript"></script>
<title>字段编辑 - 新鲜事配置管理</title>
<script type="text/javascript" src="/old-feed-list.js"></script>
<script type="text/javascript" src="/feed-admin.js"></script>
<script type="text/javascript">
var g_user_right = ${user_right};
var g_stype = ${stype};
var g_from_version_id = ${from_version_id};
var g_apply_id = ${apply_id};

if (g_user_right <= 0) {
  var f = window.location.href;
  window.location = 'https://passport.no.opi-corp.com/login.php?forward=' + escape(f);
}
</script>
</head>
<body>
<div><a href="/feed-list">全部类型列表</a> &gt; <a href="/feed-config-edit?stype=${stype}">类型${stype}</a></div>
<div id="config-placeholder"></div>
<br/>
<div id="versions-header">
<table width="1000" border="0" class="t1">
  <tbody><tr>
      <th colspan="5">Feed全部版本列表(共有 <span id="version_count">?</span> 个版本) <a id="create_version" style="float:right;" href="#nogo">新建版本</a></th>
  </tr>
</tbody></table>
</div>
</body>
<script type="text/javascript">
var g_max_version = 0;
$('#create_version').click(
  function() {
    var v = 1 + g_max_version;
    if (!confirm('确定创建新版本 ' + v + ' 吗?')) {
      return;
    }
    $.ajax('/add-stype-version?stype=' + g_stype, {
      'success' : function(text) {
        var v = parseInt(text);
        if (!isNaN(v) && v > 0) {
          var feed_key = new FeedKeyView(g_stype, v, -1, -1, 1, false);
          feed_key.AppendToBody();
           feed_key.ShowMapping(false);
           feed_key.ShowKeys(false);
           feed_key.Disable();
          ++ g_max_version;
        } else {
          alert('创建新版本失败, 请联系管理员');
        }
      },
      'error' : function(text){
        alert('创建新版本失败');
      }
    });
  }
);

if (g_apply_id > 0) {
  $('#create_version').click(
    function() {
      $.ajax('/version-apply-handled?apply_id=' + g_apply_id, {
          success : function(text) {
          },
          error : function(){
          }
        });
    }
  );
}

$(document).ready(
  function() {
    if(g_stype <= 0) {
      $('#versions-header').css('display', 'none');
    } else {
      $.ajax('/get-stype-versions?stype=' + g_stype, {
        'success' : function(text){
          var versions = $.parseJSON(text); 
          for(var i = 0; i < versions.length; ++i) {
            var v = versions[i];
            var view = new FeedKeyView(g_stype, v.version, 
                v.using_tpl_id, v.test_tpl_id, v.status, true);
            view.AppendToBody();
            view.ShowMapping(false);
            view.ShowKeys(false);
            if (g_max_version < v.version) {
              g_max_version = v.version;
            }
          }
          $('#version_count').html(versions.length);
        },
        'error' : function(){
        }
      });
    }

    var cfg_view = new FeedConfigView(g_stype);
    cfg_view.Load();
    cfg_view.AppendToNode($('#config-placeholder'));
    if (g_user_right < 2) {
      cfg_view.Disable();
      $('#create_version').hide();
    }
    // cfg_view.HideMapping();
  }
);
</script>
</html>

