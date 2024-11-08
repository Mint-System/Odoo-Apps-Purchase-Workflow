import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    partner_shipping_id = fields.Many2one(
        'res.partner',
        string='Delivery Address',
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        compute='_compute_partner_shipping_id',
        store=True,
        readonly=True
    )

    @api.depends('partner_id')
    def _compute_partner_shipping_id(self):
        for order in self:
            if order.partner_id:
                address = order.partner_id.address_get(['delivery'])
                order.partner_shipping_id = address.get('delivery', order.partner_id.id)
            else:
                order.partner_shipping_id = False
