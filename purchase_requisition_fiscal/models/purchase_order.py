from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        """Always overwrite fiscal position from purchase contract."""
        res = super(PurchaseOrder, self)._onchange_requisition_id()
        if self.requisition_id and self.requisition_id.fiscal_position_id:
            self.fiscal_position_id = self.requisition_id.fiscal_position_id
        return res