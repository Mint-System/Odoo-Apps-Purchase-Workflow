{
    "name": "Purchase Order Address",
    "summary": """
        Validate purchase order before sending or confirming.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Purchase",
    "version": "14.0.1.2.1",
    "license": "AGPL-3",
    "depends": ["purchase", "partner_type_order"],
    "data": ["views/purchase_order_form.xml", "data/mail_template_data.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
