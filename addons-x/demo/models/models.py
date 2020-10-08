# -*- coding: utf-8 -*-

from odoo import models, fields, api


class demo(models.Model):
    _name = 'demo.x_demo_odoo'
    _description = 'ข้อมูลลูกค้าที่ Corporate'
    _inherit = ['mail.thread']

    x_active = fields.Boolean('Active',default=True, track_visibility = 'onchange')
    x_name = fields.Char('บริษัท/สาขา',compute="_compute_name", store=True)
    x_branch = fields.Char('สาขา')
    x_company = fields.Char('ชื่อบริษัท')
    x_contact = fields.One2many('demo.x_demo_contact','x_m21_demo','ผู้ติดต่อ')
    x_products = fields.Many2many('demo.x_master_products','x_x_demo_odoo_x_master_products_rel',
                                    'x_demo_odoo_id','x_master_products_id','ประเภทรายการสินค้า')
    x_remark = fields.Text('หมายเหตุ')
    x_title = fields.Many2one('demo.x_master_title_company','คำนำหน้าชื่อบริษัท')

    @api.depends('x_branch','x_company','x_title')
    def _compute_name(self):
        for rec in self:
            if rec.x_branch and rec.x_company and rec.x_title:
                rec.x_name = "{} {} สาขา {}".format(rec.x_title.x_name,rec.x_company,rec.x_branch)
    
    def toggle_x_active(self):
        """ Inverse the value of the field ``x_active`` on the records in ``self``. """
        for record in self:
            record.x_active = not record.x_active

    @api.model
    def create(self, values):
        res = super(demo, self).create(values)
        # # Kully debug
        # import pdb
        # pdb.set_trace()
        body = "Welcome {}".format(res['x_name'])
        self.message_post(body=body, message_type='notification', subtype='mail.mt_comment', author_id=self.env.user.partner_id.id, notification_ids=[(0,0,{
            'res_partner_id':self.env.user.partner_id.id,
            'notification_type':'inbox'})])
        return res
    


class demoDetailContact(models.Model):
    _name = 'demo.x_demo_contact'
    _description = '[D/demo] ข้อมูลผู้ติดต่อ'

    x_email = fields.Char('อีเมล')
    x_name = fields.Char('ชื่อผู้ติดต่อ')
    x_m21_demo = fields.Many2one('demo.x_demo_odoo','ชื่อบริษัท')
    x_tel = fields.Char('เบอร์ติดต่อ')


