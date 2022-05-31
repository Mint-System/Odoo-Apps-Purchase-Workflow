import logging
_logger = logging.getLogger(__name__)
from odoo import models, api
import ast


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id')
    def onchange_product_id(self):
        hide_ref = ast.literal_eval(self.env["ir.config_parameter"].sudo().get_param("purchase.order.line.hide_ref", "False"))
        
        super().onchange_product_id()

        # Get supplier info
        supplier_info = self.product_id.seller_ids.filtered(
            lambda s: (s.name == self.partner_id)
        )
        if supplier_info:
            supplier_info = supplier_info[0]

        _logger.warning([self.product_id.seller_ids,supplier_info])

        # Set supplier product code as name
        if supplier_info.product_code and not hide_ref:
            self.name = "[" + supplier_info.product_code + "] "
        else:
            self.name = ""
        
        # Append purchase description to name
        if self.product_id.description_purchase:
            product = self.product_id.with_context(
                lang=self.partner_id.lang
            )
            self.name += product.description_purchase

        # If no purchase description is given set name
        elif self.product_id:
            self.name += self.product_id.name

        # Append supplier product name
        if supplier_info.product_name:
            self.name += '\n' + supplier_info.product_name