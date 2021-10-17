# -*- coding: utf-8 -*-
# from odoo import http


# class MyModulee(http.Controller):
#     @http.route('/my_modulee/my_modulee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_modulee/my_modulee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_modulee.listing', {
#             'root': '/my_modulee/my_modulee',
#             'objects': http.request.env['my_modulee.my_modulee'].search([]),
#         })

#     @http.route('/my_modulee/my_modulee/objects/<model("my_modulee.my_modulee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_modulee.object', {
#             'object': obj
#         })
