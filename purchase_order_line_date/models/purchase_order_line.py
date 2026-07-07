import logging
from dateutil.relativedelta import relativedelta

from odoo import fields, models


_logger = logging.getLogger(__name__)


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _prepare_stock_moves(self, picking):
        res = super()._prepare_stock_moves(picking)
        for move in res:
            move["date"] = self.date_planned + relativedelta(
                days=self.company_id.days_to_purchase
            )
            move["date_deadline"] = self.date_planned
        return res

    def write(self, values):
        """When date planned is updated update move dates."""
        if values.get("date_planned"):
            self.move_ids.date = fields.Datetime.to_datetime(
                values.get("date_planned")
            )  + relativedelta(days=self.company_id.days_to_purchase)

        return super().write(values)
