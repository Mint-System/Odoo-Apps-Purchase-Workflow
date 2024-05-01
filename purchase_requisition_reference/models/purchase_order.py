from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)
import ast


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        res = super(PurchaseOrder, self)._onchange_requisition_id()
        copy_reference = ast.literal_eval(self.env['ir.config_parameter'].sudo().get_param('purchase_requisition_reference.copy_reference', 'False'))
        if not self.partner_ref and self.requisition_id and copy_reference:
            self.partner_ref = self.requisition_id.partner_ref
        return res