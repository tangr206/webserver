from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy.types import Integer, String

from feedadmin.model.meta import Base
from sqlalchemy.sql.expression import text

class UserApply(Base):
  __tablename__ = "user_apply"

  apply_id = Column(Integer, primary_key=True)
  pm_names = Column(String(128))
  pm_emails = Column(String(128))
  dev_names = Column(String(128))
  dev_emails = Column(String(128))
  feed_stype = Column(Integer)
  feed_desc = Column(String(512))
  apply_type = Column(Integer)
  apply_desc = Column(String(4096))
  push_news = Column(Integer)
  push_mini = Column(Integer)
  news_merge_desc = Column(String(1024))
  mini_merge_desc = Column(String(1024))
  status = Column(Integer)
  apply_time = Column(types.TIMESTAMP())


  status = Column(Integer)

  def __init__(self, apply_id, pm_names, pm_emails, dev_names, dev_emails, feed_stype, feed_desc, apply_type, apply_desc, push_news, push_mini,
      news_merge_desc, mini_merge_desc, status, apply_time):
    self.apply_id = apply_id
    self.pm_names = pm_names
    self.pm_emails = pm_emails
    self.dev_names = dev_names
    self.dev_emails = dev_emails
    self.feed_stype = feed_stype
    self.feed_desc = feed_desc
    self.apply_type = apply_type
    self.apply_desc = apply_desc
    self.push_news = push_news
    self.push_mini = push_mini
    self.news_merge_desc = news_merge_desc
    self.mini_merge_desc = mini_merge_desc
    self.status = status
    self.apply_time = apply_time

  def __repr__(self):
    return "<UserApply %s>" % (self.apply_id)

