# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Product Supplierinfo Update From Invoice",
    "summary": """
        Updates the product's vendor price with the price set in a supplier invoice.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["purchase", "product", "account"],
    "data": ["views/account_move_views.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
