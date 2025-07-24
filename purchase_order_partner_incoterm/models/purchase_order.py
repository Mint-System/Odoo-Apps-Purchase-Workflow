from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange('partner_id', 'company_id')
    def onchange_partner_id(self):
        res = super().onchange_partner_id()
        if self.partner_id.purchase_incoterm_id:
            self.incoterm_id = self.partner_id.purchase_incoterm_id
        return res

    incoterm_id = fields.Many2one(
        "account.incoterms",
        "Incoterm", 
        compute="_compute_incoterm_id",
        store=True,
        help="International Commercial Terms are a series of predefined commercial terms used in international transactions."
        )

    @api.depends("partner_id")
    def _compute_incoterm_id(self):
        for order in self:
            _logger.info("######### _compute_incoterm_id called: %s", order.partner_id.purchase_incoterm_id)
            if order.partner_id and order.partner_id.purchase_incoterm_id:
                order.incoterm_id = order.partner_id.purchase_incoterm_id
            elif not order.partner_id:
                order.incoterm_id = False
            return

