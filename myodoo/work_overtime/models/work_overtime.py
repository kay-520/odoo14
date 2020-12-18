# -*- coding: utf-8 -*-

from odoo import models, fields, api


class work_overtime(models.Model):
    _name = 'work.overtime'
    _description = '加班申请'
    _order = 'addTime desc'

    name = fields.Char(string='姓名', required=True)
    itCode = fields.Char(string='ITCODE', required=True)
    department = fields.Char(string='所属部门', required=True)
    addTime = fields.Date(string='申请加班时间', column_cast_from='yyyy-MM-dd', required=True)
    duration = fields.Integer(string='加班时长', help="时长（小时）", required=True)
    description = fields.Text(string='描述', required=True)
    depPrincipal = fields.Selection([('zhoujingb', '周璟')], string='部门负责人', default='zhoujingb', required=True)
