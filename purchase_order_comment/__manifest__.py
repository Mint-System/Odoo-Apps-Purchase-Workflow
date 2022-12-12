{
    "name": "Purchase Order Comment",
    "summary": """
        Comment field for purchase order and contract.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Purchase",
    "version": "14.0.1.1.0",
    "license": "AGPL-3",
    "depends": ["purchase_requisition", "purchase_requisition_other_information_page"],
    "data": [
        "views/purchase_order_form.xml",
        "views/view_purchase_requisition_form.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
