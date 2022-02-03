from odoo import _,api,fields,models

class property_tag(models.Model):
    _name="estate.property.tag"
    _description = "estate property tag"

    name=fields.Char(string="Property Tag",required=True)
  