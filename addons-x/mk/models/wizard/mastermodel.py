# -*- coding: utf-8 -*-
from odoo import models, fields, api

class mkWizardMKApprove(models.Model):
    _name = 'mk.x_wizard_mk_approve'
    _description = '[W/MK] อนุมัติ'

    """
        [W/MK] อนุมัติ
    """

    ### -----------------------------------------       Field      ------------------------------------------------------
    x_name = fields.Char(string='ชื่อผู้ดำเนินการ + เลขที่คำขอ')

    x_approve_name = fields.Many2one(comodel_name='hr.employee', string='ชื่อผู้ดำเนินการ')
    x_m21_media_request = fields.Many2one(comodel_name='mk.x_mk_work_request', string='เลขที่คำขอ')
    x_reason = fields.Text(string='เหตุผลที่ไม่อนุมัติ')
    x_result = fields.Many2one(comodel_name='mk.​x_master_mk_result_approve', string='ผลการอนุมัติ')
    x_suggestion = fields.Text(string='ความคิดเห็น')

    ## ------------------------------------       Compute Function      ------------------------------------------------------
#####---------------------------------------------------------🌟END🌟================================================================#####

class mkWizardMKArtworkApprove(models.Model):
    _name = 'mk.x_wizard_mk_artwork_approve'
    _description = '[MK][W] Cancel'

    """
        [MK][W] Cancel
    """

    ### -----------------------------------------       Field      ------------------------------------------------------
    x_name = fields.Char(string='Name')
    x_reason = fields.Text(string='เหตุผลที่ยกเลิก')

    ## ------------------------------------       Compute Function      ------------------------------------------------------
#####---------------------------------------------------------🌟END🌟================================================================#####
