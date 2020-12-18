# -*- coding: utf-8 -*-
# from odoo import http


# class WorkOvertime(http.Controller):
#     @http.route('/work_overtime/work_overtime/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/work_overtime/work_overtime/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('work_overtime.listing', {
#             'root': '/work_overtime/work_overtime',
#             'objects': http.request.env['work_overtime.work_overtime'].search([]),
#         })

#     @http.route('/work_overtime/work_overtime/objects/<model("work_overtime.work_overtime"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('work_overtime.object', {
#             'object': obj
#         })
