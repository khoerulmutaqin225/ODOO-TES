# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class estateProperty(models.Model):
    _name = 'estate.property'

class odoo_module(models.Model):
    _name = 'odoo_module.odoo_module'
    _description = 'odoo_module.odoo_module'

    name = fields.Char("Name" ,required=True )
    code = fields.Char("Code", required=True)
    materialType = fields.Selection([
        ('fabric', 'Fabric'),
        ('Jeans', 'Jeans'),
        ('Cotton', 'Cotton'),
    ], string='Material Type', required=True )
    
    materialBuy = fields.Integer('Buy Price', required=True)
    relatedSupplier = fields.Selection([
        ('supplier1', 'Supplier 1'),
        ('supplier2', 'Supplier 2'),
        ('supplier3', 'Supplier 3'),
    ], string='Related Supplier', required=True)
    
    @api.constrains('materialBuy')
    def get_material_price(self):
        if self.materialBuy < 100:
             raise ValidationError(("Material Buy tidak boleh kurang dari 100" ))
        else:
            return{}
    


    
    

