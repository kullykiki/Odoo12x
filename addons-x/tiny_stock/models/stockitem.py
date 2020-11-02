# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Stock(models.Model):
    _name = 'tiny_stock.stock'
    _description = 'Stock List'

    """
    รายการของที่อยู่ในคลัง
        โมเดลย่อยสำหรับของที่อยู่ในคลัง ทุกประเภท เก็บในโมเดลเดียวกัน ค่อยไป context view ใน form เอา ตอนแยกประเภท
    """

    # type ของ item ที่จะฝาก
    type_item = fields.Selection([
        ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'),
        ('damaged_property','ทรัพย์สินชำรุดรอการจำหน่าย')
    ])
    # จากรายการฝากอันไหน ได้แสดงยอดของคงเหลือ เวลาฝากได้ จากการค้นหา เลขที่ แล้วคอมพิวไปใส่ stock
    deposit_id = fields.Many2one('tiny_stock.inventory','Inventory ID')
    
    
    item_name = fields.Char('รายการ')

    item = fields.Many2one('tiny_stock.m_item','Item')
    qty = fields.Integer()
    unit = fields.Char('Unit')  
    item_dp_name = fields.Char('Item Name')
    item_dp_tag = fields.Char('Item Tag')
    item_dp_serial = fields.Char('Item Serial') 

    
            

