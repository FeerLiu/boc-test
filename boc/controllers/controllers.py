# -*- coding: utf-8 -*-
# from odoo import http


class Boc(http.Controller):
    @http.route('/boc/boc/', auth='public')
    def index(self, **kw):
        return "Hello, This a test from BOC"

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
