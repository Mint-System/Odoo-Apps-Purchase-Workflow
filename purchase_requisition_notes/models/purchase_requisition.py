import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    note_header = fields.Html()
    note_footer = fields.Html()
