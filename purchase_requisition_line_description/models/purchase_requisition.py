import ast
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseRequisitionLine(models.Model):
    _inherit = "purchase.requisition.line"

    product_description_variants = fields.Text(
        string="Custom Description",
        compute="_compute_product_description_variants",
        store=True,
    )

    @api.depends("product_id", "requisition_id.vendor_id")
    def _compute_product_description_variants(self):
        for line in self:
            name = ""
            hide_ref = ast.literal_eval(
                line.env["ir.config_parameter"]
                .sudo()
                .get_param("purchase.requisition.line.hide_ref", "False")
            )

            # Get supplier info
            supplier_info = line.product_id.seller_ids.filtered(
                lambda s: s.partner_id == line.requisition_id.vendor_id
            )
            if supplier_info:
                supplier_info = supplier_info[0]

            # Set supplier product code as name
            if supplier_info.product_code and not hide_ref:
                name = (
                    "[" + supplier_info.product_code + "] "
                )

            # Append purchase description to name
            if line.product_id.description_purchase:
                product = line.product_id.with_context(
                    lang=line.requisition_id.vendor_id.lang
                )
                name += product.description_purchase

            # If no purchase description is given, set name
            elif line.product_id:
                name += line.product_id.name

            # Append supplier product name
            if supplier_info.product_name:
                name += "\n" + supplier_info.product_name
            line.product_description_variants = name

    def _prepare_purchase_order_line(self, name, product_qty=0.0, price_unit=0.0, taxes_ids=False):
        res = super(PurchaseRequisitionLine, self)._prepare_purchase_order_line(name, product_qty, price_unit, taxes_ids)
        res['name'] = self.product_description_variants
        return res
