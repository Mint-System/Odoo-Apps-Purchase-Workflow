## Date calculation for RFQs

- Open Purchase > Orders > Request for Quotations
- Create a new Request, the proposed product line arrival dates are today + the lead time defined in the products purchase tab
- Set the expected arrival date on product lines (> 1 line items)
- The purchase.order date_planned is set to the earliest purchase.order.line date_planned
- Confirm the order, in the generated transfer the field stock.picking date_scheduled is set according to sale.order date_planned and stock.move dates are set according to purchase.order.line date_planned

## Date processing for existing purchase orders

- Open Purchase > Orders > Purchase Orders
- Choose or generate a Sale Order with > 1 line item
- The linked Receipt has the same Scheduled Dates as the Purchase Order
- Change the Date Planned of the Purchase Order
- Change the Expected Arrival for one line item in the Purchase Order
- In the linked Receipt, the Date Deadline of the Receipt as well as Date Scheduled of the line item will be updated according to the dates in the Purchase Order
