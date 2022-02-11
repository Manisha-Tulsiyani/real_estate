from odoo import _,api,fields,models

class property_type(models.Model):
    _name="estate.property.type"
    _description = "estate property type"
    _order="name"

    name=fields.Char(string="Property Type",required=True)
    sequence = fields.Integer('Sequence',default=1)
    property_ids=fields.One2many('estate.property','property_type_id')

    _sql_constraints = [
        ('check_name', 'unique(name)', "Property type must be unique.")
     ]
  