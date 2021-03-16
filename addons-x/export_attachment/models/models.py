# -*- coding: utf-8 -*-

from odoo import models, fields, api

class export_attachment(models.Model):
    _name = 'export_attachment.export_attachment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

    @api.multi
    def action_export_attachment(self,rec,model_name,field_name,field_attach):
        """
        รับพารามิเตอร์ เป็น 
        record ที่ต้องการจะ zip file (rec),
        ชื่อโมเดลที่ต้องการจะทำ (model_name),
        ชื่อฟิวที่เป็น x_name (field_name),
        ชื่อฟิวที่เก็บไฟล์ที่ต้องการจะ zip (field_attach)
        
        """
        tab_id = []
        rec_id = []
        rec_ids =  self.env[model_name].sudo().search([('id','in',rec)])
        for attachment in rec_ids:
            for file in attachment[field_attach]:
                tab_id.append(file.id)
                rec_id.append(attachment.id)
        url = '/web/binary/download_documents?tab_id={}&rec_id={}&field_name={}&field_attach={}&model_name={}' .format(tab_id,rec_id,field_name,field_attach,model_name)
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }

