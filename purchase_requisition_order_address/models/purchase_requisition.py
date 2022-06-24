from odoo import _, api, fields, models
from odoo.addons.purchase.models.purchase import PurchaseOrder as Purchase
import logging
_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"
    
    partner_order_id = fields.Many2one(
        'res.partner', string='Order Address', required=True,
        states=Purchase.READONLY_STATES,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)

    @api.onchange('vendor_id')
    def _onchange_vendor_id(self):
        addr = self.vendor_id.address_get(['order'])
        values = {
            'partner_order_id': addr['order'],
        }
        self.update(values)