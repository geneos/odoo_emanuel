# -*- coding: utf-8 -*-
{
    "name": "odoo_emanuel",
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'sequence': 14,
    'author': 'GENEOS',
    'website': 'www.geneos.com.ar',
    'license': 'AGPL-3',
    'summary': '',
    "depends": [
        "base",
        "sale_management", 
    ],
    'external_dependencies': {
    },
    'data': [
        # 'security/ir.model.access.csv',
        'views/servicio_emanuel_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}