# -*- coding: utf-8 -*-
from odoo import http


class Boc-test(http.Controller):
    @http.route('/boc-test/boc-test/', auth='public')
    def index(self, **kw):
        return "Hello, This is Boc-test"
 #
 #    @http.route('/boc-test/boc-test/objects/', auth='public')
 #    def list(self, **kw):
 #        return http.request.render('boc-test.listing', {
 #            'root': '/boc-test/boc-test',
 #            'objects': http.request.env['boc-test.boc-test'].search([]),
 #        })
 #
 #    @http.route('/boc-test/boc-test/objects/<model("boc-test.boc-test"):obj>/', auth='public')
 #    def object(self, obj, **kw):
 #        return http.request.render('boc-test.object', {
 #            'object': obj
 #        })
