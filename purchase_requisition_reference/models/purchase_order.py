import ast
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    partner_ref = fields.Char(
        string="Vendor Reference",
        compute="_compute_partner_ref",
        store=True,
        copy=False,
    )

    @api.depends("requisition_id")
    def _compute_partner_ref(self):
        copy_reference = ast.literal_eval(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("purchase_requisition_reference.copy_reference", "False")
        )
        for order in self:
            if not order.partner_ref and order.requisition_id and copy_reference:
                order.partner_ref = order.requisition_id.partner_ref
            else:
                order.partner_ref = order.partner_ref or ""
