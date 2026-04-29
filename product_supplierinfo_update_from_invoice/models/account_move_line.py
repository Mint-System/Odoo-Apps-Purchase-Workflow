# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"


    can_update_product_supplierinfo = fields.Boolean(
        compute="_compute_can_update_product_supplierinfo",
        store=False
    )

    def _get_supplierinfo(self):
        self.ensure_one()
        product_id=self.product_id
        product_supplierinfo = (
            product_id._select_seller(
                partner_id=self.partner_id,
                quantity=self.quantity,
                date=self.purchase_order_id.date_order
                and self.purchase_order_id.date_order.date()
                or fields.Date.context_today(self),
                uom_id=self.product_uom_id,
                params=self.purchase_line_id._get_select_sellers_params()
                if self.purchase_line_id 
                else {},
            )
            if product_id
            else False
        )
        return product_supplierinfo


    def action_update_product_supplierinfo(self):
        self.ensure_one()

        product_supplierinfo = self._get_supplierinfo()

        if product_supplierinfo:
            product_supplierinfo.write(
                {
                    "price": self.price_unit,
                }
            )
        else:
            self.product_id.seller_ids.create(
                {
                    "partner_id": self.partner_id.id,
                    "product_tmpl_id": self.product_id.product_tmpl_id.id,
                    "price": self.price_unit,
                }
            )

    @api.onchange("product_id", "partner_id", "price_unit")
    def _compute_can_update_product_supplierinfo(self):
        for line in self:
            # We need this condition because in some situations
            # the onchange methods can fail.
            if (
                not line._origin.id
                or not line.product_id
                or not line.partner_id
                or not line.price_unit
            ):
                line.can_update_product_supplierinfo = False
                continue
            product_supplierinfo = line._get_supplierinfo()
            line.can_update_product_supplierinfo = bool(
                not product_supplierinfo
                or product_supplierinfo.price != line.price_unit
            )