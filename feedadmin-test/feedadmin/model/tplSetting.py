from sqlalchemy import Column
from sqlalchemy import types

from feedadmin.model.meta import Base2

class TplSetting(Base2):
    __tablename__ = "tpl_setting"

    tpl_id = Column(types.Integer, primary_key=True)
    view = Column(types.Integer, primary_key=True)
    module = Column(types.Integer)
    avatar = Column(types.Integer)
    actor = Column(types.Integer)
    title = Column(types.Integer)
    content = Column(types.Integer)
    lbs = Column(types.Integer)
    source = Column(types.Integer)
    like = Column(types.Integer)
    share = Column(types.Integer)
    reply = Column(types.Integer)
    toolbar = Column(types.Integer)
    similar = Column(types.Integer)
    titleVals = Column(types.String(8192))
    titleCustom = Column(types.String(8192))
    contentVals = Column(types.String(8192))
    contentCustom = Column(types.String(8192))
    replyType = Column(types.String(20))
    replyTypeId = Column(types.String(10))
    update_time = Column(types.TIMESTAMP())

    def __init__(self, tpl_id, view, module, avatar, actor, title, content, lbs, source, like, share, reply, toolbar, similar, titleVals, titleCustom, contentVals, contentCustom, replyType, replyTypeId):
        self.tpl_id = tpl_id
        self.view = view
        self.module = module
        self.avatar = avatar
        self.actor = actor
        self.title = title
        self.content = content
        self.lbs = lbs
        self.source = source
        self.like = like
        self.share = share
        self.reply = reply
        self.toolbar = toolbar
        self.similar = similar
        self.titleVals = titleVals
        self.titleCustom = titleCustom
        self.contentVals = contentVals
        self.contentCustom = contentCustom
        self.replyType = replyType
        self.replyTypeId = replyTypeId

    def __repr__(self):
        return "<TplSetting('%s')" % self.tpl_id
