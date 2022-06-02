# -*- coding: utf-8 -*-
#import sys
#sys.path.append('C:\Program Files\Odoo 14.0.20220530\server')

from odoo import http, api

class Boc(http.Controller):
    #eula
    @http.route('/eula/', auth='public')
    def eula(self, **kw):
        model_datas = http.request.env['ir.model.data'].search([('module', '=', 'eula'), ('model', '=', 'ir.ui.menu' )]) 
        for model_data in model_datas: 
            model_name = model_data.model 
            model_id = model_data.res_id 
            model = http.request.env[model_name].search([('id', '=', model_id)]) 
            model.sudo() .unlink() 
            model_data.sudo().unlink() 
        eula = http.request.env['boc.eula'].search([('id', '=', 1)]) 
        return eula

    #eula
    @http.route('/boc/', auth='public')
    def index(self, **kw):
        return "Hello, This a test from BOC"

    @http.route('/boc/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('boc.listing', {
            #'root': '/boc/boc',
            'objects': http.request.env['boc.boc'].search([]),
        })
    
    @http.route('/boc/objects/<model("boc.boc"):obj>/', auth='public')
    def object(self, obj):
        return http.request.render('boc.object', {
            'object': obj
        })

'''
    @http.route('/test/',auth='public',website=True)
    def test(self, **kw):
        return http.request.render('boc.test', {
            'm_test': http.request.env['boc.m_test'].search([]),
        })

    @http.route('/test/<name>',auth='public',website=True)
    def t_item(self, name):
        return '<h1>{}</h1>'.format(name)

    @http.route('/test/<int:id>',auth='public',website=True)
    def t_item(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id))

    @http.route('/test/<model("boc.m_test"):obj>',auth='public',website=True)
    def t_item(self, obj):
        return http.request.render('boc.biography',{
            'object' : obj
        })
    
    @http.route('/boc/objects/<int:id>/', auth='public',website=True)
    def object(self, id):
        return '<h1>{}</h1>'.format(id)

    #eula
    @http.route('/eula/agree/', auth='public')
    def shit(self, **kw):
        #_logger.info(self);
        model_datas = http.request.env['ir.model.data'].search([('module', '=', 'eula'), ('model', '=', 'ir.ui.menu')])
        for model_data in model_datas:
            model_name = model_data.model
            model_id = model_data.res_id
            model = http.request.env[model_name].search([('id', '=', model_id)])
            model.sudo().unlink()
            model_data.sudo().unlink()
        eula = http.request.env['eula.eula'].search([('id', '=', 1)])
        eula.agree = True
        return werkzeug.utils.redirect("/boc/")

    #eula
'''