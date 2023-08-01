from odoo import api,fields,models 

class Task(models.Model):
    _name="cooperative_shop.task"
    _description="Information about the tasks performed by volunteers"
    
    name=fields.Char(string="Task name", required=True)
    start_time=fields.Datetime(string="Start date")
    stop_time=fields.Datetime(string="Finish date" )
    ocurrences=fields.Integer(string="Number of ocurrences")
    description=fields.Text(string="Description")
    task_type=fields.Selection(string="Task Type",
                           selection=[
                               ('charity','Charity'),
                               ('aid','Humanitarian aid'),
                               ('collection','Donation collection'),
                               ('preservation','Wilderness preservation'),
                           ], copy=False)
    state=fields.Selection(string="Task Type", default="draft",
                           selection=[
                               ('draft','Draft'),
                               ('ready','Ready'),
                               ('in_progress','In progress'),
                               ('done','Done'),
                           ], copy=False)
    leader=fields.Char(string="Leader of task")
    active = fields.Boolean(string="active", default=True)
    
    
    @api.onchange('leader')
    def _on_change_leader(self):
        for task in self:
            if task.leader!="" and task.state=="draft":
                task.state ='ready'
            elif task.state!="draft" and task.leader=="":
                task.state ='draft' 