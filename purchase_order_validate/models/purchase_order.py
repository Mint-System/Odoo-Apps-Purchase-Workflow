from odoo import api, models, _
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def validate(self):
        if not self.user_id:
            raise ValidationError(_("The purchase representative is not set."))

    def button_confirm(self):
        self.validate()
        return super(PurchaseOrder, self).button_confirm()

    def action_rfq_send(self):
        self.validate()
        return super(PurchaseOrder, self).action_rfq_send()
