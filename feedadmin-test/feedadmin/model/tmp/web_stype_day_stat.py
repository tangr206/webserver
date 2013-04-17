from sqlalchemy import Column
from sqlalchemy import types

from feedadmin.model.meta import Base2

class WebStypeDayStat(Base2):
    __tablename__ = "web_stype_day_stat"

    number = Column(types.Integer, primary_key=True)
    uid  = Column(types.Integer)
    date = Column(types.Integer)
    stype = Column(types.Integer)        
    feed_cnt  = Column(types.Integer)    
    feed_sum  = Column(types.Integer)    
    dispatch_cnt = Column(types.Integer) 
    dispatch_sum = Column(types.Integer) 
    reply_cnt = Column(types.Integer)    
    reply_sum  = Column(types.Integer)   
    click  = Column(types.Integer)       
    position_clk = Column(types.Float) 
    position_show= Column(types.Float) 
    

    def __init__(self, uid,date,stype,feed_cnt,feed_sum ,dispatch_cnt,dispatch_sum,reply_cnt ,reply_sum,click ,position_clk  ,position_show): 
        self.uid  =uid           
        self.date  =date          
        self.stype        =stype           
        self.feed_cnt     =feed_cnt        
        self.feed_sum     =feed_sum        
        self.dispatch_cnt =dispatch_cnt    
        self.dispatch_sum =dispatch_sum    
        self.reply_cnt    =reply_cnt       
        self.reply_sum    =reply_sum       
        self.click        =click           
        self.position_clk =position_clk    
        self.position_show=position_show   

    def __repr__(self):
        return "<WebStypeStat('%s')" % self.uid
