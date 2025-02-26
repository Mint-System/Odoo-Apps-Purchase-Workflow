import logging
from odoo import api, models
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends('order_line.sale_order_id')
    def _compute_sale_order_count(self):
        """Map the analytic account id from linked sale order."""
        res = super()._compute_sale_order_count()
        for purchase in self:
            sale_order_ids = purchase._get_sale_orders()
            analytic_account_id = sale_order_ids.mapped('analytic_account_id')[:1]
            if analytic_account_id:
                #for line in purchase.order_line:
                #    line.analytic_distribution = {analytic_account_id.id: 100.0}
                purchase.order_line.analytic_distribution = {analytic_account_id.id: 100.0}
        
        return res
