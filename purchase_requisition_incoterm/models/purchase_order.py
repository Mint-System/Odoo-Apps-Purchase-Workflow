from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        """Always override incoterm from purchase contract."""
        res = super()._onchange_requisition_id()
        # _logger.warning(['purchase_requisition_incoterm', self.incoterm_id, self.requisition_id.incoterm_id])
        if not self.incoterm_id and self.requisition_id.incoterm_id:
            self.incoterm_id = self.requisition_id.incoterm_id
        return res