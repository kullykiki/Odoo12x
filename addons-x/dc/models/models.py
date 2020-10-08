# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class dc(models.Model):
    _name = 'dc.x_dc_dar'
    _description = 'Document Action Request (DAR)'
    _inherit = ['mail.thread']

    x_name = fields.Char('DAR No.')
    x_12m_attach = fields.One2many('dc.x_dc_master_list','x_m21_dc_dar','แนบไฟล์เอกสารต้นฉบับ')
    x_approver = fields.Many2one('hr.employee','ผู้อนุมัติ')
    x_attach = fields.Selection([('y','มี'),('n','ไม่มี')],'เอกสารที่แนบมาด้วย')
    x_attach_pdf_doc = fields.Many2many('dc.x_dc_master_list','x_x_dc_dar_x_dc_master_list_rel','x_dc_dar_id','x_dc_master_list_id','แนบไฟล์เอกสารที่จะเผยแพร่ (PDF)')
    x_cancel_reason = fields.Text('เหตุผลที่ยกเลิกใบ DAR')
    x_check_attach_comp = fields.Char('[comp] attach',compute="_check_attach_comp")
    x_comp_check_id = fields.Char('ตรวจสอบรหัสเอกสารซ้ำ')
    x_dept = fields.Many2one('hr.department','หน่วยงาน')
    x_detail = fields.Text('ข้อมูลการแก้ไข (แก้ไขใหม่)')
    x_doc_id = fields.Char('รหัสเอกสาร')
    x_doc_maker = fields.Many2one('hr.employee','ชื่อผู้จัดทำเอกสาร/คู่มือ')
    x_doc_name = fields.Char('ชื่อเอกสาร')
    x_doc_type = fields.Many2one('x_master_dc_doc_type','ประเภทเอกสาร')
    x_inspector = fields.Many2one('hr.employee','ผู้ทบทวน')
    x_m21_doc_master_list = fields.Many2one('dc.x_dc_master_list','Document Master List')
    x_new_revise = fields.Integer('แก้ไขครั้งที่ใหม่ (แก้ไขใหม่)')
    x_new_start_date = fields.Date('วันที่มีผลบังคับใช้ (แก้ไขใหม่)')
    x_old_doc = fields.Many2one('dc.x_dc_master_list','ข้อมูลเอกสารเดิม')
    x_page = fields.Char('หน้าที่แก้ไข (แก้ไขใหม่)')
    x_privacy = fields.Selection([('1','Private'),('2','Public')],'ความเป็นส่วนตัวของข้อมูล')
    x_publish_date = fields.Date('วันที่เผยแพร่ในระบบ')
    x_purpose = fields.Many2one('x_master_dc_purpose','ยื่นคำร้องเพื่อ')
    x_request_name = fields.Many2one('hr.employee','ผู้จัดทำ')
    x_request_phone = fields.Char('เบอร์ติดต่อผู้จัดทำ')
    x_revise_no = fields.Integer('แก้ไขครั้งที่ (เอกสารเดิม)')
    x_start_date = fields.Date('วันที่มีผลบังคับใช้ (เอกสารเดิม)')
    x_status_dar = fields.Many2one('dc.x_master_dc_status','สถานะ DAR',track_visibility = 'onchange')


    @api.depends('create_date')
    def _dar_no(self):
        for record in self:
            if record['x_name'] == False  and record['create_date'] != False:
                dar_no = self.env['ir.sequence'].next_by_code('dar_no')
                date_now = datetime.datetime.now()
                buddha_year = int(date_now.year) + 543
                by = str(buddha_year)
                record['x_name'] = "{}-{}".format(dar_no,by[2:])

    @api.depends('x_12m_attach')
    def _check_attach_comp(self):
        for record in self:
            if len(record['x_12m_attach']) > 0:
                record['x_check_attach_comp'] = "T"
            else:
                record['x_check_attach_comp'] = "F"
    
    @api.depends('x_doc_id')
    def _comp_check_id(self):
        for record in self:
            c = self.env['x_dc_dar'].search([['x_doc_id', '=', record['x_doc_id']]])
            if len(c) > 0 :
                record['x_comp_check_id'] = ""
            else:
                record['x_comp_check_id'] = "mai mee"

