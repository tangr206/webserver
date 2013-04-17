from sqlalchemy import Column
from sqlalchemy import types

from feedadmin.model.meta import Base2

#mysql> desc web_stype_stat;
#+-------------------+------------+------+-----+----------+----------------+
#| Field             | Type       | Null | Key | Default  | Extra          |
#+-------------------+------------+------+-----+----------+----------------+
#| number            | int(11)    | NO   | PRI | NULL     | auto_increment | 
#| uid               | int(11)    | YES  |     | -1       |                | 
#| date              | int(11)    | YES  |     | 20000000 |                | 
#| time              | int(11)    | YES  |     | 0        |                | 
#| stype             | varchar(4) | NO   |     |          |                | 
#| feed_sum          | int(11)    | YES  |     | NULL     |                | 
#| feed_cnt          | int(11)    | YES  |     | NULL     |                | 
#| position_show     | float      | YES  |     | NULL     |                | 
#| dispatch_cnt      | int(11)    | YES  |     | NULL     |                | 
#| dispatch_user_cnt | int(11)    | YES  |     | NULL     |                | 
#| dispatch_sum      | int(11)    | YES  |     | NULL     |                | 
#| reply_sum         | int(11)    | YES  |     | NULL     |                | 
#| reply_user_cnt    | int(11)    | YES  |     | NULL     |                | 
#| reply_feed_cnt    | int(11)    | YES  |     | NULL     |                | 
#| click_sum         | int(11)    | YES  |     | NULL     |                | 
#| click_user_cnt    | int(11)    | YES  |     | NULL     |                | 
#| position_clk      | float      | YES  |     | NULL     |                | 
#  
class WebStypeStat(Base2):
    __tablename__ = "web_stype_stat"

    number = Column(types.Integer, primary_key=True)
    uid  = Column(types.Integer)
    date = Column(types.Integer)
    time = Column(types.Integer)         
    stype = Column(types.String(4))        
    feed_sum  = Column(types.Integer)    
    feed_cnt  = Column(types.Integer)    
    position_show= Column(types.Float) 
    dispatch_cnt = Column(types.Integer) 
    dispatch_user_cnt = Column(types.Integer) 
    dispatch_sum = Column(types.Integer) 
    reply_user_cnt = Column(types.Integer)    
    reply_feed_cnt = Column(types.Integer)    
    reply_sum  = Column(types.Integer)   
    click_sum  = Column(types.Integer)       
    click_user_cnt  = Column(types.Integer)       
    position_clk = Column(types.Float) 
    

    def __init__(self, uid,date,time,stype, feed_sum,feed_cnt,position_show, dispatch_cnt,dispatch_user_cnt,dispatch_sum, \
				    reply_user_cnt,reply_feed_cnt,reply_sum, click_sum,click_user_cnt,position_clk  ): 
        self.uid  		=uid           
        self.date  		=date          
        self.time         	=time            
        self.stype        	=stype           

        self.feed_cnt     	=feed_cnt        
        self.feed_sum     	=feed_sum        
        self.position_show	=position_show   

        self.dispatch_cnt 	=dispatch_cnt    
        self.dispatch_user_cnt 	=dispatch_user_cnt    
        self.dispatch_sum 	=dispatch_sum    

        self.reply_user_cnt    	=reply_user_cnt       
        self.reply_feed_cnt    	=reply_feed_cnt       
        self.reply_sum    	=reply_sum  
     
        self.click_sum        	=click_sum           
        self.click_user_cnt     =click_user_cnt           
        self.position_clk 	=position_clk    

    def __repr__(self):
        return "<WebStypeStat('%s')" % self.uid
