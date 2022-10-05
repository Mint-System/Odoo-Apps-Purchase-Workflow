from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)
from odoo.addons.purchase.models.purchase import PurchaseOrder as Purchase


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address',
        states=Purchase.READONLY_STATES, tracking=True, 
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
