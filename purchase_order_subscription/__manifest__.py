{
    "name": "Purchase Order Subscription",
    "summary": """
        Setup recurring purchase orders.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Purchase",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["purchase", "sale_subscription"],
    "data": ["data/purchase_order_data.xml", "views/purchase_order.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
