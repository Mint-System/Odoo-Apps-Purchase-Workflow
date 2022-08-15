from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"
    
    payment_term_id = fields.Many2one('account.payment.term', 'Payment Terms', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    @api.onchange('vendor_id')
    def _onchange_vendor_id(self):
        self.payment_term_id = self.vendor_id.property_supplier_payment_term_id