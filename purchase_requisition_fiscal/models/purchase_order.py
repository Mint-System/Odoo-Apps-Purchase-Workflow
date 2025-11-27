import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    fiscal_position_id = fields.Many2one(
        "account.fiscal.position", compute="_compute_fiscal_position_id", store=True
    )

    @api.depends("requisition_id")
    def _compute_fiscal_position_id(self):
        for order in self:
            if order.requisition_id and order.requisition_id.fiscal_position_id:
                order.fiscal_position_id = order.requisition_id.fiscal_position_id
            else:
                order.fiscal_position_id = False
