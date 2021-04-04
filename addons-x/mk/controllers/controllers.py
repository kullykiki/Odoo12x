# -*- coding: utf-8 -*-
from odoo import http

# class Mk(http.Controller):
#     @http.route('/mk/mk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mk/mk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mk.listing', {
#             'root': '/mk/mk',
#             'objects': http.request.env['mk.mk'].search([]),
#         })

#     @http.route('/mk/mk/objects/<model("mk.mk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mk.object', {
#             'object': obj
#         })