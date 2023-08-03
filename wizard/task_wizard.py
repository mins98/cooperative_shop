from odoo import api, fields, models

class TaskWizard(models.TransientModel):
    _name = 'cooperative_shop.task.wizard'
    _description = "Wizard: Quickly add volunteers to tasks"

    def _default_partner(self):
        return self.env['res.partner'].browse(self._context.get('active_id'))
    volunter_id = fields.Many2one(comodel_name="res.partner" ,default=_default_partner) 
    
    volunter_tasks_ids = fields.Many2many(comodel_name="cooperative_shop.task", string="Actual tasks", related='volunter_id.tasks_ids')
    
    tasks_ids = fields.Many2many(comodel_name="cooperative_shop.task", string="New tasks")
    
    def assign_tasks_to_contact(self):
        for record in self.tasks_ids:
            ### record_field_dictionary generated here
            record.update({'volunteers_ids': [self.volunter_id.id]})
        """project_id = self.env['res.partner'].create({
            'partner_id': self.volunter_id.id,
            'tasks_ids':  self.tasks_ids
        })"""
            
            
        

