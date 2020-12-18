{
    'name': "加班申请",
    'summary': '',
    'description': """
        加班申请
    """,
    'author': "Karma",
    'website': "http://Karma520.com",
    'sequence': 0,
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/action.xml',
        'views/views.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,   # 指定模块是否在应用列表中以app的形式显示
    'license': 'LGPL-3',
}
