# -*- coding: utf-8 -*-
# from odoo import http


# class Academia(http.Controller):
#     @http.route('/academia/academia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academia/academia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academia.listing', {
#             'root': '/academia/academia',
#             'objects': http.request.env['academia.academia'].search([]),
#         })

#     @http.route('/academia/academia/objects/<model("academia.academia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academia.object', {
#             'object': obj
#         })
