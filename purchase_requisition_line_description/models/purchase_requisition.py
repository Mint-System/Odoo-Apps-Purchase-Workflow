from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)
import ast


class PurchaseRequisitionLine(models.Model):
    _inherit = 'purchase.requisition.line'
    
    product_description_variants = fields.Text('Custom Description')

    @api.onchange('product_id')
    def onchange_product_id(self):
        hide_ref = ast.literal_eval(self.env["ir.config_parameter"].sudo().get_param("purchase.requisition.line.hide_ref", "False"))
        
        # Get supplier info
        supplier_info = self.product_id.seller_ids.filtered(
            lambda s: (s.name == self.requisition_id.vendor_id)
        )
        if supplier_info:
            supplier_info = supplier_info[0]

        # Set supplier product code as name
        if supplier_info.product_code and not hide_ref:
            self.product_description_variants = "[" + supplier_info.product_code + "] "
        else:
            self.product_description_variants = ""
        
        # Append purchase description to name
        if self.product_id.description_purchase:
            product = self.product_id.with_context(
                lang=self.requisition_id.vendor_id.lang
            )
            self.product_description_variants += product.description_purchase

        # If no purchase description is given set name
        elif self.product_id:
            self.product_description_variants += self.product_id.name

        # Append supplier product name
        if supplier_info.product_name:
            self.product_description_variants += '\n' + supplier_info.product_name

    def _prepare_purchase_order_line(self, name, product_qty=0.0, price_unit=0.0, taxes_ids=False):
        res = super(PurchaseRequisitionLine, self)._prepare_purchase_order_line(name, product_qty, price_unit, taxes_ids)
        res['name'] = self.product_description_variants
        return res