from odoo import _,api,fields,models

class property_type(models.Model):
    _name="estate.property.type"
    _description = "estate property type"

    name=fields.Char(string="Property Type",required=True)
  