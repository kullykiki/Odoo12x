# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mcDrug(models.Model):
    _name = 'mc.drug'
    _description = 'ยา'

    drug_id = fields.Char('รหัสยา')
    drug_name = fields.Char('ชื่อยา')
    drug_haved = fields.Selection([('y','มีอยู่ในคลินิค'),('n','ไม่มีในคลินิค')],'การคงอยู่ในคลินิค')
    drug_active = fields.Boolean('Active')