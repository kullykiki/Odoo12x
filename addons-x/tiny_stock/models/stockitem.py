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
        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')
    ])
    # จากรายการฝากอันไหน ได้แสดงยอดของคงเหลือ เวลาฝากได้ จากการค้นหา เลขที่ แล้วคอมพิวไปใส่ stock
    deposit_id = fields.Many2one('tiny_stock.inventory','Inventory ID')
    
    # จากรายการฝากอันไหน ได้แสดงยอดของคงเหลือ เวลาฝากได้ จากการค้นหา เลขที่ แล้วคอมพิวไปใส่ stock
    request_id = fields.Many2one('tiny_stock.requistion','Requistion ID')

    
    item = fields.Many2one('tiny_stock.m_item','Item')
    qty = fields.Integer()
    unit = fields.Char('Unit',related='item.item_unit')   

    @api.multi
    def name_get(self):
        res = []
        for stock in self:
            if stock.type_item == 'office_supplies':
                name = '{} {} {}'.format(stock.item.item_name,stock.qty,stock.unit)
            elif stock.type_item == 'oracle_code_item':
                name = '{}({}) {} {}'.format(stock.item.item_name,stock.item.item_oci_code,stock.qty,stock.unit)
            res.append((stock.id, name))
        return res

