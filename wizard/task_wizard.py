from odoo import api, fields, models

class TaskWizard(models.TransientModel):
    _name = 'cooperative_shop.task.wizard'
    _description = "Wizard: Quickly add volunteers to tasks"

    def _default_partner(self):
        return self.env['res.partner'].browse(self._context.get('active_id'))

    tasks_ids = fields.Many2many(comodel_name="cooperative_shop.task", string="Volunteers in this task")
