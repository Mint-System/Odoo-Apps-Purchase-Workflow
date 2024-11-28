import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    partner_order_id = fields.Many2one(
        "res.partner",
        string="Order Address",
        required=False,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        compute="_compute_partner_order_id",
        store=True,
        readonly=False,
    )

    @api.depends("vendor_id")
    def _compute_partner_order_id(self):
        for requisition in self:
            if requisition.vendor_id:
                addr = requisition.vendor_id.address_get(["order"])
                requisition.partner_order_id = addr["order"]
            else:
                requisition.partner_order_id = False
