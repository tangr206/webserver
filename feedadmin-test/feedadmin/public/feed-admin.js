var F_PUSH_NEWS = 0x01;
var F_PUSH_MINI = 0x02;
var F_PUSH_IM = 0x04;
var F_PUSH_CLASS = 0x08;
var F_PUSH_MINI_GROUP = 0x10;

var top_keys_includeNode;
var keysAndTestVal;

function GetStypeIdsHtml(default_value) {
  $.ajax('/get-stype-ids', {
    async : false,
    success : function(text){
      ids = $.parseJSON(text);
    },
    error : function(){
      alert('/get-stype-ids 出错');
    }
  });

  var html = '<option value="' + default_value + '">' + default_value + '</option>';
  for(var i = 0; i < ids.length; ++i) {
    html += '<option value="' + ids[i] + '">' + ids[i] + '</option>';
  }

  if (typeof(g_old_feed_list) != 'undefined') {
    for(var id in g_old_feed_list) {
      html += '<option value="' + id + '">' + id + '(老版本)</option>';
    }
  }

  return html;
}

var FeedConfigView = function(stype) {
  this.stype_ = isNaN(stype) ? -1 : stype;
  this.dom_ = $('<table width="1000" border="0" class="t1">' +
          '<tr>' +
            '<th colspan="4">Feed配置信息 &nbsp; <a id="save-config" style="float:right;" href="#nogo">保存</a></th>' +
          '</tr>' +
          '<tr>' +
            '<td style="width:110px;">类型（TYPE）：</td>' +
            '<td><input id="type_id" size="4" disabled maxlength="3"/></td>' +
            '<td>小类型（STYPE）：</td>' +
            '<td><input id="stype_id" size="6" maxlength="5"/></td>' +
          '</tr>' +
          '<tr>' +
            '<td>业务类型描述：</td>' +
            '<td colspan="3"><input size="120" type="text" id="stype-desc"/>' +
          '</tr>' +
          '<tr>' +
            '<td>权重（Weight）：</td>' +
            '<td><select id="stype_weight">' +
                '<option>1</option>' +
                '<option>2</option>' +
                '<option>3</option>' +
                '<option>4</option>' +
                '<option>5</option>' +
                '<option>6</option>' +
                '<option>7</option>' +
                '<option>8</option>' +
                '<option>9</option>' +
                '<option>10</option>' +
                '<option>11</option>' +
                '<option>12</option>' +
                '<option>13</option>' +
                '<option>14</option>' +
                '<option>15</option>' +
                '<option>16</option>' +
                '<option>17</option>' +
                '<option>18</option>' +
                '<option>19</option>' +
                '<option>20</option>' +
              '</select>' +
            '</td>' +
            '<td>父小类型（PType）：</td>' +
            '<td><select id="ptype_id" style="width:70px;">' +
              '<option>0</option>' +
            '</select></td>' +
          '</tr>' +
          '<tr>' +
            '<td>持久化本体：</td>' +
            '<td>save:' +
            '<input name="SaveContent" type="radio" value="1" />&nbsp;&nbsp; not save:<input name="SaveContent" type="radio" value="0" checked="checked" /></td>' +
            '<td>持久化FeedDB：</td>' +
            '<td>save:' +
            '<input name="SaveFeedDB" type="radio" value="1" />&nbsp;&nbsp; not save:<input name="SaveFeedDB" type="radio" value="0" checked="checked" /></td>' +
          '</tr>' +
          '<tr>' +
            '<td>NewsFeed合并策略：</td>' +
            '<td>' +
               'append: <input name="NewsMergeType" type="radio" value="2" />' +
               '&nbsp; replace: <input name="NewsMergeType" type="radio" value="1" checked="checked" /></td>' +
            '<td>MiniFeed合并策略：</td>' +
            '<td>append:<input name="MiniMergeType" type="radio" value="2" />' +
              '&nbsp; replace: <input name="MiniMergeType" type="radio" value="1" checked="checked" />' +
            '</td>' +
          '</tr>' +
          '<tr>' +
            '<td>推送策略：</td>' +
            '<td colspan="3">NewsFeed:<input type="checkbox" id="PushPolicy_news"/>&nbsp;&nbsp; MiniFeed:<input id="PushPolicy_mini" type="checkbox"/>&nbsp;&nbsp; IM:<input id="PushPolicy_IM" type="checkbox"/>' +
              '&nbsp;&nbsp; Class:' +
              '<input id="PushPolicy_class" type="checkbox"/>&nbsp;&nbsp; MiniGroup:<input id="PushPolicy_mini_group" type="checkbox"/></td>' +
          '</tr>' +
          '<tr>' +
            '<td>分发表达式自定义：</td>' +
            '<td>自定义: <input name="CustomExpr" type="radio" value="1"/>' +
              '&nbsp;&nbsp;配置: <input name="CustomExpr" type="radio" value="0" checked="checked" /></td>' +
            '<td>合并后是否更新时间：</td>' +
            '<td>update:' +
              '<input name="UpdateTimeOnMerge" type="radio" value="1" />' +
              '&nbsp;&nbsp; not update:' +
            '<input name="UpdateTimeOnMerge" type="radio" value="0" checked="checked" /></td>' +
          '</tr>' +
          '<tr>' +
            '<td>保存时长：</td>' +
            '<td><input name="Lifetime" value="30" size="5" maxlength="5"/> 天（-1表示永久保存）</td>' +
            '<td>每天发送配额：</td>' +
            '<td><input name="DailyQuota" value="10000" size="9" maxlength="9"/> 条（-1表示不限制）</td>' +
          '</tr>' +
        '</table>');
  var T = this;
  $('#save-config', this.dom_).click(
    function() {
      T.Save();
    }
  );

  $('input#stype_id', this.dom_).change(
    function() {
      var stype_id = parseInt($(this).val());
      if (isNaN(stype_id) || stype_id <= 100) {
        alert('stype值必须是大于100的整数值');
        return;
      }
      var ptype = $('#ptype_id', this.dom_).val();
      $('#ptype_id', this.dom_).html(GetStypeIdsHtml(ptype));
      $('#ptype_id').prepend($('<option value="' + stype_id + '">' + stype_id + '</option>')); 

      console.log($(this).val());
      $('input#type_id', T.dom_).val(stype_id - stype_id % 100);
    }
  );
}

FeedConfigView.prototype = {
  "AppendToNode" : function(node) {
    node.append(this.dom_);
  },

  "Load" : function() {
    $('#ptype_id', this.dom_).html(GetStypeIdsHtml('0'));
    if(this.stype_ <= 0) {
      return;
    }
    $('input#type_id', this.dom_).val(this.stype_ - this.stype_ % 100).attr('disabled', true);
    $('input#stype_id', this.dom_).val(this.stype_).attr('disabled', true);
    var T = this;
    $.ajax('/get-feed-config?stype=' + this.stype_, {
      'success' : function(text){
         var o = $.parseJSON(text);
         $('#stype-desc', T.dom_).val(o.desc);
         $('#stype_weight', T.dom_).val(o.weight);
         $('#ptype_id', T.dom_).val(o.ptype);

         $("input[name='SaveContent'][value='" + o.save_content + "']", T.dom_).attr("checked", true);
         $("input[name='SaveFeedDB'][value='" + o.save_feed_db + "']", T.dom_).attr("checked", true);
         $("input[name='NewsMergeType'][value='" + o.news_merge_type + "']", T.dom_).attr("checked", true);
         $("input[name='MiniMergeType'][value='" + o.mini_merge_type + "']", T.dom_).attr("checked", true);

         $("input:checkbox#PushPolicy_news", T.dom_).attr("checked", o.push_flags & F_PUSH_NEWS);
         $("input:checkbox#PushPolicy_mini", T.dom_).attr("checked", o.push_flags & F_PUSH_MINI);
         $("input:checkbox#PushPolicy_IM", T.dom_).attr("checked", o.push_flags & F_PUSH_IM);
         $("input:checkbox#PushPolicy_class", T.dom_).attr("checked", o.push_flags & F_PUSH_CLASS);
         $("input:checkbox#PushPolicy_mini_group", T.dom_).attr("checked", o.push_flags & F_PUSH_MINI_GROUP);

         $("input[name='CustomExpr'][value='" + o.custom_expr + "']", T.dom_).attr("checked", true);
         $("input[name='UpdateTimeOnMerge'][value='" + o.update_time_on_merge + "']", T.dom_).attr("checked", true);
         $("input[name='Lifetime']", T.dom_).val(o.lifetime);
         $("input[name='DailyQuota']", T.dom_).val(o.daily_quota);

         $("#MiniMergeBy", T.dom_).val(o.mini_merge_by);
         $("#NewsMergeBy", T.dom_).val(o.news_merge_by);
         $("#SourceBy", T.dom_).val(o.source_by);
         $("#PSourceBy", T.dom_).val(o.psource_by);
         $("#ActorBy", T.dom_).val(o.actor_by);
         $("#ToGroupBy", T.dom_).val(o.togroup_by);
         $("#DispatchExpr", T.dom_).val(decodeURIComponent(o.dispatch_expr));
      },
      'error' : function(){
        alert('加载新鲜事类型 ' + T.stype_ + ' 配置信息失败');
        $('#save-config', T.dom_).unbind('click').click(
          function() {
            alert('加载失败，禁止保存');
          }
        );
      }
    });
  }, 
  Save : function(jump_to_edit, apply_id, create_new) {
    var url='/save-feed-config?';
    var type_id = parseInt($('input#type_id', this.dom_).val());
    if (isNaN(type_id) || type_id <= 0) {
      alert('请指定正确的type值');
      return;
    }
    url += 'type=' + type_id;
    var stype_id = parseInt($('input#stype_id', this.dom_).val());
    if (isNaN(stype_id) || stype_id <= 0) {
      alert('请指定正确的stype值');
      return;
    }

    if (create_new) {
      if (g_old_feed_list[stype_id]) {
        if(!confirm('类型 "' + stype_id + g_old_feed_list[stype_id] + '" 在旧版新鲜事中已经存在，确定要在创建新版吗?')) {
          return false;
        }
      }
    }

    url += '&stype=' + stype_id;
    url += '&is_new=' + (this.stype_ != stype_id ? 1 : 0);
    if ((stype_id - stype_id % 100) != type_id) {
      alert('type ' + type_id + '和stype ' + stype_id + ' 值不匹配');
      return;
    }

    url += '&title=' + $('#stype-desc', this.dom_).val();
    url += '&weight=' + $('#stype_weight', this.dom_).val();
    url += '&ptype=' + $('#ptype_id', this.dom_).val();
    url += '&save_content=' + $("input[name='SaveContent']:checked", this.dom_).val();
    url += '&save_feed_db=' + $("input[name='SaveFeedDB']:checked", this.dom_).val();
    url += '&news_merge_type=' + $("input[name='NewsMergeType']:checked", this.dom_).val();
    url += '&mini_merge_type=' + $("input[name='MiniMergeType']:checked", this.dom_).val();

    var push_flags = 0;
    if ($("input:checkbox#PushPolicy_news", this.dom_).attr("checked")) {
      push_flags |= 0x01;
    }
    if ($("input:checkbox#PushPolicy_mini", this.dom_).attr("checked")) {
      push_flags |= 0x02;
    }
    if ($("input:checkbox#PushPolicy_IM", this.dom_).attr("checked")) {
      push_flags |= 0x04;
    }
    if ($("input:checkbox#PushPolicy_class", this.dom_).attr("checked")) {
      push_flags |= 0x08;
    }
    if ($("input:checkbox#PushPolicy_mini_group", this.dom_).attr("checked")) {
      push_flags |= 0x10;
    }
    url += '&push_flags=' + push_flags;
    url += '&custom_expr=' + $("input[name='CustomExpr']:checked", this.dom_).val();
    url += '&update_time_on_merge=' + $("input[name='UpdateTimeOnMerge']:checked", this.dom_).val();
    url += '&lifetime=' + $("input[name='Lifetime']", this.dom_).val();
    url += '&daily_quota=' + $("input[name='DailyQuota']", this.dom_).val();
    if (apply_id > 0) {
      url += '&apply_id=' + apply_id;
    }
    $.ajax(url, {
      'success' : function(text){
        var o = $.parseJSON(text);
        if (o.status == 0) {
          alert('保存成功');
          if (jump_to_edit) {
            window.location = '/feed-config-edit?stype=' + stype_id;
          }
        } else {
          alert(o.desc);
        }
      },
      'error' : function(){
        alert('保存失败');
      }
    });
  },
  HideSave : function() {
    $('#save-config', this.dom_).css('display', 'none');
  },
  "Disable" : function() {
    $('input, select', this.dom_).each(
      function() {
        $(this).attr('disabled', 'true');
      }
    );
    this.HideSave();
  }
}

