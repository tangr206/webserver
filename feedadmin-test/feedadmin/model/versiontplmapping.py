from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from feedadmin.model.meta import Base
from sqlalchemy.sql.expression import text

class VersionTplMapping(Base):
    __tablename__ = "version_tpl_mapping"

    tpl_id = Column(Integer, primary_key=True)
    stype = Column(Integer)
    version = Column(Integer)

    def __init__(self, tpl_id, stype, version):
        self.tpl_id = tpl_id
        self.stype = stype
        self.version = version

    def __repr__(self):
        return "<VersionTplMapping %s>" % self.tpl_id
