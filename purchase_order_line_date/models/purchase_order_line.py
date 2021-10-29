import logging
from odoo import models, fields
from dateutil.relativedelta import relativedelta


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def write(self, values):
        if values.get('date_planned'):
             self.move_ids.date = fields.Datetime.to_datetime(values.get('date_planned')) + relativedelta(days=self.company_id.po_lead)
        return super(PurchaseOrderLine, self).write(values)