class x_dc_master_list(models.Model):
    _name = 'dc.x_dc_master_list'
    _description = 'Document Master List'

    x_name = fields.Char('รหัสเอกสาร',related='x_m21_dc_dar.x_doc_id')
    x_attach_pdf = fields.Many2many('ir.attachment','x_ir_attachment_x_dc_master_list_rel_attach_pdf','x_dc_master_list_id','ir_attachment_id','แนบไฟล์เผยแพร่ในระบบ DC')
    x_attach_url = fields.Char('Website / URL')
    x_cancel_doc = fields.Boolean('เอกสารยกเลิก')
    x_clip = fields.Many2many('ir.attachment','x_ir_attachment_x_dc_master_list_rel_x_clip','x_dc_master_list_id_x_clip','ir_attachment_id_x_clip','ไฟล์คลิปวิดีโอ')
    x_comp = fields.Char('comp')
    x_compute_url = fields.Char('[Comp] ตรวจสอบ URL ของท่าน',compute='_attach_url', store=True)
    x_dc_remark = fields.Text('หมายเหตุ (สำหรับเจ้าหน้าที่ DC)')
    x_dept = fields.Many2one('hr.department','ผู้ครอบครองเอกสาร',related='x_m21_dc_dar.x_dept')
    x_doc_file_old = fields.Many2many('ir.attachment','x_ir_attachment_x_dc_master_list_rel_file_old','x_dc_master_list_id','ir_attachment_id','ไฟล์เอกสารต้นฉบับ')
    x_doc_name = fields.Char('รายชื่อเอกสาร',related='x_m21_dc_dar.x_doc_name')
    x_doc_status = fields.Selection([('1','เอกสารกำลังใช้งาน'),('2','เอกสารยกเลิก')],'สถานะเอกสาร')
    x_end_doc = fields.Boolean('สิ้นสุดการใช้งาน')
    x_last_doc = fields.Boolean('เอกสารล่าสุด')
    x_m21_dc_dar = fields.Many2one('dc.x_dc_dar','DAR No.')
    x_new_doc = fields.Boolean('เอกสารใหม่')
    x_old_doc = fields.Boolean('เอกสารเก่า')
    x_publish_date = fields.Date('วันที่มีผลบังคับใช้',related='x_m21_dc_dar.x_new_start_date')
    x_ref_doc_type = fields.Many2one('dc.x_master_dc_doc_type','ประเภทเอกสาร',related='x_m21_dc_dar.x_doc_type')
    x_ref_privacy = fields.Selection([('1','Private'),('2','Public')],'privacy')
    x_ref_purpose = fields.Many2one('dc.x_master_dc_purpose','ยื่นคำร้องเพื่อ',related='x_m21_dc_dar.x_purpose')
    x_remark = fields.Text('หมายเหตุ (สำหรับเจ้าหน้าที่ DC)')
    x_revise_no = fields.Integer('แก้ไขครั้งที่',related='x_m21_dc_dar.x_new_revise')
    x_revise_no_char = fields.Char('แก้ไขครั้งที่ (char)',compute='_revise_no', store=True)
    x_use_doc = fields.Boolean('เอกสารกำลังใช้งาน')
    x_wait_cancel_doc = fields.Boolean('เอกสารรอการยกเลิก')

    @api.depends('x_attach_url')
    def _attach_url(self):
        for record in self:
            record['x_compute_url'] = ""
            if record['x_attach_url'] != False and record['x_attach_url'][0:4] == 'http':
                record['x_compute_url'] = record['x_attach_url']
            else:
                record['x_compute_url'] = ""
    
    @api.depends('x_revise_no')
    def _revise_no(self):
        for record in self:
            record['x_revise_no_char'] = str(record['x_revise_no'])

    