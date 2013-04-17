from sqlalchemy import Column
from sqlalchemy import types

from feedadmin.model.meta import Base2

class FeedStatTotal(Base2):
    __tablename__ = "feed_stat_total"

    date = Column(types.Date, primary_key=True)
    dispatch = Column(types.Integer)
    tosize = Column(types.BigInteger)
    dispatch_user = Column(types.Integer)
    view = Column(types.BigInteger)
    view_pos = Column(types.Integer)
    view_user = Column(types.Integer)
    viewed_user = Column(types.Integer)
    reply = Column(types.Integer)
    reply_user = Column(types.Integer)
    replyed_user = Column(types.Integer)
    click = Column(types.Integer)
    click_pos = Column(types.Integer)
    click_user = Column(types.Integer)
    clicked_user = Column(types.Integer)

    def __init__(date, dispatch, tosize, dispatch_user, view, view_pos, view_user, viewed_user, reply, reply_user, replyed_user, click, click_pos, click_user, clicked_user):
        self.date = date
        self.dispatch = dispatch
        self.tosize = tosize
        self.dispatch_user = dispatch_user
        self.view = view
        self.view_pos = view_pos
        self.view_user = view_user
        self.viewed_user = viewed_user
        self.reply = reply
        self.reply_user = reply_user
        self.replyed_user = replyed_user
        self.click = click
        self.click_pos = click_pos
        self.click_user = click_user
        self.clicked_user = clicked_user

    def __repr__(self):
        return "<FeedStatTotal('%s')" % self.date
