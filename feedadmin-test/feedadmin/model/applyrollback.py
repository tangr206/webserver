from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy.types import Integer, String

from feedadmin.model.meta import Base
from sqlalchemy.sql.expression import text

class ApplyRollback(Base):
  __tablename__ = "apply_rollback"

  apply_id = Column(Integer, primary_key=True)
  stype_id = Column(Integer)
  version = Column(Integer)
  tpl_id = Column(Integer)
  pm_names = Column(String(128))
  pm_emails = Column(String(128))
  dev_names = Column(String(128))
  dev_emails = Column(String(128))
  rollback_desc = Column(String(512))
  apply_time = Column(types.TIMESTAMP())
  status = Column(Integer)

  def __init__(self, apply_id, stype_id, version, tpl_id, pm_names, pm_emails, dev_names, dev_emails, rollback_desc, status, apply_time):
    self.apply_id = apply_id
    self.stype_id = stype_id
    self.version = version
    self.tpl_id = tpl_id
    self.pm_names = pm_names
    self.pm_emails = pm_emails
    self.dev_names = dev_names
    self.dev_emails = dev_emails
    self.rollback_desc = rollback_desc
    self.status = status
    self.apply_time = apply_time

  def __repr__(self):
    return "<FeedKeys %s>" % (self.apply_id)

