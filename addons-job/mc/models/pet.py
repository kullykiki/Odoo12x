# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mcPet(models.Model):
    _name = 'mc.pet'
    _description = 'น้องหนูที่ไม่ฉะบาย'

    pet_id = fields.Char(string='รหัสประจำตัวน้อง')
    owner = fields.Many2one('mc.owner','เจ้าของ')
    
