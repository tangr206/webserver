# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: 阳健
'''
import web

service_finder_files = "'trigger', 'edm', 'ad'"

urls = (
    '/','ServiceFinder',
)

render = web.template.render('templates/service_finder/')

app = web.application(urls, locals())

class ServiceFinder:
    '''
    classdocs
    '''
    def GET(self):
        return render.ad_xml_view(service_finder_files)
    
if __name__ == '__main__':
    app.run()      
