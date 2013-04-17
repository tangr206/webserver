<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html id="designdetector-com" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/css/new-style.css" rel="stylesheet" type="text/css"></link>
<script src="/jquery.js" type="text/javascript"></script>
<title>字段编辑 - 新鲜事配置管理</title>
<script type="text/javascript" src="/feed-admin.js"></script>
<script type="text/javascript">
var g_stype = ${stype};
</script>
</head>
<body>
<table width="70%" border="0" class="t1">
  <tr>
    <th colspan="4">Feed配置信息 &nbsp; <a id="save-config" href="#nogo">保存</a></th>
  </tr>

  <tr>
    <td style="width:110px;">类型（TYPE）：</td>
    <td><input id="type_id" size="4" maxlength="3"/></td>
    <td>小类型（STYPE）：</td>
    <td><input id="stype_id" size="6" maxlength="5"/></td>
  </tr>
  <tr>
    <td>权重（Weight）：</td>
    <td><select id="stype_weight">
          <option>0</option>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
      </select>
    </td>
    <td>父小类型（PType）：</td>
    <td><select id="ptype_id">
      <option>0</option>
      <option>1</option>

      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
      <option>6</option>
    </select></td>
  </tr>
  <tr>
    <td>持久化本体：</td>
    <td>save:
    <input name="SaveContent" type="radio" value="1" />&nbsp;&nbsp; not save:<input name="SaveContent" type="radio" value="0" checked="checked" /></td>
    <td>持久化FeedDB：</td>
    <td>save:
    <input name="SaveFeedDB" type="radio" value="1" />&nbsp;&nbsp; not save:<input name="SaveFeedDB" type="radio" value="0" checked="checked" /></td>
  </tr>
  <tr>
    <td>NewsFeed合并策略：</td>
    <td>
       append: <input name="NewsMergeType" type="radio" value="1" />
       &nbsp; replace: <input name="NewsMergeType" type="radio" value="2" checked="checked" /></td>
    <td>MiniFeed合并策略：</td>
    <td>append:
      <input name="MiniMergeType" type="radio" value="1" />
      &nbsp; replace: <input name="MiniMergeType" type="radio" value="2" checked="checked" />
    </td>
  </tr>
  <tr>
    <td>推送策略：</td>
    <td colspan="3">NewsFeed:<input type="checkbox" id="PushPolicy_news"/>&nbsp;&nbsp; MiniFeed:<input id="PushPolicy_mini" type="checkbox"/>&nbsp;&nbsp; IM:<input id="PushPolicy_IM" type="checkbox"/>

      &nbsp;&nbsp; Class:
      <input id="PushPolicy_class" type="checkbox"/>&nbsp;&nbsp; MiniGroup:<input id="PushPolicy_mini_group" type="checkbox"/></td>
  </tr>
  <tr>
    <td>分发表达式自定义：</td>
    <td>自定义: <input name="CustomExpr" type="radio" value="1"/>
      &nbsp;&nbsp;配置: <input name="CustomExpr" type="radio" value="0" checked="checked" /></td>
    <td>合并后是否更新时间：</td>
    <td>update:
      <input name="UpdateTimeOnMerge" type="radio" value="1" />
      &nbsp;&nbsp; not update:
    <input name="UpdateTimeOnMerge" type="radio" value="0" checked="checked" /></td>
  </tr>
  <tr>
    <td>保存时长：</td>

    <td><input name="Lifetime" value="-1" size="5" maxlength="5"/> 天（-1表示永久保存）</td>
    <td>每天发送配额：</td>
    <td><input name="DailyQuota" value="-1" size="9" maxlength="9"/> 条（-1表示不限制）</td>
  </tr>
</table>
<br/>

