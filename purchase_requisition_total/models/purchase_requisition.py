import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    amount_untaxed = fields.Monetary(
        string="Untaxed Amount",
        store=True,
        readonly=True,
        compute="_compute_amount_all",
        tracking=True,
    )
    amount_tax = fields.Monetary(
        string="Taxes", store=True, readonly=True, compute="_compute_amount_all"
    )
    amount_total = fields.Monetary(
        string="Total", store=True, readonly=True, compute="_compute_amount_all"
    )
    fiscal_position_id = fields.Many2one(
        "account.fiscal.position",
        string="Fiscal Position",
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )

    @api.depends("vendor_id", "company_id")
    def _compute_vendor(self):
        for requisition in self:
            requisition = requisition.with_company(requisition.company_id)
            if not requisition.vendor_id:
                requisition.fiscal_position_id = False
                requisition.currency_id = requisition.env.company.currency_id.id
            else:
                requisition.fiscal_position_id = requisition.env[
                    "account.fiscal.position"
                ].get_fiscal_position(requisition.vendor_id.id)
                requisition.currency_id = (
                    requisition.vendor_id.property_purchase_currency_id.id
                    or requisition.env.company.currency_id.id
                )

    @api.depends("line_ids.price_total")
    def _compute_amount_all(self):
        for requisition in self:
            amount_untaxed = amount_tax = 0.0
            for line in requisition.line_ids:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            requisition.update(
                {
                    "amount_untaxed": requisition.currency_id.round(amount_untaxed),
                    "amount_tax": requisition.currency_id.round(amount_tax),
                    "amount_total": amount_untaxed + amount_tax,
                }
            )


class PurchaseRequisitionLine(models.Model):
    _inherit = "purchase.requisition.line"

    currency_id = fields.Many2one(
        "res.currency", related="requisition_id.currency_id", readonly=True
    )
    taxes_id = fields.Many2many(
        "account.tax",
        string="Taxes",
        domain=["|", ("active", "=", False), ("active", "=", True)],
        compute="_compute_tax_id",
        store=True,
        readonly=False,
    )
    price_subtotal = fields.Monetary(
        compute="_compute_amount", string="Subtotal", store=True
    )
    price_total = fields.Monetary(compute="_compute_amount", string="Total", store=True)
    price_tax = fields.Float(compute="_compute_amount", string="Tax", store=True)

    @api.depends(
        "product_id",
        "requisition_id.vendor_id",
        "requisition_id.fiscal_position_id",
        "company_id",
    )
    def _compute_tax_id(self):
        for line in self:
            line = line.with_company(line.company_id)
            fpos = (
                line.requisition_id.fiscal_position_id
                or self.env['account.fiscal.position']._get_fiscal_position(
                    line.requisition_id.vendor_id
                )
            )
            # Filter taxes by company
            taxes = line.product_id.supplier_taxes_id.filtered(
                lambda r: r.company_id == line.env.company
            )
            line.taxes_id = fpos.map_tax(
                taxes
            )

    @api.depends("product_uom_id", "price_unit", "taxes_id")
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
                    "price_tax": sum(
                        t.get("amount", 0.0) for t in taxes.get("taxes", [])
                    ),
                    "price_total": taxes["total_included"],
                    "price_subtotal": taxes["total_excluded"],
                }
            )
