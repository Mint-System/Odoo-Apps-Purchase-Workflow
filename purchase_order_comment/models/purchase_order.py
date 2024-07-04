import ast

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    comment = fields.Text(
        string="Comment", readonly=False, tracking=True, compute="_compute_comment", store=True
    )

    @api.depends("requisition_id")
    def _compute_comment(self):
        copy_requisition_comment = ast.literal_eval(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("purchase.order.copy_requisition_comment", "False")
        )
        for order in self:
            if order.requisition_id and not order.comment and copy_requisition_comment:
                order.comment = order.requisition_id.comment
            elif not order.requisition_id or not copy_requisition_comment:
                order.comment = False
