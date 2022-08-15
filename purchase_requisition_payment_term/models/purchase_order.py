from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        res = super(PurchaseOrder, self)._onchange_requisition_id()
        if not self.payment_term_id and self.requisition_id:
            self.payment_term_id = self.requisition_id.payment_term_id
        return res