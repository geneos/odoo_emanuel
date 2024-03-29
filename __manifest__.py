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
        "sale", 
        "sale_management",
    ],
    'external_dependencies': {
    },
    'data': [
        'security/ir.model.access.csv',
        'wizards/reporte_servicio_cobro.xml',
        'views/servicio_emanuel_views.xml',
        'views/servicio_adquirido_views.xml',
        'views/account_payment_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
        'views/tasa_venta.xml',
        'views/tasa_resarcitorio.xml',
        'views/periodo.xml',
        'report/asociado.xml',
        'wizards/reporte_asociado.xml',
        'wizards/cuota_costo_unico.xml',
        'report/servicio_cobros.xml',
        'report/recibo.xml',
        'data/odoo_emanuel.periodo.csv'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}