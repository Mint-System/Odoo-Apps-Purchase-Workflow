# Odoo Apps: Purchase Workflow

Collection of purchase model related modules.

## Usage

Clone module into Odoo addon directory.

```bash
git clone git@github.com:mint-system/odoo-apps-purchase-workflow.git ./addons/purchase_workflow
```

## Available modules

| Module                                                                  | Summary                                                                            |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [purchase_partner_incoterm](purchase_partner_incoterm/)                 | Adds new field to partner form for registering the default pruchase incoterms.     |
| [purchase_order_line_date](purchase_order_line_date/)                   | This module ensure that line order date are propagated to stock pickings.          |
| [purchase_order_line_position](purchase_order_line_position/)           | Use purchase order line position for linked delivery orders and outgoing invoices. |
| [purchase_order_line_price_default](purchase_order_line_price_default/) | Set price to zero if seller is not available.                                      |
