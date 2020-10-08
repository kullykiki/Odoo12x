# -*- coding: utf-8 -*-

from odoo import models, fields, api

class demoMasterTitleCompany(models.Model):
    _name = 'demo.x_master_title_company'
    _description = '[M/demo] คำนำหน้าชื่อบริษัท'
    _rec_name = 'x_name'

    x_name = fields.Char('คำนำหน้าชื่อ')


class demoMasterProduct(models.Model):
    _name = 'demo.x_master_products'
    _description = '[M/demo] ข้อมูลสินค้า'
    _rec_name = 'x_name'

    x_color = fields.Integer('Color')
    x_name = fields.Char('ประเภทรายการสินค้า')
    
