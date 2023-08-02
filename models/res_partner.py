from odoo import api, fields, models

class Partner(models.Model):
    _inherit = "res.partner"
    
    tasks_ids = fields.Many2many(comodel_name="cooperative_shop.task", string="Volunteers in this task")