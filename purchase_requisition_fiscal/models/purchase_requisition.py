import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    fiscal_position_id = fields.Many2one(
        "account.fiscal.position",
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        compute="_compute_fiscal_position_id",
        store=True,
    )

    @api.depends("vendor_id")
    def _compute_fiscal_position_id(self):
        for requisition in self:
            requisition.fiscal_position_id = (
                requisition.vendor_id.property_account_position_id
            )
