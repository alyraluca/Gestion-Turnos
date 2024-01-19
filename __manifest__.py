# -*- coding: utf-8 -*-
{
    'name': "planificacion_mod1",

    'summary': "Simplifica la creacion de horarios.""
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': "Simplifica la creación de horarios y aumenta la productividad. Gestiona a la perfección los turnos y los recursos y disfruta de una nueva coordinación eficiente entre tus empleados.""
        Long description of module's purpose
    "TAB_Planeación:
-	Podremos gestionar todos los turnos y organizarlos en tablas por puesto o por empleado.
-	Podremos deja turnos sin asignar y asignarlos posteriormente con facilidad.
-	Posibilidad de enviar a los empleados sus respectivos horarios.
-	Posibilidad de copiar todos los turnos de la semana anterior y reorganizarlos.
-	Planeación: mostrar los turnos en una tabla.
-	Ver horarios por dia, semana, mes, año.
TAB_Mi Horario
-	Los empleados podran ver y gestionar sus horarios en una tabla.
-	Turnos abiertos disponibles: los empleados pueden ver los turnos abiertos disponibles.
-	Podremos verlo por dia, semana y més.
TAB_Configuración
-	Podremos crear turnos y puestos de trabajo con el boton de ‘CREAR’."",

    'author': Alexandra Raluca, Savu",
    'website': "https://github.com/alyraluca/planificacion_mod1.git",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
