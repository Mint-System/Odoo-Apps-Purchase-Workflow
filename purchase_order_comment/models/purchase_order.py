from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    comment = fields.Text(tracking=True)

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        super(PurchaseOrder, self)._onchange_requisition_id()
        if self.requisition_id and not self.comment:
            self.comment = self.requisition_id.comment