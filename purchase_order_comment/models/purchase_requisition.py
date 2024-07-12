from odoo import fields, models


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    comment = fields.Text(tracking=True)
