# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 14:32:55 2018

@author: LU WANG
"""

import requests     
    
KEY = '8d7f7a4cf91649158b0f38efba77588a' # 这里填拿到的key    
    
def get_response(msg):    
    apiUrl = 'http://www.tuling123.com/openapi/api'    
    data = {    
        'key'    : KEY,    
        'info'   : msg,    
        'userid' : '路老师',    
    }    
    try:    
        r = requests.post(apiUrl, data=data).json()    
        return r.get('text')    
    except:    
        return None
print(get_response('你好'))

