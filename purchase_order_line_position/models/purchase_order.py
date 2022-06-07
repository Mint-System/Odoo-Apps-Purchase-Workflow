from odoo import fields, models, _, api
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def set_position(self):
        for order in self:
            position = 0
            for line in order.order_line.filtered(lambda l: not l.display_type):
                position += 1
                line.position = position

    # Set position on create
    @api.model
    def create(self, values):
        res = super().create(values)
        res.set_position()

        return res

    # Set position on update
    def write(self, values):
        res = super().write(values)
        self.set_position()

        return res

    def get_position(self, product_id, product_qty=False):
        self.ensure_one()
        if product_qty:
            lines = self.order_line.filtered(lambda l: l.product_id == product_id and l.product_qty == product_qty)
        else:
            lines = self.order_line.filtered(lambda l: l.product_id == product_id)
        for line in lines:
            return line.position
        
        return 0

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    position = fields.Integer("Pos", readonly=True)
