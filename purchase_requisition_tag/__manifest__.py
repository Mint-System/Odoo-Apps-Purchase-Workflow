{
    "name": "Purchase Requisition Tag",
    "summary": """
        Set tags on purchase agreement and copy them to purchase order.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Purchase",
    "version": "14.0.1.0.2",
    "license": "AGPL-3",
    "depends": ["purchase_tag", "purchase_requisition_other_information_page"],
    "data": ["views/purchase_requisition_views.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
