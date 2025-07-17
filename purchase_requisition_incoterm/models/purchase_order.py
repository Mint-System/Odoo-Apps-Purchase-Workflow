import logging

from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    incoterm_id = fields.Many2one(
        "account.incoterms", 
        "Incoterm", 
        compute="_compute_incoterm_id",
        help="International Commercial Terms are a series of predefined commercial terms used in international transactions."
        )

    @api.depends("requisition_id")
    def _compute_incoterm_id(self):
        for order in self:
            if order.requisition_id and order.requisition_id.incoterm_id:
                order.incoterm_id = order.requisition_id.incoterm_id
            elif not order.requisition_id:
                order.incoterm_id = False
            return
