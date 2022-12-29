from odoo import fields, models, api
import ast


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    comment = fields.Text(tracking=True)

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        res = super(PurchaseOrder, self)._onchange_requisition_id()
        copy_requisition_comment = ast.literal_eval(self.env['ir.config_parameter'].sudo().get_param('purchase.order.copy_requisition_comment', 'False'))
        if self.requisition_id and not self.comment and copy_requisition_comment:
            self.comment = self.requisition_id.comment
        return res