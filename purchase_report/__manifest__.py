# -*- coding: utf-8 -*-
{
    'name': "purchase_report",
    'summary': """This module will create pdf report of remain quantity to
                deliver""",
    'description': """This module will create pdf report of remain quantity to
                     deliver""",
    'author': "Aktiv software",
    'website': "http://www.aktivsoftware.com",
    'category': 'Uncategorized',
    'version': '13.0.1.0.0',
    'depends': ['purchase','stock'],
    'data': [
        # 'security/ir.model.access.csv'
        'wizard/purchase.xml',
        'reports/report.xml',
        'reports/remain_quantity_report.xml',
    ],
}