var FeedKeyView = function(stype, version, using_seq_id, test_seq_id, status, readonly) {
  this.stype_ = stype;
  this.top_key_list_ = []
  this.version_ = version;
  this.using_seq_id_ = using_seq_id;
  // alert(using_seq_id + ' - ' +  test_seq_id + ' - ' + status);
  this.dom_ = $('<div><div id="panel" style="margin-left:0px; width:998px; line-height:24px; border:1px solid #CAD9EA;border-top:0;">'
                 + '<span id="toggle-span" class="toggle-span folded"></span> <span id="version-span">版本:<span style="color:red;">' + version + '</span></span>'
                 + ' <span id="status-span">&nbsp; 状态: <select id="version-status" disabled="true"><option value="0">disabled</option>'
                 +    '<option value="1">test</option><option value="2">read only</option><option value="3">dispatching</option>' 
                 + '</select></span>' 
                 + ' <span id="seqs-span">&nbsp; 线上模板序号:<span id="using-seq-id" style="color:red;">' + using_seq_id + '</span>' 
                 + ' &nbsp; 测试模板序号:<span id="test-seq-id" style="color:red;">' + test_seq_id + '</span></span>' 
                 
                 + ' <span class="edit-keys-panel">&nbsp; <a href="#nogo" id="validate-keys">检查合法性</a> &nbsp; <a href="#nogo" id="save-keys">保存</a></span>'

                 + ' &nbsp; <a style="display:none;" href="/feed-keys-edit?stype=' + stype + '&version='+ version + '" id="all-seqs">编辑</a>'
                 + ' &nbsp; <a href="#nogo" id="remove_schema_version">删除</a>'
                 + ' &nbsp; <a id="generate-java-code" href="#nogo">生成java代码</a>'
               + '</div>' +
      '<div><table width="1000" id="mapping-table" border="0" class="t1">' +
          '<tbody><tr>' +
              '<th colspan="3">Feed必填字段设置</th>' +
          '</tr>' +
          '<tr>' +
            '<th>KEY</th>' +
            '<th width="260">VALUE</th>' +
            '<th>说明</th>' +
          '</tr>' +
          '<tr>' +
            '<td>MiniMergeBy</td>' +
            '<td><select id="MiniMergeBy" class="key-mapping">' +
              '<option value="">(不去重)</option>' +
              //'<option value="(stype)">(按stype去重)</option>' +
            '</select></td>' +
            '<td>MiniFeed中将按此设置进行去重合并操作</td>' +
          '</tr>' +
          '<tr>' +
            '<td>NewsMergeBy</td>' +
            '<td><select id="NewsMergeBy" class="key-mapping">' +
              '<option value="">(不去重)</option>' +
              //'<option value="(stype)">(按stype去重)</option>' +
            '</select></td>' +
            '<td>NewsFeed中将按此设置进行去重合并操作</td>' +
          '</tr>' +
          '<tr>' +
            '<td>SourceBy</td>' +
            '<td><select id="SourceBy" class="key-mapping">' +
            '</select></td>' +
            '<td>产生Feed的业务的流水号，如发日志新鲜事时Source为日志表中的自增ID，即Blogid</td>' +
          '</tr>' +
          '<tr>' +
            '<td>PSourceBy</td>' +
            '<td><select id="PSourceBy" class="key-mapping">' +
            '</select></td>' +
            '<td>用于分享，照片上转等具有父子关系的新鲜事发送，如分享日志产生的Feed，PSource应该是日志业务的流水号; 上转照片产生的Feed的PSource为所在像册的ID，主要用于批量删除</td>' +
          '</tr>' +
          '<tr>' +
            '<td>ActorBy</td>' +
            '<td><select id="ActorBy" class="key-mapping">' +
            '</select></td>' +
            '<td>触发Feed的人的UID</td>' +
          '</tr>' +
          '<tr>' +
            '<td>ToGroupBy</td>' +
            '<td><select id="ToGroupBy" class="key-mapping">' +
              '<option value="">(不发给小群)</option>' +
            '</select></td>' +
            '<td>小群的id</td>' +
          '</tr>' +
          '<tr>' +
            '<td>分发表达式</td>' +
            '<td><input id="DispatchExpr" value="" size="32"/></td>' +
            '<td>由分发表达式计算出新鲜事分发给哪些用户(仅当使用"配置"分发表达式时有效)</td>' +
          '</tr>' +
        '</tbody></table></div>' 
             + '<table id="key-list-header" width="1000" border="0" class="t1">'
               + '<tr>'
                 + '<th width="200px">KEY (保留顶层字段名: <span style="color:red;">id, type,  stype,  minimerge,  newsmerge,  source,  psource,  actor, expr</span>) <input type="text" id="add-key" title="新建顶层key" class="add-child"> </th>'
                 + '<th width="260px">描述</th>'
                 + '<th width="120px">数据类型</th>'
                 + '<th width="60px">节点循环</th>'
                 + '<th width="60px">可选字段</th>'
                 + '<th>操作</th>'
               + '</tr>'
             + '</table>'
             + '<div class="key-list-container">'
               + '<ol id="key-list" style="list-style:none;padding:0;margin:0;"></ol>'
             + '</div></div>');

  var T = this;

  $('#version-status', this.dom_).val(status);
  $('#add-key', this.dom_).click(
    function() {
      T.KeyListAdd('', '', '');
    }
  );

  $('#remove_schema_version', this.dom_).click(
    function() {
      if(!confirm('确定删除版本' + T.version_ + '吗?')) {
        return;
      }
      // T.KeyListAdd('', '', '');
      $.ajax('/remove-data-version?stype=' + T.stype_ + '&version=' + T.version_, {
        success : function(text) {
          alert(text);
        },
        error : function() {
          alert('删除版本 ' + T.version_ + ' 失败');
        }
      });
    }
  );

  $('#save-keys', this.dom_).click(
    function() {
      if(!T.ValidateKeys()) {
        alert('数据格式不合法');
        return;
      }
      var url='/save-version-keys?'
        + 'stype=' + T.stype_
        + '&version=' + T.version_;

      url += '&mini_merge_by=' + $('#MiniMergeBy', T.dom_).val();
      url += '&news_merge_by=' + $('#NewsMergeBy', T.dom_).val();
      url += '&source_by=' + $('#SourceBy', T.dom_).val();
      url += '&psource_by=' + $('#PSourceBy', T.dom_).val();
      url += '&actor_by=' + $('#ActorBy', T.dom_).val();
      url += '&togroup_by=' + $('#ToGroupBy', T.dom_).val();
      url += '&dispatch_expr=' + encodeURIComponent($('#DispatchExpr', T.dom_).val());

      var keys_xml = T.GetKeysXml();
      if(!T.ValidateXmlLoop(keys_xml)) {
        return;
      }

      $.ajax(url, {
        'data' : 'kl=' + encodeURIComponent(T.GetKeysXml()),
        'type' : 'POST',
        'success' : function(text){
          alert(text);
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
        alert('Feed 数据验证通过');
      }
    }
  );
  
  $('#generate-java-code', this.dom_).click(
    function() {
      T.GenerateJavaCode();
    }
  );

  var T = this;
  $('#toggle-span', this.dom_).click(
    function() {
      if ($(this).hasClass('folded')) {
        T.ShowMapping(true);
        T.ShowKeys(true);
        $(this).removeClass('folded').addClass('expanded')
      } else {
        T.ShowMapping(false);
        T.ShowKeys(false);
        $(this).removeClass('expanded').addClass('folded')
      }
    }
  );

  $.ajax({
    'url': '/get-stype-version-info?stype=' + stype + '&version=' + version,
    'success': function(T) {
      var This = T;
      return function(text) {
        var o = $.parseJSON(text);
        This.XmlKeyListAdd($(o.keys_xml));
        This.FillTopKeys(o);
        This.UpdateOptionalCheckbox(); 
        This.stype_comment_ = o.stype_comment;

        if (readonly) {
          This.Disable(); 
        }
      };
    }(this)
  });
}

FeedKeyView.prototype.GenerateJavaCode = function() {
  var keys_xml = this.GetKeysXml();
  if(!this.ValidateXmlLoop(keys_xml)) {
    return;
  }
  var parser = new SchemaParser();
  parser.ParseSchema(this.stype_, this.version_, keys_xml, this.is_custom_expr_);
  var hdf = parser.GetHdfMap();
  hdf += ";FeedStruct.comment=" + encodeURIComponent(this.stype_comment_);

  $.ajax('/generate-code?lang=java&stype=' + this.stype_ + '&version=' + this.version_, {
    type: 'POST',
    data: 'hdf=' + encodeURIComponent(encodeURIComponent(hdf)), 
    context: document.body,
    success: function(text) {
      alert('生成代码成功，点确定后下载代码文件');
      window.location = text;
    },
    error: function(){
      alert('生成代码失败');
    }
  });
}

FeedKeyView.prototype.ValidateXmlLoop = function(keys_xml) {
  if (!keys_xml || keys_xml.length <= 0) {
    return false;
  }
  function HasLoopAncestor(node) {
    var p = node;
    console.log('parent = ' + p.parent().parent().length);
    // return false;
    p = p.parent()
    while(p.length > 0) {
      console.log('parent = ' + p);
      if (p.attr('is_loop') == "1") {
        return true;
      }
      p = p.parent();
    }
    return false;
  }

  function CheckChildren(dom) {
    var childs = dom.children();
    for(var i = 0; i < childs.length; ++i) {
      var n = $(childs[i]);
      if (n.attr('is_loop') == "1") {
        if (HasLoopAncestor(n)) {
          alert('循环节点 ' + n.attr('name') + ' 不能有可循环的上层节点');
          return false;
        }
      }
      if (n.children().length > 0) {
        if(!CheckChildren(n)) {
          return false;
        }
      }
    }

    return true;
  }

  return CheckChildren($(keys_xml));
}

FeedKeyView.prototype.ValidateKeys = function() {
  var top_keys = this.GetTopKeys();
  function FindKey(key) {
    for(var i = 0; i < top_keys.length; ++i) {
      if (key == top_keys[i]) {
        return true;
      }
    }
    return false;
  }

  var nodes = $('select', $('#mapping-table', this.dom));

  for(var i = 0; i < nodes.length; ++i) {
    var k = $(nodes[i]).val();
    if (k && k.length > 0 && !FindKey($(nodes[i]).val())) {
      alert('映射字段不合法:' + k);
      return false;
    }
  }
  return true;
}

FeedKeyView.prototype.ShowMapping = function(b) {
  $('#mapping-table', this.dom_).css('display', b ? '' : 'none');
}

FeedKeyView.prototype.ShowKeys = function(b) {
  $('#key-list-header', this.dom_).css('display', b ? '' : 'none');
  $('div.key-list-container', this.dom_).css('display', b ? '' : 'none');
}

FeedKeyView.prototype.UpdateOptionalCheckbox = function() {
  $('span.node-optional input:checkbox', this.dom_).css('visibility', 'visible');
  $('#key-list li', this.dom_).each(
    function() {
      var is_loop = $('> div > .node-loop > input:checkbox', $(this)).attr('checked');
      if ($(this).hasClass('multi') && is_loop) {
        $('ol span.node-optional input:checkbox', $(this)).css('visibility', 'hidden');
        // $('ol span.node-optional input:checkbox', $(this)).hide();
      }
      if ($(this).hasClass('multi') && !is_loop) {
        $('> div > span.node-optional input:checkbox', $(this)).css('visibility', 'hidden');
        // $('> div > span.node-optional input:checkbox', $(this)).hide();
      }
    }
  );
}

FeedKeyView.prototype.UpdateTopKeys = function() {
  this.UpdateOptionalCheckbox();
 
  var keys = this.GetTopKeys();
  var html = '';
  for(var i = 0; i < keys.length; ++ i) {
    html += '<option value="' + keys[i] + '">' + keys[i] + '</option>';
  }
  $('select', $('#mapping-table', this.dom)).each(
    function() {
      var val = $(this).val();
      $(this).html(html).val(val);
    }
  );

  $('#MiniMergeBy', this.dom_).prepend($('<option value="">(不去重)</option>'));
  $('#NewsMergeBy', this.dom_).prepend($('<option value="">(不去重)</option>'));
}

FeedKeyView.prototype.FillTopKeys = function(ver_info) {
  var keys = this.GetTopKeys();
  for(var i = 0; i < keys.length; ++ i) {
    $('select.key-mapping', this.dom_).each(
        function() {
          $(this).append('<option value="' + keys[i] + '">' + keys[i] + '</option>');
        }
      );
  }
  var o = ver_info;
  $('#MiniMergeBy', this.dom_).val(o.mini_merge_by);
  $('#NewsMergeBy', this.dom_).val(o.news_merge_by);
  $('#SourceBy', this.dom_).val(o.source_by);
  $('#PSourceBy', this.dom_).val(o.psource_by);
  $('#ActorBy', this.dom_).val(o.actor_by);
  $('#ToGroupBy', this.dom_).val(o.togroup_by);
  if (o.is_custom_expr) {
    this.is_custom_expr_ = true;
    $('#DispatchExpr', this.dom_).attr('disabled', true).val("");
  } else {
    $('#DispatchExpr', this.dom_).val(decodeURIComponent(o.dispatch_expr));
  }
}

FeedKeyView.prototype.XmlKeyListAdd = function(xml_dom) {
  var child = xml_dom.children('key');
  var T = this;
  child.each(
    function() {
      var t = $(this);
      var root = T.KeyListAdd(t.attr('name'), t.attr('comment'), t.attr('type'), null, t.attr('is_loop'), t.attr('optional'));

      var kids = t.children('key');
      if (kids && kids.length) {
        $('select[name=DataType]', root).append($('<option value="node">node</option>')).val('node').attr('disabled',true);
        T.XmlKeyListAddChild(root, kids);
      } else {
        if (t.attr('type') == 'number' && t.attr('is_loop') != '1') {
          T.top_key_list_[T.top_key_list_.length] = t.attr('name');
        }
      }
    }
  );
  this.top_key_ready_ = true;
}

FeedKeyView.prototype.XmlKeyListAddChild = function(root, kids) {
  // var child = xml_dom.children(':first-child').children('key');
  var T = this;
  kids.each(
    function() {
      var t = $(this);
      var li = T.KeyListAddChild(root, t.attr('name'), t.attr('comment'), 
          t.attr('type'), null, t.attr('is_loop'), t.attr('optional'));

      var kids = t.children('key');
      if (kids && kids.length) {
        // $('select[name=DataType]', li).append($('<option value="node">node</option>')).val('node').attr('disabled',true);
        T.XmlKeyListAddChild(li, kids);
      }
    }
  );
}

FeedKeyView.prototype.KeyListAddChild = function(root, key, note, data_type, kids, is_loop, optional) {
  var T = this;
  if (root.hasClass('multi')) {
    root.removeClass('plus');
  } else {
    root.addClass('multi');
    $('select[name=DataType]', root).append($('<option value="node">node</option>')).val('node').attr('disabled',true);
    root.click( function() {
        var t = $(this);
        if (!t.hasClass('multi'))
          return;
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
      '<select name="DataType"><option>string</option><option>number</option><option>link</option><option>headurl</option></select>' + 
      '<span class="node-loop"><input type="checkbox"/></span><span class="node-optional"><input type="checkbox"/></span><input type="text" class="add-child"/><input type="text" class="remove-child"/></div></li>');
  $('input.note', li).val(decodeURIComponent(note));
  $('select[name=DataType]', li).val(data_type).change(
    function() {
      T.UpdateTopKeys();
    }
  );

  $('.node-loop input:checkbox', li).attr('checked', is_loop);
  $('.node-optional input:checkbox', li).attr('checked', optional);
  $('.node-loop input:checkbox', li).change(
    function() {
      T.UpdateTopKeys();
    }
  );

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
      T.KeyListAddChild(li, '', '', '');
    }
  );
  $('input.remove-child', li).click(
    function(e) {
      if(!confirm('确定删除该key吗?')) {
        return;
      }
      var li = $(this).parent().parent()
      var ol = li.parent();
      li.remove();
      if ($('li', ol).length <= 0) {
        var r = ol.parent();
        r.removeClass('multi');
        r.removeClass('plus');
        r.removeClass('minus');

        $('option[value=node]', r).remove();
        $('select[name=DataType]', r).val('string').attr('disabled',false);;
        ol.remove();
      }
    }
  );

  if (kids && kids.length) {
    for(var i = 0; i < kids.length; ++i) {
      this.KeyListAddChild(li, kids[i].key, kids[i].note, kids[i].data_type, kids[i].kids);
    }
  }
  ol.append(li);
  ol.show();
  return li;
}

FeedKeyView.prototype.KeyListAdd = function(key, note, data_type, kids, is_loop, optional) {
  var n = $('<li class="feed-key"><input type="text" class="key" value="' + key + '"/><div style="float:right; width:759px;"><input type="text" class="note"/>'
        + '<select name="DataType"><option>string</option><option>number</option><option>link</option><option>headurl</option></select>'
        + '<span class="node-loop"><input type="checkbox"/></span><span class="node-optional"><input type="checkbox"/></span><input type="text" class="add-child"/>'
        + '<input type="text" class="remove-child" href="#nogo"/></div></li>');
  var T = this;
  $('input.note', n).val(decodeURIComponent(note));
  $('select[name=DataType]', n).val(data_type).change(
    function() {
      T.UpdateTopKeys();
    }
  );
  $('.node-loop input:checkbox', n).attr('checked', is_loop);
  $('.node-optional input:checkbox', n).attr('checked', optional);

  $('input.add-child', n).click(
    function(e) {
      T.KeyListAddChild(n, '', '', '') ;
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

  $('> input.key', n).change(
    function() {
      var k = $(this).val();
      if (T.IsReservedKey(k)) {
        alert('不能使用保留字段名:' + k);
        $(this).val('');
      }
    }
  );

  n.children().click(
    function(e) {
      e.cancelBubble = true;
      e.stopPropagation && e.stopPropagation();
    }
  );

  $('span.node-loop > input:checkbox', n).change(
    function() {
      T.UpdateTopKeys();
    }
  );

  if (kids && kids.length) {
    for(var i = 0; i < kids.length; ++i) {
      this.KeyListAddChild(n, kids[i].key, kids[i].note, kids[i].data_type, kids[i].kids);
    }
  }
  $('#key-list', this.dom_).append(n);

  return n;
}

FeedKeyView.prototype.AppendToBody = function() {
  $(document.body).append(this.dom_);
}
FeedKeyView.prototype.AppendToNode = function(node) {
  node.append(this.dom_);
}

FeedKeyView.prototype.Disable = function() {
  $('span.edit-keys-panel',this.dom_).css('display', 'none');
  $('#add-key', this.dom_).css('display', 'none');
  $('input, select', this.dom_).attr('disabled', true);
  $('#key-list input.add-child, #key-list input.remove-child', this.dom_).hide();
  $('#all-seqs', this.dom_).css('display', 'inline');
  $('#remove_schema_version', this.dom_).css('display', 'inline');
}

FeedKeyView.prototype.HideToggle= function() {
  $('#toggle-span', this.dom_).css('display', 'none');
}

FeedKeyView.prototype.HideVersion = function() {
  $('#version-span', this.dom_).css('display', 'none');
}
FeedKeyView.prototype.HideStatus = function() {
  $('#status-span', this.dom_).css('display', 'none');
}
FeedKeyView.prototype.HideSeqs = function() {
  $('#seqs-span', this.dom_).css('display', 'none');
}
FeedKeyView.prototype.HideAllPanel = function() {
  $('#panel', this.dom_).css('display', 'none');
}

// 返回顶层的数据，且数据类型必须是number
FeedKeyView.prototype.GetTopKeys = function(root) {
  var top_keys = [];
  top_keys_includeNode = [];
  keysAndTestVal = "";
  function GetKeys(ol, prefix) {
    $('> li', ol).each(
      function() {
        // if ($('> div input:checkbox', $(this)).attr('checked')) {
        //   return;
        // }
        var node_type = $('> div > select', $(this)).val();
        var node_name = $('> input.key', $(this)).val();
        if (prefix && prefix.length > 0) {
          node_name = prefix + '.' + node_name;
        }

        if ($('> div .node-loop input:checkbox', $(this)).attr('checked')) {
          node_name += ".0";
        }
        
        var isNode = false;
        var isNum = false;
        if (node_type == 'number') {
          top_keys[top_keys.length] = node_name;
          isNum = true;
        } else if (node_type == 'node') {
          GetKeys($('> ol', $(this)), node_name);
          isNode = true;
        }
        if(node_name.lastIndexOf(".0") == node_name.length - 2) {
          node_name = node_name.substring(0, node_name.length - 2) + "(loop_node)";
        } else if(isNode) {
          node_name += "(node)";
        }
        top_keys_includeNode[top_keys_includeNode.length] = node_name;
        if(isNum) {
          keysAndTestVal += node_name + "=" + "123456&";
        } else if(!isNode) {
          keysAndTestVal += node_name + "=" + node_name + "&";
        }
      }
    );
  }

  GetKeys($('#key-list', this.dom_));
  
  if(keysAndTestVal.lastIndexOf("&") == keysAndTestVal.length - 1) {
    keysAndTestVal = keysAndTestVal.substring(0, keysAndTestVal.length - 1);
  }

  return top_keys;
}

FeedKeyView.prototype.IsReservedKey = function(key) {
  var rsv = ['id', 'type', 'stype', 'minimerge', 'newsmerge', 'source', 'psource', 'actor', 'expr'];
  var lower_key = key.toLowerCase();
  for(var i = 0; i < rsv.length; ++i) {
    if (lower_key == rsv[i]) {
      return true;
    }
  }
  return false;
}

FeedKeyView.prototype.GetKeysXml = function(root) {
  var is_root_node = false;
  if(!root) {
    is_root_node = true;
    root = $("#key-list", this.dom_);
  }
  var T = this;
  var nodes = $("li", root);
  var i = 0;
  var xml = is_root_node ? '<key name="f" comment="root" type="node">' : '';
  var keys = $('input.key', root);
  for(var i = 0; i < keys.length; ++i) {
    var key = $(keys[i]).val();
    if (!key || key.length < 0) {
      alert('字段名不能为空');
      return '';
    }
    if (!/^[a-zA-Z][a-zA-Z0-9]*$/.test(key)) {
      alert('字段' + key + '命名不合法, 字段名必须由字母或数字组成, 且以字母开头');
      return '';
    }
  }
      
  var notes = $('input.note', root);
  for(var i = 0; i < notes.length; ++i) {
    var note = $(notes[i]).val();
    if (!note || note.length < 0) {
      alert('字段' + key + ' 描述不能为空');
      return '';
    }
  }

  nodes.each(
    function() {
      var n = $(this);
      if (!(n.parent().get(0) === root.get(0))) {
        return;
      }

      var key = $('input.key', n).val();
      var note = $('input.note', n).val();
      xml += '<key';
      if ($('> div .node-loop input:checkbox', n).attr('checked')) {
        xml += ' is_loop="1"';
      }
      var checkbox_optional =  $('> div .node-optional input:checkbox', n);
      if (checkbox_optional.css('visibility') != 'hidden' && checkbox_optional.attr('checked')) {
        xml += ' optional="1"';
      }
      xml += ' name="' + key + '"';
      xml += ' comment="' + encodeURIComponent(note) + '"';
      xml += ' type="' + $('select[name=DataType]', n).val() + '">';

      if (n.hasClass('multi')) {
        var kids = T.GetKeysXml($('ol', n));
        if (kids.length > 0) {
          xml += kids;
        }
      }
      xml += '</key>';
      ++i;
    }
  );
  if (is_root_node) {
    xml += '</key>';
  }
  return xml;
}

var TplListItem = function(view, status, view_desc, tpl_content, g_user_right, g_stype, g_version) {
  // var view_desc = $('#add-template-view option[value="' + view + '"]').text();
  this.view_ = view;
  this.dom_ = $('<tr height="2"><td><span id="toggle-span" class="toggle-span folded"></span>' 
              + ' View类型:<span class="view-desc">' + view_desc + '</span>'
              + ' | 状态<a id="tpl-status-edit" href="#nogo">(修改)</a>:<select disabled="true" id="tpl-view-status"><option value="0">测试模板</option><option value="1">线上模板</option></select>'
              + '</td>'
              +'<td width="400"> <a href="#nogo" id="validate-template">检查ClearSilver语法</a> &nbsp; <a style="font-size:120%;font-weight:bold;" href="#nogo" id="save-template">保存</a> &nbsp; <a style="margin-left:170px;"href="#nogo" id="remove-template">删除</a> </td></tr>');
              
  this.tplModule_ = $('<tr><td colspan="2"><table align="center" width="990" border="0" style="border-top:1px solid #cad9ea;border-bottom:1px solid #cad9ea;margin-top:5px;">'
              + '<tr><td width="20%" style="font-size:120%;padding-left:35px;font-weight:bold;">选择新鲜事模板模块:</td>'
              + '<td width="80%" style="font-size:120%;">'
              + '头像:<input type="checkbox" name="tpl_avatar" style="margin-right:15px">'
              + '触发人:<input type="checkbox" name="tpl_actor" style="margin-right:15px">'
              + '标题:<input type="checkbox" name="tpl_title" style="margin-right:15px">'
              + '内容:<input type="checkbox" name="tpl_mcontent" style="margin-right:15px">'
              + 'lbs:<input type="checkbox" name="tpl_lbs" style="margin-right:15px">'
              + '来源:<input type="checkbox" name="tpl_origin" style="margin-right:15px">'
              + '喜欢按钮:<input type="checkbox" name="tpl_like" style="margin-right:15px">'
              + '分享按钮:<input type="checkbox" name="tpl_share" style="margin-right:15px">'
              + '回复框:<input type="checkbox" name="tpl_reply" style="margin-right:15px"><br>'
              + '删除/关注/忽略等按钮:<input type="checkbox" name="tpl_toolbar" style="margin-right:15px">'
              + '查看相似新鲜事链接:<input type="checkbox" name="tpl_similar" style="margin-right:15px">'
              + '</td></tr></table></td></tr>');

  this.tplPreview_ = $(
                '<tr>'
              //以下为新鲜事预览图部分
              + '  <td width="40%" class="tplPreview" valign="top">'
              + '    <article>'
              + '      <aside>'
              + '        <figure>'
              + '          <img width="50" src="http://head.xiaonei.com/photos/0/0/men_tiny.gif"/>'
              + '          <div class="tplVipHat"></div>'
              + '        </figure>'
              + '      </aside>'
              + '      <h3>'
              + '        <span class="tplActor">触发人</span>'
              + '        <img src="http://a.xnimg.cn/n/core/feed/cssimg/feed-vip-23-05.png" id="preview_vipIcon">'
              + '        <img src="http://a.xnimg.cn/imgpro/icons/ambassador.png" id="preview_mbassadorIcon"/>'
              + '        <img src="http://a.xnimg.cn/imgpro/icons/school-channel.gif" id="preview_choolAmbIcon"/>'
              + '        <img src="http://xnimg.cn/imgpro/icons/follow.gif" width="13px" id="preview_ageIcon">'
              + '        <span class ="tplTitleStaticText">(标题)</span>'
              + '      </h3>'
              + '      <div class="tplContent">'
              + '        <span class="tplContentNormalImg">'
              + '          <img  width="100" src="content-share-eg.jpg"/>'
              + '          <p class="tplContentAudioBtn"></p>'
              + '        </span>'
              + '        <p class="tplContentBigImg">'
              + '          <img  width="300" src="content-share-eg.jpg"/>'
              + '        </p>'
              + '        <p class="tplContentTitle">(内容标题)</p>'
              + '        <p class="tplContentDesc">(内容描述)</p>'
              + '        <p id="preview_contentPsourceTitle">所属:&nbsp;<span class="tplContentPsourceTitle">(父业务标题)</span></p>'
              + '        <p id="preview_contentPsourceUsername">来自:&nbsp;<span class="tplContentPsourceUsername">(来源人名字)</span></p>'
              + '        <span class="tplContentCustom">自定义</span>'
              + '      </div>'
              + '      <div class="tplLbs">'
              + '        <div>'
              + '          <img src="http://a.xnimg.cn/imgpro/icons/lbs-new.png"/>在'
              + '          <span>某地点</span>'
              + '        </div>'
              + '      </div>'
              + '      <div class="tplDetail">'
              + '        <div class="tpllegend">'
              + '          <span class="tplTime">10分钟前</span>&nbsp;'
              + '          <span class="tplOrigin">通过某来源发布'
              + '            <img class="tplOriginIcon" width="15px" src="http://app.xnimg.cn/application/20110527/15/00/LGAds116a018153.gif"/>'
              + '          </span>'
              + '          <span class="tplShareBtn">分享</span>'
              + '          <span class="tplSeparator">|</span>'
              + '          <span class="tplLikeBtn">喜欢</span>'
              + '        </div>'
              + '        <div id="preview_reply">'
              + '          <div style="margin-right:30px;margin-top:5px;">'
              + '            <div class="tplReply">'
              + '              <span class="tplReplyAvatar">'
              + '                <img src="http://head.xiaonei.com/photos/0/0/men_tiny.gif" />'
              + '              </span>'
              + '              <div class="tplReplyMainbody">'
              + '                <p class="tplReplyContent">'
              + '                  <span>回复者</span>:'
              + '                  <span>回复内容</span>'
              + '                </p>'
              + '                <p class="tplReplyTime">'
              + '                  <span>2012-03-08 14:40</span>'
              + '                </p>'
              + '              </div>'
              + '            </div>'
              + '            <div class="tplMoreReply">'
              + '              <span>还有1条回复</span>'
              + '            </div>'
              + '            <div class="tplReply">'
              + '              <span class="tplReplyAvatar">'
              + '                <img src="http://head.xiaonei.com/photos/0/0/men_tiny.gif"/>'
              + '              </span>'
              + '              <div class="tplReplyMainbody">'
              + '                <p class="tplReplyContent">'
              + '                  <span>回复者</span>:'
              + '                  <span>回复内容</span>'
              + '                </p>'
              + '                <p class="tplReplyTime">'
              + '                  <span>2012-03-08 15:40</span>'
              + '                </p>'
              + '              </div>'
              + '            </div>'
              + '          </div>'
              + '          <div class="tplReplyTextarea">'
              + '            <span class="tplReplyTextareaAvatar">'
              + '              <img src="http://head.xiaonei.com/photos/0/0/men_tiny.gif"/>'
              + '              <textarea>评论...</textarea>'
              + '            </span>'
              + '            <div class="tplReplyOption">'
              + '              <div class="tplReplyOption-l">'
              + '                <span class="tplReplyOptionEmotion"></span>'
              + '                <span class="tplReplyOptionMention"></span>'
              + '                <span class="tplReplyShareBtn">'
              + '                  <input type="checkbox" style="float:left;margin:0 3px 0 0;">'
              + '                  <span style="float:left;">同时分享</span>'
              + '                </span>'
              + '              </div>'
              + '              <div class="tplReplyOption-r">'
              + '                <span class="tplReplyOptionPublishBtn">评论</span>'
              + '                <span class="tplReplyOptionMaxlen">5/140</span>'
              + '              </div>'
              + '            </div>'
              + '          </div>'
              + '        </div>'
              + '      </div>'
              + '      <div class="tplHideBtn">'
              + '        <span class="tplToolbarBtn"></span>'
              + '        <span class="tplDelBtn"></span>'
              + '      </div>'
              + '      <div class="tplSimilar">查看另外2条相似的新鲜事</div>'
              + '    </article>'
              + '  </td>'

              //以下是各模块属性配置部分
              + '  <td valign="top">'
              + '    <table border="0" style="font-size:120%;">'
              /*
              + '      <tr id="tplAvatarSet" >'
              + '        <td  style="padding:10px 0px 10px 10px;" width="80px">'
              + '          <span style="font-weight:bold;">头像设置:</span>'
              + '        </td>'
              + '        <td>'
              + '          <input type="checkbox" name="checkAvatarHat">需要VIP帽子'
              + '        </td>'
              + '      </tr>'
              + '      <tr id="tplActorSet">'
              + '        <td style="padding:10px 0px 10px 10px;" width="80px">'
              + '          <span style="font-weight:bold;">触发人设置:</span>'
              + '        </td>'
              + '        <td>'
              + '          <input type="checkbox" name="checkActorVipIcon">需要VIP标志&nbsp;'
              + '          <input type="checkbox" name="checkActorSchoolIcon">需要校园大使标志&nbsp;'
              + '          <input type="checkbox" name="checkActorAmbIcon">需要推广大使标志&nbsp;'
              + '          <input type="checkbox" name="checkActorPageIcon">需要公共主页标志'
              + '        </td>'
              + '      </tr>'
              */
              + '      <tr id="mset_titleSet">'
              + '        <td style="padding:10px 0px 10px 10px;" width="80px">'
              + '          <span style="font-weight:bold;">标题设置:</span>'
              + '        </td>'
              + '        <td>'
              + '          <input type="checkbox" name="checkTitleComment">显示发新鲜事时的评论'
              + '        </td>'
              + '      </tr>'
              + '      <tr id="mset_contentSet">'
              + '        <td style="padding:10px 0px 10px 10px;" width="80px">'
              + '          <span style="font-weight:bold;">内容设置:</span>'
              + '        </td>'
              + '        <td>'
              + '          <input type="checkbox" name="checkMContentBackground">灰色背景&nbsp;'
              + '          <input type="checkbox" name="checkMContentImg">图片'
              + '          (<input type="checkbox" name="checkMContentImgPlayBtn">需要播放按钮'
              + '          <select name="checkMContentImgPlayBtnType">'
              + '            <option value="0">无交互按钮</option>'
              + '            <option value="1">播放音乐按钮</option>'
              + '          </select>)&nbsp;'
              + '          <input type="checkbox" name="checkMContentTitle">标题&nbsp;'
              + '          <input type="checkbox" name="checkMContentDesc">描述&nbsp;'
              + '          <input type="checkbox" name="checkMContentParentTitle">父业务标题&nbsp;'
              + '          <input type="checkbox" name="checkMContentOriginUserName">来源人名字&nbsp;'
              + '          <input type="checkbox" name="checkMContentPhotoOnly">纯照片新鲜事(大图)&nbsp;'
              + '          <input type="checkbox" name="checkMContentCustom">完全自定义'
              + '        </td>'
              + '      </tr>'
              + '      <tr id="mset_originSet">'
              + '        <td style="padding:10px 0px 10px 10px;" width="80px">'
              + '          <span style="font-weight:bold;">来源设置:</span>'
              + '        </td>'
              + '        <td>'
              + '          <input type="checkbox" name="checkOriginIcon">需要图标'
              + '        </td>'
              + '      </tr>'
              + '      <tr id="mset_replySet">'
              + '        <td style="padding:10px 0px 10px 10px;" width="80px">'
              + '          <span style="font-weight:bold;">回复框设置:</span>'
              + '        </td>'
              + '        <td>'
              + '          <input type="checkbox" name="checkReplyEmotion">需要表情&nbsp;'
              + '          <input type="checkbox" name="checkReplyMention">需要@&nbsp;'
              + '          <input type="checkbox" name="checkReplyShare">需要同时分享&nbsp;'
              + '          <br>回复请求的URI&nbsp;<select name="tplReplyUri">'
              + '            <option value="1">普通</option>'
              + '            <option value="2">PAGE日志</option>'
              + '            <option value="3">PAGE相册</option>'
              + '            <option value="4">PAGE状态</option>'
              + '            <option value="5">小站</option>'
              + '          </select>'
              + '        </td>'
              + '      </tr>'
              + '    </table>'
              + '  </td>'
              + '</tr>');

  this.tplValSet_ = $(
                '<tr>'
              + '<td colspan="2" class="tplValSet">'
              + '<div>'
              + '  <div class="tplValSet1 folded">模板变量设置</div>'
              + '  <div id="vset_title" style="float:left;width:800px;"><div class="tplValSet2 folded">标题</div>'
              + '    <div id="vset_title_static" class="tplValSet3">静态文本:&nbsp;'
              + '      <input type="text" name="vset_title_static">'
              + '    </div>'
              + '    <div id="vset_title_comment" class="tplValSet3">用户评论:&nbsp;'
              + '      '
              + '    </div>'
              + '  </div>'
              + '  <div id="vset_content" style="float:left;width:800px;"><div class="tplValSet2 folded">内容</div>'
              + '    <div id="vset_content_img_src" class="tplValSet3">图片src:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_content_img_url" class="tplValSet3">点击图片跳转链接:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_content_title_text" class="tplValSet3">标题内容:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_content_title_url" class="tplValSet3">标题URL:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_content_desc_text" class="tplValSet3">描述内容:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_content_psource_text" class="tplValSet3">父业务标题内容:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_content_psource_url" class="tplValSet3">父业务标题URL:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_content_from_id" class="tplValSet3">来源人id:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_content_from_name" class="tplValSet3">来源人名字:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_content_from_url" class="tplValSet3">来源人URL:&nbsp;'
              /*
              + '      <input type="text" name="tplValSetUseStaticContentOriginUserUrl" title="使用输入" class="useStaticText">|'
              + '      <input type="text" name="tplValSetUseFieldContentOriginUserUrl" title="使用字段" class="useField">'
              */
              + '    </div>'
              + '    <div id="vset_content_custom" class="tplValSet3"><div>自定义:&nbsp;</div>'
              + '        <textarea rows="14" name="vset_content_custom"></textarea>'
              + '    </div>'
              + '  </div>'
              + '  <div id="vset_reply" style=":float:left;width:800px;"><div class="tplValSet2 folded">回复</div>'
              + '    <div id="vset_reply_replyType" class="tplValSet3">replyType:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_reply_replyTypeId" class="tplValSet3">replyTypeId:&nbsp;'
              + '      '
              + '    </div>'
              + '  </div>'
              + '  <div id="vset_lbs" style=":float:left;width:800px;"><div class="tplValSet2 folded">回复</div>'
              + '    <div id="vset_reply_replyType" class="tplValSet3">replyType:&nbsp;'
              + '      '
              + '    </div>'
              + '    <div id="vset_reply_replyTypeId" class="tplValSet3">replyTypeId:&nbsp;'
              + '      '
              + '    </div>'
              + '  </div>'
              + '</div>'
              + '</td>'
              + '</tr>'
              );
              
              
  this.tpl_ =  $('<tr class="expanded-row" style="display:none;"><td colspan="2">'
              + '<textarea width="80%" rows="30" readonly style="background-color:#EEEEEE;">' + decodeURIComponent(tpl_content) + '</textarea>'
              + '<ul style="margin-left:80%;padding-left:2px;list-style:circle;">'
              + '<input type="button" name="tplGenerator" value="生成模板" style="border:1px outset #00008;"/><br/>'
              + '<div class="admin-only hidden"><input type="checkbox" name="tplCustom" ><label for="tplCustom">模板完全自定义</label></div><br/>'
              + '<a href="http://www.clearsilver.net/docs/man_templates.hdf" target="_blank">clearsilver模板语言文档</a><br/> <br/>'
              + '<div id="tplSendTest" style="margin-bottom:11px;"><span style="font-weight:bold;">一键测试发送:</span> 发送给<br/>'
              + '<input type="text" name="tplSendTestUid" size="8" />&nbsp;&nbsp;'
              + '<input type="button" name="tplSendTestSend" value="发送" style="border:1px outset #00008;"/>'
              + '</div>'
              + '<b>默认变量</b><li>新鲜事id : &lt?cs var:id ?&gt </li>' 
              + '<li>新鲜事小类型 : &lt?cs var:stype ?&gt </li>'
              + '<li>source值 : &lt?cs var:source ?&gt </li>'
              + '<li>在列表中的位置: &lt?cs var:feedIndex ?&gt </li>'
              + '<li>是否是newsfeed : &lt?cs var:isNewsFeed ?&gt </li>'
              + '<li>是否是自己的新鲜事 : &lt?cs var:isSelf ?&gt </li>'
              + '<li>当前用户id : &lt?cs var:userID ?&gt </li>'
              + '<li>当前用户name : &lt?cs var:userName ?&gt </li>'
              + '<li>自己点赞的次数: &lt?cs var:selfzancount ?&gt </li>'
              + '<li>所有人点赞的次数: &lt?cs var:totalzancount ?&gt </li>'
              + '<li>统计信息: &lt?cs var:vType ?&gt </li></ul>'
              + '<ul style="margin-left:80%;padding-left:2px;list-style:circle;"><b>include文件内容(utf8编码)</b>'
              + '<li><a href="/include-AVATAR.txt" target="_blank">AVATAR</a> : 头像等信息</li>' 
              + '<li><a href="/include-SOURCE.txt" target="_blank">SOURCE</a> : 新鲜事发布来源信息</li>' 
              + '<li><a href="/include-TOOLBAR.txt" target="_blank">TOOLBAR</a> : 删除/关注/忽略等按钮</li>' 
              + '<li><a href="/include-SIMILAR.txt" target="_blank">SIMILAR</a> : 查看相似新鲜事链接</li>' 
              + '<li><a href="/include-REPLY.txt" target="_blank">REPLY</a> : 新鲜事回复</li>' 
              + '</ul>'
              + '</td></tr>');
  
  var T = this;
  $('#toggle-span', this.dom_).click(
    function() {
      if ($(this).hasClass('folded')) {
        if(!$('input[name=tplCustom]', T.tpl_).attr("checked")) {
          T.tplModule_.show();
          T.tplPreview_.show();
          T.tplValSet_.show();
        }
        $("input[name=tplValSetUseStaticImgNode]", T.tplValSet_).hide();
        $("#tplValSetTitleSet, #tplValSetContentSet, #tplValSetReplySet", T.tplValSet_).hide();
        T.tpl_.css('display', '');
        if(g_user_right > 2) {
          $('.admin-only', T.tpl_).removeClass('hidden');
        }
        $(this).removeClass('folded').addClass('expanded')
      } else {
        T.tplModule_.hide();
        T.tplPreview_.hide();
        T.tplValSet_.hide();
        T.tpl_.css('display', 'none');
        $(this).removeClass('expanded').addClass('folded')
      }
    }
  );
  
  // tplModule_中复选框的事件处理
  for(var i=0; i<this.moduleNames_.length; ++i) {
    var moduleName = this.moduleNames_[i];
    $('input[name=tpl_' + moduleName + ']', this.tplModule_).change(function(){
      if($(this).attr("checked")) {
        switch($(this).attr('name').substring('tpl_'.length)) {
          case 'avatar': $("figure, #tplAvatarSet", T.tplPreview_).show(); break;
          case 'actor': $(".tplActor, #tplActorSet", T.tplPreview_).show(); break;
          case 'title': $(".tplTitleStaticText1, #tplTitleSet", T.tplPreview_).show();
                  if($(".tplValSet1", T.tplValSet_).hasClass('expanded')) {
                    $("#tplValSetTitleSet", T.ValSet_).show();
                    if($("#tplValSetTitleSet div:eq(0)", T.ValSet_).hasClass('folded')) {
                      $("#tplValSetTitleSet div:eq(0)", T.ValSet_).removeClass('folded').addClass('expanded');
                    }
                    T.tplValSetShowTitle();
                  }
                  break;
          case 'mcontent': $(".tplContent, #tplContentSet", T.tplPreview_).show();
                  T.showContent();
                  if($(".tplValSet1", T.tplValSet_).hasClass('expanded')) {
                    $("#tplValSetContentSet", T.ValSet_).show();
                    T.tplValSetShowContent();
                    if($("#tplValSetContentSet div:eq(0)", T.tplValSet_).hasClass('folded')) {
                      $("#tplValSetContentSet div:eq(0)", T.tplValSet_).removeClass('folded').addClass('expanded');
                    }
                  }
                  break;
          case 'lbs': $(".tplLbs", T.tplPreview_).show(); break;
          case 'origin': if($("input[name=checkOriginIcon]", T.tplPreview_).attr("checked")) {
                    $(".tplOriginIcon", T.tplPreview_).show();
                  }
                  $(".tplOrigin, #tplOriginSet", T.tplPreview_).show();
                  break;
          case 'like': $(".tplLikeBtn", T.tplPreview_).show();
                  if($('input[name=tpl_share]', T.tplModule_).attr("checked")) {
                    $(".tplSeparator", T.tplPreview_).show();
                  }
                  break;
          case 'share': $(".tplShareBtn", T.tplPreview_).show();
                  if($('input[name=tpl_like]', T.tplModule_).attr("checked")) {
                    $(".tplSeparator", T.tplPreview_).show();
                  }
                  break;
          case 'reply': $("#tplReply, #tplReplySet", T.tplPreview_).show();
                  if($('input[name=checkReplyEmotion]', T.tplPreview_).attr("checked")) $(".tplReplyOptionEmotion", T.tplPreview_).show();
                  if($('input[name=checkReplyMention]', T.tplPreview_).attr("checked")) $(".tplReplyOptionMention", T.tplPreview_).show();
                  if($('input[name=checkReplyShare]', T.tplPreview_).attr("checked")) $(".tplReplyShareBtn", T.tplPreview_).show();
                  if($(".tplValSet1", T.tplValSet_).hasClass('expanded')) {
                    $("#tplValSetReplySet, #tplValSetReplyType, #tplValSetReplyTypeId", T.ValSet_).show();
                    if($("#tplValSetReplySet div:eq(0)", T.tplValSet_).hasClass('folded')) {
                      $("#tplValSetReplySet div:eq(0)", T.tplValSet_).removeClass('folded').addClass('expanded');
                    }
                  }
                  break;
          case 'toolbar': $(".tplHideBtn", T.tplPreview_).show(); break;
          case 'similar': $(".tplSimilar", T.tplPreview_).show(); break;
          default: break;
        }
      } else {
        switch($(this).attr('name').substring('tpl_'.length)) {
          case 'avatar': $("figure, #tplAvatarSet", T.tplPreview_).hide(); break;
          case 'actor': $(".tplActor, #tplActorSet", T.tplPreview_).hide(); break;
          case 'title': $(".tplTitleStaticText1, .tplTitleLink1, .tplTitleStaticText2, .tplTitleLink2, .tplTitleCustom, #tplTitleSet", T.tplPreview_).hide();
                  $("#tplValSetTitleSet", T.ValSet_).hide(); break;
          case 'mcontent': $(".tplContent, #tplContentSet", T.tplPreview_).hide();
                  $("#tplValSetContentSet", T.ValSet_).hide(); break;
          case 'lbs': $(".tplLbs", T.tplPreview_).hide(); break;
          case 'origin': $(".tplOrigin, #tplOriginSet", T.tplPreview_).hide(); break;
          case 'like': $(".tplLikeBtn", T.tplPreview_).hide();
                  if($('input[name=tpl_share]', T.tplModule_).attr("checked")) {
                    $(".tplSeparator", T.tplPreview_).hide();
                  }
                  break;
          case 'share': $(".tplShareBtn, .tplSeparator", T.tplPreview_).hide(); break;
          case 'reply': $(".tplReplyOptionEmotion, .tplReplyOptionMention, .tplReplyShareBtn, #tplReply, #tplReplySet", T.tplPreview_).hide();
                  $("#tplValSetReplySet", T.ValSet_).hide();
                  break;
          case 'toolbar': $(".tplHideBtn", T.tplPreview_).hide(); break;
          case 'similar': $(".tplSimilar", T.tplPreview_).hide(); break;
          default: break;
        }
      }
    });
  }

  $('input[name=checkAvatarHat]', this.tplPreview_).change(function(){
      if($('input[name=checkAvatarHat]', T.tplPreview_).attr("checked")) {
        $(".tplVipHat", T.tplPreview_).show();
      } else {
        $(".tplVipHat", T.tplPreview_).hide();
      }
  });

  // 触发人设置选项复选框的事件处理
  var checkActorNames = ["VipIcon", "SchoolIcon", "AmbIcon", "PageIcon"];
  for(var i=0; i<checkActorNames.length; ++i) {
    checkActorName = checkActorNames[i];
    $('input[name=checkActor' + checkActorName + ']', this.tplPreview_).change(function(){
      if($(this).attr('checked')) {
        switch($(this).attr('name').substring('checkActor'.length)) {
          case 'VipIcon': $("#tplVipIcon", T.tplPreview_).show(); break;
          case 'SchoolIcon': $("#tplSchoolAmbIcon", T.tplPreview_).show(); break;
          case 'AmbIcon': $("#tplAmbassadorIcon", T.tplPreview_).show(); break;
          case 'PageIcon': $("#tplPageIcon", T.tplPreview_).show(); break;
          default: break;
        }
      } else {
        switch($(this).attr('name').substring('checkActor'.length)) {
          case 'VipIcon': $("#tplVipIcon", T.tplPreview_).hide(); break;
          case 'SchoolIcon': $("#tplSchoolAmbIcon", T.tplPreview_).hide(); break;
          case 'AmbIcon': $("#tplAmbassadorIcon", T.tplPreview_).hide(); break;
          case 'PageIcon': $("#tplPageIcon", T.tplPreview_).hide(); break;
          default: break;
        }
      }
    });
  }

  $('select[name=tplTitleStyle]', this.tplPreview_).change(function(){
      var titleStyle = parseInt($('select[name=tplTitleStyle]',T.tplPreview_).val());
      $(".tplTitleStaticText1, .tplTitleLink1, .tplTitleStaticText2, .tplTitleLink2, .tplTitleCustom", this.tplPreview_).hide();
      if(titleStyle == 1) {
        $(".tplTitleStaticText1", this.tplPreview_).show();
      } else if(titleStyle == 2){
        $(".tplTitleStaticText1, .tplTitleLink1", this.tplPreview_).show();
      } else if(titleStyle == 3){
        $(".tplTitleStaticText1, .tplTitleLink1, .tplTitleStaticText2", this.tplPreview_).show();
      } else if(titleStyle == 4){
        $(".tplTitleStaticText1, .tplTitleLink1, .tplTitleStaticText2, .tplTitleLink2", this.tplPreview_).show();
      } else if(titleStyle == 0){
        $(".tplTitleCustom", this.tplPreview_).show();
      }
      if($(".tplValSet1", T.tplValSet_).hasClass('expanded') && $("#tplValSetTitleSet div:eq(0)", T.tplValSet_).hasClass('expanded')) {
        T.tplValSetShowTitle();
      }
  });

  //内容设置选项复选框的事件处理
  var checkMContentNames = ["Background", "Photo", "PhotoPlayBtn", "Title", "Desc", "ParentTitle", "OriginUserName", "PhotoOnly", "Custom"];
  for(var i=0; i<checkMContentNames.length; ++i) {
    var checkMContentName = checkMContentNames[i];
    $('input[name=checkMContent' + checkMContentName + ']', T.tplPreview_).change(function(){
      if($(this).attr("checked")) {
        switch($(this).attr("name").substring('checkMContent'.length)) {
          case 'Background': T.tplContentSet_ = T.tplContentSet_ | 0x1; break;
          case 'Photo': T.tplContentSet_ = T.tplContentSet_ | 0x2; break;
          case 'Title': T.tplContentSet_ = T.tplContentSet_ | 0x10; break;
          case 'Desc': T.tplContentSet_ = T.tplContentSet_ | 0x20; break;
          case 'ParentTitle': T.tplContentSet_ = T.tplContentSet_ | 0x40; break;
          case 'OriginUserName': T.tplContentSet_ = T.tplContentSet_ | 0x80; break;
          case 'PhotoOnly': T.tplContentSet_ = T.tplContentSet_ | 0x100; break;
          case 'Custom': T.tplContentSet_ = T.tplContentSet_ | 0x200; break;
          default: break;
        }
      } else {
        switch($(this).attr("name").substring('checkMContent'.length)) {
          case 'Background': T.tplContentSet_ = T.tplContentSet_ & 0xFFFFFFFE; break;
          case 'Photo': T.tplContentSet_ = T.tplContentSet_ & 0xFFFFFFFD; break;
          case 'Title': T.tplContentSet_ = T.tplContentSet_ & 0xFFFFFFEF; break;
          case 'Desc': tplContentSet_ = tplContentSet_ & 0xFFFFFFDF; break;
          case 'ParentTitle': T.tplContentSet_ = T.tplContentSet_ & 0xFFFFFFBF; break;
          case 'OriginUserName': T.tplContentSet_ = T.tplContentSet_ & 0xFFFFFF7F; break;
          case 'PhotoOnly': T.tplContentSet_ = T.tplContentSet_ & 0xFFFFFEFF; break;
          case 'Custom': T.tplContentSet_ = T.tplContentSet_ & 0xFFFFFDFF; break;
          default: break;
        }
      }
      if($(".tplValSet1", T.tplValSet_).hasClass('expanded') && $("#tplValSetContentSet div:eq(0)", T.tplValSet_).hasClass('expanded')) {
        T.tplValSetShowContent();
      }
      T.showContent();
    });
  }

  $('input[name=checkMContentPhotoPlayBtn]', this.tplPreview_).change(function(){
      if($('input[name=checkMContentPhotoPlayBtn][value=1]', this.tplPreview_).attr("checked")) {
        T.tplContentSet_ = (T.tplContentSet_ & 0xFFFFFFF3) | 0x4;
      } else if($('input[name=checkMContentPhotoPlayBtn][value=2]', this.tplPreview_).attr("checked")) {
        T.tplContentSet_ = (T.tplContentSet_ & 0xFFFFFFF3) | 0x8;
      } else {
        T.tplContentSet_ = T.tplContentSet_ & 0xFFFFFFF3;
      }
      T.showContent();
  });

  var otherCheckNames = ["OriginIcon", "ReplyEmotion", "ReplyMention", "ReplyShare"];
  for(var i=0; i<otherCheckNames.length; ++i) {
    var otherCheckName = otherCheckNames[i];
    $('input[name=check' + otherCheckName + ']', T.tplPreview_).change(function(){
      if($(this).attr("checked")) {
        switch($(this).attr("name").substring('check'.length)) {
          case 'OriginIcon': $('.tplOriginIcon', T.tplPreview_).show(); break;
          case 'ReplyEmotion': $('.tplReplyOptionEmotion', T.tplPreview_).show(); break;
          case 'ReplyMention': $('.tplReplyOptionMention', T.tplPreview_).show(); break;
          case 'ReplyShare': $('.tplReplyShareBtn', T.tplPreview_).show(); break;
          default: break;
        }
      } else {
        switch($(this).attr("name").substring('check'.length)) {
          case 'OriginIcon': $('.tplOriginIcon', T.tplPreview_).hide(); break;
          case 'ReplyEmotion': $('.tplReplyOptionEmotion', T.tplPreview_).hide(); break;
          case 'ReplyMention': $('.tplReplyOptionMention', T.tplPreview_).hide(); break;
          case 'ReplyShare': $('.tplReplyShareBtn', T.tplPreview_).hide(); break;
          default: break;
        }
      }
    });
  }

  var tplValSetUseStaticTextCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  function tplValSetUseStaticText(name, prefix, index) {
    tplValSetUseStaticTextCount[index] += 1;
    var fields = '<span id="' + prefix + tplValSetUseStaticTextCount[index].toString() + '" class="tplValSetForm"><input type="text"  name="' + prefix + tplValSetUseStaticTextCount[index].toString() + '" size="10"><em id="' + prefix + tplValSetUseStaticTextCount[index].toString() + 'Del" class="tplValSetDel">(删除)</em>';
    var element = $(fields).insertBefore($("input[name=" + name + "]", T.tplValSet_));
    element.mouseover(function(){
      $("em", element).show();
    });
    element.mouseout(function(){
      $("em", element).hide();
    });
    $("em", element).click(function(){
      element.remove();
    });
  }

  $("input[name=tplValSetUseStaticTitleStaticText1]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticTitleStaticText1", "tplTitleStaticText1Static", 0);});
  $("input[name=tplValSetUseStaticTitleStaticText2]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticTitleStaticText2", "tplTitleStaticText2Static", 1);});
  $("input[name=tplValSetUseStaticLinkTitle1]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticLinkTitle1", "tplTitleLinkTitle1Static", 2);});
  $("input[name=tplValSetUseStaticLinkUrl1]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticLinkUrl1", "tplTitleLinkUrl1Static", 3);});
  $("input[name=tplValSetUseStaticLinkTitle2]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticLinkTitle2", "tplTitleLinkTitle2Static", 4);});
  $("input[name=tplValSetUseStaticLinkUrl2]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticLinkUrl2", "tplTitleLinkUrl2Static", 5);});
  $("input[name=tplValSetUseStaticContentTitleText]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticContentTitleText", "tplContentTitleTextStatic", 6);});
  $("input[name=tplValSetUseStaticContentTitleUrl]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticContentTitleUrl", "tplContentTitleUrlStatic", 7);});
  $("input[name=tplValSetUseStaticContentDescText]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticContentDescText", "tplContentDescTextStatic", 8);});
  $("input[name=tplValSetUseStaticContentPtitleText]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticContentPtitleText", "tplContentPtitleTextStatic", 9);});
  $("input[name=tplValSetUseStaticContentPtitleUrl]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticContentPtitleUrl", "tplContentPtitleUrlStatic", 10);});
  $("input[name=tplValSetUseStaticContentOriginUserName]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticContentOriginUserName", "tplContentOriginUserNameStatic", 11);});
  $("input[name=tplValSetUseStaticContentOriginUserUrl]", this.tplValSet_).click(function(){
    tplValSetUseStaticText("tplValSetUseStaticContentOriginUserUrl", "tplContentOriginUserUrlStatic", 12);});

  var tplValSetUseFieldCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  function tplValSetUseField(name, prefix, index) {
    tplValSetUseFieldCount[index] += 1;
    var fields = '<span id="' + prefix + tplValSetUseFieldCount[index].toString() + '" class="tplValSetForm"><select name="' + prefix + tplValSetUseFieldCount[index].toString() + '">';
    for(var i in top_keys_includeNode) {
      fields += '<option value="' + top_keys_includeNode[i] + '">' + top_keys_includeNode[i] + '</option>'
    }
    fields += '</select><em id="' + prefix + tplValSetUseFieldCount[index].toString() +'Del" class="tplValSetDel">(删除)</em><em id="' + prefix + tplValSetUseFieldCount[index].toString() +'Flush" class="tplValSetFlush">(刷新)</em>';
    var element = $(fields).insertBefore($("input[name=" + name + "]", T.tplValSet_));
    element.mouseover(function(){
      $("em", element).show();
    });
    element.mouseout(function(){
      $("em", element).hide();
    });
    element.bind("click", function(e){
      if(e.target.id.lastIndexOf("Del") != -1) {
        $(e.target).parent().remove();
      } else if(e.target.id.lastIndexOf("Flush") != -1) {
        var flushfields = "";
        for(var i in top_keys_includeNode) {
          flushfields += '<option value="' + top_keys_includeNode[i] + '">' + top_keys_includeNode[i] + '</option>'
        }
        $("select", $(e.target).parent()).html(flushfields);
      }
    });
  }

  $("input[name=tplValSetUseFieldTitleStaticText1]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticTitleStaticText1", "tplTitleStaticText1Field", 0);});
  $("input[name=tplValSetUseFieldTitleStaticText2]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticTitleStaticText2", "tplTitleStaticText2Field", 1);});
  $("input[name=tplValSetUseFieldLinkTitle1]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticLinkTitle1", "tplTitleLinkTitle1Field", 2);});
  $("input[name=tplValSetUseFieldLinkUrl1]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticLinkUrl1", "tplTitleLinkUrl1Field", 3);});
  $("input[name=tplValSetUseFieldLinkTitle2]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticLinkTitle2", "tplTitleLinkTitle2Field", 4);});
  $("input[name=tplValSetUseFieldLinkUrl2]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticLinkUrl2", "tplTitleLinkUrl2Field", 5);});
  $("input[name=tplValSetUseFieldImgNode]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticImgNode", "tplContentImgNodeField", 6);});
  $("input[name=tplValSetUseFieldContentTitleText]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticContentTitleText", "tplContentTitleTextField", 7);});
  $("input[name=tplValSetUseFieldContentTitleUrl]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticContentTitleUrl", "tplContentTitleUrlField", 8);});
  $("input[name=tplValSetUseFieldContentDescText]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticContentDescText", "tplContentDescTextField", 9);});
  $("input[name=tplValSetUseFieldContentPtitleText]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticContentPtitleText", "tplContentPtitleTextField", 10);});
  $("input[name=tplValSetUseFieldContentPtitleUrl]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticContentPtitleUrl", "tplContentPtitleUrlField", 11);});
  $("input[name=tplValSetUseFieldContentOriginUserName]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticContentOriginUserName", "tplContentOriginUserNameField", 12);});
  $("input[name=tplValSetUseFieldContentOriginUserUrl]", this.tplValSet_).click(function(){
    tplValSetUseField("tplValSetUseStaticContentOriginUserUrl", "tplContentOriginUserUrlField", 13);});

  $(".tplValSet1", T.tplValSet_).click(function(){
    if($(this).hasClass('folded')) {
      $("#tplValSetTitleSet, #tplValSetContentSet, #tplValSetReplySet", T.tplValSet_).hide();
      if($("input[name=tpl_title]", T.tplModule_).attr("checked")) {
        $("#tplValSetTitleSet", T.tplValSet_).show();
        T.tplValSetShowTitle();
        if($("#tplValSetTitleSet div:eq(0)", T.tplValSet_).hasClass('folded')) {
          $("#tplValSetTitleSet div:eq(0)", T.tplValSet_).removeClass('folded').addClass('expanded');
        }
      }
      if($("input[name=tpl_mcontent]", T.tplModule_).attr("checked")) {
        $("#tplValSetContentSet", T.tplValSet_).show();
        T.tplValSetShowContent();
        if($("#tplValSetContentSet div:eq(0)", T.tplValSet_).hasClass('folded')) {
          $("#tplValSetContentSet div:eq(0)", T.tplValSet_).removeClass('folded').addClass('expanded');
        }
      }
      if($("input[name=tpl_reply]", T.tplModule_).attr("checked")) {
        $("#tplValSetReplySet", T.tplValSet_).show();
        $("#tplValSetReplyType, #tplValSetReplyTypeId", T.tplValSet_).show();
        if($("#tplValSetReplySet div:eq(0)", T.tplValSet_).hasClass('folded')) {
          $("#tplValSetReplySet div:eq(0)", T.tplValSet_).removeClass('folded').addClass('expanded');
        }
      }
      $(this).removeClass('folded').addClass('expanded');
    } else {
      $("#tplValSetTitleSet, #tplValSetContentSet, #tplValSetReplySet", T.tplValSet_).hide();
      $(this).removeClass('expanded').addClass('folded');
    }
  });

  $("#tplValSetTitleSet div:eq(0)", this.tplValSet_).click(function(){
    if($(this).hasClass('folded')) {
      T.tplValSetShowTitle();
      $(this).removeClass('folded').addClass('expanded');
    } else {
      $("#tplValSetTitleStaticText1, #tplValSetTitleStaticText2, #tplValSetTitleLinkTitle1, #tplValSetTitleLinkUrl1, #tplValSetTitleLinkTitle2, #tplValSetTitleLinkUrl2, #tplValSetTitleCustom", T.tplValSet_).hide();
      $(this).removeClass('expanded').addClass('folded');
    }
  });

  $("#tplValSetContentSet div:eq(0)", this.tplValSet_).click(function(){
    if($(this).hasClass('folded')) {
      T.tplValSetShowContent();
      $(this).removeClass('folded').addClass('expanded');
    } else {
      $("#tplValSetContentImgNode, #tplValSetContentTitleText, #tplValSetContentTitleUrl, #tplValSetContentDescText, #tplValSetContentPtilteText, #tplValSetContentPtitleUrl, #tplValSetContentOriginUserName, #tplValSetContentOriginUserUrl, #tplValSetContentCustom", T.tplValSet_).hide();
      $(this).removeClass('expanded').addClass('folded');
    }
  });

  $("#tplValSetReplySet div:eq(0)", this.tplValSet_).click(function(){
    if($(this).hasClass('folded')) {
      $("#tplValSetReplyType, #tplValSetReplyTypeId", T.tplValSet_).show();
      $(this).removeClass('folded').addClass('expanded');
    } else {
      $("#tplValSetReplyType, #tplValSetReplyTypeId", T.tplValSet_).hide();
      $(this).removeClass('expanded').addClass('folded');
    }
  });

  function getValSet(node) {
    var val = "";
    var size = $("span", node).size();
    for(var i = 0; i < size; i++) {
      var inputNode = $("span:eq(" + i.toString() + ") > input", node);
      if(inputNode.val()) {
        if(i == 0) {
          val += ' "' + inputNode.val() + '"';
        } else {
          val += ' + "' + inputNode.val() + '"';
        }
      } else {
        var selectNode = $("span:eq(" + i.toString() + ") > select", node);
        if(selectNode.val()) {
          if(i == 0) {
            val += ' f.' + (selectNode.val().indexOf("(") == -1 ? (selectNode.val()) : (selectNode.val().substring(0, selectNode.val().indexOf("("))));
          } else {
            val += ' + f.' + (selectNode.val().indexOf("(") == -1 ? (selectNode.val()) : (selectNode.val().substring(0, selectNode.val().indexOf("("))));
          }
        }
      }
    }
    return val;
  }
 
  $('input[name=tplGenerator]', this.tpl_).click(function(){
    var tpl = '';
    tpl += '<article id="newsfeed-<?cs var:id ?>" class="a-feed">\n';
    if($("input[name=tpl_avatar]", T.tplModule_).attr("checked")) {
      if($("input[name=checkAvatarHat]", T.tplPreview_).attr("checked")) {
        tpl += '<?cs set:needAvatarHat = "1" ?>\n';
      }
      tpl += '<?cs include:AVATAR ?>\n';
    }
    tpl += '<h3>\n';
    if($("input[name=tpl_actor]", T.tplModule_).attr("checked")) {
      if($("input[name=checkActorVipIcon]", T.tplPreview_).attr("checked")) {
        tpl += '<?cs set:needActorVipIcon = "1" ?>\n';
      }
      if($("input[name=checkActorSchoolIcon]", T.tplPreview_).attr("checked")) {
        tpl += '<?cs set:needActorSchoolIcon = "1" ?>\n';
      }
      if($("input[name=checkActorAmbIcon]", T.tplPreview_).attr("checked")) {
        tpl += '<?cs set:needActorAmbIcon = "1" ?>\n';
      }
      if($("input[name=checkActorPageIcon]", T.tplPreview_).attr("checked")) {
        tpl += '<?cs set:needActorPageIcon = "1" ?>\n';
      }
      tpl += '<?cs include:ACTOR ?>\n';
    }
    if($("input[name=tpl_title]", T.tplModule_).attr("checked")) {
      var tplTitleStyle = $("select[name=tplTitleStyle]", T.tplPreview_).val();
      if(tplTitleStyle == 0) {
        tpl += $("textarea[name=tplTitleCustom]", T.tplValSet_).val() + '\n';
      } else {
        tpl += '<?cs set:titleStyle = #' + tplTitleStyle.toString() + ' ?>\n';
        if(tplTitleStyle > 0) {
          tpl += '<?cs set:tplTitleStaticText1 = ' + getValSet($("#tplValSetTitleStaticText1", T.tplValSet_)) + ' ?>\n';
        }
        if(tplTitleStyle > 1) {
          tpl += '<?cs set:tplTitleLinkName1 = ' + getValSet($("#tplValSetTitleLinkTitle1", T.tplValSet_)) + ' ?>\n';
          tpl += '<?cs set:tplTitleLinkUrl1 = ' + getValSet($("#tplValSetTitleLinkUrl1", T.tplValSet_)) + ' ?>\n';
        }
        if(tplTitleStyle > 2) {
          tpl += '<?cs set:tplTitleStaticText2 = ' + getValSet($("#tplValSetTitleStaticText2", T.tplValSet_)) + ' ?>\n';
        }
        if(tplTitleStyle > 3) {
          tpl += '<?cs set:tplTitleLinkName2 = ' + getValSet($("#tplValSetTitleLinkTitle2", T.tplValSet_)) + ' ?>\n';
          tpl += '<?cs set:tplTitleLinkUrl2 = ' + getValSet($("#tplValSetTitleLinkUrl2", T.tplValSet_)) + ' ?>\n';
        }
        tpl += '<?cs include:TITLE ?>\n';
      }
    }
    tpl += '</h3>\n<div class="content">\n';
    if($("input[name=tpl_mcontent]", T.tplModule_).attr("checked")) {
      if($("input[name=checkMContentCustom]", T.tplPreview_).attr("checked")) {
        tpl += $("textarea[name=tplContentCustom]", T.tplValSet_).val() + '\n';
      } else if($("input[name=checkMContentPhotoOnly]", T.tplPreview_).attr("checked")) {
        tpl += '<?cs set:tplMContentPhotoOnly = #1 ?>\n';
        tpl += '<?cs def:generateTplMContent(tplMContentPhoto) ?>\n';
        tpl += '<?cs include:CONTENT ?>\n<?cs /def ?>\n';
        tpl += '<?cs call:generateTplMContent(' + getValSet($("#tplValSetContentImgNode", T.tplValSet_)) + ') ?>\n';
      } else {
        if($("input[name=checkMContentBackground]", T.tplPreview_).attr("checked")) {
          tpl += "<?cs set:tplMContentBackground = #1 ?>\n";
        }
        if($("input[name=checkMContentTitle]", T.tplPreview_).attr("checked")) {
          tpl += '<?cs set:tplMContentTitleText = ' + getValSet($("#tplValSetContentTitleText", T.tplValSet_)) + ' ?>\n';
          tpl += '<?cs set:tplMContentTitleLink = ' + getValSet($("#tplValSetContentTitleUrl", T.tplValSet_)) + ' ?>\n';
        }
        if($("input[name=checkMContentDesc]", T.tplPreview_).attr("checked")) {
          tpl += '<?cs set:tplMContentDescText = ' + getValSet($("#tplValSetContentDescText", T.tplValSet_)) + ' ?>\n';
        }
        if($("input[name=checkMContentParentTitle]", T.tplPreview_).attr("checked")) {
          tpl += '<?cs set:tplMContentParentTitleText = ' + getValSet($("#tplValSetContentPtilteText", T.tplValSet_)) + ' ?>\n';
          tpl += '<?cs set:tplMContentParentTitleLink = ' + getValSet($("#tplValSetContentPtitleUrl", T.tplValSet_)) + ' ?>\n';
        }
        if($("input[name=checkMContentOriginUserName]", T.tplPreview_).attr("checked")) {
          tpl += '<?cs set:tplMContentOriginUserName = ' + getValSet($("#tplValSetContentOriginUserName", T.tplValSet_)) + ' ?>\n';
          tpl += '<?cs set:tplMContentParentTitleLink = ' + getValSet($("#tplValSetContentOriginUserUrl", T.tplValSet_)) + ' ?>\n';
        }
        if($("input[name=checkMContentPhoto]", T.tplPreview_).attr("checked")) {
          if($("input[name=checkMContentPhotoPlayBtn][value=1]", T.tplPreview_).attr("checked")) {
            tpl += '<?cs set:tplMContentPhotoPlayBtn = #1 ?>\n';
          } else if($("input[name=checkMContentPhotoPlayBtn][value=2]", T.tplPreview_).attr("checked")) {
            tpl += '<?cs set:tplMContentPhotoPlayBtn = #2 ?>\n';
          } else {
            tpl += '<?cs set:tplMContentPhotoPlayBtn = #0 ?>\n';
          }
          tpl += '<?cs def:generateTplMContent(tplMContentPhoto) ?>\n';
        }
        tpl += '<?cs include:CONTENT ?>\n';
        if($("input[name=checkMContentPhoto]", T.tplPreview_).attr("checked")) {
          tpl += '<?cs /def ?>\n';
          tpl += '<?cs call:generateTplMContent(' + getValSet($("#tplValSetContentImgNode", T.tplValSet_)) + ') ?>\n';
        }
      }
    }
    tpl += '</div>\n';
    if($("input[name=tpl_lbs]", T.tplModule_).attr("checked")) {
      tpl += '<?cs include:LBS ?>\n';
    }
    tpl += '<div class="details">\n<div class="legend">\n<span class="duration"><?cs var:x_rfeedtime(f.time) ?></span>\n';
    if($("input[name=tpl_origin]", T.tplModule_).attr("checked")) {
      tpl += '<?cs include:SOURCE ?>\n';
    }
    if($("input[name=tpl_share]", T.tplModule_).attr("checked")) {
      tpl += '<?cs include:SHAREBTN ?>\n';
    }
    if($("input[name=tpl_like]", T.tplModule_).attr("checked")) {
      if($("input[name=tpl_share]", T.tplModule_).attr("checked")) {
        tpl += '<span class="seperator">|</span>\n';
      }
      tpl += '<?cs include:LIKEBTN ?>\n';
    }
    tpl += '</div>\n';
    if($("input[name=tpl_reply]", T.tplModule_).attr("checked")) {
      tpl += '<?cs set:replyType = "' + $("input[name=tplReplyReplyType]", T.tplValSet_).val() + '" ?>\n';
      tpl += '<?cs set:replyTypeId = "' + $("input[name=tplReplyReplyTypeId]", T.tplValSet_).val() + '" ?>\n';
      if($("input[name=checkReplyEmotion]", T.tplPreview_).attr("checked")) {
        tpl += '<?cs set:replyTextArea_showEmotionBtn = "1" ?>\n';
      }
      if($("input[name=checkReplyMention]", T.tplPreview_).attr("checked")) {
        tpl += '<?cs set:replyTextArea_showAtBtn = "1" ?>\n';
      }
      if($("input[name=checkReplyShare]", T.tplPreview_).attr("checked")) {
        tpl += '<?cs set:replyTextArea_showShareBtn = "1" ?>\n';
      }
      tpl += '<?cs set:replyTextArea_maxLen = "140" ?>\n';
      if($("select[name=tplReplyUri]", T.tplValSet_).val() == 1) {
        tpl += '<?cs set:replyURI_common = "1" ?>\n';
      } else if($("select[name=tplReplyUri]", T.tplValSet_).val() == 2) {
        tpl += '<?cs set:replyURI_pageBlog = "1" ?>\n';
      } else if($("select[name=tplReplyUri]", T.tplValSet_).val() == 3) {
        tpl += '<?cs set:replyURI_pageAlbum = "1" ?>\n';
      } else if($("select[name=tplReplyUri]", T.tplValSet_).val() == 4) {
        tpl += '<?cs set:replyURI_pageDoing = "1" ?>\n';
      } else if($("select[name=tplReplyUri]", T.tplValSet_).val() == 5) {
        tpl += '<?cs set:replyURI_zhan = "1" ?>\n';
      }
      tpl += '<?cs include:REPLY_2 ?>\n</div>\n';
    }
    if($("input[name=tpl_toolbar]", T.tplModule_).attr("checked")) {
      tpl += '<?cs include:TOOLBAR ?>\n';
    }
    if($("input[name=tpl_similar]", T.tplModule_).attr("checked")) {
      tpl += '<?cs include:SIMILAR ?>\n';
    }
    tpl += '</article>\n';
    $("textarea", T.tpl_).val(tpl);
  });

  $("input[name=tplCustom]", T.tpl_).click(function(){
    if($("input[name=tplCustom]", T.tpl_).attr("checked")) {
      $("textarea", T.tpl_).removeAttr("readonly");
      $("textarea", T.tpl_).css('background-color', '#FFFFFF');
      T.tplModule_.hide();
      T.tplPreview_.hide();
      T.tplValSet_.hide();
    } else {
      $("textarea", T.tpl_).attr('readonly', 'readonly');
      $("textarea", T.tpl_).css('background-color', '#F7F7F7');
      T.tplModule_.show();
      T.tplPreview_.show();
      T.tplValSet_.show();
    }
  });

  $("input[name=tplSendTestUid]", T.tpl_).keyup(function(){
    var uid = $("input[name=tplSendTestUid]", T.tpl_).val().toString();
    var index = uid.search(/[^0-9]/);
    if(index != -1) {
      alert("uid请输入数字");
      $("input[name=tplSendTestUid]", T.tpl_).val(uid.substring(0, index));
    }
  });

  $("input[name=tplSendTestSend]", T.tpl_).click(function(){
    if($("input[name=tplSendTestUid]", T.tpl_).val() == 0) {
      alert("请输入用户id!");
    } else {
      if(keysAndTestVal.indexOf("version=") != 0 && keysAndTestVal.indexOf("&stype=") == -1) {
        keysAndTestVal = "version=" + g_version.toString() + "&" + keysAndTestVal;
      }
      if(keysAndTestVal.indexOf("stype=") != 0 && keysAndTestVal.indexOf("&stype=") == -1) {
        keysAndTestVal = "stype=" + g_stype.toString() + "&" + keysAndTestVal;
      }
      if(keysAndTestVal.indexOf("&time=")) {
        var index = keysAndTestVal.indexOf("&time=");
        var index2 = keysAndTestVal.indexOf("&", index + "&time=".length);
        keysAndTestVal = keysAndTestVal.substring(0, index + "&time=".length) + (new Date()).getTime().toString() + keysAndTestVal.substring(index2);
      }
      var actor = $("input[name=tplSendTestUid]", T.tpl_).val();
      if(keysAndTestVal.indexOf("&from.id=") != -1) {
        var index = keysAndTestVal.indexOf("&from.id=");
        var index2 = keysAndTestVal.indexOf("&", index + "&from.id=".length);
        keysAndTestVal = keysAndTestVal.substring(0, index + "&from.id=".length) + actor + keysAndTestVal.substring(index2);
      }
      if(keysAndTestVal.indexOf("&from.tinyimg=") != -1) {
        var index = keysAndTestVal.indexOf("&from.tinyimg=");
        var index2 = keysAndTestVal.indexOf("&", index + "&from.tinyimg=".length);
        keysAndTestVal = keysAndTestVal.substring(0, index + "&from.tinyimg=".length) + encodeURIComponent("http://head.xiaonei.com/photos/0/0/men_tiny.gif") + keysAndTestVal.substring(index2);
      }
      if($("#tplValSetContentImgNode > span:eq(0) > select", T.tplValSet_).val()) {
        var imgSrc = $("#tplValSetContentImgNode > span:eq(0) > select", T.tplValSet_).val();
        imgSrc = imgSrc.substring(0, imgSrc.indexOf("(")) + ".0.src";
        var index = keysAndTestVal.indexOf("&" + imgSrc + "=");
        if(index != -1) {
          var index2 = keysAndTestVal.indexOf("&", index + ("&" + imgSrc + "=").length);
          keysAndTestVal = keysAndTestVal.substring(0, index + ("&" + imgSrc + "=").length) + encodeURIComponent("http://fmn.rrimg.com/fmn060/20111230/1030/p_large_NLsa_485400007f271261.jpg") + keysAndTestVal.substring(index2);
        }
      }

      $.ajax({
        type: "POST",
        url: "/send-test",
        data: keysAndTestVal,
        'success' : function(text){
          alert(text);
        },
        'error' : function(xmlReq, textStatus) {
          alert(textStatus);
          alert("发送失败");
        }
      });
    }
  });

  $('#tpl-view-status', T.dom_).val(status);
  
  $('#tpl-status-edit', this.dom_).click(function() {
      if (!confirm("该操作会影响到线上新鲜事。确定要" + $(this).html() + "吗?")) {
        return;
      }
      if ($(this).html() == '保存') {
        $.ajax('/update-tpl-view-status?tpl_id=' + g_tpl_id + '&view=' + T.view_ + '&status=' + $('#tpl-view-status', T.dom_).val(), {
          'success' : function(text){
            alert(text);
            $(this).html('修改');
            $('#tpl-view-status', T.dom_).attr('disabled', true);
          },
          'error' : function() {
            alert('保存失败');
          }
        });
      } else {
        $(this).html('保存');
        $('#tpl-view-status', T.dom_).attr('disabled', false);
      }
    });

  $('#validate-template', this.dom_).click(function() {
      var view_type = view;
      var textarea = $('textarea', T.tpl_);
      return function() {
        var stype_id = $('#edit-tpl span.stype_id').text();
        var version = $('#edit-tpl span.stype_version').text();
        var tpl = textarea.val();
        var url = '/validate-tpl?stype=' + stype_id + '&version=' + version;
        $.ajax(url, {
          type: 'POST',
          data: 'tpl=' + encodeURIComponent(encodeURIComponent(tpl)), 
          context: document.body,
          success: function(msg){
            alert(decodeURIComponent(msg));
          },
          error: function(){
            alert('验证出错');
          }
        });
      };
    }());
  
  $('#save-template', this.dom_).click(function() {
      var view_type = view;
      var textarea = $('textarea', T.tpl_);
      return function() {
        var stype_id = $('#edit-tpl span.stype_id').text();
        var version = $('#edit-tpl span.stype_version').text();
        var tpl = textarea.val();
        var url = '/save-tpl?tpl_id=' + g_tpl_id
            + '&view=' + view_type;
        // alert(textarea.val());

        var tplSettingData = "tpl_id=" + g_tpl_id + '&view=' + view_type + "&";
        var module = 0;
        for(var i=0; i<T.moduleNames_.length; ++i) {
          module = ($("input[name=tpl_" + T.moduleNames_[i] + "]", T.tplModule_).attr("checked") ? module | Math.pow(2, i) : module);
        }
        tplSettingData += "module=" + module.toString() + "&";
        var avatar = 0;
        var avatarSettings = ["checkAvatarHat"];
        for(var i=0; i<avatarSettings.length; ++i) {
          avatar = ($("input[name=" + avatarSettings[i] + "]", T.tplPreview_).attr("checked") ? avatar | Math.pow(2, i) : avatar);
        }
        tplSettingData += "avatar=" + avatar.toString() + "&";
        var actor = 0;
        var actorSettings = ["checkActorVipIcon", "checkActorSchoolIcon", "checkActorAmbIcon", "checkActorPageIcon"];
        for(var i=0; i<actorSettings.length; ++i) {
          actor = ($("input[name=" + actorSettings[i] + "]", T.tplPreview_).attr("checked") ? actor | Math.pow(2, i) : actor);
        }
        tplSettingData += "actor=" + actor.toString() + "&";
        var title = parseInt($("select[name=tplTitleStyle]", T.tplPreview_).val());
        tplSettingData += "title=" + title.toString() + "&";
        var content = 0;
        var contentSettings = ["checkMContentBackground", "checkMContentPhoto", "checkMContentPhotoPlayBtn", "checkMContentTitle", "checkMContentDesc", "checkMContentParentTitle", "checkMContentOriginUserName", "checkMContentPhotoOnly", "checkMContentCustom"];
        for(var i=0; i<contentSettings.length; ++i) {
          if(i < 2) {
            content = ($("input[name=" + contentSettings[i] + "]", T.tplPreview_).attr("checked") ? content | Math.pow(2, i) : content);
          } else if(i == 2) {
            content = content | (parseInt($("input[name=" + contentSettings[i] + "]", T.tplPreview_).val()) * Math.pow(2, i));
          } else {
            content = ($("input[name=" + contentSettings[i] + "]", T.tplPreview_).attr("checked") ? content | Math.pow(2, i+1) : content);
          }
        }
        tplSettingData += "content=" + content.toString() + "&";
        var lbs = 0;
        var source = 0;
        var sourceSetting = ["checkOriginIcon"];
        for(var i=0; i<sourceSetting.length; ++i) {
          source = ($("input[name=" + sourceSetting[i] + "]", T.tplPreview_).attr("checked") ? source | Math.pow(2, i) : source);
        }
        var like = 0;
        var share = 0;
        tplSettingData += "lbs=" + lbs.toString() + "&source=" + source.toString() + "&like=" + like.toString() + "&share=" + share.toString() + "&";
        var reply = 0;
        var replySettings = ["checkReplyEmotion", "checkReplyMention", "checkReplyShare", "tplReplyUri"];
        for(var i=0; i<replySettings.length; ++i) {
          if(i == 3) {
            reply += parseInt($("select[name=" + replySettings[i] + "]", T.tplPreview_).val()) * Math.pow(2, 3);
          } else {
            reply = ($("input[name=" + replySettings[i] + "]", T.tplPreview_).attr("checked") ? reply | Math.pow(2, i) : reply);
          }
        }
        tplSettingData += "reply=" + reply.toString() + "&";
        var toolbar = 0;
        var similar = 0;
        tplSettingData += "toolbar=" + toolbar.toString() + "&similar=" + similar.toString() + "&";
        
        var titleValXml = "<titleVal>";
        for(var i=0; i < T.valSetTitleCtrl_.length; ++i) {
          if( i != T.valSetTitleCtrl_.length - 1) {
            titleValXml += "<valset name=\"" + T.valSetTitleCtrl_[i] + "\">";
          }
          $("span > input, span > select, textarea", $("#" + T.valSetTitleCtrl_[i], T.tplValSet_)).each(function(){
            if($(this).attr("name").indexOf("Field") != -1 && $(this).val().length != 0) {
              titleValXml += "<val type=\"field\">" + $(this).val() + "</val>";
            } else if($(this).attr("name").indexOf("Custom") != -1 && $(this).val().length != 0){
              tplSettingData += "tplValSetTitleCustom=" + encodeURIComponent(encodeURIComponent($(this).val())) + "&";
            } else if($(this).val().length != 0){
              titleValXml += "<val type=\"static\">" + encodeURIComponent(encodeURIComponent($(this).val())) + "</val>";
            }
          });
          if( i != T.valSetTitleCtrl_.length - 1) {
            titleValXml += "</valset>";
          }
        }
        titleValXml += "</titleVal>";
        tplSettingData += "titleVals=" + titleValXml + "&";
        
        var contentValXml = "<contentVal>"
        for(var i=0; i < T.valSetContentCtrl_.length; ++i) {
          if(i != T.valSetContentCtrl_.length - 1) {
            contentValXml += "<valset name=\"" + T.valSetContentCtrl_[i] + "\">";
          }
          $("span > input, span > select, textarea", $("#" + T.valSetContentCtrl_[i], T.tplValSet_)).each(function(){
            if($(this).attr("name").indexOf("Field") != -1 && $(this).val().length != 0) {
              contentValXml += "<val type=\"field\">" + $(this).val() + "</val>";
            } else if($(this).attr("name").indexOf("Custom") != -1 && $(this).val().length != 0){
              tplSettingData += "tplValSetContentCustom=" + encodeURIComponent(encodeURIComponent($(this).val())) + "&";
            } else if($(this).val().length != 0){
              contentValXml += "<val type=\"static\">" + encodeURIComponent(encodeURIComponent($(this).val())) + "</val>";
            }
          });
          if(i != T.valSetContentCtrl_.length - 1) {
            contentValXml += "</valset>";
          }
        }
        contentValXml += "</contentVal>";
        tplSettingData += "contentVals=" + contentValXml + "&";
        
        tplSettingData += "tplValSetReplyType=" + $("#tplValSetReplyType input[name=tplReplyReplyType]", T.tplValSet_).val() + "&";
        tplSettingData += "tplValSetReplyTypeId=" + $("#tplValSetReplyTypeId input[name=tplReplyReplyTypeId]", T.tplValSet_).val() + "&";
        
        tplSettingData = tplSettingData.substring(0, tplSettingData.length-1);
        
        $.ajax(url, {
          type: 'POST',
          data: 'tpl=' + encodeURIComponent(encodeURIComponent(tpl)),
          context: document.body,
          success: function(msg){
            alert(msg);
          },
          error: function(){
            alert('保存出错');
          }
        });

        $.ajax({
          type: 'POST',
          url: '/save-tpl-setting',
          data: tplSettingData,
          error : function(xmlReq, textStatus) {
            alert(textStatus);
            alert("保存模板设置失败");
          } 
        });
      };
    }());

  $('#remove-template', this.dom_).click(function() {
      var view_type = view;
      return function() {
        if (!confirm('确定删除该模板吗?')) {
          return;
        }
        var stype_id = $('#edit-tpl span.stype_id').text();
        var version = $('#edit-tpl span.stype_version').text();
        var url = '/remove-tpl?tpl_id=' + g_tpl_id + '&view=' + view_type;
        $.ajax(url, {
          context: $(this).parent().parent(),
          success: function(msg){
            alert(msg);
            $(this).remove();
            var option = $('<option value="' + view_type + '">' + $('span.view-desc', $(this)).text() + '</option>');
            $("#add-template-view").append(option);
          },
          error: function(){
            alert('删除模板失败');
          }
        });
      };
    }());
}

