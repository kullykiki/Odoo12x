# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mcMedicalHistory(models.Model):
    _name = 'mc.medical_history'
    _description = 'ประวัติการรักษา'

    create_date = fields.Date(string='วันที่บันทีก')
    medical_result = fields.Text(string='บันทึกการรักษา')
    drug_in_use = fields.Many2many('mc.drug','ยาที่จะใช้ในการรักษา')
    doctor = fields.Many2one('hr.employee','หมอที่ทำการตรวจ')
    