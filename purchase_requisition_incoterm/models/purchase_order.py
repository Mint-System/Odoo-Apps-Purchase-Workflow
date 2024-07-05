import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    incoterm_id = fields.Many2one(
        "account.incoterms",
        compute="_compute_incoterm_id",
        store=True,
    )

    @api.depends("requisition_id")
    def _compute_incoterm_id(self):
        for order in self:
            if order.requisition_id and order.requisition_id.incoterm_id:
                order.incoterm_id = order.requisition_id.incoterm_id
            elif not order.requisition_id:
                order.incoterm_id = False

    @api.model
    def create(self, vals):
        if vals.get("requisition_id"):
            requisition = self.env["purchase.requisition"].browse(
                vals["requisition_id"]
            )
            if requisition.incoterm_id:
                vals["incoterm_id"] = requisition.incoterm_id.id
        return super(PurchaseOrder, self).create(vals)