TplListItem.prototype.moduleNames_ = ["avatar", "actor", "title", "mcontent", "lbs", "origin", "like", "share", "reply", "toolbar", "similar"];
TplListItem.prototype.tplContentSet_ = 0;
TplListItem.prototype.valSetTitleCtrl_ = ["tplValSetTitleStaticText1", "tplValSetTitleStaticText2", "tplValSetTitleLinkTitle1", "tplValSetTitleLinkUrl1", "tplValSetTitleLinkTitle2", "tplValSetTitleLinkUrl2", "tplValSetTitleCustom"];
TplListItem.prototype.valSetContentCtrl_ = ["tplValSetContentImgNode", "tplValSetContentTitleText", "tplValSetContentTitleUrl", "tplValSetContentDescText", "tplValSetContentPtilteText", "tplValSetContentPtitleUrl", "tplValSetContentOriginUserName", "tplValSetContentOriginUserUrl", "tplValSetContentCustom"];

TplListItem.prototype.tplValSetShowTitle = function(){
  $("#tplValSetTitleStaticText1, #tplValSetTitleStaticText2, #tplValSetTitleLinkTitle1, #tplValSetTitleLinkUrl1, #tplValSetTitleLinkTitle2, #tplValSetTitleLinkUrl2, #tplValSetTitleCustom", this.tplValSet_).hide();
  var tplTitleStyle = $("select[name=tplTitleStyle]", this.tplPreview_).val();
  if(tplTitleStyle == "1") {
    $("#tplValSetTitleStaticText1", this.tplValSet_).show();
  } else if(tplTitleStyle == "2") {
    $("#tplValSetTitleStaticText1, #tplValSetTitleLinkTitle1, #tplValSetTitleLinkUrl1", this.tplValSet_).show();
  } else if(tplTitleStyle == "3") {
    $("#tplValSetTitleStaticText1, #tplValSetTitleLinkTitle1, #tplValSetTitleLinkUrl1, #tplValSetTitleStaticText2", this.tplValSet_).show();
  } else if(tplTitleStyle == "4") {
    $("#tplValSetTitleStaticText1, #tplValSetTitleLinkTitle1, #tplValSetTitleLinkUrl1, #tplValSetTitleStaticText2, #tplValSetTitleLinkTitle2, #tplValSetTitleLinkUrl2", this.tplValSet_).show();
  } else if(tplTitleStyle == "0") {
    $("#tplValSetTitleCustom", this.tplValSet_).show();
  }
}

