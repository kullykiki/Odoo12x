# -*- coding: utf-8 -*-
{
    'name': "Document Control",

    'summary': """
        ระบบจัดเก็บเอกสารสำหรับหน่วยงาน QC/QA""",

    'description': """
        Long description of module's purpose
    """,

    'author': "🤖 Odoo Ranger ✨",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','mail','smile_base_automation'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/group.xml',
        'data/m_status.xml',
        'views/automation.xml',
        'views/assets.xml',
        'views/schedule.xml',
        'views/serveraction_dar.xml',
        'views/serveraction_masterlist.xml',
        'views/serveraction_wizard.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/master/view.xml',
        'views/master/windowaction.xml',
        'views/master/menu.xml',
        'views/view_dar.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}