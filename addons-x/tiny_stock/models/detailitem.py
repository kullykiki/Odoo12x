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
        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')
    ])
    
    # รายละเอียดรายการที่ฝาก
    item = fields.Many2one('tiny_stock.m_item','Item')
    qty = fields.Integer()
    unit = fields.Char('Unit',related='item.item_unit')

    ## วัสดุสำนักงานสิ้นเปลือง
    ### m2o for o2m วัสดุสำนักงานสิ้นเปลือง
    m2o_office_supplies = fields.Many2one('tiny_stock.inventory','(o2m) วัสดุสำนักงานสิ้นเปลือง')

    ## อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    ### m2o for o2m อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    m2o_oracle_code_item = fields.Many2one('tiny_stock.inventory','(o2m) อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')

    


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
        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')
    ])

    # รายละเอียดรายการที่สามารถเบิกได้
    item = fields.Many2one('tiny_stock.m_item','Item')
    qty = fields.Integer()
    unit = fields.Char('Unit',related='item.item_unit')
    
    # เก็บ id ของ record ใน โมเดล stock เอาไว้เวลาตัดใน stock ได้ตัดถูกว่ามาจาก record ไหน
    stock_id = fields.Many2one('tiny_stock.stock','Stock ID')



