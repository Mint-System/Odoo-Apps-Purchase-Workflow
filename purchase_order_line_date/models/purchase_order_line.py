import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def write(self, values):
        if values.get('date_planned'):
             self.move_ids.date = fields.Datetime.to_datetime(values.get('date_planned'))
        return super(PurchaseOrderLine, self).write(values)
