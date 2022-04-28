from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    note_header = fields.Html()
    note_footer = fields.Html()
