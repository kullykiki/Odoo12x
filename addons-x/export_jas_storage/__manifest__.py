# -*- coding: utf-8 -*-
{
    'name': "export_jas_storage",

    'summary': """
        สำหรับ ดาวน์โหลด ไฟล์รูปภาพที่อัพโหลดเข้าฟิวส์ attach เป็น ไฟล์ .zip """,

    'description': """
        สำหรับ ดาวน์โหลด ไฟล์รูปภาพที่อัพโหลดเข้าฟิวส์ attach ของโมดูล Jas Storage เป็น ไฟล์ .zip 
    """,

    'author': "3BB",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','jas_storage'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}