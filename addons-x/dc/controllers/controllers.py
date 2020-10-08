# -*- coding: utf-8 -*-
from odoo import http

# class Dc(http.Controller):
#     @http.route('/dc/dc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dc/dc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dc.listing', {
#             'root': '/dc/dc',
#             'objects': http.request.env['dc.dc'].search([]),
#         })

#     @http.route('/dc/dc/objects/<model("dc.dc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dc.object', {
#             'object': obj
#         })