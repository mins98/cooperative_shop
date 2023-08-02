{
    'name': 'Cooperative Shoop',
    "summary":"""Module to handle the work of volunteers""",
    "description":"""Module to handle:
        - Volunteers
        - Organizations
        - Shoop
    """,
    'license':'OPL-1',
    'author': 'Miguel',
    'website':'www.odoo.com',
    'category': 'Custom Modules/Cooperative',
    'version': '0.1',
    'depends':  ['hr_expense'],
    'data':  [
        'security/cooperative_groups.xml',
        'security/ir.model.access.csv',
        'security/cooperative_security.xml',
        'views/cooperative_menuitems.xml',
        'views/task_views.xml',
        'views/hr_expense_views_inherit.xml',
        'wizard/task_wizard_view.xml',
        ],
    'demo':  [
               'demo/task_demo.xml',
               ],
    'application': True,
}