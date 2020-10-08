# -*- coding: utf-8 -*-


import json
from odoo import http
from odoo.http import Response, request
from datetime import datetime
import requests
from requests import Request,Session


class Demo(http.Controller):
#     @http.route('/demo/demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo/demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo.listing', {
#             'root': '/demo/demo',
#             'objects': http.request.env['demo.demo'].search([]),
#         })

#     @http.route('/demo/demo/objects/<model("demo.demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo.object', {
#             'object': obj
#         })

    @http.route('/get_data_employee/', auth='public',type='http',website=True,csrf=False)
    def get_employee(self, **kw):
        headers = {'Content-Type': 'application/json'}
        body = http.request.env['hr.employee'].search([['active','=',True]]).read(['name','work_email','active','work_location','gender'])
        return Response(json.dumps(body), headers=headers)

    @http.route('/get_demo/', auth='public',type='http',website=True,csrf=False)
    def get_demo(self, **kw):
        headers = {'Content-Type': 'application/json'}
        body = http.request.env['demo.x_demo_odoo'].search([]).read(['x_title','x_company','x_branch','x_contact','x_products','x_remark'])
        dict = {}
        index_i = 0
        for i in body:
            new_dict = {}
            new_dict = i
            index_j = 0
            contact = {}
            index_p = 0
            products = {}
            for j in i['x_contact'] :
                data = http.request.env['demo.x_demo_contact'].search([['id','=',j]]).read([
                    'id','x_name','x_email','x_tel','x_m21_demo'   
                ])
                contact[index_j] = data
                index_j = index_j + 1
            for p in i['x_products'] :
                data = http.request.env['demo.x_master_products'].search([['id','=',p]]).read([
                    'id','x_name'   
                ])
                products[index_p] = data
                index_p = index_p + 1
            new_dict['x_contact'] = contact
            new_dict['x_products'] = products
            dict[index_i] = new_dict
            index_i = index_i + 1

        # return dict
        
        return Response(json.dumps(dict), headers=headers)
