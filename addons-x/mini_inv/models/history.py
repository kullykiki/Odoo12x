# -*- coding: utf-8 -*-

from odoo import models, fields, api

## ---------------------------------------    🎍 History 🎍   --------------------------------------------------------
class LGHistory(models.Model):
    _name = 'mini_inv.x_lg_history'
    _description = 'ประวัติการทำรายการ'

    """
    รายการของที่อยู่ในคลัง
        โมเดลสำหรับ เก็บ ประวัติการทำรายการของของที่ฝากในคลัง โดย การทำรายการ มี 3 อย่าง คือ ฝาก เบิก รับของ
    *** ,related='x_inv_id.x_stock' ***
    """

### -----------------------------------------       Field      ------------------------------------------------------
    x_name = fields.Char(string='รายการ')
    x_activity = fields.Selection([('d', 'ฝาก'),('r', 'เบิก'),('p', 'รับของ')], string='กิจกรรม')
    x_history_item_type = fields.Selection( string='ประเภทของที่ทำรายการ', 
                                            selection=[ 
                                                    ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
                                                    ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'),   
                                                    ('safety','อุปกรณ์ความปลอดภัย'),
                                                    ('media','สินค้าพรีเมียม หรือสื่อการตลาด'), 
                                                    ('damaged_property','ทรัพย์สินชำรุดรอการจำหน่าย')  
                                            ])
    x_qty = fields.Integer('จำนวน')
    x_unit = fields.Many2one('mini_inv.x_master_lg_unit','หน่วยนับ')  
    
    ## การทำรายการเกิดจากรายการใด
    x_inv_id = fields.Many2one('mini_inv.x_lg_inventory','ใบนำฝาก/เบิกเลขที่')

    ## มีการทำรายการที่คลังอะไร
    x_stock_id = fields.Many2one('mini_inv.x_master_lg_stock','คลัง',related='x_inv_id.x_stock')

    ## ประเภทของที่ทำรายการ
    x_item = fields.Many2one(comodel_name='mini_inv.x_master_lg_product', string='รายการของฝาก')
    ## ทรัพย์สินชำรุดรอการจำหน่าย
    x_destroy_item = fields.Char(string='[DP] Category Name')
    x_destroy_serial = fields.Char(string='[DP] Serial No.')
    x_destroy_tag = fields.Char(string='[DP] Tag No.')
    x_destroy_model = fields.Char(string='[DP] Model')
