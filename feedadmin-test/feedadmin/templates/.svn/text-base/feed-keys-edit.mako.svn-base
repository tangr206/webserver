<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>
<script src="/jquery.js" type="text/javascript"></script>
<title>字段编辑 - 新鲜事配置管理</title>
<script type="text/javascript" src="/feed-admin.js"></script>
<script type="text/javascript">
var g_user_right = ${user_right};
var g_stype = ${stype};
var g_version = ${version};
var g_from_tpl_id = ${from_tpl_id};
var g_apply_id = ${apply_id};
var g_is_user = ${is_user};
if (g_user_right <= 0) {
  var f = window.location.href;
  window.location = 'https://passport.no.opi-corp.com/login.php?forward=' + escape(f);
}
</script>
</head>
<body>
<div><a href="/feed-list">全部类型列表</a> &gt; <a href="/feed-config-edit?stype=${stype}">类型${stype}</a>
&gt; <a href="/feed-keys-edit?stype=${stype}&version=${version}">数据版本${version}</a>
</div>
<table width="1000" border="0" class="t1">
  <tbody><tr>
      <th colspan="5">Feed数据字段定义(stype:<span>${stype}</span>, 版本号: ${version}) 
        <span class="admin-only hidden">&nbsp; 状态 <a id="version-status-edit" href="#nogo">修改</a> <select id="version-status" disabled="true"><option value="0">disabled</option><option value="1">test</option><option value="2">read only</option><option value="3">dispatching</option></select></span>
        </th>
  </tr>
</tbody></table>
<div id="feed-key-container"></div>
<div class="seq-list-container"><div>模板序号管理：
<a id="create_seq" href="#nogo">新建</a> | 线上模板序号 <a class="admin-only hidden" id="using-version-id-edit" href="#nogo">修改</a> <select id="using-version-id" value="" disabled="true"><option>0</option></select> | 测试模板序号 <a id="test-version-id-edit" href="#nogo">修改</a> <select id="test-version-id" value="" disabled="true"><option>0</option></select>&nbsp; </div>
全部序号列表：
</div>
<br/>
</body>
<script type="text/javascript">
$('#create_seq').click(
  function() {
      $.ajax('/add-version-seq?stype=' + g_stype + '&version=' + g_version, {
          success : function(text) {
            alert('成功新建模板序号 : ' + text);
            var seq_list = $('div.seq-list-container');
            seq_list.append($('<a style="margin-left:10px;" href="/feed-tpl-edit?stype=' + g_stype 
                + '&version=' + g_version + '&tpl_id=' + text + '">模板序号' + text + '</a>'));
          },
          error : function(){
          }
        });
  }
);

if (g_apply_id > 0) {
  $('#create_seq').click(
    function() {
      $.ajax('/seq-apply-handled?apply_id=' + g_apply_id, {
          success : function(text) {
          },
          error : function(){
          }
        });
    }
  );
}

$('#using-version-id-edit').click(
  function() {
    if (!confirm("该操作会影响到线上新鲜事。确定要" + $(this).html() + "吗?")) {
      return;
    }
    if ($(this).html() == '保存') {
      $.ajax('/update-stype-version-using-id?stype=' + g_stype + '&version=' + g_version + '&tpl_id=' + $('#using-version-id').val(), {
        'success' : function(text){
          alert(text);
          $(this).html('修改');
          $('#using-version-id').attr('disabled', true);
        },
        'error' : function() {
          alert('保存失败');
        }
      });
    } else {
      $(this).html('保存');
      $('#using-version-id').attr('disabled', false);
    }
  }
);

$('#version-status-edit').click(
  function() {
    if (!confirm("该操作会影响到线上新鲜事。确定要" + $(this).html() + "吗?")) {
      return;
    }
    if ($(this).html() == '保存') {
      $.ajax('/update-stype-version-status?stype=' + g_stype + '&version=' + g_version + '&status=' + $('#version-status').val(), {
        "context" : $(this),
        'success' : function(text){
          alert(text);
          $(this).html('修改');
          $('#version-status').attr('disabled', true);
        },
        'error' : function() {
          alert('保存失败');
        }
      });
    } else {
      $(this).html('保存');
      $('#version-status').attr('disabled', false);
    }
  }
);

$('#test-version-id-edit').click(
  function() {
    if ($(this).html() == '保存') {
      $.ajax('/update-stype-version-test-id?stype=' + g_stype + '&version=' + g_version + '&tpl_id=' + $('#test-version-id').val(), {
        'success' : function(text){
          alert(text);
          $(this).html('修改');
          $('#test-version-id').attr('disabled', true);
        },
        'error' : function() {
          alert('保存失败');
        }
      });
    } else {
      $(this).html('保存');
      $('#test-version-id').attr('disabled', false);
    }
  }
);

$(document).ready(
  function() {
    if (g_user_right >= 2) {
      $('.admin-only').removeClass('hidden');
    }

    if(g_stype <= 0) {
      return;
    }
    $.ajax('/get-stype-version-seqs?stype=' + g_stype + '&version=' + g_version, {
      'success' : function(text){
        var seqs = $.parseJSON(text); 
        for(var i = 0; i < seqs.length; ++i) {
          // var view = new FeedKeyView(g_stype, g_version, seqs[i]);
          // view.AppendToBody();
          var seq_list = $('div.seq-list-container');
          if (seq_list.length <= 0) {
            seq_list = $('<div class="seq-list-container"> 模板序号列表(点击编辑模板): </div>');
            $(document.body).append(seq_list);
          }
          seq_list.append($('<a id="seq_entrance_' + seqs[i] + '" style="margin-left:10px;" href="/feed-tpl-edit?stype=' + g_stype 
              + '&version=' + g_version + '&tpl_id=' + seqs[i] + '">模板序号' + seqs[i] + '</a>'));
          
          $('#test-version-id').append($('<option value=' + seqs[i] + '>' + seqs[i] + '</option>'));
          $('#using-version-id').append($('<option value=' + seqs[i] + '>' + seqs[i] + '</option>'));
        }
        $.ajax('/get-stype-version-info?stype=' + g_stype + '&version=' + g_version, {
           'success' : function(text) {
             var o = $.parseJSON(text);
             $('#test-version-id').val(o.test_id);
             $('#seq_entrance_' + o.test_id).html('模板序号' + o.test_id + '(正在测试)').css('color', 'green');
             
             $('#using-version-id').val(o.using_id);
             $('#seq_entrance_' + o.using_id).html('模板序号' + o.using_id + '(线上生效)').css('color', 'red');

             $('#version-status').val(o.status);
             var readonly = (o.status > 1 && g_user_right < 2);

             var view = new FeedKeyView(g_stype, g_version, o.using_id, o.test_id, o.status, readonly);
             view.AppendToNode($('#feed-key-container'));
             view.HideVersion();
             view.HideStatus();
             view.HideSeqs();
             view.HideToggle();
           },
           'error' : function() {
             alert('加载id出错');
           }
        });
      },
      'error' : function(text){
      }
    });
  }
);
</script>
</html>

