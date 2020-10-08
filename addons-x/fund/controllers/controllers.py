# -*- coding: utf-8 -*-
from odoo import http
import json
from odoo import http
from odoo.http import Response, request
# from datetime import datetime
import datetime
import requests
from requests import Request,Session

class Fund(http.Controller):
    @http.route('/fund/export/', auth='public')
    def export_all(self, **kw):
        body = http.request.env['x_fund_injured'].search([ ])

        return http.request.render('fund.export_xml', {
            'object': body
        })

#     @http.route('/fund/fund/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fund.listing', {
#             'root': '/fund/fund',
#             'objects': http.request.env['fund.fund'].search([]),
#         })

#     @http.route('/fund/fund/objects/<model("fund.fund"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fund.object', {
#             'object': obj
#         })