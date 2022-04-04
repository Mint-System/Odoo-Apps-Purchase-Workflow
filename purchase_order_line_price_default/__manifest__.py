{
    'name': "Purchase Order Line Price Default",

    'summary': """
        Set price to zero if seller is not available.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Purchse',
    'version': '14.0.1.1.0',
    'license': 'AGPL-3',
    
    'depends': ['purchase'],

    'installable': True,
    'application': False,
    'auto_install': False,
    "images": ["images/screen.png"],
}