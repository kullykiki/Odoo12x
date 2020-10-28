# -*- coding: utf-8 -*-

from odoo import models, fields, api

class History(models.Model):
    _name = 'tiny_stock.history'
    _description = 'History List'

    """
    รายการประวัติการฝากการเบิกของ
        โมเดลที่จะแสดงประวัติการเบิกฝากของ ตามรายการของ เหมือน bookbank
    """
    
    # type ของ item ที่จะฝาก
    type_item = fields.Selection([
        ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')
    ])

    # รายละเอียดรายการที่สามารถเบิกได้
    item = fields.Many2one('tiny_stock.m_item','Item')
    qty = fields.Integer()
    unit = fields.Char('Unit',related='item.item_unit')

    # การทำรายการเกิดจากรายการใด
    main_id = fields.Many2one('tiny_stock.inventory','เลขที่รายการ')

    # สถานะรายการ
    status_list = fields.Selection([
        ('deposition', 'ฝาก'),
        ('requistion', 'ถอน')], 
        string='กิจกรรม'
        )