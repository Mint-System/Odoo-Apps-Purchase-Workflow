import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    payment_term_id = fields.Many2one(
        "account.payment.term",
        string="Payment Terms",
        compute="_compute_payment_term_id",
        store=True,
        readonly=False,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )

    @api.depends("requisition_id", "partner_id", "company_id")
    def _compute_payment_term_id(self):
        for order in self:
            if order.requisition_id and order.requisition_id.payment_term_id:
                order.payment_term_id = order.requisition_id.payment_term_id
            elif (
                order.partner_id and order.partner_id.property_supplier_payment_term_id
            ):
                order.payment_term_id = (
                    order.partner_id.property_supplier_payment_term_id
                )
            else:
                order.payment_term_id = False
