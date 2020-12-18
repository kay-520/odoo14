# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Academy(models.Model):
    _name = 'academy'
    _description = 'academy.academy'

    academy_name = fields.Char(string='学院名称', require=True)
    teacher_count = fields.Integer(compute="_value_pc", string='教师总数', default=0, store=True)
    email_code = fields.Integer(string='邮政编码')
    teacher_ids = fields.One2many('academy.teachers', 'academy_id', string='教师ID')
    description = fields.Text(string='简介')

    @api.depends('teacher_ids')
    def _value_pc(self):
        for record in self:
            record.teacher_count = len(record.teacher_ids)

