# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LGInventory(models.Model):
    _name = 'mini_inv.x_lg_inventory'
    _description = 'ระบบฝากของ'

    x_name = fields.Char('เลขที่คำขอ')
    x_activity = fields.Selection(string='ประเภทคำขอ', selection=[('d', 'ฝาก'), ('r', 'เบิก')])
    x_stock = fields.Many2one(comodel_name='mini_inv.x_master_lg_stock', string='คลังที่นำฝาก')
    x_ref_deposit_id = fields.Many2one(comodel_name='mini_inv.x_lg_inventory', string='รายการฝากเลขที่')
    x_status = fields.Many2one(comodel_name='mini_inv.x_master_lg_status', string='สถานะ')
    x_approve1 = fields.Many2one(comodel_name='hr.employee', string='หัวหน้างาน')
    x_approve2 = fields.Many2one(comodel_name='hr.employee', string='ผู้มีอำนาจอนุมัติ')
    
    ## ข้อมูลผู้บันทึก
    x_emp_name = fields.Many2one(comodel_name='hr.employee', string='ชื่อผู้บันทึก')


    ## ฝาก

    ### วัสดุสำนักงานสิ้นเปลือง
    x_d_b_consumables = fields.Boolean(string='[B/D] วัสดุสำนักงานสิ้นเปลือง')
    x_d_l_consumables = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_office_supplies', string='[L/D] วัสดุสำนักงานสิ้นเปลือง')

    ### อุปกรณ์ในระบบ Oracle มี Item Code
    x_d_b_oracle_product = fields.Boolean(string='[B/D] อุปกรณ์ในระบบ Oracle มี Item Code')
    x_d_l_oracle_product = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_oracle_item', string='[L/D] อุปกรณ์ในระบบ Oracle มี Item Code')

    ### อุุปกรณ์ความปลอดภัย
    x_d_b_safety = fields.Boolean(string='[B/D] อุุปกรณ์ความปลอดภัย')
    x_d_l_safety = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_safety', string='[L/D] อุุปกรณ์ความปลอดภัย')

    ### สินค้าพรีเมียม หรือสื่อการตลาด
    x_d_b_media = fields.Boolean(string='[B/D] สินค้าพรีเมียม หรือสื่อการตลาด')
    x_d_l_media = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_media', string='[L/D] สิ้นค้าพรีเมียม หรือสื่อการตลาด')

    ### สินค้าพรีเมียม หรือสื่อการตลาด
    x_d_b_damage_product = fields.Boolean(string='[B/D] ทรัพย์สินชำรุดรอการจำหน่าย')
    x_d_l_damage_product = fields.One2many(comodel_name='mini_inv.x_lg_d_deposit', inverse_name='x_destroy_product', string='[L/D] ทรัพย์สินชำรุดรอการจำหน่าย')


    ## เบิก 

    ### วัสดุสำนักงานสิ้นเปลือง
    x_r_b_consumables = fields.Boolean(string='[B/R] วัสดุสำนักงานสิ้นเปลือง')
    x_r_l_consumables = fields.One2many(comodel_name='mini_inv.x_lg_d_requistion', inverse_name='x_office_supplies', string='[L/R] วัสดุสำนักงานสิ้นเปลือง')

    ### อุปกรณ์ในระบบ Oracle มี Item Code
    x_r_b_oracle_product = fields.Boolean(string='[B/R] อุปกรณ์ในระบบ Oracle มี Item Code')
    x_r_l_oracle_product = fields.One2many(comodel_name='mini_inv.x_lg_d_requistion', inverse_name='x_oracle_item', string='[L/R] อุปกรณ์ในระบบ Oracle มี Item Code')

    ### อุุปกรณ์ความปลอดภัย
    x_r_b_safety = fields.Boolean(string='[B/R] อุุปกรณ์ความปลอดภัย')
    x_r_l_safety = fields.One2many(comodel_name='mini_inv.x_lg_d_requistion', inverse_name='x_safety', string='[L/R] อุุปกรณ์ความปลอดภัย')

    ### สินค้าพรีเมียม หรือสื่อการตลาด
    x_r_b_media = fields.Boolean(string='[B/R] สินค้าพรีเมียม หรือสื่อการตลาด')
    x_r_l_media = fields.One2many(comodel_name='mini_inv.x_lg_d_requistion', inverse_name='x_media', string='[L/R] สิ้นค้าพรีเมียม หรือสื่อการตลาด')

    ### สินค้าพรีเมียม หรือสื่อการตลาด
    x_r_b_damage_product = fields.Boolean(string='[B/R] ทรัพย์สินชำรุดรอการจำหน่าย')
    x_r_l_damage_product = fields.One2many(comodel_name='mini_inv.x_lg_d_requistion', inverse_name='x_destroy_product', string='[L/R] ทรัพย์สินชำรุดรอการจำหน่าย')
    
    
    ## อนุมัติ

    ###หัวหน้างาน
    x_approve1_date = fields.Date(string='วันที่อนุมัติ(ผู้อนุมัติ1)')
    x_approve1 = fields.Many2one(comodel_name='hr.employee', string='ชื่อหัวหน้างาน')
    x_approve1_result = fields.Selection(string='ผลการอนุมัติ(ผู้อนุมัติ1)', selection=[('y', 'อนุมัติ'), ('n', 'ไม่อนุมัติ'),])
    x_approve1_reason = fields.Text(string='เหตุผลที่ไม่อนุมัติ(ผู้อนุมัติ1)')
    
    ###ผู้อนุมัติ
    x_approve2_date = fields.Date(string='วันที่อนุมัติ(ผู้อนุมัติ2)')
    x_approve2 = fields.Many2one(comodel_name='hr.employee', string='ชื่อผู้มีอำนาจอนุมัติ')
    x_approve2_result = fields.Selection(string='ผลการอนุมัติ(ผู้อนุมัติ2)', selection=[('y', 'อนุมัติ'), ('n', 'ไม่อนุมัติ'),])
    x_approve2_reason = fields.Text(string='เหตุผลที่ไม่อนุมัติ(ผู้อนุมัติ2)')

    ## ตรวจรับของฝาก
    x_logist_check_date = fields.Date(string='วันที่ตรวจรับ (ฝากของ)')
    x_logist_name = fields.Many2one(comodel_name='hr.employee', string='ชื่อผู้ตรวจรับ (ฝากของ)')
    x_logist_result = fields.Selection(string='ผลการตรวจรับ (ฝากของ)', selection=[('y', 'ผ่าน'), ('n', 'ไม่ผ่าน'),])
    x_logist_reason = fields.Text(string='เหตุผลที่ตรวจรับไม่ผ่าน (ฝากของ)')
    

    ## คืนของฝาก 
    x_logist_return_date = fields.Date(string='วันที่คืนของฝาก (ฝากของ)')
    x_logist_receiver = fields.Many2one(comodel_name='hr.employee', string='ชื่อผู้รับคืนของฝาก (ฝากของ)')
    x_logist_return_name = fields.Many2one(comodel_name='hr.employee', string='ชื่อผู้คืนของฝาก (ฝากของ)')
    
    ## ประวัติการเบิกของ
    x_history = fields.One2many(comodel_name='mini_inv.x_lg_inventory', inverse_name='x_ref_deposit', string='ประวัติการเบิกของ')
    
    ## รับของฝาก 
    x_r_receive_date = fields.Date(string='วันที่รับของฝาก (เบิกของ)')
    x_r_receiver = fields.Many2one(comodel_name='hr.employee', string='ชื่อผู้รับของฝากคืน (เบิกของ)')
    x_r_return_name = fields.Many2one(comodel_name='hr.employee', string='ชื่อผู้คืนของฝาก (เบิกของ)')
    
    ## ยกเลิกคำขอ
    x_cancel_date = fields.Date(string='วันที่ยกเลิกคำขอ')
    x_cancel_emp = fields.Many2one(comodel_name='hr.employee', string='ชื่อผู้ยกเลิกคำขอ')
    x_cancel_reason = fields.Text(string='เหตุผลที่ยกเลิก')
    
    ## EMAIL
    x_email_cc = fields.Char(string='email_cc')
    x_email_subject = fields.Char(string='email_subject')
    x_email_to = fields.Char(string='email_to')
    
    
    
    
    
