# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Help ia',
    'version': '1.0',
    'author' : 'Luis Fernando Hinojosa Flores',
    'summary': 'Consults ia',
    'description': "module developed for consults from ia",
    'depends': ['base'],
    'category': 'customizations',
    'demo': [],
    'data': [
        #views
        'views/tree_help_ia.xml',
        'views/res.setting.xml',

        #security
        'security/mimodel_security.xml',
        'security/ir.model.access.csv',

        # reports
        'report/ia_report.xml',
        'report/script.xml'
        
        ],
    'external_dependencies': {'python': ['openai']},
    'installable': True,
    'application': True,
    'auto_install': False,
    'pre_init_hook': '',
    'images': ['static/descriptions/icon.png'],
    'post_init_hook': '',
    'assets': {},
    'license': 'OPL-1',
    'website': '',
    'routes': [
        {'type': 'http', 'handler': 'dev_help_ia.models.help_ia'},
    ],
    'maintainer': 'Luis Fernando Hinojosa Flores',
    'contributors': ['Luis Fernando Hinojosa Flores']
}
