# -*- coding: utf-8 -*-
{
    'name': "ExamenRepaso",

    'summary': "Módulo de repaso para el examen para repasar para el examen",

    'description': """
Módulo que consistirá en un modelo de datos que permite añadir información sobre alumnos 
y sus proyectos de fin de ciclo.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/views.xml',
        'views/templates.xml',
        'views/proyectoView.xml',
        'views/menu.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

