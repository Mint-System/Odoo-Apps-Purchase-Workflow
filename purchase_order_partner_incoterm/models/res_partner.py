from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    purchase_incoterm_id = fields.Many2one(
        string="Default Purchase Incoterm",
        comodel_name="account.incoterms",
        help="The default incoterm for new purchase orders for this customer.",
    )
