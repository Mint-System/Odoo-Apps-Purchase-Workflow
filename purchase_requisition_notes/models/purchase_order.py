import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    note_header = fields.Html(compute="_compute_notes", store=True)
    note_footer = fields.Html(compute="_compute_notes", store=True)

    @api.depends("requisition_id")
    def _compute_notes(self):
        for order in self:
            if order.requisition_id:
                if not order.note_header or order.note_header == "<p><br></p>":
                    order.note_header = order.requisition_id.note_header
                if not order.note_footer or order.note_footer == "<p><br></p>":
                    order.note_footer = order.requisition_id.note_footer
            else:
                order.note_header = (
                    order.note_header if order.note_header else "<p><br></p>"
                )
                order.note_footer = (
                    order.note_footer if order.note_footer else "<p><br></p>"
                )
