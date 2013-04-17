from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from feedadmin.model.meta import Base

class DataVersion(Base):
  __tablename__ = "data_config"

  stype = Column(Integer, primary_key=True)
  version = Column(Integer, primary_key=True)
  test_tpl_id = Column(Integer)
  using_tpl_id = Column(Integer)
  keys_xml = Column(String(2048))
  news_merge_by = Column(String(128))
  mini_merge_by = Column(String(128))
  source_by = Column(String(128))
  psource_by = Column(String(128))
  actor_by = Column(String(128))
  togroup_by = Column(String(128))
  dispatch_expr = Column(String(128))


  status = Column(Integer)

  def __init__(self, stype, version, test_version_id, using_version_id, keys_xml = '', 
      news_merge_by = '', mini_merge_by = '', source_by = '', psource_by = '', actor_by = '', togroup_by = '', dispatch_expr = '', status = 1):
    self.news_merge_by = news_merge_by
    self.mini_merge_by = mini_merge_by
    self.source_by = source_by
    self.psource_by = psource_by
    self.actor_by = actor_by
    self.togroup_by = togroup_by
    self.dispatch_expr = dispatch_expr
    self.stype = stype
    self.version = version
    self.test_tpl_id = test_version_id
    self.using_tpl_id = using_version_id
    self.keys_xml = keys_xml
    self.status = status

  def __repr__(self):
    return "<FeedKeys %s,%s>" % (self.stype, self.version)
