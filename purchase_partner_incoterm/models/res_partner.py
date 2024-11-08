from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    purchase_incoterm_id = fields.Many2one(
        "account.incoterms",
    )
