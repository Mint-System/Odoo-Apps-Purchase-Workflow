import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    incoterm_id = fields.Many2one(
        "account.incoterms",
        store=True,
        readonly=False,
    )

    # @api.depends("vendor_id")
    # def _compute_incoterm_id(self):
    #     for requisition in self:
    #         requisition.incoterm_id = (
    #             requisition.vendor_id.purchase_incoterm_id
    #             if requisition.vendor_id
    #             else False
    #         )
