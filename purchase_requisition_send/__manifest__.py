{
    "name": "Purchase Requisition Send",
    "summary": """
        Add send action to purchase contract.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Purchase",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["purchase_requisition", "purchase_requisition_order_address"],
    "data": ["views/purchase_requisition_views.xml", "data/mail_data.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
