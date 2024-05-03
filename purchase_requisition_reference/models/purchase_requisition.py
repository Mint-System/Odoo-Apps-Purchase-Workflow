from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"
    
    partner_ref = fields.Char(string='Vendor Reference', copy=False)