TplListItem.prototype.tplValSetShowContent = function(){
  $("#tplValSetContentImgNode, #tplValSetContentTitleText, #tplValSetContentTitleUrl, #tplValSetContentDescText, #tplValSetContentPtilteText, #tplValSetContentPtitleUrl, #tplValSetContentOriginUserName, #tplValSetContentOriginUserUrl, #tplValSetContentCustom", this.tplValSet_).hide();
  if($("input[name=checkMContentCustom]", this.tplPreview_).attr("checked")) {
    $("#tplValSetContentCustom", this.tplValSet_).show();
  } else if($("input[name=checkMContentPhotoOnly]", this.tplPreview_).attr("checked")) {
    $("#tplValSetContentImgNode", this.tplValSet_).show();
  } else {
    if($("input[name=checkMContentPhoto]", this.tplPreview_).attr("checked")) {
      $("#tplValSetContentImgNode", this.tplValSet_).show();
    }
    if($("input[name=checkMContentTitle]", this.tplPreview_).attr("checked")) {
      $("#tplValSetContentTitleText, #tplValSetContentTitleUrl", this.tplValSet_).show();
    }
    if($("input[name=checkMContentDesc]", this.tplPreview_).attr("checked")) {
      $("#tplValSetContentDescText", this.tplValSet_).show();
    }
    if($("input[name=checkMContentParentTitle]", this.tplPreview_).attr("checked")) {
      $("#tplValSetContentPtilteText, #tplValSetContentPtitleUrl", this.tplValSet_).show();
    }
    if($("input[name=checkMContentOriginUserName]", this.tplPreview_).attr("checked")) {
      $("#tplValSetContentOriginUserName, #tplValSetContentOriginUserUrl", this.tplValSet_).show();
    }
  }
}

