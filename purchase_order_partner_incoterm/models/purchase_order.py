from odoo import api, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange('partner_id', 'company_id')
    def onchange_partner_id(self):
        res = super().onchange_partner_id()
        if self.partner_id.purchase_incoterm_id:
            self.incoterm_id = self.partner_id.purchase_incoterm_id
        return res