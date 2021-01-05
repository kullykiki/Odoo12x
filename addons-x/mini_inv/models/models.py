# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LGInventory(models.Model):
    _name = 'mini_inv.x_lg_inventory'

    name = fields.Char()