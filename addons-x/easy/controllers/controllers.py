# -*- coding: utf-8 -*-
from odoo import http

# class Easy(http.Controller):
#     @http.route('/easy/easy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/easy/easy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('easy.listing', {
#             'root': '/easy/easy',
#             'objects': http.request.env['easy.easy'].search([]),
#         })

#     @http.route('/easy/easy/objects/<model("easy.easy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('easy.object', {
#             'object': obj
#         })