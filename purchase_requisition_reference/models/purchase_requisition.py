import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    partner_ref = fields.Char("Vendor Reference", copy=False)
