import logging

from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # @api.onchange("requisition_id")
    # def _onchange_requisition_id(self):
    #     super()._onchange_requisition_id()
    #     if self.requisition_id and self.requisition_id.incoterm_id:
    #         self.incoterm_id = self.requisition_id.incoterm_id


    def _apply_requisition_incoterm(self):
        for order in self:
            if order.requisition_id and order.requisition_id.incoterm_id:
                order.incoterm_id = order.requisition_id.incoterm_id
            elif order.partner_id and order.partner_id.purchase_incoterm_id:
                order.incoterm_id = order.partner_id.purchase_incoterm_id
            else:
                order.incoterm_id = False

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        res = super()._onchange_requisition_id()
        self._apply_requisition_incoterm()
        return res

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super().onchange_partner_id()
        self._apply_requisition_incoterm()
        return res

    @api.model
    def default_get(self, fields_list):
        vals = super().default_get(fields_list)
        requisition_id = vals.get('requisition_id')
        if requisition_id and 'incoterm_id' in fields_list:
            requisition = self.env['purchase.requisition'].browse(requisition_id)
            if requisition.incoterm_id:
                vals['incoterm_id'] = requisition.incoterm_id.id
        return vals



