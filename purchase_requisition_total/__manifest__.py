{
    "name": "Purchase Requisition Total",
    "summary": """
        Caclulate taxed and untaxed total for order and lines.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Purchase",
    "version": "14.0.1.2.1",
    "license": "AGPL-3",
    "depends": ["purchase_requisition"],
    "data": ["views/purchase_requisition.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
