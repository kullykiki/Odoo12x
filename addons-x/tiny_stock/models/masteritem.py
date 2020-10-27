# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class MasterItem(models.Model):
    _name = 'tiny_stock.m_item'
    _description = '[M] Item'
    _rec_name = 'item_name'

    item_name = fields.Char('Item Name')
    item_unit = fields.Char('Item Unit')
    item_type = fields.Selection([
        ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')
    ])
    item_oci_code = fields.Char('Item Code')