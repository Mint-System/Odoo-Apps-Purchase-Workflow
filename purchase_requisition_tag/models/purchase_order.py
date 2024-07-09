import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    tag_ids = fields.Many2many(
        comodel_name="purchase.tag",
        relation="purchase_order_tag_rel",
        column1="purchase_order_id",
        column2="tag_id",
        string="Tags",
        compute="_compute_tag_ids",
        store=True,
    )

    @api.depends("requisition_id")
    def _compute_tag_ids(self):
        for order in self:
            if order.requisition_id and not order.tag_ids:
                order.tag_ids = order.requisition_id.tag_ids
            else:
                order.tag_ids = order.tag_ids or False
