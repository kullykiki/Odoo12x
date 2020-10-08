# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class fund(models.Model):
#     _name = 'fund.fund'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Employee(models.Model):
    _inherit = "hr.employee"

    employee_id = fields.Char('Employee Id')