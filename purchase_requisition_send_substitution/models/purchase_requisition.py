# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    def action_order_send(self):
        action = super().action_order_send()
        ctx = dict(action.get("context") or {})
        template = self.env["mail.template"].browse(ctx.get("default_template_id"))
        if not template:
            return action

        substitute = template._get_substitution_template(template.model_id, self.ids)
        if substitute:
            ctx.update({
                "default_template_id": substitute.id,
                "default_subject": substitute._render_field("subject", self.ids)[self.id],
                "default_body": substitute._render_field("body_html", self.ids)[self.id],
            })
            action["context"] = ctx
        return action