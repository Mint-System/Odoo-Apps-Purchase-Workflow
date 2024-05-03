from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """If requisition_id is not set get defaults from partner."""
        res = super().onchange_partner_id()
        if self.requisition_id and self.requisition_id.partner_order_id:
            self.partner_order_id = self.requisition_id.partner_order_id
        return res

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        """Always overwrite order partner from purchase contract."""
        res = super()._onchange_requisition_id()
        if self.requisition_id and self.requisition_id.partner_order_id:
            self.partner_order_id = self.requisition_id.partner_order_id
        return res