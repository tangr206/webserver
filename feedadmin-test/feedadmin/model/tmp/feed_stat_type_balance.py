from sqlalchemy import Column
from sqlalchemy import types

from feedadmin.model.meta import Base2

class FeedStatTypeBalance(Base2):
    __tablename__ = "feed_stat_type_balance_t"

#date    | date         | NO   | PRI | 0000-00-00 |       | 
#| type   | bigint(20)   | NO   | PRI | 0          |       | 
#| profit  | float(20,10) | YES  |     | NULL       |       | 
#| cost    | float(20,10) | YES  |     | NULL       |       | 
#| balance | float(20,10) | YES  |     | NULL 

    date = Column(types.Date, primary_key=True)
    type = Column(types.BigInteger, primary_key=True)
    profit = Column(types.Float)
    cost = Column(types.Float)
    balance = Column(types.Float)
    view = Column(types.Float)

    def __init__(date, stype, profit, cost, balance):
        self.date = date
        self.type = type
        self.profit = profit
        self.cost = cost
        self.balance = balance
        self.view = view

    def __repr__(self):
        return "<FeedStatTypeBalance('%s')" % self.stype
