from sqlalchemy import Column
from sqlalchemy import types

from feedadmin.model.meta import Base2

class ViewStat(Base2):
    __tablename__ = "view_stat"

    number = Column(types.Integer, primary_key=True)
    uid  = Column(types.Integer)
    date = Column(types.Integer)
    time = Column(types.Integer)         
    view = Column(types.String(4))        
    uv  = Column(types.Integer)         
    rv  = Column(types.Integer)         
    session_cnt= Column(types.Integer)  
    session_sum= Column(types.Integer)  
    feed_cnt   = Column(types.Integer)  
    feed_sum   = Column(types.Integer)  
        


    def __init__(self, uid,date,time,view ,uv ,rv ,session_cnt,session_sum ,feed_cnt ,feed_sum): 
        self.uid  =uid           
        self.date  =date          
        self.time        =time            
        self.view        =view            
        self.uv          =uv              
        self.rv          =rv              
        self.session_cnt =session_cnt     
        self.session_sum =session_sum     
        self.feed_cnt    =feed_cnt        
        self.feed_sum    =feed_sum        

    def __repr__(self):
        return "<WebStypeStat('%s')" % self.uid
