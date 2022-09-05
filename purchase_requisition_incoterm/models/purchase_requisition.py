from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"
    
    incoterm_id = fields.Many2one('account.incoterms')

    @api.onchange('vendor_id')
    def _onchange_incoterm_id(self):
        self.incoterm_id = self.vendor_id.purchase_incoterm_id