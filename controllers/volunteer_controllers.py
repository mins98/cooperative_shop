from odoo import http

class Academy(http.Controller):
    @http.route("/cooperative/", auth="public", website=True)
    def index(self,**kw):
        return "Hello, world"
    
    @http.route("/cooperative/volunteers/", auth="public", website=True)
    def courses(self,**kw):
        partners=http.request.env['res.partner'].search([])
        return http.request.render("cooperative_shop.volunteers_website",
            {
                "partners": partners,
            },)
        
    @http.route(
        '/cooperative/<model("cooperative_shop.task"):task>/', auth="public", website=True
    )
    def task(self, task):
        return http.request.render(
            "cooperative_shop.task_website",
            {
                "task": task,
            },
        )