TplListItem.prototype.showContent =  function () {
  if(this.tplContentSet_ & 0x200) {
    $(".tplContentNormalImg, .tplContentBigImg, .tplContentTitle, .tplContentDesc, #tplContentPsourceTitle, #tplContentPsourceUsername", this.tplPreview_).hide();
    $("input[name=checkMContentBackground], input[name=checkMContentPhoto], input[name=checkMContentPhotoPlayBtn], input[name=checkMContentTitle], input[name=checkMContentDesc], input[name=checkMContentParentTitle], input[name=checkMContentOriginUserName], input[name=checkMContentPhotoOnly]", this.tplPreview_).attr("disabled", true);
    $(".tplContent", this.tplPreview_).css({"height":"100px", "padding-top":"0px", "padding-left": "0px", "background-color":"#FFFFFF"});
    $(".tplContentCustom", this.tplPreview_).show();
    return;
  }
  if(this.tplContentSet_ & 0x100) {
    $("input[name=checkMContentPhotoOnly]", this.tplPreview_).attr("disabled", false);
    $(".tplContentNormalImg, .tplContentTitle, .tplContentDesc, #tplContentPsourceTitle, #tplContentPsourceUsername, .tplContentCustom", this.tplPreview_).hide();
    $("input[name=checkMContentBackground], input[name=checkMContentPhoto], input[name=checkMContentPhotoPlayBtn], input[name=checkMContentTitle], input[name=checkMContentDesc], input[name=checkMContentParentTitle], input[name=checkMContentOriginUserName]", this.tplPreview_).attr("disabled", true);
    $(".tplContent", this.tplPreview_).css({"height":"230px", "padding-top":"0px", "padding-left": "0px", "background-color":"#FFFFFF"});
    $(".tplContentBigImg", this.tplPreview_).show();
    return;
  }
  $(".tplContentCustom, .tplContentBigImg", this.tplPreview_).hide();
  $("input[name=checkMContentBackground], input[name=checkMContentPhoto], input[name=checkMContentTitle], input[name=checkMContentDesc], input[name=checkMContentParentTitle], input[name=checkMContentOriginUserName], input[name=checkMContentPhotoOnly]", this.tplPreview_).attr("disabled", false);
  $("input[name=checkMContentPhotoPlayBtn]", this.tplPreview_).attr("disabled", true);
  if(this.tplContentSet_ & 0x1) {
    $(".tplContent", this.tplPreview_).css("background-color", "#F7F7F7");
    $(".tplContent", this.tplPreview_).css({"padding-top":"8px", "padding-left": "8px"});
  } else {
    $(".tplContent", this.tplPreview_).css("background-color", "#FFFFFF");
    $(".tplContent", this.tplPreview_).css({"padding-top":"0px", "padding-left": "0px"});
  }
  if(this.tplContentSet_ & 0x2) {
    $(".tplContentNormalImg", this.tplPreview_).show();
    $("input[name=checkMContentPhotoPlayBtn]", this.tplPreview_).attr("disabled", false);
    if(this.tplContentSet_ & 0x4) {
      $(".tplContentAudioBtn", this.tplPreview_).show();
    } else { 
      $(".tplContentAudioBtn", this.tplPreview_).hide();
    }
    if(this.tplContentSet_ & 0x8) {
      $(".tplContentVideoBtn", this.tplPreview_).show();
    } else {
      $(".tplContentVideoBtn", this.tplPreview_).hide();
    }
  } else {
    $(".tplContentNormalImg", this.tplPreview_).hide();
  }
  if(this.tplContentSet_ & 0x10) {
    $(".tplContentTitle", this.tplPreview_).show();
  } else {
    $(".tplContentTitle", this.tplPreview_).hide();
  }
  if(this.tplContentSet_ & 0x20) {
    $(".tplContentDesc", this.tplPreview_).show();
  } else {
    $(".tplContentDesc", this.tplPreview_).hide();
  }
  if(this.tplContentSet_ & 0x40) {
    $("#tplContentPsourceTitle", this.tplPreview_).show();
  } else {
    $("#tplContentPsourceTitle", this.tplPreview_).hide();
  }
  if(this.tplContentSet_ & 0x80) {
    $("#tplContentPsourceUsername", this.tplPreview_).show();
  } else {
    $("#tplContentPsourceUsername", this.tplPreview_).hide();
  }
  
  var showHeight = this.tplContentSet_ & 0xFFFFFFF2;
  if(showHeight == 0x10 || showHeight == 0x40 || showHeight == 0x80) {
    $(".tplContent", this.tplPreview_).css("height", "20px");
  } else if(showHeight == 0x20 || showHeight == (0x40 + 0x80) || showHeight == (0x10 + 0x40) || showHeight == (0x10 + 0x80)) {
    $(".tplContent", this.tplPreview_).css("height", "40px");
  } else if(showHeight == (0x10 + 0x20) || showHeight == (0x10 + 0x40 + 0x80)) {
    $(".tplContent", this.tplPreview_).css("height", "60px");
  } else {
    $(".tplContent", this.tplPreview_).css("height", "100px");
  }
}

