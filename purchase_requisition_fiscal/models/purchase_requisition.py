from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"
    
    fiscal_position_id = fields.Many2one('account.fiscal.position', string='Fiscal Position', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    @api.onchange('vendor_id')
    def _onchange_vendor(self):
        res = super()._onchange_vendor()
        self.fiscal_position_id = self.vendor_id.property_account_position_id
        return res