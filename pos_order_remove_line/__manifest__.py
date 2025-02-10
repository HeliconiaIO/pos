# Copyright 2023 LevelPrime
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "POS Order Remove Line",
    "summary": "Add button to remove POS order line.",
    "author": "Roberto Fichera, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/pos",
    "category": "Point of Sale",
    "maintainers": ["robyf70"],
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_order_remove_line/static/src/js/*.js",
            "pos_order_remove_line/static/src/css/*.scss",
            "pos_order_remove_line/static/src/xml/*xml",
        ]
    },
}
