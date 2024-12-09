import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    price_unit = fields.Float(compute='_compute_price_unit', store=True)

    @api.depends('product_qty', 'product_uom', 'product_id', 'order_id.date_order', 'partner_id')
    def _compute_price_unit(self):
        for line in self:
            if not line.product_id:
                line.price_unit = 0.0
                continue

            params = {'order_id': line.order_id}
            seller = line.product_id._select_seller(
                partner_id=line.partner_id,
                quantity=line.product_qty,
                date=line.order_id.date_order and line.order_id.date_order.date(),
                uom_id=line.product_uom,
                params=params
            )

            if not seller:
                line.price_unit = 0.0
            else:
                line.price_unit = seller.price
