import logging
_logger = logging.getLogger(__name__)
from odoo import models, api
from odoo.tools.misc import get_lang


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id')
    def onchange_product_id(self):
        res = super().onchange_product_id()
        # Use purchase description if it exists and transalte with partner lang
        if self.product_id.description_purchase:
            product_lang = self.product_id.with_context(
                lang=get_lang(self.env, self.partner_id.lang).code,
                partner_id=self.partner_id.id,
                company_id=self.company_id.id,
            )
            self.name = product_lang.description_purchase
        return res
