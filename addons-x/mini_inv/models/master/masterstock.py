# -*- coding: utf-8 -*-

from odoo import api, fields, models

## ------------------------------------    🎁 Stock Master 📦  --------------------------------------------------------
class MasterLGStock(models.Model):
    _name = 'mini_inv.x_master_lg_stock'
    _description = '[M] คลังฝากของ'

    """
    Master Model Product
        โมเดลย่อยสำหรับ เก็บรายละเอียดของรายการของที่จะฝาก ทุกประเภท ยกเว้น 'ทรัพย์สินชำรุดรอการจำหน่าย'
    """

    x_name = fields.Char(string='คลังที่นำฝาก',related='x_code.x_cluster_name')
    x_code = fields.Many2one(comodel_name='mini_inv.x_master_lg_code', string='รหัสคลัง')
    x_cluster = fields.Many2one(comodel_name='mini_inv.x_master_lg_cluster', string='Cluster คลังสินค้า')
    x_ro = fields.Many2one(comodel_name='mini_inv.x_master_lg_ro', string='RO สังกัดคลัง',related='x_cluster.x_ro')
    
    


## ------------------------------------    🎁 Stock Sub Master 📦  --------------------------------------------------------

## ------🌻 [M] RO คลัง
class MasterLGRO(models.Model):
    _name = 'mini_inv.x_master_lg_ro'
    _description = '[M] RO คลัง'

    """
    Sub Master Model RO
        โมเดลย่อยสำหรับ เก็บ RO คลัง เพื่อ m2o กับ โมเดล [M] Cluster คลัง
    """

    x_name = fields.Char(string='RO สังกัดคลัง')


## ------🌻 [M] Cluster คลัง
class MasterLGCluster(models.Model):
    _name = 'mini_inv.x_master_lg_cluster'
    _description = '[M] Cluster คลัง'

    """
    Sub Master Model Cluster
        โมเดลย่อยสำหรับ เก็บ Cluster คลัง เพื่อ m2o กับ โมเดล [M] คลังฝากของ
    """

    x_name = fields.Char(string='Cluster คลังสินค้า')
    x_ro    = fields.Many2one(comodel_name='mini_inv.x_master_lg_ro',string='RO')


## ------🌻 [M] รหัสคลัง
class MasterLGCode(models.Model):
    _name = 'mini_inv.x_master_lg_code'
    _description = '[M] รหัสคลัง'

    """
    Sub Master Model Code
        โมเดลย่อยสำหรับ เก็บ รหัสคลัง เพื่อ m2o กับ โมเดล [M] คลังฝากของ
    """

    x_name = fields.Char(string='รหัสคลัง')
    x_cluster_name = fields.Char(string='ชื่อคลัง')

    

