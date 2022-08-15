{
    "name": "Purchase Requisition Incoterm",
    "summary": """
        Set incoterm on purchase contract.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Purchase",
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "depends": ["purchase_order_partner_incoterm", "purchase_requisition", "purchase_requisition_payment_term"],
    "data": ["views/purchase_requisition_views.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
