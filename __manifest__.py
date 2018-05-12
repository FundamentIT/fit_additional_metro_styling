# -*- coding: utf-8 -*-
{
    'name': "fit_additional_metro_styling",

    'summary': """
        Additional CSS styling within Metro Theme""",

    'description': """
         Additional CSS styling within Metro Theme
    """,

    'author': "Fundament IT",
    'website': "https://fundament.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': '',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}