from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from feedadmin.model.meta import Base

class StypeConfig(Base):
    __tablename__ = "feed_config"

    stype = Column(Integer, primary_key=True)
    weight = Column(Integer)
    type = Column(Integer)
    ptype = Column(Integer)
    description = Column(String(256))
    push_flag = Column(Integer)
    news_merge_type = Column(Integer)
    mini_merge_type = Column(Integer)
    is_update_time = Column(Integer)
    is_custom_expr = Column(Integer)
    is_persist_content = Column(Integer)
    is_persist_feeddb = Column(Integer)
    lifetime = Column(Integer)
    daily_quota = Column(Integer)

    def __init__(self, stype, weight, type, ptype, description, push_feed_flags, news_merge_type, mini_merge_type, is_update_time_on_merge, is_custom_expr,
            persist_body, persist_feeddb, lifetime, daily_quota):
        self.stype = stype
        self.weight = weight
        self.type = type
        self.ptype = ptype
        self.description = description

        self.push_flag = push_feed_flags
        self.news_merge_type = news_merge_type
        self.mini_merge_type = mini_merge_type
        self.is_update_time = is_update_time_on_merge
        self.is_custom_expr = is_custom_expr
        self.is_persist_content = persist_body
        self.is_persist_feeddb = persist_feeddb
        self.lifetime = lifetime
        self.daily_quota = daily_quota
        
    def __repr__(self):
        return "<StypeConfig ('%s')" % self.stype

