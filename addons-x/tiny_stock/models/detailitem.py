# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Depostion(models.Model):
    _name = 'tiny_stock.deposition'
    _description = 'Depostion List'

    """
    รายการที่ฝาก 
        โมเดลย่อยสำหรับการฝาก ทุกประเภท เก็บในโมเดลเดียวกัน ค่อยไป context view ใน form เอา ตอนแยกประเภท
    """

    # type ของ item ที่จะฝาก
    type_item = fields.Selection([
        ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'),
        ('damaged_property','ทรัพย์สินชำรุดรอการจำหน่าย')
    ])
    
    # รายละเอียดรายการที่ฝาก
    item = fields.Many2one('tiny_stock.m_item','Item')
    qty = fields.Integer(default=1)
    unit = fields.Char('Unit',related='item.item_unit')

    ## วัสดุสำนักงานสิ้นเปลือง
    ### m2o for o2m วัสดุสำนักงานสิ้นเปลือง
    m2o_office_supplies = fields.Many2one('tiny_stock.inventory','(o2m) วัสดุสำนักงานสิ้นเปลือง')

    ## อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    ### m2o for o2m อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    m2o_oracle_code_item = fields.Many2one('tiny_stock.inventory','(o2m) อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')

    ## ทรัพย์สินชำรุดรอการจำหน่าย
    ### m2o for o2m ทรัพย์สินชำรุดรอการจำหน่าย
    m2o_damaged_property = fields.Many2one('tiny_stock.inventory','(o2m) ทรัพย์สินชำรุดรอการจำหน่าย')
    item_dp_name = fields.Char('Item Name')
    item_dp_tag = fields.Char('Item Tag')
    item_dp_serial = fields.Char('Item Serial') 

class Requistion(models.Model):
    _name = 'tiny_stock.requistion'
    _description = 'Requistion List'

    """
    รายการของเบิก 
        โมเดลย่อยสำหรับการเบิก ทุกประเภท เก็บในโมเดลเดียวกัน ค่อยไป context view ใน form เอา ตอนแยกประเภท
    """

    # type ของ item ที่จะเบิก
    type_item = fields.Selection([
        ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'),
        ('damaged_property','ทรัพย์สินชำรุดรอการจำหน่าย')
    ])

    # รายละเอียดรายการที่สามารถเบิกได้
    item = fields.Many2one('tiny_stock.m_item','Item')
    qty = fields.Integer()
    unit = fields.Char('Unit',related='item.item_unit')
    stock_qty = fields.Integer('สินค้าคงเหลือ',compute="_compute_stock_qty", store=True)
    

    ## วัสดุสำนักงานสิ้นเปลือง
    ### m2o for o2m วัสดุสำนักงานสิ้นเปลือง
    m2o_office_supplies = fields.Many2one('tiny_stock.inventory','(o2m) วัสดุสำนักงานสิ้นเปลือง')

    ## อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    ### m2o for o2m อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    m2o_oracle_code_item = fields.Many2one('tiny_stock.inventory','(o2m) อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')

    ## ทรัพย์สินชำรุดรอการจำหน่าย
    ### m2o for o2m ทรัพย์สินชำรุดรอการจำหน่าย
    m2o_damaged_property = fields.Many2one('tiny_stock.inventory','(o2m) ทรัพย์สินชำรุดรอการจำหน่าย')
    item_dp_name = fields.Char('Item Name')
    item_dp_tag = fields.Char('Item Tag')
    item_dp_serial = fields.Char('Item Serial') 


    @api.depends('item')
    def _compute_stock_qty(self):
        for rec in self:
            if rec.m2o_office_supplies and rec.item:
                rec.stock_qty = self.env['tiny_stock.stock'].search([
                    ('deposit_id','=',rec.m2o_office_supplies.deposit_id.id),
                    ('item','=',rec.item.id)
                ],limit=1)['qty']
                # rec.stock_qty = rec.m2o_office_supplies.deposit_id.id
            elif rec.m2o_oracle_code_item and rec.item:
                rec.stock_qty = self.env['tiny_stock.stock'].search([
                    ('deposit_id','=',rec.m2o_oracle_code_item.deposit_id.id),
                    ('item','=',rec.item.id)
                ],limit=1)['qty']
            elif rec.m2o_damaged_property and rec.item:
                rec.stock_qty = self.env['tiny_stock.stock'].search([
                    ('deposit_id','=',rec.m2o_damaged_property.deposit_id.id),
                    ('item','=',rec.item.id)
                ],limit=1)['qty']
                    