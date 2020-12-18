import psycopg2

from odoo import models, api, fields, http


class Teachers(models.Model):
    _name = 'academy.teachers'
    _description = '教师详情'

    name = fields.Char(string='姓名')
    teach_school = fields.Char(related='academy_id.academy_name', string='学校ID')
    gender = fields.Selection([('man', '男'), ('woman', '女'), ('unknown', '不明')], string='性别')
    age = fields.Integer(string='年龄', default='0')
    academy_id = fields.Many2one('academy', string='学院ID', ondelete='cascade')
    education = fields.Char(string='学历')
    judge_status = fields.Boolean(string='是否在职', default=True)

    def academy_teachers_button_search(self):
        print('hello')



    def action_supplier_form_applicant(self):

        """
        查看详情
        :return: xml页面
        """
        context = dict(self._context)
        context['name'] = self.name
        context['teach_school'] = self.teach_school
        context['gender'] = self.gender
        context['age'] = self.age
        context['education'] = self.education
        context['academy_id'] = self.academy_id
        context['judge_status'] = self.judge_status
        view_id = self.env.ref('academy.academy_teachers_form_view').id

        return {
            'name': '教师详情',

            'type': 'ir.actions.act_window',

            'view_type': 'form',

            'view_mode': 'form',

            'res_model': 'academy.teachers',

            'res_id': self.id,

            'views': [(view_id, 'form')],

            'target': 'new',
            'context': context,
        }

    @api.model
    def create(self, vals_list):
        res = super(Teachers, self).create(vals_list)
        self.flush()
        self.clear_caches()
        return res

class ReloadTeachers(models.Model):
    _name = 'reload.teachers'
    _inherit = 'academy.teachers'

    # @api.one
    def creat_teacher(self):
        context = dict(self._context)
        context['name'] = self.name
        context['teach_school'] = self.teach_school
        context['gender'] = self.gender
        context['age'] = self.age
        # self.env.ref加载xml的id
        views_id = self.env.ref('academy.academy_teachers_tree_view').id
        view_id = self.env.ref('academy.reload_academy_teachers_form_view').id
        print(view_id)
        print(views_id)
        return {
            'view_id': view_id,
            'context': context
        }
        # return {
        #     'name': '教师详情',  # 可以写一些描述性的语言作为视图标题
        #     'type': 'ir.actions.act_window',   # 动作类型，默认为ir.actions.act_window
        #     'view_type': 'form',  # 跳转时打开的视图类型
        #     'view_mode': 'form',  # 列出跳转过去允许使用的视图模式
        #     'context': self.env.context,  # 给定的参数传递
        #     # 'limit': 80,  # 如果是tree，指定一页所能显示的行数
        #     'target': 'current',  # 有两个参数，current是在当前视图打开，new是弹出一个窗口打
        #     'auto_refresh': 0,  # 为1时在视图中添加一个刷新功能
        #     'auto_search': True,  # 加载默认视图后，自动搜索
        #     'multi': False, # 视图中有个更多按钮时，若multi设为True, 按钮显示在tree视图，否则显示在form视图
        #     'res_model': 'academy.teachers',  # 想打开视图的对应模块
        #     'res_id': 'academy.reload_academy_teachers_form_view',  # 加载指定id的视图，但只在view_type为form时生效，若没有这个参数则会新建一条记录
        #     'view_id': view_id,  # 指定视图的id，如果一个模块只有一个视图的时候可以忽略不计，但建议最好写入
        #     'views': [(view_id, 'form')],  # 是一个(view_id,view_type) 的元组对列表，默认打开第一组的动作视图
        #     'flags': {'initial_mode': 'edit'},
        #     'auto_refresh': 1,  # 为1时在视图中添加一个刷新功能
        #     # 对视图面板进行一些设置，如{'form': {'action_button': True, 'options': {'mode': 'edit'}}}即对form视图进行的一些设置，action_buttons为True时调出编辑保存按钮，options’: {‘mode’: ‘edit’}时则打开时对默认状态为编辑状态
        # }
