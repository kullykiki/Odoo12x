# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class export_jas_storage(models.Model):
#     _name = 'export_jas_storage.export_jas_storage'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class main(models.Model):
    _inherit = 'jas_storage.main'

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