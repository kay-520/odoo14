# -*- coding: utf-8 -*-
from odoo import http

# 处理外部http请求
class Academy(http.Controller):
    # 生成可访问的接口,通过route方法把路由联系在一起，
    # http://localhost:8069/academy/academy/
    @http.route('/academy/academy/', auth='public', website=True)
    def academy_academy(self, **kw):
        Teachers = http.request.env['academy.teachers']
        # 用于渲染页面， academy是我们的模块名，index是我们的文件名id，后面的字典用于传值,返回给页面
        return http.request.render('academy.index', {'teachers': Teachers.search([])})
        # return "Hello, world"

    # @http.route('/academy/academy/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('academy.listing', {
    #         'root': '/academy/academy',
    #         'objects': http.request.env['academy.academy'].search([]),
    #     })

    @http.route('/academy/hello', auth='public')
    def list(self, **kw):
        return "helle"


