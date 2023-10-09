import logging

from odoo import api, fields, models
from odoo.osv import expression
from odoo.tools.date_utils import get_timedelta

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_subscription = fields.Boolean(
        compute="_compute_is_subscription", store=True, index=True
    )
    recurrence_id = fields.Many2one(
        "sale.temporal.recurrence",
        ondelete="restrict",
        readonly=False,
        store=True,
    )
    start_date = fields.Date(
        compute="_compute_subscription_dates",
        readonly=False,
        store=True,
        copy=False,
        tracking=True,
    )
    next_invoice_date = fields.Date(
        compute="_compute_subscription_dates",
        store=True,
        copy=False,
        tracking=True,
        readonly=False,
    )
    end_date = fields.Date(tracking=True)
    last_invoice_date = fields.Date(compute="_compute_last_invoice_date")

    @api.depends("recurrence_id")
    def _compute_is_subscription(self):
        """If recurrence is selelcted, the order becomes a subscription."""
        for order in self:
            if not order.recurrence_id:
                order.is_subscription = False
                continue
            order.is_subscription = True

    @api.depends("is_subscription")
    def _compute_subscription_dates(self):
        """Update start date when order becomes subscription."""
        for order in self:
            if not order.is_subscription:
                order.start_date = False
            elif not order.start_date:
                order.start_date = order.date_planned or fields.Date.today()
                order.next_invoice_date = order.date_planned or fields.Date.today()

    @api.depends("state", "next_invoice_date")
    def _compute_last_invoice_date(self):
        """Last invoice date is next invoice date minus the recurrence delta."""
        for order in self:
            if order.recurrence_id:
                last_date = (
                    order.next_invoice_date
                    and order.next_invoice_date
                    - get_timedelta(
                        order.recurrence_id.duration, order.recurrence_id.unit
                    )
                )
                if (
                    order.state in ["purchase", "done"]
                    and last_date
                    and order.start_date
                    and last_date >= order.start_date
                ):
                    order.last_invoice_date = last_date
                else:
                    order.last_invoice_date = False
            else:
                order.last_invoice_date = False

    def button_confirm(self):
        self._compute_subscription_dates()
        return super().button_confirm()

    def _update_next_invoice_date(self):
        """Update the next_invoice_date according to the periodicity of the order."""
        for order in self:
            if not order.is_subscription:
                continue
            last_invoice_date = order.next_invoice_date or order.start_date
            if last_invoice_date:
                order.next_invoice_date = last_invoice_date + get_timedelta(
                    order.recurrence_id.duration, order.recurrence_id.unit
                )

    def _recurring_purchase_domain(self, extra_domain=None):
        if not extra_domain:
            extra_domain = []
        current_date = fields.Date.today()
        search_domain = [
            "&",
            ("is_subscription", "=", True),
            "&",
            ("state", "in", ["purchase", "done"]),
            "&",
            ("next_invoice_date", "<=", current_date),
            "|",
            ("end_date", ">=", current_date),
            ("end_date", "=", False),
        ]
        if extra_domain:
            search_domain = expression.AND([search_domain, extra_domain])
        return search_domain

    def _increase_qty_received(self):
        """Increase qty received for recurring purchase orders."""
        for order in self:
            for line in order.order_line:
                line.write({"qty_received": line.qty_received + line.product_qty})

    @api.model
    def _cron_recurring_purchase_order(self):
        """Recurring action for purchase order subscriptions."""
        search_domain = self._recurring_purchase_domain()
        subscriptions = self.search(search_domain)
        subscriptions._increase_qty_received()
        subscriptions._update_next_invoice_date()
