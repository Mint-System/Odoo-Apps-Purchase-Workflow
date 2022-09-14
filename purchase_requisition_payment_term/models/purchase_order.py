from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        """Always override payment term from purchase contract."""
        res = super()._onchange_requisition_id()
        if self.requisition_id.payment_term_id:
            self.payment_term_id = self.requisition_id.payment_term_id
        return res

    @api.onchange('partner_id', 'company_id')
    def onchange_partner_id(self):
        """Always override payment term from purchase contract."""
        res = super().onchange_partner_id()
        if self.requisition_id.payment_term_id:
            self.payment_term_id = self.requisition_id.payment_term_id
        return res