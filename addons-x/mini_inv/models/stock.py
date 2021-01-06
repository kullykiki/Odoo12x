# -*- coding: utf-8 -*-

from odoo import models, fields, api

## ---------------------------------------    🥗 Stock 🥗   --------------------------------------------------------
class LGStock(models.Model):
    _name = 'mini_inv.x_lg_stock'
    _description = 'Stock'

    """
    รายการของที่อยู่ในคลัง
        โมเดลสำหรับ เก็บ รายการของที่ฝากอยู่ในคลัง
    """

### -----------------------------------------       Field      ------------------------------------------------------
    x_name = fields.Char(string='รายการ')

    x_stock_item_type = fields.Selection(    string='ประเภทของที่อยู่ในคลัง', 
                                        selection=[ 
                                                ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
                                                ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'),   
                                                ('safety','อุปกรณ์ความปลอดภัย'),
                                                ('media','สินค้าพรีเมียม หรือสื่อการตลาด'), 
                                                ('damaged_property','ทรัพย์สินชำรุดรอการจำหน่าย')  
                                        ])
    # จากรายการฝากอันไหน ได้แสดงยอดของคงเหลือ เวลาฝากได้ จากการค้นหา เลขที่ แล้วคอมพิวไปใส่ stock
    x_deposit_id = fields.Many2one('mini_inv.x_lg_inventory','จากรายการฝากเลขที่')
    x_item = fields.Many2one('mini_inv.x_master_lg_product','ชื่อรายการ')
    x_qty_remain = fields.Integer('ยอดคงเหลือ',help='ยอดของคงเหลือในคลังที่สามารถให้เบิกได้')
    x_qty_lock = fields.Integer('ยอดรอการรับ',help='ยอดของที่ไม่สามารถเบิกได้ เนื่องจากได้มีการทำเรื่องเบิกแล้ว แต่ยังไม่มีการรับของ')
    x_unit = fields.Many2one('mini_inv.x_master_lg_unit','หน่วยนับ')  
    
    ## ทรัพย์สินชำรุดรอการจำหน่าย
    x_destroy_item = fields.Char(string='[DP] Category Name')
    x_destroy_serial = fields.Char(string='[DP] Serial No.')
    x_destroy_tag = fields.Char(string='[DP] Tag No.')
    x_destroy_model = fields.Char(string='[DP] Model') 

    ## คลังนำฝาก
    x_stock_id = fields.Many2one('mini_inv.x_master_lg_stock','นำฝากคลัง')



## ------------------------------------       Compute Function      ------------------------------------------------------
    