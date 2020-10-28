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
    
    
    
    
    ## CASE: Deposition
    history_requistion = fields.One2many('tiny_stock.inventory','deposit_id','ประวัติการเบิก')

    ### วัสดุสำนักงานสิ้นเปลือง
    b_d_office_supplies = fields.Boolean('[D] วัสดุสำนักงานสิ้นเปลือง')
    d_office_supplies_list = fields.One2many('tiny_stock.deposition','m2o_office_supplies','รายการฝากของ วัสดุสำนักงานสิ้นเปลือง')

    ### อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    b_d_oracle_code_item = fields.Boolean('[D] อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')
    d_oracle_code_item_list = fields.One2many('tiny_stock.deposition','m2o_oracle_code_item','รายการฝากของ อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')


    
    
    ## CASE: Requistion
    deposit_id = fields.Many2one('tiny_stock.inventory', 'รายการฝากเลขที่')

    ### วัสดุสำนักงานสิ้นเปลือง
    b_r_office_supplies = fields.Boolean('[R] วัสดุสำนักงานสิ้นเปลือง')
    r_office_supplies_list = fields.One2many('tiny_stock.requistion','m2o_office_supplies','รายการเบิกของ วัสดุสำนักงานสิ้นเปลือง')

    ### อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    b_r_oracle_code_item = fields.Boolean('[R] อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')
    r_oracle_code_item_list = fields.One2many('tiny_stock.requistion','m2o_oracle_code_item','รายการเบิกของ อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด')



    ## STOCK

    ### วัสดุสำนักงานสิ้นเปลือง
    s_office_supplies_list = fields.Many2many('tiny_stock.stock','s_os_inventory_x_stock','s_os_inventory_id','stock_id','รายการของคงเหลือของ วัสดุสำนักงานสิ้นเปลือง', store=True, compute="_compute_stock_item")
    
    ### อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด
    s_oracle_code_item_list = fields.Many2many('tiny_stock.stock','s_oci_inventory_x_stock','s_oci_inventory_id','stock_id','รายการของคงเหลือของ อุปกรณ์ในระบบ Oracle มีไอเท็มโค้ด', store=True, compute="_compute_stock_item")

    
    
    # @api.onchange('deposit_id')
    # def _onchange_stock_item(self):
    #     stock_list = [ x.id for x in self.env['tiny_stock.stock'].search([('deposit_id','=',self.deposit_id.id)]) ]
    #     self.stock_item = [(6,0,stock_list)]
    
    
    @api.depends('deposit_id')
    def _compute_stock_item(self):
        for rec in self:
            rec.b_r_office_supplies = True if rec.deposit_id.b_d_office_supplies else False
            rec.b_r_oracle_code_item = True if rec.deposit_id.b_d_oracle_code_item else False
            for s_item in self.env['tiny_stock.stock'].search([('deposit_id','=',rec.deposit_id.id)]):
                if s_item.type_item == 'office_supplies': 
                    rec.s_office_supplies_list = [(4,s_item.id)]
                elif s_item.type_item == 'oracle_code_item': 
                    rec.s_oracle_code_item_list = [(4,s_item.id)]                  
            # for item in self.env['tiny_stock.stock'].search([('deposit_id','=',rec.deposit_id.id)]):
            #     rec.write({'stock_item':[(4,item.id)]})
    
    
    def add_stock(self):
        """
        add item to stock.
        """
        for item in self.env['tiny_stock.deposition'].search(['|',('m2o_office_supplies','=',self.id),('m2o_oracle_code_item','=',self.id)]):
            if item.m2o_office_supplies:
                self.env['tiny_stock.stock'].create({
                    'type_item':'office_supplies',
                    'deposit_id':item.m2o_office_supplies.id,
                    'item':item.item.id,
                    'qty':item.qty,
                    'unit':item.unit})
                self.env['tiny_stock.history'].create({
                    'type_item':'office_supplies',
                    'main_id':self.id,
                    'item':item.item.id,
                    'qty':item.qty,
                    'unit':item.unit,
                    'status_list':'deposition'})
            elif item.m2o_oracle_code_item :
                self.env['tiny_stock.stock'].create({
                    'type_item':'oracle_code_item',
                    'deposit_id':item.m2o_oracle_code_item.id,
                    'item':item.item.id,
                    'qty':item.qty,
                    'unit':item.unit})
                self.env['tiny_stock.history'].create({
                    'type_item':'oracle_code_item',
                    'main_id':self.id,
                    'item':item.item.id,
                    'qty':item.qty,
                    'unit':item.unit,
                    'status_list':'deposition'})
                
               

    def reduce_stock(self):
        """
        remove item from stock.
        """
        strer = False
        if self.b_r_office_supplies:
            for item in self.r_office_supplies_list:
                if item.qty > item.stock_qty:
                    strer = "สินค้าไม่พอเบิก {} มีจำนวนสินค้าคงเหลือ : {}\n".format(item.item.item_name,item.stock_qty)
                    raise ValidationError(strer)
                elif item.qty <= item.stock_qty:
                    stock_item = self.env['tiny_stock.stock'].search([
                                        ('deposit_id','=',item.m2o_office_supplies.deposit_id.id),
                                        ('item','=',item.item.id)
                                    ],limit=1)
                    stock_item.qty = stock_item.qty - item.qty
        if self.b_r_oracle_code_item:
            for item in self.r_oracle_code_item_list:
                if item.qty > item.stock_qty:
                    strer = "สินค้าไม่พอเบิก {} มีจำนวนสินค้าคงเหลือ : {}\n".format(item.item.item_name,item.stock_qty)
                    raise ValidationError(strer)
                elif item.qty <= item.stock_qty:
                    stock_item = self.env['tiny_stock.stock'].search([
                                        ('deposit_id','=',item.m2o_oracle_code_item.deposit_id.id),
                                        ('item','=',item.item.id)
                                    ],limit=1)
                    stock_item.qty = stock_item.qty - item.qty
                    # item.stock_id.qty = item.stock_id.qty - item.qty

        
            # stock_id = self.env['tiny_stock.stock'].create({'deposit_id':self.id,'item':item.item.id,'qty':item.qty,'unit':item.unit})
            # required_id = self.env['tiny_stock.required_item'].create({'stock_id':stock_id.id,'item':item.item.id,'qty':item.qty,'unit':item.unit})
            # self.write({'required_list':[(4,required_id.id)],'stock_list':[(4,stock_id.id)]})
    # @api.model
    # def create(self, vals):
    #     if vals['value2'] > vals['value']:
    #         strer = "สินค้าไม่พอเบิก จำนวนสินค้าคงเหลือ : {}".format(vals['value'])
    #         raise ValidationError(strer)
    #     else:
    #         return super(TinyStock, self).create(vals)
    


