from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy.types import Integer, String

from feedadmin.model.meta import Base
from sqlalchemy.sql.expression import text

class ApplyNewVersion(Base):
  __tablename__ = "apply_new_version"

  apply_id = Column(Integer, primary_key=True)
  stype_id = Column(Integer)
  from_version_id = Column(Integer)
  pm_names = Column(String(128))
  pm_emails = Column(String(128))
  dev_names = Column(String(128))
  dev_emails = Column(String(128))
  version_desc = Column(String(512))
  version_text = Column(String(1024))
  apply_time = Column(types.TIMESTAMP())
  status = Column(Integer)

  def __init__(self, apply_id, stype_id, from_version_id, pm_names, pm_emails, dev_names, dev_emails, version_desc, version_text, status, apply_time):
    self.apply_id = apply_id
    self.stype_id = stype_id
    self.from_version_id = from_version_id
    self.pm_names = pm_names
    self.pm_emails = pm_emails
    self.dev_names = dev_names
    self.dev_emails = dev_emails
    self.version_desc = version_desc
    self.version_text = version_text
    self.status = status
    self.apply_time = apply_time

  def __repr__(self):
    return "<FeedKeys %s>" % (self.apply_id)

