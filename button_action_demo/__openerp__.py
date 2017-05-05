# -*- coding: utf-8 -*-
{
    'name': "button_action_demo",

    'summary': """
        Calcul de mesures""",

    'description': """
       Calcul de mesures
    """,

    'author': "Albert Morote and Oriol Perez",
    'website': "https://github.com/orpenu1516daw2/grup2.git",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'button_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
}
