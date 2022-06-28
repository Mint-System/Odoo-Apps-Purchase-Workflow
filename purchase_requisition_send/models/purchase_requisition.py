from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"
    
    state = fields.Selection(selection_add=[
        ('sent', 'Sent'),
    ], ondelete={'sent': 'cascade'})

    @api.model
    def create(self,vals):
        """Generate name from sequence on create"""
        _logger.warning([vals,self.is_quantity_copy])
        if vals.get('name', _('New')) ==  _('New') and vals.get('type_id'):
            type_id = self.env['purchase.requisition.type'].browse(vals['type_id'])
            if type_id.quantity_copy != 'none':
                vals['name'] = self.env['ir.sequence'].next_by_code('purchase.requisition.purchase.tender')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('purchase.requisition.blanket.order')
        return super().create(vals)

    def action_order_send(self):
        """Opens a wizard to compose an email, with relevant mail template loaded by default"""
        self.ensure_one()
        
        lang = self.env.context.get('lang')
        template = self.env.ref('purchase_requisition_send.email_template_purchase_requisition')
        if template.lang:
            lang = template._render_lang(self.ids)[self.id]

        compose_form = self.env.ref('mail.email_compose_message_wizard_form')
        ctx = {
            'default_model': 'purchase.requisition',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template),
            'default_template_id': template.id,
            'default_composition_mode': 'comment',
            'mark_pr_as_sent': True,
            'force_email': True,
        }  
        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx
        }

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        if self.env.context.get('mark_pr_as_sent'):
            self.filtered(lambda o: o.state == 'draft').write({'state': 'sent'})
        return super(PurchaseRequisition, self.with_context(mail_post_autofollow=True)).message_post(**kwargs)