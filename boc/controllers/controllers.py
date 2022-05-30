# -*- coding: utf-8 -*-
from odoo import http

class Boc(http.Controller):
     @http.route('/boc-test/', auth='public')
     def index(self, **kw):
         #return "Hello, This is a test from BOC"
         return self.pool.get('warning').info(cr, uid, title='Export imformation', message="%s products Created, %s products Updated "%(str(prod_new),str(prod_update)))
#     @http.route('/boc/boc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('boc.listing', {
#             'root': '/boc/boc',
#             'objects': http.request.env['boc.boc'].search([]),
#         })

#     @http.route('/boc/boc/objects/<model("boc.boc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('boc.object', {
#             'object': obj
#         })