TplListItem.prototype.AddToList = function() {
  $("#add-template-view option[value='" + this.view_ + "']").remove();

  if($('#tpl-list').length <= 0) {
    var n = $('<br/><table width="1000" id="tpl-list"></table>');
    $(document.body).append(n);
  }
  $('#tpl-list').append(this.dom_);
  $('#tpl-list').append(this.tplModule_);
  $('#tpl-list').append(this.tplPreview_);
  $('#tpl-list').append(this.tplValSet_);
  $('#tpl-list').append(this.tpl_);

  this.tplModule_.hide();
  this.tplPreview_.hide();
  this.tplValSet_.hide();
  $("figure, .tplVipHat, .tplActor, #tplVipIcon, #tplAmbassadorIcon, #tplSchoolAmbIcon, #tplPageIcon", this.tplPreview_).hide();
  $(".tplTitleStaticText1, .tplTitleLink1, .tplTitleStaticText2, .tplTitleLink2, .tplTitleCustom", this.tplPreview_).hide();
  $(".tplContent, .tplLbs", this.tplPreview_).hide();
  $(".tplOrigin, .tplOriginIcon, .tplShareBtn, .tplSeparator, .tplLikeBtn", this.tplPreview_).hide();
  $("#tplReply, .tplReplyOptionEmotion, .tplReplyOptionMention, .tplReplyShareBtn, .tplSimilar, .tplHideBtn", this.tplPreview_).hide();
  $("#tplAvatarSet, #tplActorSet, #tplTitleSet, #tplContentSet, #tplOriginSet, #tplReplySet", this.tplPreview_).hide();

  var tpl_settings;
  $.ajax('/get-tpl-setting?tpl_id=' + g_tpl_id + '&view=' + this.view_, {
    type: 'post',
    async: false,
    success : function(text) {
      if(text) {
        tpl_settings = eval('(' + text + ')');
      }
    },
    error : function() {
      alert('加载模板设置失败, 请刷新页面');
    }
  });
  
  if(tpl_settings) {
    var module = parseInt(tpl_settings['module']);
    for(var i=0; i < this.moduleNames_.length; ++i) {
      var checked = false;
      checked = module & Math.pow(2, i) ? true : false;
      $("input[name=tpl_" + this.moduleNames_[i] + "]", this.tplModule_).attr("checked", checked);
      if(checked) {
        switch(i) {
          case 0: $("figure, #tplAvatarSet", this.tplPreview_).show(); break;
          case 1: $(".tplActor, #tplActorSet", this.tplPreview_).show(); break;
          case 2: $("#tplTitleSet", this.tplPreview_).show();
                  break;
          case 3: $(".tplContent, #tplContentSet", this.tplPreview_).show(); break;
          case 4: $(".tplLbs", this.tplPreview_).show(); break;
          case 5: $(".tplOrigin, #tplOriginSet", this.tplPreview_).show(); break;
          case 6: $(".tplLikeBtn", this.tplPreview_).show();
                  if(module & Math.pow(2, 7)) $(".tplSeparator", this.tplPreview_).show();
                  break;
          case 7: $(".tplShareBtn", this.tplPreview_).show(); break;
          case 8: $("#tplReply, #tplReplySet", this.tplPreview_).show(); break;
          case 9: $(".tplHideBtn", this.tplPreview_).show(); break;
          case 10: $(".tplSimilar", this.tplPreview_).show(); break;
          default: break;
        }
      }
    }

    var avatar = parseInt(tpl_settings['avatar']);
    var avatarSettings = ["checkAvatarHat"];
    for(var i=0; i<avatarSettings.length; ++i) {
      avatar & Math.pow(2, i) ? $("input[name=tpl_" + avatarSettings[i] + "]", this.tplPreview_).attr("checked", true) : $("input[name=tpl_" + avatarSettings[i] + "]", this.tplPreview_).attr("checked", false);
    }
    
    var actor = parseInt(tpl_settings['actor']);
    var actorSettings = ["checkActorVipIcon", "checkActorSchoolIcon", "checkActorAmbIcon", "checkActorPageIcon"];
    for(var i=0; i<actorSettings.length; ++i) {
      actor & Math.pow(2, i) ? $("input[name=tpl_" + actorSettings[i] + "]", this.tplPreview_).attr("checked", true) : $("input[name=tpl_" + actorSettings[i] + "]", this.tplPreview_).attr("checked", false);
    }
    
    var titleStyle = parseInt(tpl_settings['title']);
    $("select[name=tplTitleStyle]", this.tplPreview_).val(tpl_settings['title']);
    if(titleStyle == 0) {
      $("article h3 .tplTitleCustom", this.tplPreview_).show();
    }
    if(titleStyle >= 1) {
      $("article h3 .tplTitleStaticText1", this.tplPreview_).show();
    }
    if(titleStyle >= 2) {
      $("article h3 .tplTitleLink1", this.tplPreview_).show();
    }
    if(titleStyle >= 3) {
      $("article h3 .tplTitleStaticText2", this.tplPreview_).show();
    }
    if(titleStyle >= 4) {
      $("article h3 .tplTitleLink2", this.tplPreview_).show();
    }
    
    var content = parseInt(tpl_settings['content']);
    this.tplContentSet_ = content;
    var contentSettings = ["checkMContentBackground", "checkMContentPhoto", "checkMContentPhotoPlayBtn", "checkMContentTitle", "checkMContentDesc", "checkMContentParentTitle", "checkMContentOriginUserName", "checkMContentPhotoOnly", "checkMContentCustom"];
    for(var i=0; i<contentSettings.length; ++i) {
      if(i < 2) {
        content & Math.pow(2, i) ? $("input[name=" + contentSettings[i] + "]", this.tplPreview_).attr("checked", true) : $("input[name="+ contentSettings[i] + "]", this.tplPreview_).attr("checked", false);
      } else if(i == 2) {
        if(content & Math.pow(2, 2)) {
          $("input[name=" + contentSettings[i] + "][value=1]", this.tplPreview_).attr("checked", true);
        } else if(content & Math.pow(2, 3)) {
          $("input[name=" + contentSettings[i] + "][value=2]", this.tplPreview_).attr("checked", true);
        } else {
          $("input[name=" + contentSettings[i] + "][value=0]", this.tplPreview_).attr("checked", true);
        }
      } else {
        content & Math.pow(2, i+1) ? $("input[name=" + contentSettings[i] + "]", this.tplPreview_).attr("checked", true) : $("input[name="+ contentSettings[i] + "]", this.tplPreview_).attr("checked", false);
      }
      this.showContent();
    }
    
    var source = parseInt(tpl_settings['source']);
    var sourceSetting = ["checkOriginIcon"];
    for(var i=0; i < sourceSetting.length; ++i) {
       source & Math.pow(2, i) ? $("input[name=" + sourceSetting[i] + "]", this.tplPreview_).attr("checked", true) : $("input[name=" + sourceSetting[i] + "]", this.tplPreview_).attr("checked", false);
    }
    if(source & Math.pow(2, 0)) $(".tplOriginIcon", this.tplPreview_).show();
    
    var reply = parseInt(tpl_settings['reply']);
    var replySettings = ["checkReplyEmotion", "checkReplyMention", "checkReplyShare", "tplReplyUri"];
    for(var i=0; i < replySettings.length; ++i) {
      if(i == 3) {
        if(Math.floor(reply / 8)  > 0) {
          $("select[name=" + replySettings[i] + "]", this.tplPreview_).val((Math.floor(reply / 8)).toString());
        } else {
          $("select[name=" + replySettings[i] + "]", this.tplPreview_).val("1");
        }
      } else {
        reply & Math.pow(2, i) ? $("input[name=" + replySettings[i] + "]", this.tplPreview_).attr("checked", true) : $("input[name=" + replySettings[i] + "]", this.tplPreview_).attr("checked", false);
      }
    }
    if(reply & Math.pow(2, 0)) $(".tplReplyOptionEmotion", this.tplPreview_).show();
    if(reply & Math.pow(2, 1)) $(".tplReplyOptionMention", this.tplPreview_).show();
    if(reply & Math.pow(2, 2)) $(".tplReplyShareBtn", this.tplPreview_).show();
    
    var titleVals = decodeURIComponent(decodeURIComponent(tpl_settings['titleVals']));
    for(var i=0; i < this.valSetTitleCtrl_.length-1; ++i) {
      var s = 0, f = 0;
      $("valset[name=" + this.valSetTitleCtrl_[i] + "] val", $(titleVals)).each(function(){
        if($(this).attr("type") == "static") {
          if($(this).text().length > 0) {
            $("#" + $(this).parent().attr("name") + " .useStaticText", this.tplValSet_).click();
            ++s;
            $("#" + $(this).parent().attr("name") + " > span > input[name$=Static" + s.toString() + "]", this.tplValSet_).val($(this).text());
          }
        }
        if($(this).attr("type") == "field") {
          if($(this).text().length > 0) {
            $("#" + $(this).parent().attr("name") + " .useField", this.tplValSet_).click();
            ++f;
            $("#" + $(this).parent().attr("name") + " > span > select[name$=Field" + f.toString() + "]", this.tplValSet_).val($(this).text());
          }
        }
      });
    }
    var tplValSetTitleCustom = decodeURIComponent(decodeURIComponent(tpl_settings['tplValSetTitleCustom']));
    if(tplValSetTitleCustom && tplValSetTitleCustom.length > 0) {
      $("#tplValSetTitleCustom textarea", this.tplValSet_).val(tplValSetTitleCustom);
    }
    
    var contentVals = decodeURIComponent(decodeURIComponent(tpl_settings['contentVals']));
    for(var i=0; i < this.valSetContentCtrl_.length-1; ++i) {
      var s = 0, f = 0;
      $("valset[name=" + this.valSetContentCtrl_[i] + "] val", $(contentVals)).each(function(){
        if($(this).attr("type") == "static") {
          if($(this).text().length > 0) {
            $("#" + $(this).parent().attr("name") + " .useStaticText", this.tplValSet_).click();
            ++s;
            $("#" + $(this).parent().attr("name") + " > span > input[name$=Static" + s.toString() + "]", this.tplValSet_).val($(this).text());
          }
        }
        if($(this).attr("type") == "field") {
          if($(this).text().length > 0) {
            $("#" + $(this).parent().attr("name") + " .useField", this.tplValSet_).click();
            ++f;
            $("#" + $(this).parent().attr("name") + " > span > select[name$=Field" + f.toString() + "]", this.tplValSet_).val($(this).text());
          }
        }
      });
    }
    var tplValSetContentCustom = decodeURIComponent(decodeURIComponent(tpl_settings['tplValSetContentCustom']));
    if(tplValSetContentCustom && tplValSetContentCustom.length > 0) {
      $("#tplValSetContentCustom textarea", this.tplValSet_).val(tplValSetContentCustom);
    }
    
    var replyType = tpl_settings["tplValSetReplyType"];
    if(replyType && replyType.length > 0) {
      $("#tplValSetReplyType input[name=tplReplyReplyType]", this.tplValSet_).val(replyType);
    }
    var replyTypeId = tpl_settings["tplValSetReplyTypeId"];
    if(replyTypeId && replyTypeId.length > 0) {
      $("#tplValSetReplyTypeId input[name=tplReplyReplyTypeId]", this.tplValSet_).val(replyTypeId);
    }
  }
}
TplListItem.prototype.Readonly = function() {
  $('textarea', this.tpl_).attr('readonly', 'readonly');
  $('#remove-template, #save-template', this.dom_).css('display', 'none');
  $('input[name=tplGenerator], input[name=tplCustom]', this.tpl_).hide();
}
TplListItem.prototype.HideEditStatus = function() {
  $('#tpl-status-edit', this.dom_).hide();
}

