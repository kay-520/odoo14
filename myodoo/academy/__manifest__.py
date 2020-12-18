# -*- coding: utf-8 -*-
{
    # 模块的可读名称，安装的模块名
    'name': "学院教师",
    'version': '13.0.1.0.0',
    # 关键词
    'summary': """
        """,
    'sequence': 1,
    #  模块说明
    'description': """
        Long description of module's purpose
    """,
    # 模块作者的姓名
    'author': "OSCG",
    # 网站
    'website': "http://www.oscg.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # 类别
    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    # 必须先加载的模块，本模块所依赖的模块
    'depends': ['base', 'web', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/academy_action.xml',
        'views/academy_views.xml',
        'views/templates.xml',
        'views/reload_view.xml',
        'views/academy_teachers_action.xml',

        'views/academy_teachers_views.xml',

        'views/import_src.xml',

        'views/academy_menu.xml',
        'views/academy_teachers_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'css': ['static/src/css/calaulate.css'],
    # 主要模板引擎
    'qweb': [
        'static/src/xml/assete_equip_sync_bt_view.xml',
        # 'static/src/xml/tree_view_button.xml',

        # 'static/src/xml/base.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,   # 指定模块是否在应用列表中以app的形式显示
    'license': 'LGPL-3',
}
