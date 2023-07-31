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
    'depends':  ['base'],
    'data':  [
        'security/cooperative_groups.xml',
        'security/ir.model.access.csv',
        'security/cooperative_security.xml',
        'views/cooperative_menuitems.xml'
        ],
    'demo':  [
               'demo/task_demo.xml',
               ],
    'application': True,
}