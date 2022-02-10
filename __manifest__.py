{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'Manages Real Estate Advertisement and Services',
    'description': "",
    'website': 'http://www.odoo.com/real_estate',
    'depends': [],
    'data':[
       'security/ir.model.access.csv',
       'views/property_views.xml',
       'views/property_type_views.xml',
       'views/property_tag_views.xml',
       'views/property_offer_views.xml',
       'views/estate_menus.xml',
       'wizard/assign_buyer_view.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'


}
