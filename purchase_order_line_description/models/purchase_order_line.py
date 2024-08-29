import ast
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _compute_price_unit_and_date_planned_and_name(self):
        super()._compute_price_unit_and_date_planned_and_name()

        hide_ref = ast.literal_eval(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("purchase.order.line.hide_ref", "False")
        )

        for line in self:
            name = ""
            # Get supplier info
            supplier_info = line.product_id.seller_ids.filtered(
                lambda s: (s.partner_id == line.partner_id)
            )
            if supplier_info:
                supplier_info = supplier_info[0]

            # Set supplier product code as name
            if supplier_info.product_code and not hide_ref:
                name = "[" + supplier_info.product_code + "] "

            # Append purchase description to name
            if line.product_id.description_purchase:
                product = line.product_id.with_context(
                    lang=line.partner_id.lang
                )
                name += product.description_purchase

            # If no purchase description is given set name
            elif line.product_id:
                name += line.product_id.name

            # Append supplier product name
            if supplier_info.product_name:
                name += '\n' + supplier_info.product_name
            line.name = name
