from odoo import _,api,fields,models
from odoo.exceptions import UserError

class Property(models.Model):
    _name="estate.property"
    _description = "estate property"
           
    name=fields.Char(string="Property Name",required=True)
    description=fields.Text(string="Property details")
    postcode=fields.Char(string="Postcode")
    date_availability=fields.Date(string="Availability Date",copy=False,default=fields.Date.today())
    expected_price=fields.Float(string="Expected Price",required=True)
    selling_price=fields.Float(string="Selling Price",copy=False,readonly=True)
    bedrooms=fields.Integer(string="Bedrooms",default="2")
    living_area=fields.Integer(string="Living Area")
    facades=fields.Integer(string="Facades")
    garage=fields.Boolean(default=True)
    garden=fields.Boolean(default=True)
    garden_area=fields.Integer(string="Garden Area")
    garden_orientation=fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')],default="north")        
    active = fields.Boolean(default=True)
    state = fields.Selection([('new', 'New'), ('offer recieved', 'Offer Received'), ('offer accepted','Offer Accepted'),
    ('sold','Sold'),('canceled','Canceled')],default="new",copy=False,required=True)


    property_type_id= fields.Many2one('estate.property.type')
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    
    best_price = fields.Float(compute="_compute_best_price")
    total_area = fields.Float(compute="_compute_totalarea")

    _sql_constraints = [
        ('check_excepted_price', 'check(expected_price>0)', "Excepted price must be strictly Positive."),
        ('check_selling_price', 'check(selling_price>=0)', "Selling price must be Positive.")
    ]
    
    @api.depends("living_area","garden_area")
    def _compute_totalarea(self):
        for record in self:
            record.total_area=record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            x = 0
            for offer in record.offer_ids:
                if not x or offer.price>x:
                    x = offer.price
            record.best_price = x

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = None

    def sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("Canceled properties cannot be sold.")
            record.state = "sold"
        return True

    def cancel(self):
        for record in self:
            if record.state=='sold':
                raise UserError("Sold properties cannot be canceled")
            record.state="canceled"
        return True
   