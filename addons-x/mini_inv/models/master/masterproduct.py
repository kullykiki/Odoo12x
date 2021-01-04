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
    x_version = fields.Char(string='รุ่น')
    x_color = fields.Char(string='สี')
    x_detail = fields.Char(string='รายละเอียดรายการ')
    
    @api.onchange('x_item_type')
    def _clear_data(self):
        """
        clear ยี่ห้อ รุ่น สี รหัสรายการ รายละเอียด
        """
        self.x_brand = False
        self.x_color = False
        self.x_detail = False
        self.x_item_oci_code = False
        self.x_version = False


    @api.depends('x_item_name','x_item_oci_code','x_brand','x_color','x_version','x_item_unit') 
    def _comp_name(self):
        """
        Compute x_name สำหรับ รายการต่างๆ
        """
        for rec in self:
            rec.x_name = rec.x_item_name
            if rec.x_item_unit:
                rec.x_name = rec.x_name + ' [หน่วยนับ:' + rec.x_item_unit + ']'
            if rec.x_item_oci_code:
                rec.x_name = rec.x_name + ' รหัส ' + rec.x_item_oci_code
            if rec.x_brand:
                rec.x_name = rec.x_name + ' ยี่ห้อ ' + rec.x_brand
            if rec.x_version:
                rec.x_name = rec.x_name + ' ' + rec.x_version
            if rec.x_color :
                rec.x_name = rec.x_name + ' ' + rec.x_color
            


    
    
