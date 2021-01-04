# -*- coding: utf-8 -*-

from odoo import api, fields, models

## ------------------------------------    🎁 Stock Master 📦  --------------------------------------------------------
class MasterLGStatus(models.Model):
    _name = 'mini_inv.x_master_lg_status'
    _description = '[M] สถานะของใบรับฝากของ'

    """
    Master Model Status
        โมเดลย่อยสำหรับ เก็บสถานะ ของ ใบฝาก/ใบเบิกของ
    """

    x_name = fields.Char(string='สถานะ')
    x_activity = fields.Selection(string='ฝาก / เบิก', selection=[('d','ฝาก'),('r','เบิก')])
    