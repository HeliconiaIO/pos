{
    "name": "Point of Sale Re-order",
    "version": "17.0.1.0.0",
    "category": "Sales/Point of Sale",
    "summary": "Simple Re-order in the Point of Sale ",
    "depends": ["point_of_sale"],
    "website": "https://github.com/OCA/pos",
    "author": "Cetmix,Odoo Community Association (OCA)",
    "images": ["static/description/banner.png"],
    "data": [
        "views/res_config_settings_view.xml",
    ],
    "installable": True,
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_order_reorder/static/src/js/**/*.js",
            "pos_order_reorder/static/src/xml/**/*.xml",
        ],
    },
    "license": "LGPL-3",
}
