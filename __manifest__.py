# -*- coding: utf-8 -*-
{
    'name': "Gestion Turnos",

    'summary': "Simplifica la creacion de horarios.""
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': "Simplifica la creación de horarios y aumenta la productividad. Gestiona a la perfección los turnos y los recursos y disfruta de una nueva coordinación eficiente entre tus empleados.""
        Long description of module's purpose
    "El módulo también nos facilita el seguimiento de las horas trabajadas por cada empleado y podrá generar informes para la gestión de nóminas y cumplimiento laboral.
	Así mismo, el módulo podrá alertar al supervisor sobre posibles conflictos o ausencias o simplemente, cada vez que haya un cambio.
	Teniendo en cuenta los turnos asignados todas las semanas, nos genera automáticamente los turnos del mes siguiente. El gerente lo podrá revisar y dar el visto bueno antes de publicarlo.
	El sistema podrá predecir la demanda teniendo en cuenta los días de la semana, los días festivos o las horas del día, y asignar automáticamente más personal cuando sea necesario para lidiar con la oleada de clientela. 
Otra cosa que podrá hacer el sistema es avisar automáticamente, al empleado que ha rellenado su disponibilidad, de un hueco en los turnos, y este podrá aceptar la solicitud o denegarla.
"",

    'author': Alexandra Raluca, Savu",
    'website': "https://github.com/alyraluca/Gestion-Turnos.git",

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
