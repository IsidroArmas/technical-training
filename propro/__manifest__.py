{
    'name': 'Propro',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Módulo de fabricación Propro',
    'description': """Este módulo controla la fabricación del Producto en Proceso.""",
    'author': 'Isidro Armas',
    'depends': ['base'],
    'data': [
        'views/propro_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}