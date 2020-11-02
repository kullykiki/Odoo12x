# -*- coding: utf-8 -*-

from odoo import models, fields, api

class History(models.Model):
    _name = 'tiny_stock.history'
    _description = 'History List'

    """
    รายการประวัติการฝากการเบิกของ
        โมเดลที่จะแสดงประวัติการเบิกฝากของ ตามรายการของ เหมือน bookbank
    """
    
    

    # tree view ที่จะแสดง

    ## สถานะรายการ
    status_list = fields.Selection([
        ('deposition', 'ฝาก'),
        ('requistion', 'เบิก')], 
        string='กิจกรรม'
        )
    ## type ของ item ที่จะฝาก
    type_item = fields.Selection([
        ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'),
        ('damaged_property','ทรัพย์สินชำรุดรอการจำหน่าย')
    ])
    item_name = fields.Char('รายการ')
    qty = fields.Integer()
    unit = fields.Char('Unit')
    ## การทำรายการเกิดจากรายการใด
    main_id = fields.Many2one('tiny_stock.inventory','เลขที่รายการ')

    
    # รายละเอียดรายการที่สามารถเบิกได้
    item = fields.Many2one('tiny_stock.m_item','Item')
    
    ## ทรัพย์สินชำรุดรอการจำหน่าย
    item_dp_name = fields.Char('Item Name')
    item_dp_tag = fields.Char('Item Tag')
    item_dp_serial = fields.Char('Item Serial')

    

    