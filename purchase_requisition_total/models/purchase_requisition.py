from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    @api.depends('line_ids.price_total')
    def _compute_amount_all(self):
        for requisition in self:
            amount_untaxed = amount_tax = 0.0
            for line in requisition.line_ids:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            requisition.update(
                {
                    'amount_untaxed': requisition.currency_id.round(amount_untaxed),
                    'amount_tax': requisition.currency_id.round(amount_tax),
                    'amount_total': amount_untaxed + amount_tax,
                }
            )

    amount_untaxed = fields.Monetary(
        string='Untaxed Amount',
        store=True,
        readonly=True,
        compute='_compute_amount_all',
        tracking=True,
    )
    amount_tax = fields.Monetary(
        string='Taxes', store=True, readonly=True, compute='_compute_amount_all'
    )
    amount_total = fields.Monetary(
        string='Total', store=True, readonly=True, compute='_compute_amount_all'
    )
    fiscal_position_id = fields.Many2one('account.fiscal.position', 
        string='Fiscal Position',
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]"
    )

    @api.onchange('vendor_id', 'company_id')
    def _onchange_vendor(self):
        super()._onchange_vendor()
        self = self.with_company(self.company_id)
        if not self.vendor_id:
            self.fiscal_position_id = False
            self.currency_id = self.env.company.currency_id.id
        else:
            self.fiscal_position_id = self.env['account.fiscal.position'].get_fiscal_position(self.vendor_id.id)
            self.currency_id = self.vendor_id.property_purchase_currency_id.id or self.env.company.currency_id.id
        return {}

class PurchaseRequisitionLine(models.Model):
    _inherit = 'purchase.requisition.line'

    @api.depends('product_uom_id', 'price_unit', 'taxes_id')
    def _compute_amount(self):
        for line in self:
            taxes = line.taxes_id.compute_all(
                line.price_unit,
                currency=line.requisition_id.currency_id,
                quantity=line.product_qty,
                product=line.product_id,
                partner=line.requisition_id.vendor_id,
            )
            line.update(
                {
                    'price_tax': sum(
                        t.get('amount', 0.0) for t in taxes.get('taxes', [])
                    ),
                    'price_total': taxes['total_included'],
                    'price_subtotal': taxes['total_excluded'],
                }
            )

    currency_id = fields.Many2one(
        'res.currency', related='requisition_id.currency_id', readonly=True
    )
    taxes_id = fields.Many2many(
        'account.tax',
        string='Taxes',
        domain=['|', ('active', '=', False), ('active', '=', True)],
    )
    price_subtotal = fields.Monetary(
        compute='_compute_amount', string='Subtotal', store=True
    )
    price_total = fields.Monetary(compute='_compute_amount', string='Total', store=True)
    price_tax = fields.Float(compute='_compute_amount', string='Tax', store=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        super()._onchange_product_id()
        self._compute_tax_id()

    def _compute_tax_id(self):
        for line in self:
            line = line.with_company(line.company_id)
            fpos = line.requisition_id.fiscal_position_id or line.requisition_id.fiscal_position_id.get_fiscal_position(line.requisition_id.vendor_id.id)
            # Filter taxes by company
            taxes = line.product_id.supplier_taxes_id.filtered(lambda r: r.company_id == line.env.company)
            line.taxes_id = fpos.map_tax(taxes, line.product_id, line.requisition_id.vendor_id)