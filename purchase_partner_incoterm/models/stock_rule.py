from odoo import models


class StockRule(models.Model):
    _inherit = 'stock.rule'
    
    def _prepare_purchase_order(self, company_id, origins, values):
        res = super(StockRule, self)._prepare_purchase_order(company_id, origins, values)
        values = values[0]
        res['incoterm_id'] = values['supplier'].name.purchase_incoterm_id.id
        return res
