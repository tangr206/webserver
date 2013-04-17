from sqlalchemy import Column
from sqlalchemy import types

from feedadmin.model.meta import Base

class TplView(Base):
    __tablename__ = "tpl_view"

    tpl_id = Column(types.Integer, primary_key=True)
    view = Column(types.Integer, primary_key=True)
    status = Column(types.Integer)
    template = Column(types.String(8192))
    # update_time = Column(types.TIMESTAMP(), default=now())
    update_time = Column(types.TIMESTAMP())

    def __init__(self, tpl_id, view, status, template):
        self.tpl_id = tpl_id
        self.view = view
        self.status = status
        self.template = template

    def __repr__(self):
        return "<TplView('%s')" % self.tpl_id
