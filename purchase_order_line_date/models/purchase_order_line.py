from odoo import models, fields
from dateutil.relativedelta import relativedelta
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _prepare_stock_moves(self, picking):
        res = super()._prepare_stock_moves(picking)
        for move in res:
            move["date"] = self.date_planned + relativedelta(days=self.company_id.po_lead)
            move["date_deadline"] = self.date_planned
        _logger.warning(res)
        return res

    def write(self, values):
        """When date planned is updated update move dates."""
        _logger.warning('write')
        if values.get('date_planned'):
            self.move_ids.date = fields.Datetime.to_datetime(values.get('date_planned')) + relativedelta(days=self.company_id.po_lead)
        return super(PurchaseOrderLine, self).write(values)

    def _update_move_date_deadline(self, new_date):
        """Remove security lead time from date deadline."""
        _logger.warning('_update_move_date_deadline')
        new_date = new_date - relativedelta(days=self.company_id.po_lead)
        super()._update_move_date_deadline(new_date)