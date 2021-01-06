# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LGInventory(models.Model):
    _name = 'mini_inv.x_lg_inventory'
    _description = 'ระบบฝากของ'

    x_name = fields.Char('เลขที่คำขอ')
    x_activity = fields.Selection(string='ประเภทคำขอ', selection=[('d', 'ฝาก'), ('r', 'เบิก')])
    x_stock = fields.Many2one(comodel_name='mini_inv.x_master_lg_stock', string='คลังที่นำฝาก')
    x_ref_deposit_id = fields.Many2one(comodel_name='mini_inv.x_lg_inventory', string='รายการฝากเลขที่')

    ## ฝาก

    ### วัสดุสำนักงานสิ้นเปลือง
    x_d_b_consumables = fields.Boolean(string='[B/D] วัสดุสำนักงานสิ้นเปลือง')
    x_d_l_consumables = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_office_supplies', string='[L/D] วัสดุสำนักงานสิ้นเปลือง')

    ### อุปกรณ์ในระบบ Oracle มี Item Code
    x_d_b_oracle_product = fields.Boolean(string='[B/D] อุปกรณ์ในระบบ Oracle มี Item Code')
    x_d_l_oracle_product = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_oracle_item', string='[L/D] อุปกรณ์ในระบบ Oracle มี Item Code')

    ### อุุปกรณ์ความปลอดภัย
    x_d_b_safety = fields.Boolean(string='[B/D] อุุปกรณ์ความปลอดภัย')
    x_d_l_safety = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_safety', string='[L/D] อุุปกรณ์ความปลอดภัย')

    ### สินค้าพรีเมียม หรือสื่อการตลาด
    x_d_b_media = fields.Boolean(string='[B/D] สินค้าพรีเมียม หรือสื่อการตลาด')
    x_d_l_media = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_media', string='[L/D] สิ้นค้าพรีเมียม หรือสื่อการตลาด')

    ### สินค้าพรีเมียม หรือสื่อการตลาด
    x_d_b_damage_product = fields.Boolean(string='[B/D] ทรัพย์สินชำรุดรอการจำหน่าย')
    x_d_l_damage_product = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_destroy_product', string='[L/D] ทรัพย์สินชำรุดรอการจำหน่าย')
    
    

    
    
    
    
    
