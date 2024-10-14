# -*- coding: utf-8 -*-
# from odoo import http


# class BaseAddon(http.Controller):
#     @http.route('/base_addon/base_addon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_addon/base_addon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_addon.listing', {
#             'root': '/base_addon/base_addon',
#             'objects': http.request.env['base_addon.base_addon'].search([]),
#         })

#     @http.route('/base_addon/base_addon/objects/<model("base_addon.base_addon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_addon.object', {
#             'object': obj
#         })

