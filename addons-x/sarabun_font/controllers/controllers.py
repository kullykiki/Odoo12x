# -*- coding: utf-8 -*-
from odoo import http

# class SarabunFont(http.Controller):
#     @http.route('/sarabun_font/sarabun_font/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sarabun_font/sarabun_font/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sarabun_font.listing', {
#             'root': '/sarabun_font/sarabun_font',
#             'objects': http.request.env['sarabun_font.sarabun_font'].search([]),
#         })

#     @http.route('/sarabun_font/sarabun_font/objects/<model("sarabun_font.sarabun_font"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sarabun_font.object', {
#             'object': obj
#         })