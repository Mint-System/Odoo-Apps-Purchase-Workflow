import logging

from odoo import models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _compute_partner_order_id(self):
        super()._compute_partner_order_id()
        for order in self:
            if order.requisition_id and order.requisition_id.partner_order_id:
                order.partner_order_id = order.requisition_id.partner_order_id
        return
