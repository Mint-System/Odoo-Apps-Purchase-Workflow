import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    fiscal_position_id = fields.Many2one(
        "account.fiscal.position", compute="_compute_fiscal_position_id", store=True
    )


    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        _logger.warning("#### CALLED")
        res = super()._onchange_requisition_id()
        if self.requisition_id and self.requisition_id.fiscal_position_id:
            self.fiscal_position_id = self.requisition_id.fiscal_position_id
        elif self.partner_id:
            self.fiscal_position_id = self.env['account.fiscal.position'].with_company(
                self.company_id
            )._get_fiscal_position(self.partner_id)
        else:
            self.fiscal_position_id = False
        return res


    @api.depends("requisition_id", "requisition_id.fiscal_position_id", "partner_id", "company_id")
    def _compute_fiscal_position_id(self):
        for order in self:
            if order.requisition_id and order.requisition_id.fiscal_position_id:
                order.fiscal_position_id = order.requisition_id.fiscal_position_id
            elif order.partner_id:
                order.fiscal_position_id = self.env['account.fiscal.position'].with_company(
                    order.company_id
                )._get_fiscal_position(order.partner_id)
            else:
                order.fiscal_position_id = False