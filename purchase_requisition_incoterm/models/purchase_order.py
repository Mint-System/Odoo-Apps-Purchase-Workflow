import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.depends("requisition_id")
    def _compute_incoterm_id(self):
        super()._compute_incoterm_id()
        for order in self:
            if order.requisition_id and order.requisition_id.incoterm_id:
                order.incoterm_id = order.requisition_id.incoterm_id
            elif not order.requisition_id:
                order.incoterm_id = False