var UserApplyView = function(apply_id) {
  this.apply_id_ = (!isNaN(apply_id) && apply_id > 0) ? apply_id : 0;
  this.dom_ = $('<div><table id="apply-table" width="1200" border="1" class="t1">' +
          '<tr>' +
            '<th colspan="2" style="font-size:20px;">新鲜事申请流程单</th>' +
          '</tr>' +
          '<tr>' +
            '<td width="30">产品：</td>' +
            '<td width="30"><input id="pm-names" type="text"/>例：张三,李四,王五</td>' +
          '</tr>' +
          '<tr>' +
            '<td width="30">产品Email：</td>' +
            '<td width="30">' +
                '<input id="pm-emails" size="50" type="text"/><span class="flag no-mark"></span>' +
                '例：xxx@renren-inc.com,ooo@renren-inc.com(只接受renren-inc.com域名)' +
            '</td>' +
          '</tr>' +
          '<tr>' +
            '<td width="30">开发：</td>' +
            '<td width="30"><input id="dev-names" type="text"/>例：张三,李四,王五</td>' +
          '</tr>' +
          '<tr>' +
            '<td width="30">开发Email：：</td>' +
            '<td width="30">' +
              '<input id="dev-emails" size="50" type="text"/><span class="flag no-mark"></span>' +
              '例：xxx@renren-inc.com,ooo@renren-inc.com(只接受renren-inc.com域名)' +
            '</td>' +
          '</tr>' +
          '<tr>' +
            '<td width="30">申请类型：</td>' +
            '<td><select id="apply_type">' +
                '<option value="1">新建新鲜事类型</option>' +
                '<option value="2">修改新鲜事类型数据格式</option>' +
                '<option value="3">修改新鲜事类型渲染模板</option>' +
             '</td>' +
          '</tr>' +
          '<tr>' +
            '<td>新鲜事类型ID：</td>' +
            '<td colspan="3"><input size="120" type="text" id="feed_stype"/>(不确定请填0)' +
          '</tr>' +
          '<tr>' +
            '<td width="30">新鲜事描述：</td>' +
            '<td width="30"><input id="stype-desc" type="text"/> 例：用户发日志时产生的日志新鲜事, 如果有stype，请指定</td>' +
          '</tr>' +
          '<tr>' +
            '<td width="30">申请描述：</td>' +
            '<td width="30"><textarea id="apply-desc" rows="5" cols="60"></textarea></td>' +
          '</tr>' +
          '<tr>' +
            '<td width="30">是否发NewsFeed？</td>' +
            '<td width="30"><input type="checkbox" id="PushPolicy_news"/></td>' +
          '</tr>' +
           '<tr>' +
            '<td width="30">是否发MiniFeed？</td>' +
            '<td width="30"><input id="PushPolicy_mini" type="checkbox"/></td>' +
          '</tr>' +
           '<tr>' +
             '<td width="30">NewsFeed如何合并或去重？</td>' +
             '<td width="30"><input id="news-merge-desc" size="100" type="text"/></td>' +
          '</tr>' +
           '<tr>' +
             '<td width="30">MiniFeed如何合并或去重？</td>' +
             '<td width="30"><input id="mini-merge-desc" size="100" type="text"/></td>' +
          '</tr>' +
           '<tr>' +
            '<td colspan="2" align="right"><input id="apply-submit" type="button" value="提交申请"/></td>' +
          '</tr>' +
        '</table></div>');
  var email_pat = /^([_a-z0-9.]+@renren-inc[.]com,)*[_a-z0-9.]+@renren-inc\.com$/;
  function ValidateMails(node) {
    var text = node.val();
    console.log(text);
    if(email_pat.test(text)) {
      node.next().addClass('yes-mark').removeClass('no-mark');
    } else {
      node.next().addClass('no-mark').removeClass('yes-mark');
    }
  }

  $('#pm-emails, #dev-emails', this.dom_).keyup(
    function() {
      ValidateMails($(this));
    }
  );

  $('#pm-emails, #dev-emails', this.dom_).each(
    function() {
      ValidateMails($(this));
    }
  );
  var T = this;
  if (!isNaN(apply_id) && apply_id > 0) {
    $.ajax('/get-user-apply-item?apply_id=' + apply_id, {
      'type' : 'GET',
      'async' : false,
      'success' : function(text) {
        var o = $.parseJSON(text);
        if (!o.apply_id) {
          alert('该申请id不存在');
          return;
        }
        var d = T.dom_;
        $('#pm-names', d).val(o.pm_names);
        $('#pm-emails', d).val(o.pm_emails);
        $('#dev-names', d).val(o.dev_names);
        $('#dev-emails', d).val(o.dev_emails);
        $('#feed_stype', d).val(o.feed_stype);
        $('#stype-desc', d).val(o.feed_desc);
        $('#apply-desc', d).val(o.apply_desc);
        $("input:checkbox#PushPolicy_news", d).attr("checked", o.push_news);
        $("input:checkbox#PushPolicy_mini", d).attr("checked", o.push_mini);
        $('#news-merge-desc', d).val(o.news_merge_desc);
        $('#mini-merge-desc', d).val(o.mini_merge_desc);
        $('#lifetime', d).val(o.lifetime);
      },
      'error' : function() {
        alert('加载申请信息出错');
      }
    });
  }

  $('#apply-submit', this.dom_).click(
    function() {
      if ($('#pm-names', this.dom_).val().length <= 0) {
        alert('产品名字字段不能为空');
        return;
      }
      var data = 'pm_names=' + encodeURIComponent($('#pm-names', this.dom_).val());
      if (T.apply_id_ > 0) {
        data += '&apply_id=' + T.apply_id_;
      }

      var pm_emails = $('#pm-emails', this.dom_).val();
      if (pm_emails.length <=0 || !email_pat.test(pm_emails)) {
        alert('产品email字段不合法');
        return;
      }
      data += '&pm_emails=' + pm_emails;

      if ($('#dev-names', this.dom_).val().length <= 0) {
        alert('开发名字字段不能为空');
        return;
      }
      data += '&dev_names=' + encodeURIComponent($('#dev-names', this.dom_).val());

      var dev_emails = $('#dev-emails', this.dom_).val();
      if (dev_emails.length <=0 || !email_pat.test(dev_emails)) {
        alert('开发email字段不合法');
        return;
      }
      data += '&dev_emails=' + dev_emails;

      var feed_stype = $('#feed_stype', this.dom_).val();
      if (isNaN(parseInt(feed_stype))) {
         alert('类型ID字段不合法');
         return;
      }
      data += '&feed_stype=' + feed_stype;

      var feed_desc = $('#stype-desc', this.dom_).val();
      if (feed_desc.length <= 0) {
        alert('新鲜事描述字段不能为空');
        return;
      }
      data += '&feed_desc=' + encodeURIComponent(feed_desc);

      data += '&apply_type=' + $("#apply_type", this.dom_).val();

      var apply_desc = $('#apply-desc', this.dom_).val();
      if (apply_desc.length <= 0) {
        alert('申请描述字段不能为空');
        return;
      }
      data += '&apply_desc=' + encodeURIComponent(apply_desc);

      data += '&push_news=' + ($("input:checkbox#PushPolicy_news", this.dom_).attr("checked") ? 1 : 0);
      data += '&push_mini=' + ($("input:checkbox#PushPolicy_mini", this.dom_).attr("checked") ? 1 : 0);

      var news_merge_desc = $('#news-merge-desc', this.dom_).val();
      if (news_merge_desc.length <= 0) {
        alert('NewsFeed合并策略描述不能为空');
        return;
      }
      data += '&news_merge_desc=' + encodeURIComponent(news_merge_desc);

      var mini_merge_desc = $('#mini-merge-desc', this.dom_).val();
      if (mini_merge_desc.length <= 0) {
        alert('MiniFeed合并策略描述不能为空');
        return;
      }
      data += '&mini_merge_desc=' + encodeURIComponent(mini_merge_desc);

      $.ajax('/user-apply-submit', {
        'type' : 'POST',
        'data' : data,
        'success' : function(text) {
          alert(text);
          if (T.apply_id_ <= 0) {
            window.location = '/feed-list';
          }
        },
        'error' : function() {
          alert('提交出错');
        }
      });
    }
  );
}

