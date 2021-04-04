# -*- coding: utf-8 -*-
from odoo import models, fields, api

class mkDetailMKBudget(models.Model):
    _name = 'mk.x_mk_budget'
    _description = 'รายละเอียดงบประมาณ'

    """
        รายละเอียดงบประมาณ
    """

    ### -----------------------------------------       Field      ------------------------------------------------------
    x_name = fields.Char(string='ชื่อ Supplies + สื่อ')

    x_b_vat = fields.Boolean(string='มี VAT หรือไม่')
    
    x_exclude_vat = fields.Float(string='จำนวนเงินก่อน VAT',digits=(16,2))
    x_include_vat = fields.Float(string='จำนวนเงินรวม VAT',digits=(16,2))
    
    x_m21_media_request = fields.Many2one(comodel_name='mk.x_mk_work_request', string='เลขที่คำขอ')
    x_media = fields.Char(string='สื่อ')
    x_num = fields.Integer(string='จำนวน')
    
    x_per_unit = fields.Float(string='ราคาต่อหน่วย',digits=(16,2))
    x_price = fields.Float(string='ราคารวม',digits=(16,2))
    x_supplies_name = fields.Char(string='ชื่อ Supplier')
    x_vat = fields.Float(string='ภาษีมูลค่าเพิ่ม (7%)',digits=(16,2))

    ## ------------------------------------       Compute Function      ------------------------------------------------------
#####---------------------------------------------------------🌟END🌟================================================================#####
