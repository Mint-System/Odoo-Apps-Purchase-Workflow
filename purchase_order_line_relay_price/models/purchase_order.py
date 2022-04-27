import logging
from odoo import models, fields, api, _
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def button_confirm(self):
        self.check_prices()
        return super().button_confirm()

    def check_prices(self):
        for line in self.order_line:
            
            # Check prices if product has sellers
            if line.product_id.seller_ids:
                product_id = line.product_id
                
                # Get all sellers with price minimum qty
                seller_ids = line.product_id.seller_ids.filtered(lambda l: l.min_qty > 0 and l.price > 0)
                
                # Move on if sellers found
                if seller_ids:
                    # Calculate minimal price
                    # min_price = min(seller_ids.mapped(lambda l: l.min_qty * l.price))
                    
                    # Get all sellers with lower price and exluding current price
                    min_seller_ids = seller_ids.filtered(lambda l: l.min_qty * l.price < line.price_subtotal and l.price != line.price_unit)
                    
                    # Move on if sellers with lower price found
                    if min_seller_ids:
                        
                        # Generate note with lower prices
                        summary = _('Check lower relay price')
                        note = _('<p>For the product "%s" a lower relay price has been found:</p>') % product_id.display_name
                        note += "<ul>"
                        for seller in min_seller_ids:
                            note += _('<li>%s %s for %s with delivery time of %s days.</li>') % (seller.min_qty, product_id.uom_id.name, seller.price, seller.delay)
                        note += "</ul>"

                        # Create activity to check prices
                        line.order_id.activity_schedule(
                            activity_type_id=self.env.ref('mail.mail_activity_data_todo').id,
                            summary=summary,
                            note=note,
                            user_id=line.order_id.user_id.id
                        )