UserApplyView.prototype.AppendToNode = function(node) {
  node.append(this.dom_);
}

UserApplyView.prototype.Disable = function() {
  var t = $('#apply-table', this.com_);
  $('input, select, textarea, submit', t).attr('readonly', 'readonly');
  $('select', t).attr('disabled', 'true');
  $('#apply-submit', this.com_).parent().hide();
}

var SchemaParser = function() {
  var non_loop_nodes = [], loop_nodes = [];
  function GetNodePath(nodes, sep) {
    var ret = '';
    for(var i = 0; i < nodes.length; ++i) {
      if (i > 0) {
        ret += sep;
      }
      ret += nodes[i];
    }

    return ret;
  }

  function GetPathValue() {
    var value;
    if (loop_nodes.length > 0) {
      value = GetNodePath(loop_nodes, '.');
    } else {
      value = GetNodePath(non_loop_nodes, '.');
    }
    return value;
  }

  function GetFullKey(key, firstnode) {
    var prefix;
    if (loop_nodes.length > 0) {
      // prefix = 'loop.' + GetNodePath(non_loop_nodes, '_') + '.' + GetNodePath(non_loop_nodes, '_') + '_' + GetNodePath(loop_nodes, '_');
      prefix = 'loop.' + GetNodePath(non_loop_nodes, '_') + '.' + GetNodePath(loop_nodes, '_');
    } else {
      prefix = (firstnode ? firstnode : 'keys.') + GetNodePath(non_loop_nodes, '_');
    }

    return prefix + '.' + key;
  }

  var hdf_map_ = '';
  this.GetHdfMap = function() {
    return hdf_map_;
  }

  function AddHdfMap(item) {
    if (hdf_map_.length > 0) {
      hdf_map_ += ';';
    }
    hdf_map_ += item;
  }

  function DoParse(node, looping) {
    var childs = node.children();
    if (looping) {
      loop_nodes.push(node.attr("name"));
    } else {
      if (node.attr("name") != "f") {
        non_loop_nodes.push(node.attr("name"));
      }
    }
    // console.log("looping = " + looping);
    var current_looping = (node.attr("is_loop") == "1");

    if (childs.length > 0) {
      if (current_looping) {
        AddHdfMap("FeedStruct." + GetFullKey("name", "loop.") + "=" + GetPathValue());
        AddHdfMap("FeedStruct." + GetFullKey("type", "loop.") + "=node");
        AddHdfMap("FeedStruct." + GetFullKey("comment", "loop.") + "=" + node.attr("comment"));
        var opt = parseInt(node.attr("optional")) ? 'true' : 'false';
        AddHdfMap("FeedStruct." + GetFullKey("optional", "loop.") + "=" + opt);

        console.log("FeedStruct." + GetFullKey("name", "loop.") + "=" + GetPathValue());
        console.log("FeedStruct." + GetFullKey("type", "loop.") + "=" + "node");
        console.log("FeedStruct." + GetFullKey("comment", "loop.") + "=" + node.attr("comment"));
        console.log("FeedStruct." + GetFullKey("optional", "loop.") + "=" + opt);
        console.log('');
      }

      for(var i = 0; i < childs.length; ++i) {
        DoParse($(childs[i]), current_looping || looping);
      }
    } else {
      var firstnode;
      if (current_looping) {
        firstnode = "loop.";
      }
      AddHdfMap("FeedStruct." + GetFullKey("name", firstnode) + "=" + GetPathValue());
      AddHdfMap("FeedStruct." + GetFullKey("type", firstnode) + "=" + node.attr("type"));
      AddHdfMap("FeedStruct." + GetFullKey("comment", firstnode) + '=' + node.attr("comment"));
      var opt = parseInt(node.attr("optional")) ? 'true' : 'false';
      AddHdfMap("FeedStruct." + GetFullKey("optional", firstnode) + '=' + opt);

      console.log("FeedStruct." + GetFullKey("name", firstnode) + "=" + GetPathValue());
      console.log("FeedStruct." + GetFullKey("type", firstnode) + "=" + node.attr("type"));
      console.log("FeedStruct." + GetFullKey("comment", firstnode) + '=' + node.attr("comment"));
      console.log("FeedStruct." + GetFullKey("optional", firstnode) + '=' + opt);
      console.log('');
    }

    if (looping) {
      loop_nodes.pop();
    } else {
      if (node.attr("name") != "f") {
        non_loop_nodes.pop();
      }
    }
  }

  this.ParseSchema = function(stype, version, xml, custom_expr) {
    hdf_map_ = "FeedStruct.stype=" + stype + ";FeedStruct.version=" + version + ";";
    hdf_map_ += "FeedStruct.is_custom_expr=" + (custom_expr ? 'true;':'false;');
    DoParse($('<key name="f" comment="feedroot" type="node">' + xml + '</key>'));
  }
}

