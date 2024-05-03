from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    note_header = fields.Html(string='Note Header')
    note_footer = fields.Html(string='Note Footer')
