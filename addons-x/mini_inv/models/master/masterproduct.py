# -*- coding: utf-8 -*-

from odoo import api, fields, models

## ------------------------------------    🎁 Item Detail 📦  --------------------------------------------------------
class MasterLGProduct(models.Model):
    _name = 'mini_inv.x_master_lg_product'
    _description = '[M] Item'

    """
    Master Model Product
        โมเดลย่อยสำหรับ เก็บรายละเอียดของรายการของที่จะฝาก ทุกประเภท ยกเว้น 'ทรัพย์สินชำรุดรอการจำหน่าย'
    """

    x_name = fields.Char(string='รายการของฝาก',compute="_comp_name")
    x_item_name = fields.Char(string='ชื่อรายการ')
    x_item_unit = fields.Char(string='หน่วยนับ')
    x_item_type = fields.Selection( string='ประเภทรายการ', 
                                    selection=[ 
                                        ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
                                        ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'),
                                        ('safety','อุปกรณ์ความปลอดภัย'),
                                        ('media','สินค้าพรีเมียม หรือสื่อการตลาด')
                                    ])
    x_item_oci_code = fields.Char(string='รหัสรายการ')
    x_brand = fields.Char(string='ยี่ห้อ')
    x_version = fields.Date(string='รุ่น')
    x_color = fields.Char(string='สี')
    x_detail = fields.Char(string='รายละเอียดรายการ')
    

    @api.depends('x_item_name') 
    def _comp_name(self):
        """
        Compute x_name สำหรับ รายการต่างๆ
        """
        for rec in self:
            rec.x_name = rec.x_item_name


    
    
