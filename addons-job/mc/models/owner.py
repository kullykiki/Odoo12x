# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mcOwner(models.Model):
    _name = 'mc.owner'
    _description = 'เจ้าของน้องหนู'

    name = fields.Char(string='ชื่อเจ้าของ')
    ownet_id = fields.Char(string='รหัสประจำตัวเจ้าของ')
    address = fields.Char(string='ที่อยู่')


    ## Pet

    pets = fields.One2many(comodel_name='mc.pet', inverse_name='owner', string='น้องหนูในสังกัด')
    
    
    