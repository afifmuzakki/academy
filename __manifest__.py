# -*- coding: utf-8 -*-
{
    'name': "Academy",

    'summary': """
        Daya Motor Website Custom Module Odoo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Muhammad Afif Muzakki",
    'website': "http://www.daya-motor.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        "views/header.xml",
        'views/footer.xml',
        'views/aftersales.xml',
        'views/home.xml',
        'views/product.xml',
        'views/promo.xml',
        'views/apparel.xml',
        'views/booking_service.xml',
        'views/live_chat.xml',
        'views/nearest_dealer.xml',
        'views/pricelist.xml',
        'views/product_detail.xml',
        'views/estimated_price.xml',
        'views/spare_parts.xml',
        'views/news.xml',
        'views/unit_order.xml',
        'views/service_order.xml',
        'views/apparel_order.xml',
        'views/apparel_detail.xml',
    ],

    # loaded css file
    'css': [
        "static/src/css/style.css"
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
