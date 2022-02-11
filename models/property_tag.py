from odoo import _,api,fields,models

class property_tag(models.Model):
    _name="estate.property.tag"
    _description = "estate property tag"
    _order="name"

    name=fields.Char(string="Property Tag",required=True)

    _sql_constraints = [
        ('check_name', 'unique(name)', "Property tag must be unique.")
     ]
  