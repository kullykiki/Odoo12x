# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class sarabun_font(models.Model):
#     _name = 'sarabun_font.sarabun_font'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100