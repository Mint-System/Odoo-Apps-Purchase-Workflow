{
    "name": "Purchase Requisition Line Description",
    "summary": """
        Set description field on purchase contract lines from purchase description.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Purchase",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["purchase_requisition"],
    "data": ["views/purchase_requisition.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
