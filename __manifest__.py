# -*- coding: utf-8 -*-
{
    'name': "my_modulee",

    'summary': """
        My Modulee, a module that replics the Open Academy tutorial module from Odoo.""",

    'description': """
        In this module, we are capable to manage a course and sessions system.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/wizard.xml',
        'views/templates.xml',
        'views/courses.xml',
        'views/sessions.xml',
        'views/partners.xml',
        'reports/reports.xml',
        'reports/dashboard.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
