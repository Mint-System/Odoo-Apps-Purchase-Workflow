from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"
    
    tag_ids = fields.Many2many(
        comodel_name="purchase.tag",
        relation="purchase_requisition_tag_rel",
        column1="purchase_requisition_id",
        column2="tag_id",
        string="Tags",
    )
