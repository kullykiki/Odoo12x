# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Inventory(models.Model):
    _name = 'tiny_stock.inventory'
    _description = 'Inventory'

    """
    ระบบรับฝากของ ทำทั้งการ ฝาก และ เบิกของที่ฝากไว้
    """

   
    name = fields.Char(string='เลขที่')
    
    type_doc = fields.Selection([
        ('deposition', 'Deposition'),
        ('requistion', 'Requistion')], string='กิจกรรม',
        copy=False, default='deposition', required=True)
    
    actor = fields.Many2one('hr.employee','ผู้เขียนคำร้อง')
    
    
    
    ## CASE: Deposition
    history_requistion = fields.One2many('tiny_stock.inventory','deposit_id','ประวัติการเบิก')

    ### วัสดุสำนักงานสิ้นเปลือง
    b_d_office_supplies = fields.Boolean('[D] วัสดุสำนักงานสิ้นเปลือง')
    d_office_supplies_list = fields.One2many('tiny_stock.deposition','m2o_office_supplies','รายการฝากของ วัสดุสำนักงานสิ้นเปลือง')

    ### อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    b_d_oracle_code_item = fields.Boolean('[D] อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')
    d_oracle_code_item_list = fields.One2many('tiny_stock.deposition','m2o_oracle_code_item','รายการฝากของ อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')

    ## ทรัพย์สินชำรุดรอการจำหน่าย
    b_d_damaged_property = fields.Boolean('[D] ทรัพย์สินชำรุดรอการจำหน่าย')
    d_damaged_property_list = fields.One2many('tiny_stock.deposition','m2o_damaged_property','รายการฝากของ ทรัพย์สินชำรุดรอการจำหน่าย')
    
    ## CASE: Requistion
    deposit_id = fields.Many2one('tiny_stock.inventory', 'รายการฝากเลขที่')

    ##### o2m
    ### วัสดุสำนักงานสิ้นเปลือง
    b_r_office_supplies = fields.Boolean('[R] วัสดุสำนักงานสิ้นเปลือง')
    r_office_supplies_list = fields.One2many('tiny_stock.requistion','m2o_office_supplies','รายการเบิกของ วัสดุสำนักงานสิ้นเปลือง')

    ##### o2m
    ### อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    b_r_oracle_code_item = fields.Boolean('[R] อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')
    r_oracle_code_item_list = fields.One2many('tiny_stock.requistion','m2o_oracle_code_item','รายการเบิกของ อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')

    ##### m2m
    ### ทรัพย์สินชำรุดรอการจำหน่าย
    b_r_damaged_property = fields.Boolean('[R] ทรัพย์สินชำรุดรอการจำหน่าย')
    r_damaged_property_list = fields.Many2many('tiny_stock.requistion',
                                                'r_dp_inventory_x_requistion',
                                                'r_dp_inventory_id','requistion_id',
                                                'รายการเบิกของ ทรัพย์สินชำรุดรอการจำหน่าย'
                                                )



    ## STOCK

    ### วัสดุสำนักงานสิ้นเปลือง
    s_office_supplies_list = fields.Many2many('tiny_stock.stock','s_os_inventory_x_stock','s_os_inventory_id','stock_id','รายการของคงเหลือของ วัสดุสำนักงานสิ้นเปลือง', store=True, compute="_compute_stock_item")
    
    ### อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    s_oracle_code_item_list = fields.Many2many('tiny_stock.stock','s_oci_inventory_x_stock','s_oci_inventory_id','stock_id','รายการของคงเหลือของ อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด', store=True, compute="_compute_stock_item")

    ### ทรัพย์สินชำรุดรอการจำหน่าย
    s_damaged_property_list = fields.Many2many('tiny_stock.stock','s_dp_inventory_x_stock','s_dp_inventory_id','stock_id','รายการของคงเหลือของ ทรัพย์สินชำรุดรอการจำหน่าย', store=True, compute="_compute_stock_item")

    
    
    # @api.onchange('deposit_id')
    # def _onchange_stock_item(self):
    #     stock_list = [ x.id for x in self.env['tiny_stock.stock'].search([('deposit_id','=',self.deposit_id.id)]) ]
    #     self.stock_item = [(6,0,stock_list)]
    
    
    @api.depends('deposit_id')
    def _compute_stock_item(self):
        for rec in self:
            rec.b_r_office_supplies = True if rec.deposit_id.b_d_office_supplies else False
            rec.b_r_oracle_code_item = True if rec.deposit_id.b_d_oracle_code_item else False
            rec.b_r_damaged_property = True if rec.deposit_id.b_d_damaged_property else False
            for s_item in self.env['tiny_stock.stock'].search([('deposit_id','=',rec.deposit_id.id)]):
                if s_item.type_item == 'office_supplies': 
                    rec.s_office_supplies_list = [(4,s_item.id)]
                elif s_item.type_item == 'oracle_code_item': 
                    rec.s_oracle_code_item_list = [(4,s_item.id)]    
                elif s_item.type_item == 'damaged_property': 
                    rec.s_damaged_property_list = [(4,s_item.id)]                 
            
    
    def add_stock(self):
        """
        add item to stock.
        """
        office_supplies_item_all_id = [ x.item.id for x in self.env['tiny_stock.deposition'].search([('m2o_office_supplies','=',self.id)]) ]
        office_supplies_item_dup = [ x for x in office_supplies_item_all_id if office_supplies_item_all_id.count(x) > 1 ]
        if len(office_supplies_item_dup) > 0:
            raise ValidationError("มีการเลือกรายการสินค้าซ้ำ กรุณารวบยอดเป็นก้อนเดียว ใน 'วัสดุสำนักงานสิ้นเปลือง'")
        
        oracle_code_item_all_id = [ x.item.id for x in self.env['tiny_stock.deposition'].search([('m2o_oracle_code_item','=',self.id)]) ]
        oracle_code_item_dup = [x for x in oracle_code_item_all_id if oracle_code_item_all_id.count(x) > 1]
        if len(oracle_code_item_dup) > 0:
            raise ValidationError("มีการเลือกรายการสินค้าซ้ำ กรุณารวบยอดเป็นก้อนเดียว ใน 'อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด'")
        
        
        for item in self.env['tiny_stock.deposition'].search(['|','|',('m2o_office_supplies','=',self.id),('m2o_oracle_code_item','=',self.id),('m2o_damaged_property','=',self.id)]):
            if item.m2o_office_supplies and not item.acheive:
                self.env['tiny_stock.stock'].create({
                    'type_item':'office_supplies',
                    'deposit_id':item.m2o_office_supplies.id,
                    'item_name':item.item.item_name,
                    'item':item.item.id,
                    'qty':item.qty,
                    'qty_lock':0,
                    'unit':item.item.item_unit})
                self.env['tiny_stock.history'].create({
                    'type_item':'office_supplies',
                    'main_id':self.id,
                    'item_name':item.item.item_name,
                    'item':item.item.id,
                    'qty':item.qty,
                    'unit':item.item.item_unit,
                    'status_list':'deposition'})
                item.acheive = True
            elif item.m2o_oracle_code_item and not item.acheive:
                self.env['tiny_stock.stock'].create({
                    'type_item':'oracle_code_item',
                    'deposit_id':item.m2o_oracle_code_item.id,
                    'item_name':item.item.item_name,
                    'item':item.item.id,
                    'qty':item.qty,
                    'qty_lock':0,
                    'unit':item.item.item_unit})
                self.env['tiny_stock.history'].create({
                    'type_item':'oracle_code_item',
                    'main_id':self.id,
                    'item_name':item.item.item_name,
                    'item':item.item.id,
                    'qty':item.qty,
                    'unit':item.item.item_unit,
                    'status_list':'deposition'})
                item.acheive = True
            elif item.m2o_damaged_property and not item.acheive:
                stock_id = self.env['tiny_stock.stock'].create({
                    'type_item':'damaged_property',
                    'deposit_id':item.m2o_damaged_property.id,
                    'item_name':"{} (S: {}/T: {})".format(item.item_dp_name,item.item_dp_serial,item.item_dp_tag),
                    'item_dp_name':item.item_dp_name,
                    'item_dp_tag':item.item_dp_tag,
                    'item_dp_serial':item.item_dp_serial,
                    'qty':1,
                    'qty_lock':0,
                    'unit':'ชิ้น'
                    })
                self.env['tiny_stock.history'].create({
                    'type_item':'damaged_property',
                    'main_id':self.id,
                    'item_name':"{} (S: {}/T: {})".format(item.item_dp_name,item.item_dp_serial,item.item_dp_tag),
                    'item_dp_name':item.item_dp_name,
                    'item_dp_tag':item.item_dp_tag,
                    'item_dp_serial':item.item_dp_serial,
                    'qty':1,
                    'unit':'ชิ้น',
                    'status_list':'deposition'})
                self.env['tiny_stock.requistion'].create({
                    'type_item':'damaged_property',
                    'm2o_s_damaged_property':stock_id.id,
                    'm2o_inv_damaged_property':self.id,
                    'main_id':self.id,
                    'item_name':"{} (S: {}/T: {})".format(item.item_dp_name,item.item_dp_serial,item.item_dp_tag),
                    'item_dp_name':item.item_dp_name,
                    'item_dp_tag':item.item_dp_tag,
                    'item_dp_serial':item.item_dp_serial,
                    'qty':1,
                    'unit':'ชิ้น',
                    'status_list':'deposition'})
                item.acheive = True
                
               

    def reduce_stock(self):
        """
        remove item from stock.
        """
        strer = False
        if self.b_r_office_supplies:
            for item in self.r_office_supplies_list:
                item.item_name = item.item.item_name
                if item.qty > item.stock_qty:
                    strer = "สินค้าไม่พอเบิก {} มีจำนวนสินค้าคงเหลือ : {}\n".format(item.item.item_name,item.stock_qty)
                    raise ValidationError(strer)
                elif item.qty <= item.stock_qty and not item.acheive:
                    stock_item = self.env['tiny_stock.stock'].search([
                                        ('deposit_id','=',item.m2o_office_supplies.deposit_id.id),
                                        ('item','=',item.item.id)
                                    ],limit=1)
                    self.env['tiny_stock.history'].create({
                    'type_item':'office_supplies',
                    'main_id':self.id,
                    'item_name':item.item.item_name,
                    'item':item.item.id,
                    'qty':item.qty,
                    'unit':item.item.item_unit,
                    'status_list':'requistion'})
                    stock_item.qty = stock_item.qty - item.qty
                    stock_item.qty_lock = item.qty
                    item.acheive = True
        if self.b_r_oracle_code_item:
            for item in self.r_oracle_code_item_list:
                item.item_name = item.item.item_name
                if item.qty > item.stock_qty:
                    strer = "สินค้าไม่พอเบิก {} มีจำนวนสินค้าคงเหลือ : {}\n".format(item.item.item_name,item.stock_qty)
                    raise ValidationError(strer)
                elif item.qty <= item.stock_qty and not item.acheive:
                    stock_item = self.env['tiny_stock.stock'].search([
                                        ('deposit_id','=',item.m2o_oracle_code_item.deposit_id.id),
                                        ('item','=',item.item.id)
                                    ],limit=1)
                    self.env['tiny_stock.history'].create({
                    'type_item':'oracle_code_item',
                    'main_id':self.id,
                    'item_name':item.item.item_name,
                    'item':item.item.id,
                    'qty':item.qty,
                    'unit':item.item.item_unit,
                    'status_list':'requistion'})
                    stock_item.qty = stock_item.qty - item.qty
                    stock_item.qty_lock = item.qty
                    item.acheive = True
        if self.b_r_damaged_property:
            for item in self.r_damaged_property_list:
                if not item.qty:
                    strer = "สินค้ารายการ {} มีจำนวนสินค้าคงเหลือ : {}\n".format(item.item_dp_name,item.qty)
                    raise ValidationError(strer)
                elif item.qty and not item.acheive:
                    stock_item = self.env['tiny_stock.stock'].search([
                                        ('id','=',item.m2o_s_damaged_property.id)
                                    ],limit=1)
                    self.env['tiny_stock.history'].create({
                    'type_item':'damaged_property',
                    'main_id':self.id,
                    'item_name':"{} (S: {}/T: {})".format(item.item_dp_name,item.item_dp_serial,item.item_dp_tag),
                    'item_dp_name':item.item_dp_name,
                    'qty':1,
                    'unit':'ชิ้น',
                    'status_list':'requistion'})
                    stock_item.qty = 0
                    stock_item.qty_lock = 1
                    item.qty = 0
                    item.acheive = True
                  
    def pick_up_item(self):
        """
        รับของออกจากคลังแล้วจร้าา
        """
        if self.b_r_office_supplies :
            for item in self.r_office_supplies_list:
                stock = self.env['tiny_stock.stock'].search([('deposit_id','=',self.deposit_id.id),('item','=',item.item.id)])
                stock.qty_lock = 0
        if self.b_r_oracle_code_item :
            for item in self.r_oracle_code_item_list:
                stock = self.env['tiny_stock.stock'].search([('deposit_id','=',self.deposit_id.id),('item','=',item.item.id)])
                stock.qty_lock = 0
        if self.b_r_damaged_property :
            for item in self.r_damaged_property_list:
                stock = self.env['tiny_stock.stock'].search([('deposit_id','=',self.deposit_id.id),('item_dp_name','=',item.item_dp_name),('item_dp_tag','=',item.item_dp_tag),('item_dp_serial','=',item.item_dp_serial)])
                stock.qty_lock = 0
        

    # @api.model
    # def create(self, vals):
    #     if vals['value2'] > vals['value']:
    #         strer = "สินค้าไม่พอเบิก จำนวนสินค้าคงเหลือ : {}".format(vals['value'])
    #         raise ValidationError(strer)
    #     else:
    #         return super(TinyStock, self).create(vals)
    


