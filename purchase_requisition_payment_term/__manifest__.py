{
    "name": "Purchase Requisition Payment Term",
    "summary": """
        Set payment term on purchase contract.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Purchase",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["purchase_order_partner_incoterm", "purchase_requisition"],
    "data": ["views/purchase_requisition_views.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
