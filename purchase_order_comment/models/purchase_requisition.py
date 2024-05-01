from odoo import fields, models, _


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    comment = fields.Text(string="Comment", tracking=True)
