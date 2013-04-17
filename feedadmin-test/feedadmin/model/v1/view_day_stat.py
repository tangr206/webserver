from sqlalchemy import Column
from sqlalchemy import types

from feedadmin.model.meta import Base2
#
#mysql> desc view_day_stat;
#+-------------+------------+------+-----+----------+----------------+
#| Field       | Type       | Null | Key | Default  | Extra          |
#+-------------+------------+------+-----+----------+----------------+
#| number      | int(11)    | NO   | PRI | NULL     | auto_increment | 
#| uid         | int(11)    | NO   |     | -1       |                | 
#| date        | int(11)    | YES  |     | 20000000 |                | 
#| view        | varchar(4) | NO   |     |          |                | 
#| uv          | int(11)    | YES  |     | NULL     |                | 
#| rv          | int(11)    | YES  |     | NULL     |                | 
#| session_cnt | int(11)    | YES  |     | NULL     |                | 
#| session_sum | int(11)    | YES  |     | NULL     |                | 
#| feed_cnt    | int(11)    | YES  |     | NULL     |                | 
#| feed_sum    | bigint(20) | YES  |     | NULL     |                | 
#+-------------+------------+------+-----+----------+----------------+
#


class ViewDayStat(Base2):
    __tablename__ = "view_day_stat"

    number = Column(types.Integer, primary_key=True)
    uid  = Column(types.Integer)
    date = Column(types.Integer)
    view = Column(types.String(4))        
    uv  = Column(types.Integer)         
    rv  = Column(types.Integer)         
    session_cnt= Column(types.Integer)  
    session_sum= Column(types.Integer)  
    feed_cnt   = Column(types.Integer)  
    feed_sum   = Column(types.Integer)  
        


    def __init__(self, uid,date,view ,uv ,rv ,session_cnt,session_sum ,feed_cnt ,feed_sum): 
        self.uid  =uid           
        self.date  =date          
        self.view        =view            
        self.uv          =uv              
        self.rv          =rv              
        self.session_cnt =session_cnt     
        self.session_sum =session_sum     
        self.feed_cnt    =feed_cnt        
        self.feed_sum    =feed_sum        

    def __repr__(self):
        return "<ViewDayStat('%s')" % self.uid
