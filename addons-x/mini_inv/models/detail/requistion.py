# -*- coding: utf-8 -*-

from odoo import api, fields, models


## ----------------------------------------   🎅 Requistion 🤶   --------------------------------------------------------
class detailLGRequistion(models.Model):
    _name = 'mini_inv.x_lg_d_requistion'
    _description = 'Requistion'

    """
    Detail Model Requistion
        โมเดลย่อยสำหรับ เก็บรายการของที่จะเบิก โมเดลนี้มีไว้สำหรับ o2m กับ โมเดลหลัก (ใบนำฝาก/เบิก) 
        แต่ในกรณีของ 'ทรัพย์สินชำรุดรอการจำหน่าย' จะเป็น m2m แทน 
        โมเดลนี้คล้ายโมเดลย่อยฝาก (mini_inv.x_lg_d_deposit) มาก แต่ต่างกันหลายจุด 
        - จะลิ้งค์กับใบหลักเมื่อใบหลักเลือกกิจกรรมเป็น เบิก
        - หน่วยนับจะเป็น compute แทน ref
        - มีคอมพิวแสดง ยอดคงเหลือ ของของในคลัง

    ***_remain_item ยังไม่เสร็จ เพราะต้องทำ stock ให้เสร็จก่อน ***

    """

### -----------------------------------------       Field      ------------------------------------------------------

    x_name = fields.Char(string='ข้อมูลการเบิก',compute='_comp_name', store=True)
    x_requistion_type = fields.Selection(  string='ประเภทของเบิก', 
                                        selection=[ 
                                                ('office_supplies','วัสดุสำนักงานสิ้นเปลือง'),
                                                ('oracle_code_item','อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'),   
                                                ('safety','อุปกรณ์ความปลอดภัย'),
                                                ('media','สินค้าพรีเมียม หรือสื่อการตลาด'), 
                                                ('damaged_property','ทรัพย์สินชำรุดรอการจำหน่าย')  
                                        ])
    x_item = fields.Many2one(comodel_name='mini_inv.x_master_lg_product', string='รายการของฝาก')
    x_num = fields.Integer(string='จำนวน',help="จำนวนของที่ต้องการเบิก")
    x_unit = fields.Many2one(comodel_name='mini_inv.x_master_lg_unit',string='หน่วยนับ',compute="_compute_stock_unit", store=True)
    x_active = fields.Boolean(string='Active')
    x_balance = fields.Integer(string='ยอดคงเหลือ',compute='_comp_remain_item', store=True ,help='ยอดคงเหลือที่ยังสามารถเบิกได้')
    
    

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
    x_m21_lg_inventory = fields.Many2one(   comodel_name='mini_inv.x_lg_inventory', string='เลขที่ระบบฝากของ',
                                            help='มีไว้ลิ้งค์กับใบฝาก มีไว้สำหรับกรองให้เลือกของที่จะเบิกได้ จากใบฝากเลขที่ xxx เท่านั้น')
    x_m21_lg_stock = fields.Many2one(   comodel_name='mini_inv.x_lg_stock', string='อ้างอิง Stock ฝากของ',
                                        help='มีไว้สำหรับลิ้งกับ stock ในตอนเบิก จะได้ใช้ฟิวนี้ เพื่อไปตัดของใน stock' )
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
                rec.name = rec.x_destroy_item
    

    @api.depends('x_item')
    def _comp_remain_item(self):

        """
        Compute remain amount of item for requistion. except for 'ทรัพย์สินชำรุดรอการจำหน่าย'
        """
        for rec in self:
            if rec.x_office_supplies and rec.x_item:
                rec.x_balance = self.env['mini_inv.x_lg_stock'].search([
                    ('x_deposit_id','=',rec.x_office_supplies.x_deposit_id.id),
                    ('x_item','=',rec.x_item.id)
                ],limit=1)['x_qty_remain']
            elif rec.x_oracle_item and rec.x_item:
                rec.x_balance = self.env['mini_inv.x_lg_stock'].search([
                    ('x_deposit_id','=',rec.x_oracle_item.x_deposit_id.id),
                    ('x_item','=',rec.x_item.id)
                ],limit=1)['x_qty_remain']
            elif rec.x_safety and rec.x_item:
                rec.x_balance = self.env['mini_inv.x_lg_stock'].search([
                    ('x_deposit_id','=',rec.x_safety.x_deposit_id.id),
                    ('x_item','=',rec.x_item.id)
                ],limit=1)['x_qty_remain']
            elif rec.x_media and rec.x_item:
                rec.x_balance = self.env['mini_inv.x_lg_stock'].search([
                    ('x_deposit_id','=',rec.x_media.x_deposit_id.id),
                    ('x_item','=',rec.x_item.id)
                ],limit=1)['x_qty_remain']

    
    @api.depends('x_item','x_destroy_item')
    def _compute_stock_unit(self):
        """
        Compute unit of item for requistion.
        """
        for rec in self:
            if rec.x_requistion_type == 'damaged_property':
                rec.x_unit = self.env.ref('mini_inv.unit_object1')
            else:
                rec.x_unit = rec.x_item.x_item_unit.id
                