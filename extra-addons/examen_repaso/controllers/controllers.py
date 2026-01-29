# -*- coding: utf-8 -*-
# from odoo import http


# class ExamenRepaso(http.Controller):
#     @http.route('/examen_repaso/examen_repaso', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examen_repaso/examen_repaso/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen_repaso.listing', {
#             'root': '/examen_repaso/examen_repaso',
#             'objects': http.request.env['examen_repaso.examen_repaso'].search([]),
#         })

#     @http.route('/examen_repaso/examen_repaso/objects/<model("examen_repaso.examen_repaso"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen_repaso.object', {
#             'object': obj
#         })

