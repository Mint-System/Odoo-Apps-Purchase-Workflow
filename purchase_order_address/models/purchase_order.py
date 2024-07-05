import logging

from odoo import api, fields, models

from odoo.addons.purchase.models.purchase import PurchaseOrder as Purchase

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    partner_order_id = fields.Many2one(
        "res.partner",
        string="Order Address",
        required=False,
        states=Purchase.READONLY_STATES,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        compute="_compute_partner_order_id",
        store=True,
    )

    @api.depends("partner_id")
    def _compute_partner_order_id(self):
        for order in self:
            if order.partner_id:
                addr = order.partner_id.address_get(["order"])
                order.partner_order_id = addr["order"]
            else:
                order.partner_order_id = False

    def action_rfq_send(self):
        action = super().action_rfq_send()
        ctx = action["context"]
        ctx["default_partner_ids"] = [self.partner_order_id.id]
        action.update({"context": ctx})
        return action
