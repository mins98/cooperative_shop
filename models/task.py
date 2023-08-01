from odoo import fields,models 

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
    
    active = fields.Boolean(string="active", default=True)