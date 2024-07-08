import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    partner_order_id = fields.Many2one(
        "res.partner",
        string="Order Address",
        compute="_compute_partner_order_id",
        store=True,
        readonly=False,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )

    @api.depends("partner_id", "requisition_id")
    def _compute_partner_order_id(self):
        for order in self:
            if order.requisition_id and order.requisition_id.partner_order_id:
                order.partner_order_id = order.requisition_id.partner_order_id
            elif order.partner_id:
                addr = order.partner_id.address_get(["order"])
                order.partner_order_id = addr["order"]
            else:
                order.partner_order_id = False
