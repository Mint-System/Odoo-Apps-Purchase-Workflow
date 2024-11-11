import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    partner_order_id = fields.Many2one(
        "res.partner",
        string="Order Address",
        required=False,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        compute="_compute_partner_order_id",
        store=True,
        readonly=False,
    )

    @api.depends("partner_id")
    def _compute_partner_order_id(self):
        for order in self:
            if order.partner_id:
                addr = order.partner_id.address_get(["order"])
                order.partner_order_id = addr["order"]
            else:
                order.partner_order_id = False
