from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy.types import Integer, String

from feedadmin.model.meta import Base
from sqlalchemy.sql.expression import text

class ApplyNewFeed(Base):
  __tablename__ = "apply_new_feed"

  apply_id = Column(Integer, primary_key=True)
  pm_names = Column(String(128))
  pm_emails = Column(String(128))
  dev_names = Column(String(128))
  dev_emails = Column(String(128))
  stype_desc = Column(String(512))
  stype_text = Column(String(1024))
  push_news = Column(Integer)
  push_mini = Column(Integer)
  news_merge_desc = Column(String(256))
  mini_merge_desc = Column(String(256))
  lifetime = Column(Integer)
  apply_time = Column(types.TIMESTAMP())


  status = Column(Integer)

  def __init__(self, apply_id, pm_names, pm_emails, dev_names, dev_emails, stype_desc, stype_text, push_news, push_mini,
      news_merge_desc, mini_merge_desc, lifetime, status, apply_time):
    self.apply_id = apply_id
    self.pm_names = pm_names
    self.pm_emails = pm_emails
    self.dev_names = dev_names
    self.dev_emails = dev_emails
    self.stype_desc = stype_desc
    self.stype_text = stype_text
    self.push_news = push_news
    self.push_mini = push_mini
    self.news_merge_desc = news_merge_desc
    self.mini_merge_desc = mini_merge_desc
    self.lifetime = lifetime
    self.status = status
    self.apply_time = apply_time

  def __repr__(self):
    return "<FeedKeys %s>" % (self.apply_id)

