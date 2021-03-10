# -*- coding: utf-8 -*-

from odoo import models, fields, api

class easy(models.Model):
    _name = 'easy.easy'

    name = fields.Char()
    value = fields.Integer()
    file = fields.Many2many('ir.attachment','easy_x_attach','easy_id','attach_id','Attach')
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

# class mastertitlename(models.Model):
#     _name = 'easy.master_title_name'

#     name = fields.Char()
#     description = fields.Text()