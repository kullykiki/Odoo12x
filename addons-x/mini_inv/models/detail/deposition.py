# -*- coding: utf-8 -*-

from odoo import api, fields, models

## ------------------------------------    🎅 Deposition 🤶  --------------------------------------------------------
class detailLGDeposit(models.Model):
    _name = 'mini_inv.x_lg_d_deposit'
    _description = 'Deposition'

    """
    Detail Model Deposition
        โมเดลย่อยสำหรับ เก็บรายการของที่จะฝาก โมเดลนี้มีไว้สำหรับ o2m กับ โมเดลหลัก (ใบนำฝาก/เบิก)
    """

### -----------------------------------------       Field      ------------------------------------------------------

    x_name = fields.Char(string='ข้อมูลการฝาก',compute='_comp_name', store=True)
    x_deposit_type = fields.Selection(  string='ประเภทของฝาก', 
                                        selection=[ 
                                                ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
                                                ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'),   
                                                ('safety','อุปกรณ์ความปลอดภัย'),
                                                ('media','สินค้าพรีเมียม หรือสื่อการตลาด'), 
                                                ('damaged_property','ทรัพย์สินชำรุดรอการจำหน่าย')  
                                        ])
    x_item = fields.Many2one(comodel_name='mini_inv.x_master_lg_product', string='รายการของฝาก')
    x_num = fields.Integer(string='จำนวน')
    x_unit = fields.Many2one(comodel_name='mini_inv.x_master_lg_unit',string='หน่วยนับ',related='x_item.x_item_unit')
    x_active = fields.Boolean(string='Active')

    ## วัสดุสำนักงานสิ้นเปลือง
    ### m2o for o2m วัสดุสำนักงานสิ้นเปลือง
    x_office_supplies = fields.Many2one(comodel_name='mini_inv.x_lg_inventory', string='(o2m) วัสดุสำนักงานสิ้นเปลือง')
    
    ## อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    x_oracle_item_code = fields.Char(string='Item code',related="x_item.x_item_oci_code")
    ### m2o for o2m อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด  
    x_oracle_item = fields.Many2one(comodel_name='mini_inv.x_lg_inventory', string='(o2m) อุปกรณ์ในระบบ Oracle มี Item Code')
    
    ## อุปกรณ์ความปลอดภัย
    ### m2o for o2m อุปกรณ์ความปลอดภัย
    x_safety = fields.Many2one(comodel_name='mini_inv.x_lg_inventory', string='(o2m) อุุปกรณ์ความปลอดภัย')

    ## สินค้าพรีเมียม หรือสื่อการตลาด
    ### m2o for o2m สินค้าพรีเมียม หรือสื่อการตลาด
    x_media = fields.Many2one(comodel_name='mini_inv.x_lg_inventory', string='(o2m) สินค้าพรีเมียม หรือสื่อการตลาด')
    
    ## ทรัพย์สินชำรุดรอการจำหน่าย
    x_destroy_item = fields.Char(string='[DP] Category Name')
    x_destroy_serial = fields.Char(string='[DP] Serial No.')
    x_destroy_tag = fields.Char(string='[DP] Tag No.')
    x_destroy_model = fields.Char(string='[DP] Model')
    ### m2o for o2m ทรัพย์สินชำรุดรอการจำหน่าย
    x_destroy_product = fields.Many2one(comodel_name='mini_inv.x_lg_inventory', string='(o2m) ทรัพย์สินชำรุดรอการจำหน่าย')
    
### ------------------------------------       Compute Function      ------------------------------------------------------
    @api.depends('x_item','x_destroy_item')
    def _comp_name(self):
        """
        Compute x_name of Deposition
        """
        for rec in self:
            if rec.x_item:
                rec.x_name = rec.x_item.x_name
            elif rec.x_destroy_item:
                rec.x_name = rec.x_destroy_item