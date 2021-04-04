# -*- coding: utf-8 -*-
from odoo import http

# class Mc(http.Controller):
#     @http.route('/mc/mc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mc/mc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mc.listing', {
#             'root': '/mc/mc',
#             'objects': http.request.env['mc.mc'].search([]),
#         })

#     @http.route('/mc/mc/objects/<model("mc.mc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mc.object', {
#             'object': obj
#         })