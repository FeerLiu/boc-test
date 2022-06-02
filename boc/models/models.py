# -*- coding: utf-8 -*-
from odoo import models, fields, api

class boc(models.Model):
    _name = 'boc.boc'
    _description = 'boc.boc'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
    def action_do_sth(self):
        return {
            "type": "ir.actions.act_window",
            'name': 'EULA Agreement', 
            "res_model": "boc.eula",
            "views": [[False, "form"]],
            "target": "new",
        }

class eula(models.Model):    
    _name = 'boc.eula'
    _description = 'boc.eula'

    name = fields.Char(default="eula")
    eulaContent = fields.Html(readonly=True)
    agree = fields.Boolean(string="Agree", help="By checking this , you agree to the EULA.", default=False)
    def trigger(self):
        return {
                  'type': 'ir.actions.act_window', 
                  'name': 'EULA',
                  'res_model': 'boc.eula',
                  'res_id': 1,                  
                  "views": [[False, "tree"], [False, "form"]],
                  'target': 'new'
        }

class m_test(models.Model):
    _name = 'boc.m_test'
    _description = 'boc.test'

    name = fields.Char()
    biography = fields.Html()

