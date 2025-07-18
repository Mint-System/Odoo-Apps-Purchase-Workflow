import logging

from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        res = super().onchange_partner_id()
        if self.requisition_id and self.requisition_id.incoterm_id:
            self.incoterm_id = self.requisition_id.incoterm_id
        # self.incoterm_id = self.partner_id.commercial_partner_id.purchase_incoterm_id
        return res


    incoterm_id = fields.Many2one(
        "account.incoterms",
        "Incoterm", 
        compute="_compute_incoterm_id",
        store=True,
        help="International Commercial Terms are a series of predefined commercial terms used in international transactions."
        )

    @api.depends("requisition_id")
    def _compute_incoterm_id(self):
        _logger.warning("############### compute incoterm called")
        for order in self:
            if order.requisition_id and order.requisition_id.incoterm_id:
                order.incoterm_id = order.requisition_id.incoterm_id
            elif not order.requisition_id:
                order.incoterm_id = False
            return

    # @api.onchange("requisition_id")
    # def _onchange_requisition_id(self):
    #     _logger.info("############### onchange req id called")
    #     _logger.info("self.requisition_id: %s" % self.requisition_id)
    #     _logger.info("self.requisition_id.incoterm_id: %s" % self.requisition_id.incoterm_id)
    #     if self.requisition_id and self.requisition_id.incoterm_id:
    #         self.incoterm_id = self.requisition_id.incoterm_id
    #     elif not self.requisition_id:
    #         self.incoterm_id = False


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            _logger.info("########### vals: %s" % vals)
        orders = super(PurchaseOrder, self).create(vals_list)
        return orders
        

