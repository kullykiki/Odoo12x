# -*- coding: utf-8 -*-
from odoo import http

# class MiniInv(http.Controller):
#     @http.route('/mini_inv/mini_inv/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mini_inv/mini_inv/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mini_inv.listing', {
#             'root': '/mini_inv/mini_inv',
#             'objects': http.request.env['mini_inv.mini_inv'].search([]),
#         })

#     @http.route('/mini_inv/mini_inv/objects/<model("mini_inv.mini_inv"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mini_inv.object', {
#             'object': obj
#         })