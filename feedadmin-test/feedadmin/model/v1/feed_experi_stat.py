from sqlalchemy import Column
from sqlalchemy import types

from feedadmin.model.meta import Base2

class ExperiStat(Base2):
    __tablename__ = "experiment_stat"

    number = Column(types.Integer, primary_key=True)
    begin = Column(types.Integer)
    end = Column(types.Integer)
    tail = Column(types.String(10))
    describ = Column(types.String(100))
    contact = Column(types.String(30))
    summary = Column(types.String(100))

    def __init__(self, begin, end, tail, describ, contact, summary = ""):
        self.begin = begin
        self.end = end
        self.tail = tail
        self.describ = describ
        self.contact = contact
        self.summary = summary

    def __repr__(self):
        return "<Experiment('%s')" % self.number
