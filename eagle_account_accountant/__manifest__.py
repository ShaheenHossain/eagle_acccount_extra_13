# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

{
    'name': 'Eagle 13 Accounting',
    'version': '13.0.1.0.1',
    'category': 'Accounting',
    'summary': 'Accounting Reports, Asset Management and Account Budget For Eagle13 Community Edition',
    'sequence': '8',
    'author': 'Eagle ERP',
    'support': 'eagle-erp@gmail.com',
    'website': '',
    'depends': ['accounting_pdf_reports', 'eagle_account_asset', 'eagle_account_budget'],
    'demo': [],
    'data': [
        'views/account.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
    'qweb': [],
}
