import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_subscription = fields.Boolean(
        compute="_compute_is_subscription", store=True, index=True
    )
    recurrence_id = fields.Many2one(
        "sale.temporal.recurrence",
        compute="_compute_recurrence_id",
        ondelete="restrict",
        readonly=False,
        store=True,
    )
    start_date = fields.Date(
        compute="_compute_start_date",
        readonly=False,
        store=True,
        tracking=True,
    )
    end_date = fields.Date(tracking=True)

    def _compute_start_date(self):
        for po in self:
            if not po.is_subscription:
                po.start_date = False
            elif not po.start_date:
                po.start_date = fields.Date.today()

    @api.depends("recurrence_id")
    def _compute_is_subscription(self):
        for order in self:
            if order.recurrence_id:
                order.is_subscription = True
            else:
                order.is_subscription = False
