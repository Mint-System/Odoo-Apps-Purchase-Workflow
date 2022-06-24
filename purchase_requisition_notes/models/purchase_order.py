from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('requisition_id')
    def _onchange_requisition_id(self):
        super(PurchaseOrder, self)._onchange_requisition_id()
        
        if self.requisition_id and (not self.note_header or self.note_header == '<p><br></p>'):
            self.note_header = self.requisition_id.note_header

        if self.requisition_id and (not self.note_footer or self.note_footer == '<p><br></p>'):
            self.note_footer = self.requisition_id.note_footer