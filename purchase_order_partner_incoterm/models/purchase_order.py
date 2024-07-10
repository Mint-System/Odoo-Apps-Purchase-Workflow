import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    incoterm_id = fields.Many2one(
        "account.incoterms", compute="_compute_incoterm_id", store=True, readonly=False,
    )

    @api.depends("partner_id", "company_id")
    def _compute_incoterm_id(self):
        for order in self:
            if not order.incoterm_id and order.partner_id.purchase_incoterm_id:
                order.incoterm_id = order.partner_id.purchase_incoterm_id
            elif not order.partner_id.purchase_incoterm_id:
                order.incoterm_id = False
