# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import datetime
from odoo.http import Response, request

class m_dept(models.Model):
    _name = 'jas_storage.m_dept'

    name = fields.Char(string="ฝ่าย")

class m_rights(models.Model):
    _name = 'jas_storage.m_rights'

    name = fields.Char(string="email")
    dept = fields.Many2one(comodel_name='jas_storage.m_dept', string='ฝ่าย', track_visibility='onchange')
    section = fields.Char(string="ส่วนงาน", track_visibility='onchange')
    province = fields.Char(string="จังหวัด", track_visibility='onchange')
    user_rights = fields.Boolean(string="สิทธิ์ User")
    admin_rights = fields.Boolean(string="สิทธิ์ Admin")

class main(models.Model):
    _name = 'jas_storage.main'
    _inherit = 'mail.thread'

    def _default_employee(self):
        return self.env['hr.employee'].search([('user_id', '=', self.env.uid)],order="id desc", limit=1)

    # def _default_user(self):
    #     data = self.env['hr.employee'].search([('user_id', '=', self.env.uid)],order="id desc", limit=1)
    #     data_access_user = self.env['jas_storage.m_rigths'].search([['name','=',data[0]['email']]])
    #     if len(data_access_user) > 0 :
    #         return 


    name = fields.Char(string="เลขที่")
    attach = fields.Many2many(comodel_name="ir.attachment",relation="ir_attachment_jas_storage_rel_attach",string="แนบไฟล์", track_visibility='onchange')
    create_name = fields.Many2one(comodel_name='jas_storage.m_rights', string='ผู้สร้าง', track_visibility='onchange')
    dept = fields.Many2one(comodel_name='jas_storage.m_dept', string='ฝ่าย', track_visibility='onchange')
    section = fields.Char(string="ส่วนงาน", related='create_name.section', track_visibility='onchange')
    province = fields.Char(string="จังหวัด", related='create_name.province', track_visibility='onchange')
    employee_ids = fields.Many2one(comodel_name='hr.employee', string="พนักงาน", default=_default_employee, track_visibility='onchange')
    employee_work_place = fields.Char(string="สถานที่ทำงาน", related="employee_ids.work_location", track_visibility='onchange')

    

    @api.model
    def create(self, values):
        data = self.env['res.users'].search([['id','=',self.env.uid]])
        data_access_user = self.env['jas_storage.m_rights'].search([['name','=',data[0]['email']]])
        if len(data_access_user) > 0 :
            sequence =  self.env['jas_storage.main'].search([['dept','=',data_access_user[0]['dept']['id']]])
            values['name'] = str(data_access_user[0]['dept']['name']) + "_" +str(len(sequence)+1)
        res = super(main, self).create(values)
        return res

    @api.onchange('employee_ids')
    def _onchange_defualt(self):
        for record in self:
            data = self.env['res.users'].search([['id','=',self.env.uid]])
            data_access_user = self.env['jas_storage.m_rights'].search([['name','=',data[0]['email']]])
            record['create_name'] = data_access_user[0]['id']
            record['dept'] = data_access_user[0]['dept']

    @api.multi
    def action_download_attachment(self):
        tab_id = []
        rec_id = []
        for attachment in self:
            for file in attachment['attach']:
                tab_id.append(file.id)
                rec_id.append(attachment.id)
        url = '/web/binary/download_document?tab_id={}&rec_id={}' .format(tab_id,rec_id)
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }
    
    