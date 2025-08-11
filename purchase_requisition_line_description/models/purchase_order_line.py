import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def _compute_price_unit_and_date_planned_and_name(self):
        res = super()._compute_price_unit_and_date_planned_and_name()
        for pol in self:
            for line in pol.order_id.requisition_id.line_ids:
                if line.product_id == pol.product_id:
                    if line.product_description_variants:
                        pol.name = line.product_description_variants

        return res
