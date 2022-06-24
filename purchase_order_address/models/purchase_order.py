from odoo import api, models, _, fields
from odoo.addons.purchase.models.purchase import PurchaseOrder as Purchase
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    partner_order_id = fields.Many2one(
        'res.partner', string='Order Address', required=True,
        states=Purchase.READONLY_STATES,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if not self.requisition_id.partner_order_id:
            res= super().onchange_partner_id()
            addr = self.partner_id.address_get(['order'])
            values = {
                'partner_order_id': addr['order'],
            }
            self.update(values)
            return res
        else:
            self._onchange_requisition_id()

    def action_rfq_send(self):
        action = super().action_rfq_send()
        ctx = action['context']
        ctx['default_partner_ids'] = [self.partner_order_id.id]
        action.update({'context': ctx})
        return action
