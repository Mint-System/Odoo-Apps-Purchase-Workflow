Setup:

- Add system parameter 'purchase.requisition.line.hide_ref'.
- If set to True product reference is shown.

Test:

- Open Purchase > Products > Products and add a purchase description to product [FURN_8855] Drawer
- Open Purchase > Orders > Blanket Orders and create a new Blanket Order for product [FURN_8855] Drawer and vendor Azure Interior the newly set description is shown on the Blanket Order line
- Confirm the Blanket Order and create a Purchase Order, the description is copied to the purchase order line
