# -*- coding: utf-8 -*-
from odoo import http

# class OnlineMediaForm(http.Controller):
#     @http.route('/online_media_form/online_media_form/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/online_media_form/online_media_form/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('online_media_form.listing', {
#             'root': '/online_media_form/online_media_form',
#             'objects': http.request.env['online_media_form.online_media_form'].search([]),
#         })

#     @http.route('/online_media_form/online_media_form/objects/<model("online_media_form.online_media_form"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('online_media_form.object', {
#             'object': obj
#         })

# import logging
# try:
#     from BytesIO import BytesIO
# except ImportError:
#     from io import BytesIO
# import zipfile
# from datetime import datetime
# from openerp import http
# from openerp.http import request
# from openerp.addons.web.controllers.main import content_disposition
# import ast

# _logger = logging.getLogger(__name__)


# class Binary(http.Controller):
#     @http.route('/web/binary/download_document', type='http', auth="public")
#     def download_document(self, tab_id, rec_id ,**kw):
#         new_tab = ast.literal_eval(tab_id)
#         new_rec = ast.literal_eval(rec_id)
#         attachment_ids = request.env['ir.attachment'].sudo().search([('id', 'in', new_tab)])
#         rec_ids = request.env['jas_storage.main'].sudo().search([('id', 'in', new_rec)])
#         file_dict = {}
#         for attachment_id in attachment_ids:
#             for rec in rec_ids:
#                 if attachment_id in rec['attach']:
#                     file_store = attachment_id.store_fname
#                     if file_store:
#                         file_name = '{}/{}'.format(rec.id,attachment_id.name)
#                         file_path = attachment_id._full_path(file_store)
#                         file_dict["%s:%s" % (file_name,file_path)] = dict( name=file_name , path=file_path)
#         zip_filename = datetime.now()
#         zip_filename = "%s.zip" % zip_filename
#         bitIO = BytesIO()
#         zip_file = zipfile.ZipFile(bitIO, "w", zipfile.ZIP_DEFLATED)
#         for file_info in file_dict.values():
#             zip_file.write(file_info["path"], file_info["name"])
#         zip_file.close()
#         return request.make_response(bitIO.getvalue(),
#                                      headers=[('Content-Type', 'application/x-zip-compressed'),
#                                               ('Content-Disposition', content_disposition(zip_filename))])
