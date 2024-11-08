from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    incoterm_id = fields.Many2one(
        "account.incoterms",
        compute="_compute_incoterm_id",
        store=True,
        readonly=False,
    )

    @api.depends("partner_id")
    def _compute_incoterm_id(self):
        for order in self:
            if order.partner_id:
                order.incoterm_id = order.partner_id.purchase_incoterm_id
            else:
                order.incoterm_id = False
