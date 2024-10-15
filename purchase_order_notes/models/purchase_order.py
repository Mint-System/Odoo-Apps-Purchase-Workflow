from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    note_header = fields.Html(translate=False, readonly=False)
    note_footer = fields.Html(translate=False, readonly=False)
