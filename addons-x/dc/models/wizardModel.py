# -*- coding: utf-8 -*-

from odoo import models, fields, api


class x_dc_wizard_attach_file(models.TransientModel):
    _name = 'dc.x_dc_wizard_attach_file'
    _description = '[DC][W] แนบเอกสารต้นฉบับ'

    x_name = fields.Char('Name')
    x_attach_file = fields.Many2many('ir.attachment','x_ir_attachment_x_dc_wizard_attach_file_rel_af',
        'x_dc_wizard_attach_file_id','ir_attachment_id','แนบไฟล์เอกสารต้นฉบับ')
    x_clip = fields.Many2many('ir.attachment','x_ir_attachment_x_dc_wizard_attach_file_rel_x_clip',
        'x_dc_wizard_attach_file_id_x_clip','ir_attachment_id_x_clip','แนบไฟล์คลิปวิดีโอ')
    x_remark = fields.Text('หมายเหตุ')
    x_url = fields.Char('Website / Url')

class x_dc_wizard_cancel_dar(models.TransientModel):
    _name = 'dc.x_dc_wizard_cancel_dar'
    _description = '[DC][W] ยกเลิกใบ DAR'

    x_name = fields.Char('Id record')
    x_cancle_reason = fields.Text('เหตุผลที่ยกเลิก')

class x_dc_wizard_publish_date(models.TransientModel):
    _name = 'dc.x_dc_wizard_publish_date'
    _description = '[DC][W] เผยแพร่ในระบบ DC'

    x_name = fields.Char('Id record')
    x_attach_pdf_doc = fields.Many2many('ir.attachment','x_ir_attachment_x_dc_wizard_publish_date_rel',
        'x_dc_wizard_publish_date_id','ir_attachment_id','แนบไฟล์เอกสารที่จะเผยแพร่ (PDF)')
    x_public_date = fields.Date('วันที่เผยแพร่ในระบบ DC')

class x_dc_wizard_edit(models.TransientModel):
    _name = 'dc.x_dc_wizard_edit'
    _description = '[DC][W] แก้ไขเอกสารต้นฉบับ / คลิปวีดีโอ'

    x_name = fields.Char('Id record')
    x_attach = fields.Selection([('y','มี'),('n','ไม่มี')],'เอกสารที่แนบมาด้วย')
    x_attach_doc = fields.Many2many('ir.attachment','x_ir_attachment_x_dc_wizard_edit_rel_attach_doc',
        'x_dc_wizard_edit_id','ir_attachment_id','แนบไฟล์เอกสาร')
    x_clip = fields.Many2many('ir.attachment','x_ir_attachment_x_dc_wizard_edit_rel_x_clip',
        'x_dc_wizard_edit_id_x_clip','ir_attachment_id_x_clip','แนบไฟล์คลิปวิดีโอ')
    x_detail = fields.Text('ข้อมูลการแก้ไข (แก้ไขใหม่)')
    x_new_revise = fields.Integer('แก้ไขครั้งที่ใหม่ (แก้ไขใหม่)')
    x_new_start_date = fields.Date('วันที่เริ่มใช้ (แก้ไขใหม่)')
    x_page = fields.Char('หน้าที่แก้ไข (แก้ไขใหม่)')
    x_remark = fields.Text('หมายเหตุ')
    x_url = fields.Char('Website / Url')
