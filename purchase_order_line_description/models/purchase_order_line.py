import logging
_logger = logging.getLogger(__name__)
from odoo import models, api
import ast


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id')
    def onchange_product_id(self):
        hide_ref = ast.literal_eval(self.env["ir.config_parameter"].sudo().get_param("purchase.order.line.hide_ref", "True"))
        super().onchange_product_id()
        # Use purchase description if it exists and translate with partner lang
        if self.product_id.description_purchase:
            product = self.product_id.with_context(
                lang=self.partner_id.lang
            )
            self.name = product.description_purchase
        elif self.product_id and hide_ref:
            self.name = self.product_id.name