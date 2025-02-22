# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class PosSession(models.Model):
    _inherit = "pos.session"

    def _loader_params_product_pricelist(self):
        result = super()._loader_params_product_pricelist()
        result["search_params"]["fields"].extend(["is_technical"])
        return result
