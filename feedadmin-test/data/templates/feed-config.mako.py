# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1306489323.15536
_template_filename='/data/xce/pylons-dev/feedadmin/feedadmin/templates/feed-config.mako'
_template_uri='/feed-config.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        save_content = context.get('save_content', UNDEFINED)
        weight = context.get('weight', UNDEFINED)
        custom_expr = context.get('custom_expr', UNDEFINED)
        save_feed_db = context.get('save_feed_db', UNDEFINED)
        news_merge_type = context.get('news_merge_type', UNDEFINED)
        ptype = context.get('ptype', UNDEFINED)
        update_time_on_merge = context.get('update_time_on_merge', UNDEFINED)
        daily_quota = context.get('daily_quota', UNDEFINED)
        push_flags = context.get('push_flags', UNDEFINED)
        mini_merge_type = context.get('mini_merge_type', UNDEFINED)
        lifetime = context.get('lifetime', UNDEFINED)
        type = context.get('type', UNDEFINED)
        stype = context.get('stype', UNDEFINED)
        desc = context.get('desc', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{"type": ')
        __M_writer(escape(type))
        __M_writer(u', "stype": ')
        __M_writer(escape(stype))
        __M_writer(u', "desc":"')
        __M_writer(escape(desc))
        __M_writer(u'", "weight":')
        __M_writer(escape(weight))
        __M_writer(u', "ptype":')
        __M_writer(escape(ptype))
        __M_writer(u', "save_content":')
        __M_writer(escape(save_content))
        __M_writer(u', "save_feed_db":')
        __M_writer(escape(save_feed_db))
        __M_writer(u', "news_merge_type":')
        __M_writer(escape(news_merge_type))
        __M_writer(u', "mini_merge_type":')
        __M_writer(escape(mini_merge_type))
        __M_writer(u', "push_flags":')
        __M_writer(escape(push_flags))
        __M_writer(u', "custom_expr":')
        __M_writer(escape(custom_expr))
        __M_writer(u', "update_time_on_merge":')
        __M_writer(escape(update_time_on_merge))
        __M_writer(u', "lifetime":')
        __M_writer(escape(lifetime))
        __M_writer(u', "daily_quota":')
        __M_writer(escape(daily_quota))
        __M_writer(u', "d": "\u4e2d\u6587"}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


