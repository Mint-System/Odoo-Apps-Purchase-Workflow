import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    payment_term_id = fields.Many2one(
        "account.payment.term",
        string="Payment Terms",
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        compute="_compute_payment_term_id",
        store=True,
        readonly=False,
    )

    @api.depends("vendor_id")
    def _compute_payment_term_id(self):
        for requisition in self:
            if requisition.vendor_id:
                requisition.payment_term_id = (
                    requisition.vendor_id.property_supplier_payment_term_id
                )
            else:
                requisition.payment_term_id = False
