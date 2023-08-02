from odoo import api, fields, models


class Project(models.Model):
    _inherit = 'hr.expense'

    task_id = fields.Many2one(comodel_name="cooperative_shop.task",
                                 string="Related Task",
                                 ondelete="set null")
    