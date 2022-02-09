from odoo import _, api, fields, models

class AssignBuyer(models.TransientModel):
    _name = "assign.buyer"

    buyer_id = fields.Many2one("res.partner", string="Buyer")

    def action_assign_buyer(self):
        self.ensure_one()
        Session = self.env['estate.property']
        ids = self.env.context.get('active_ids')
        sessions = Session.browse(ids)
        sessions.write({'buyer_id': self.buyer_id})
        return True 
