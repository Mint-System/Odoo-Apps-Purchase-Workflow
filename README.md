# Odoo Apps: Purchase Workflow

Collection of purchase model related modules.

## Usage

Clone module into Odoo addon directory.

```bash
git clone git@github.com:mint-system/odoo-apps-purchase-workflow.git ./addons/purchase_workflow
```

## Available modules

| Module | Summary |
| --- | --- |
| [purchase_order_address](purchase_order_address) |         Validate purchase order before sending or confirming. |
| [purchase_order_comment](purchase_order_comment) |         Comment field for purchase order. |
| [purchase_order_line_date](purchase_order_line_date) |         This module ensure that line order date are propagated to stock pickings. |
| [purchase_order_line_description](purchase_order_line_description) |         This module sets to use only product's purchase description field on the purchase order lines. |
| [purchase_order_line_position](purchase_order_line_position) |         Use purchase order line position for linked delivery orders and outgoing invoices. |
| [purchase_order_line_price_default](purchase_order_line_price_default) |         Set price to zero if seller is not available. |
| [purchase_order_line_relay_price](purchase_order_line_relay_price) |         Calculates the best price possible for a purchase line and notifies the purchaser. |
| [purchase_order_notes](purchase_order_notes) |         Header and footer note fields for purchase order. |
| [purchase_order_partner_incoterm](purchase_order_partner_incoterm) |         Adds new field to partner form for registering the default pruchase incoterms. |
| [purchase_order_validate](purchase_order_validate) |         Validate purchase order before sending or confirming. |
| [purchase_requisition_fiscal](purchase_requisition_fiscal) |         Set tax code on purchse contract. |
| [purchase_requisition_incoterm](purchase_requisition_incoterm) |         Set incoterm on purchase contract. |
| [purchase_requisition_notes](purchase_requisition_notes) |         Add notes on purchase agreement and copy them to purchase orders. |
| [purchase_requisition_order_address](purchase_requisition_order_address) |         Set order address on purchase agreement and copy to order. |
| [purchase_requisition_payment_term](purchase_requisition_payment_term) |         Set payment term on purchase contract. |
| [purchase_requisition_send](purchase_requisition_send) |         Add send action to purchase contract. |
| [purchase_requisition_tag](purchase_requisition_tag) |         Set tags on purchase agreement and copy them to purchase order. |
