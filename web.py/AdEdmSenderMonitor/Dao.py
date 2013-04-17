# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: 阳健
'''
import json
import datetime

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return super(JSONDateTimeEncoder,self).default(obj)
        
def json_encode(data):
    return json.dumps(data,cls=JSONDateTimeEncoder)