<table width="70%" border="0" class="t1">
  <tbody><tr>
    <th colspan="3">Feed必填字段设置 (线上版本：xxx，测试版本：BBB）</th>
  </tr>
  <tr>
    <th>KEY</th>
    <th>VALUE</th>
    <th>说明</th>
  </tr>
  <tr>
    <td>MiniMergeBy</td>
    <td><select id="MiniMergeBy" style="width:90px;">
      <option>key1</option>
    </select></td>
    <td>MiniFeed中将按此设置进行去重合并操作</td>
  </tr>
  <tr>
    <td>NewsMergeBy</td>
    <td><select id="NewsMergeBy" style="width:90px;">
      <option>key1</option>
    </select></td>
    <td>NewsFeed中将按此设置进行去重合并操作</td>
  </tr>
  <tr>
    <td>SourceBy</td>
    <td><select id="SourceBy" style="width:90px;">
      <option>source</option>
    </select></td>
    <td>产生Feed的业务的流水号，如发日志新鲜事时Source为日志表中的自增ID，即Blogid</td>
  </tr>
  <tr>
    <td>PSourceBy</td>
    <td><select id="PSourceBy" style="width:90px;">
      <option>x</option>
    </select></td>
    <td>用于分享，照片上转等具有父子关系的新鲜事发送，如分享日志产生的Feed，PSource应该是日志业务的流水号; 上转照片产生的Feed的PSource为所在像册的ID，主要用于批量删除</td>
  </tr>
  <tr>
    <td>ActorBy</td>
    <td><select id="ActorBy" style="width:90px;">
      <option>owner</option>
    </select></td>
    <td>触发Feed的人的UID</td>
  </tr>
  <tr>
    <td>分发表达式</td>
    <td><input id="DispatchExpr" value="" size="21"/></td>
    <td>由分发表达式计算出新鲜事分发给哪些用户</td>
  </tr>
  
</tbody></table>
<br/>
<table width="70%" border="0" class="t1">
  <tbody><tr>
      <th colspan="5">Feed数据字段定义(共有 <span id="version_count">?</span> 个版本) <a id="create_version" href="#nogo">新建版本</a></th>
  </tr>
</tbody></table>
<br/>
<table width="70%" border="0" class="t1">
  <tr align="right">
    <td colspan="5">
      版本<span>0</span>
      <a href="#nogo" id="validate-keys">检查合法性</a> &nbsp; <a href="#nogo" id="save-keys">保存</a>
      <a href="/feed-tpl-edit?stype=${stype}" target="_blank">编辑模板</a>
      &nbsp; <input type="submit" id="GenerateCode" value="生成Java代码" name="GenerateCode">
  </tr>
  <tr>
    <th width="200px">KEY <input type="text" id="add-key" title="新建顶层key" class="add-child"> </th>
    <th width="260px">描述</th>
    <th width="120px">数据类型</th>
    <th width="120px">节点循环</th>
    <th>操作</th>
  </tr>
</table>
<div class="key-list-container">
<ol id="key-list" style="list-style:none;padding:0;margin:0;"></ol>
</div>
</body>
<script type="text/javascript">
$('#save-config').click(
  function() {
    var url='/save-feed-config?';
    var type_id = parseInt($('input#type_id').val());
    if (isNaN(type_id) || type_id <= 0) {
      alert('请指定正确的type值');
      return;
    }
    url += 'type=' + type_id;
    var stype_id = parseInt($('input#stype_id').val());
    if (isNaN(stype_id) || stype_id <= 0) {
      alert('请指定正确的stype值');
      return;
    }
    url += '&stype=' + stype_id;
    if (Math.floor(stype_id / 100) != type_id) {
      alert('type ' + type_id + '和stype ' + stype_id + ' 值不匹配');
      return;
    }

    url += '&title=' + 'notset';
    url += '&weight=' + $('#stype_weight').val();
    url += '&ptype=' + $('#ptype_id').val();
    url += '&save_content=' + $("input[name='SaveContent']:checked").val();
    url += '&save_feed_db=' + $("input[name='SaveFeedDB']:checked").val();
    url += '&news_merge_type=' + $("input[name='NewsMergeType']:checked").val();
    url += '&mini_merge_type=' + $("input[name='MiniMergeType']:checked").val();

    var push_flags = 0;
    if ($("input:checkbox#PushPolicy_news").attr("checked")) {
      push_flags |= 0x01;
    }
    if ($("input:checkbox#PushPolicy_mini").attr("checked")) {
      push_flags |= 0x02;
    }
    if ($("input:checkbox#PushPolicy_IM").attr("checked")) {
      push_flags |= 0x04;
    }
    if ($("input:checkbox#PushPolicy_class").attr("checked")) {
      push_flags |= 0x08;
    }
    if ($("input:checkbox#PushPolicy_mini_group").attr("checked")) {
      push_flags |= 0x10;
    }
    url += '&push_flags=' + push_flags;
    url += '&custom_expr=' + $("input[name='CustomExpr']:checked").val();
    url += '&update_time_on_merge=' + $("input[name='UpdateTimeOnMerge']:checked").val();
    url += '&lifetime=' + $("input[name='Lifetime']").val();
    url += '&daily_quota=' + $("input[name='DailyQuota']").val();
    
    url += '&mini_merge_by=' + $('#MiniMergeBy').val();
    url += '&news_merge_by=' + $('#NewsMergeBy').val();
    url += '&source_by=' + $('#SourceBy').val();
    url += '&psource_by=' + $('#PSourceBy').val();
    url += '&actor_by=' + $('#ActorBy').val();
    url += '&dispatch_expr=' + $('#DispatchExpr').val();

    $.ajax(url, {
      'success' : function(){
        alert('保存成功');
      },
      'error' : function(){
        alert('保存失败');
      }
    });
  }
);


function JsonEscape(s) {
  var es = s.replace(/[\"\']/g, '\\\\\\\"');
  return es;
}
function GetKeysJson(root) {
  if(!root) {
    root = $("#key-list");
  }
  var nodes = $("li", root);
  var i = 0;
  var json = '[';
  nodes.each(
    function() {
      var n = $(this);
      if (!(n.parent().get(0) === root.get(0))) {
        return;
      }

      if (i > 0) {
        json += ",";
      }
      json += '{';
      var key = $('input.key', n).val();
      if (!key || key.length < 0) {
        alert('字段名不能为空');
        return '';
      }
      json += '"key":"' + key + '", ';
      var note = $('input.note', n).val();
      if (!note || note.length < 0) {
        alert('字段' + key + ' 描述不能为空');
        return '';
      }
      json += '"note":"' + JsonEscape(note) + '"';
      if (n.hasClass('multi')) {
        var kids = GetKeysJson($('ol', n));
        // console.log('kids : ' + kids);
        var o = [];
        try {
          var o = $.parseJSON(kids); 
        } catch (e) {
          alert('子节点错误' + e);
          return '';
        }
        if (o && o.length > 0) {
          json += ', "kids":' + kids;
        }
      }
      json += '}';
      ++i;
    }
  );
  json += ']';
  // console.log(json);
  return json;
}

function GetKeysXml(root) {
  if(!root) {
    root = $("#key-list");
  }
  var nodes = $("li", root);
  var i = 0;
  var xml = '<keylist>';
  nodes.each(
    function() {
      var n = $(this);
      if (!(n.parent().get(0) === root.get(0))) {
        return;
      }

      var key = $('input.key', n).val();
      if (!key || key.length < 0) {
        alert('字段名不能为空');
        return '';
      }
      xml += '<key>';
      xml += '<name>' + key + '</name>';
      var note = $('input.note', n).val();
      if (!note || note.length < 0) {
        alert('字段' + key + ' 描述不能为空');
        return '';
      }
      xml += '<note>' + encodeURIComponent(note) + '</note>';
      xml += '<data_type>' + $('select[name=DataType]', n).val() + '</data_type>';
      if (n.hasClass('multi')) {
        var kids = GetKeysXml($('ol', n));
        // console.log('kids : ' + kids);
        if (kids.length > 0) {
          xml += '<kids';
          if ($("input:checkbox", n).attr("checked")) {
            xml += ' is_loop="1"';
          }
          xml += '>' + kids + '</kids>';
        }
      }
      xml += '</key>';
      ++i;
    }
  );
  xml += '</keylist>';
  // console.log(xml);
  return xml;
}

function ValidateKeys() {
  var json = GetKeysJson();
  if (json.length <= 0) {
    alert('key数据格式错误');
    return false;
  }
  try {
    var o = $.parseJSON(json); 
  } catch (e) {
    alert('key数据格式错误:' + e);
    return false;
  }
  return true;
}

$('#add-key').click(
  function() {
    KeyListAdd('#key-list', '', '', '');
  }
);

$('#create_version').click(
  function() {
    var v = new FeedKeyView(g_stype, 1, 2);
    v.AppendToBody();
  }
);

$('#save-keys').click(
  function() {
    if(!ValidateKeys()) {
      return;
    }
    var url='/save-feed-keys?'
      + 'id=' + 1
      + '&stype=' + g_stype 
      + '&version=' + $('#SelVersion').val();
    alert(GetKeysXml());
    $.ajax(url, {
      'data' : 'kl=' + encodeURIComponent(GetKeysXml()),
      'type' : 'POST',
      'success' : function(){
        alert('保存成功');
      },
      'error' : function(){
        alert('保存出错');
      }
    });
  }
);

$('#validate-keys').click(
  function() {
    if(ValidateKeys()) {
      alert('验证通过');
    }
  }
);

var FeedKeyView = function(stype, version, seq_id) {
  this.stype_ = stype;
  this.version_ = version;
  this.seq_id_ = seq_id;
  this.dom_ = $('<br/>'
             + '<table width="70%" border="0" class="t1">'
               +   '<tr align="right">'
                 + '<td colspan="5">'
                 + '版本<span>0</span>'
                 + ' &nbsp; <a href="#nogo" id="validate-keys">检查合法性</a> &nbsp; <a href="#nogo" id="save-keys">保存</a>'
                 + ' &nbsp; <a href="/feed-tpl-edit?stype=${stype}" target="_blank">编辑模板</a>'
                 + ' &nbsp; <a href="#nogo" target="_blank">生成java代码</a>'
               + '</tr>'
               + '<tr>'
                 + '<th width="200px">KEY <input type="text" id="add-key" title="新建顶层key" class="add-child"> </th>'
                 + '<th width="260px">描述</th>'
                 + '<th width="120px">数据类型</th>'
                 + '<th width="120px">节点循环</th>'
                 + '<th>操作</th>'
               + '</tr>'
             + '</table>'
             + '<div class="key-list-container">'
               + '<ol id="key-list" style="list-style:none;padding:0;margin:0;"></ol>'
             + '</div>');

  var T = this;
  $('#save-keys', this.dom_).click(
    function() {
      if(!T.ValidateKeys()) {
        return;
      }
      var url='/save-feed-keys?'
        + 'stype=' + T.stype_
        + '&version=' + T.version_
        + '&id=' + T.seq_id_;
      alert(T.GetKeysXml());
      $.ajax(url, {
        'data' : 'kl=' + encodeURIComponent(T.GetKeysXml()),
        'type' : 'POST',
        'success' : function(){
          alert('保存成功');
        },
        'error' : function(){
          alert('保存出错');
        }
      });
    }
  );
  $('#validate-keys', this.dom_).click(
    function() {
      if(T.ValidateKeys()) {
        alert('Feed 数据 ' + T.seq_id_ + ' 验证通过');
      }
    }
  );

  $.ajax({
    'url': '/get-feed-keys?stype=' + stype + '&version=' + version + '&id=' + seq_id,
    'success': function(T) {
      var This = T;
      return function(text) {
        This.XmlKeyListAdd($(text));
      };
    }(this)
  });
}

FeedKeyView.prototype.ValidateKeys = function() {
  return true;
}

FeedKeyView.prototype.XmlKeyListAdd = function(xml_dom) {
  var child = xml_dom.children('key');
  var T = this;
  child.each(
    function() {
      var t = $(this);
      var kids = t.children('kids');
      var root = T.KeyListAdd(t.children('name').text(), t.children('note').text(), 
          t.children('data_type').text(), null, kids.attr('is_loop'));
      if (kids && kids.length) {
        T.XmlKeyListAddChild(root, kids);
      }
    }
  );
}

FeedKeyView.prototype.XmlKeyListAddChild = function(root, xml_dom) {
  var child = xml_dom.children(':first-child').children('key');
  var T = this;
  child.each(
    function() {
      var t = $(this);
      var kids = t.children('kids');
      var li = T.KeyListAddChild(root, t.children('name').text(), t.children('note').text(), 
          t.children('data_type').text(), null, kids.attr('is_loop'));
      if (kids && kids.length) {
        T.XmlKeyListAddChild(li, kids);
      }
    }
  );
}

FeedKeyView.prototype.KeyListAddChild = function(root, key, note, data_type, kids, is_loop) {
  if (root.hasClass('multi')) {
    root.removeClass('plus');
  } else {
    root.addClass('multi');
    $('span.child-loop', root).css('display', 'inline');
    root.click( function() {
        var t = $(this);
        if (t.hasClass('plus')) {
          t.removeClass('plus');
          t.addClass('minus');
          $('ol', t).show();
        } else {
          t.removeClass('minus');
          $('ol', t).hide();
          t.addClass('plus');
        }
      }
    );
  }
  root.addClass('minus');
  var ol = $($('ol', root).get(0));
  if (ol.length <= 0) {
    ol = $('<ol style="margin:3px 0 3px 1px; padding:0;list-style:none;"></ol>');
    root.append(ol);
  }
  var li = $('<li><input type="text" class="key" value="' + key + '"/><div style="float:right; width:759px;"><input type="text" class="note"/>' +
      '<select name="DataType"><option></option><option>number</option><option>string</option></select>' + 
      '<span class="child-loop"><input type="checkbox"/></span><input type="text" class="add-child"/><input type="text" class="remove-child"/></div></li>');
  $('input.note', li).val(decodeURIComponent(note));
  $('select[name=DataType]', li).val(data_type);
  $('input:checkbox', li).attr('checked', is_loop);

  li.children().click(
    function(e) {
      e.cancelBubble = true;
      e.stopPropagation && e.stopPropagation();
    }
  );

  li.click(
    function(e) {
      e.cancelBubble = true;
      e.stopPropagation && e.stopPropagation();
    }
  );

  $('input.add-child', li).click(
    function(e) {
      KeyListAddChild(li, '', '', '');
    }
  );
  $('input.remove-child', li).click(
    function(e) {
      if(!confirm('确定删除该key吗?')) {
        return;
      }
      $(this).parent().parent().remove();
    }
  );

  if (kids && kids.length) {
    for(var i = 0; i < kids.length; ++i) {
      KeyListAddChild(li, kids[i].key, kids[i].note, kids[i].data_type, kids[i].kids);
    }
  }
  ol.append(li);
  ol.show();
  return li;
}
FeedKeyView.prototype.KeyListAdd = function(key, note, data_type, kids, is_loop) {
  var n = $('<li class="feed-key"><input type="text" class="key" value="' + key + '"/><div style="float:right; width:759px;"><input type="text" class="note"/>'
        + '<select name="DataType"><option></option><option>number</option><option>string</option></select>'
        + '<span class="child-loop"><input type="checkbox"/></span><input type="text" class="add-child"/>'
        + '<input type="text" class="remove-child" href="#nogo"/></div></li>');

  $('input.note', n).val(decodeURIComponent(note));
  $('select[name=DataType]', n).val(data_type);
  $('input:checkbox', n).attr('checked', is_loop);

  $('input.add-child', n).click(
    function(e) {
      KeyListAddChild(n, '', '', '') ;
    }
  );
  $('input.remove-child', n).click(
    function(e) {
      if(!confirm('确定删除该key吗?')) {
        return;
      }
      $(this).parent().parent().remove();
    }
  );
  n.children().click(
    function(e) {
      e.cancelBubble = true;
      e.stopPropagation && e.stopPropagation();
    }
  );
  if (kids && kids.length) {
    for(var i = 0; i < kids.length; ++i) {
      KeyListAddChild(n, kids[i].key, kids[i].note, kids[i].data_type, kids[i].kids);
    }
  }
  $('#key-list', this.dom_).append(n);
  return n;
}

FeedKeyView.prototype.AppendToBody = function() {
  $(document.body).append(this.dom_);
}
FeedKeyView.prototype.Disable = function() {
}

FeedKeyView.prototype.GetKeysXml = function(root) {
  if(!root) {
    root = $("#key-list", this.dom_);
  }
  var T = this;
  var nodes = $("li", root);
  var i = 0;
  var xml = '<keylist>';
  nodes.each(
    function() {
      var n = $(this);
      if (!(n.parent().get(0) === root.get(0))) {
        return;
      }

      var key = $('input.key', n).val();
      if (!key || key.length < 0) {
        alert('字段名不能为空');
        return '';
      }
      xml += '<key>';
      xml += '<name>' + key + '</name>';
      var note = $('input.note', n).val();
      if (!note || note.length < 0) {
        alert('字段' + key + ' 描述不能为空');
        return '';
      }
      xml += '<note>' + encodeURIComponent(note) + '</note>';
      xml += '<data_type>' + $('select[name=DataType]', n).val() + '</data_type>';
      if (n.hasClass('multi')) {
        var kids = T.GetKeysXml($('ol', n));
        // console.log('kids : ' + kids);
        if (kids.length > 0) {
          xml += '<kids';
          if ($("input:checkbox", n).attr("checked")) {
            xml += ' is_loop="1"';
          }
          xml += '>' + kids + '</kids>';
        }
      }
      xml += '</key>';
      ++i;
    }
  );
  xml += '</keylist>';
  // console.log(xml);
  return xml;
}

$(document).ready(
  function() {
    if(g_stype <= 0) {
      return;
    }
    $('input#type_id').val(Math.floor(g_stype / 100)).attr('disabled', true);
    $('input#stype_id').val(g_stype).attr('disabled', true);
    $.ajax('/get-feed-config?stype=' + g_stype, {
      'success' : function(text){
         var o = $.parseJSON(text);

         $('#stype_weight').val(o.weight);
         $('#ptype_id').val(o.ptype);
         $("input[name='SaveContent'][value='" + o.save_content + "']").attr("checked", true);
         $("input[name='SaveFeedDB'][value='" + o.save_feed_db + "']").attr("checked", true);
         $("input[name='NewsMergeType'][value='" + o.news_merge_type + "']").attr("checked", true);
         $("input[name='MiniMergeType'][value='" + o.mini_merge_type + "']").attr("checked", true);

         $("input:checkbox#PushPolicy_news").attr("checked", o.push_flags & 0x01);
         $("input:checkbox#PushPolicy_mini").attr("checked", o.push_flags & 0x02);
         $("input:checkbox#PushPolicy_IM").attr("checked", o.push_flags & 0x04);
         $("input:checkbox#PushPolicy_class").attr("checked", o.push_flags & 0x08);
         $("input:checkbox#PushPolicy_mini_group").attr("checked", o.push_flags & 0x10);

         $("input[name='CustomExpr']:checked").val(o.custom_expr);
         $("input[name='UpdateTimeOnMerge']:checked").val(o.update_time_on_merge);
         $("input[name='Lifetime']").val(o.lifetime);
         $("input[name='DailyQuota']").val(o.daily_quota);

         $("#MiniMergeBy").val(o.mini_merge_by);
         $("#NewsMergeBy").val(o.news_merge_by);
         $("#SourceBy").val(o.source_by);
         $("#PSourceBy").val(o.psource_by);
         $("#ActorBy").val(o.actor_by);
         $("#DispatchExpr").val(o.dispatch_expr);
      },
      'error' : function(){
        alert('加载 stype ' + g_stype + ' 配置信息失败');
        $('#save-config').unbind('click').click(
          function() {
            alert('加载失败，禁止保存');
          }
        );
      }
    });
    ShowEditKeys(g_stype, 0);
    var v = new FeedKeyView(g_stype, 0, 2);
    v.AppendToBody();
  }
);
</script>
</html>

