# -*- coding: utf-8 -*-
from odoo import http

# class TinyStock(http.Controller):
#     @http.route('/tiny_stock/tiny_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tiny_stock/tiny_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tiny_stock.listing', {
#             'root': '/tiny_stock/tiny_stock',
#             'objects': http.request.env['tiny_stock.tiny_stock'].search([]),
#         })

#     @http.route('/tiny_stock/tiny_stock/objects/<model("tiny_stock.tiny_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tiny_stock.object', {
#             'object': obj
#         })