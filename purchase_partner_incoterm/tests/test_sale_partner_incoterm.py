from odoo.tests.common import TransactionCase


class TestPurchasePartnerIncoterm(TransactionCase):
    def test_purchase_partner_incoterm(self):
        """
        Check that the customer's default incoterm is retrieved in the
        purchases order's onchange
        """
        customer = self.env.ref("base.res_partner_3")
        incoterm = self.env["account.incoterms"].search([], limit=1)
        customer.write({"purchase_incoterm_id": incoterm.id})
        purchase_order = self.env["purchase.order"].create({"partner_id": customer.id})
        purchase_order.onchange_partner_id()
        self.assertEqual(purchase_order.incoterm, incoterm)
