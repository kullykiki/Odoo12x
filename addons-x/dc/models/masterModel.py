from odoo import models, fields, api

class masterDcDocType(models.Model):
    _name = 'dc.x_master_dc_doc_type'
    _description = '[M] ประเภทเอกสาร'

    x_name = fields.Char('ประเภทเอกสาร')

class masterDcPurpose(models.Model):
    _name = 'dc.x_master_dc_purpose'
    _description = '[M] วัตถุประสงค์ยื่นคำร้อง'

    x_name = fields.Char('วัตถุประสงค์ยิ่นคำร้อง')

class masterDcStatus(models.Model):
    _name = 'dc.x_master_dc_status'
    _description = '[M] สถานะเอกสาร (DAR)'

    x_name = fields.Char('สถานะเอกสาร')