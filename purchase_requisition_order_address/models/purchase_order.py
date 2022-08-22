from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        """Always overrite order partner from purchase contract."""
        res = super(PurchaseOrder, self)._onchange_requisition_id()
        if self.requisition_id and self.requisition_id.partner_order_id:
            self.partner_order_id = self.requisition_id.partner_order_id
        return res