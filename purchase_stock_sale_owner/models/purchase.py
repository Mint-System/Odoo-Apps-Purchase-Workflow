from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _prepare_picking(self):
        """Set shipping partner of first linked sale order as move owner if consigment is enabled."""
        res = super()._prepare_picking()
        consignment_enabled = self.user_has_groups('stock.group_tracking_owner')
        sale_order_ids = self._get_sale_orders()
        if consignment_enabled and len(sale_order_ids) == 1:
            res['owner_id'] = sale_order_ids.partner_shipping_id.id if sale_order_ids.partner_shipping_id else sale_order_ids.partner_id.id
        return res
        