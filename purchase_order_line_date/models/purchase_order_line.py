import logging
from dateutil.relativedelta import relativedelta

from odoo import fields, models


_logger = logging.getLogger(__name__)


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def write(self, values):
        """When date planned is updated update move dates."""
        if values.get("date_planned"):
            self.move_ids.date = fields.Datetime.to_datetime(
                values.get("date_planned")
            )

        return super().write(values)

