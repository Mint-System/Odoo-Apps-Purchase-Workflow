Setup:

- Install purchase_sale_order_analytic_account
- Install Inventory App
- In Settings search "Analytic Accounting" and enable it
- Enable "Multi-Step Routes" in Inventory Settings
- In Inventory Settings > Routes filter archived routes and unarchive "Replenish on Order (MTO)"
- Create or Edit Product and enable "Can be Sold" and "Can be Purchased"
- On Inventory Tab enable "Replenish on Order (MTO)" and "Buy"


Check Analytic Account handling:

- Change to Sales App and create new quotation
- Choose product prepared for "Replenish on Order (MTO)"
- Confirm quotation
- On "Other info" tab choose an arbitrary "Analytic Account"
- On generated purchase orders activate line field "Analytic Distribution"
- Check Analytic Account compliance on sales and purchase order
