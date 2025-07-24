import logging

from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange("requisition_id")
    def _onchange_requisition_id(self):
        super().onchange_partner_id()
        if self.requisition_id and self.requisition_id.incoterm_id:
            self.incoterm_id = self.requisition_id.incoterm_id



