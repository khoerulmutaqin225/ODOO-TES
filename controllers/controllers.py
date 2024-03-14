# -*- coding: utf-8 -*-
from odoo import http, exceptions
from odoo.http import content_disposition, request


class OdooModule(http.Controller):
    @http.route('/odoo_module/odoo_module/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/odoo_module/odoo_module/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('odoo_module.listing', {
            'root': '/odoo_module/odoo_module',
            'objects': http.request.env['odoo_module.odoo_module'].search([]),
        })

    @http.route('/odoo_module/odoo_module/objects/<model("odoo_module.odoo_module"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('odoo_module.object', {
            'object': obj
        })
    

    @http.route('/odoo_module/odoo_module/objects/<model("odoo_module.odoo_module"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('odoo_module.object', {
            'object': obj
        }) 
    # API GET
    @http.route(['/api/get'], auth='public', website=False, csrf=False,  type='json', methods=['GET'])
    def show_material(self, **kw):
        materials = request.env['odoo_module.odoo_module'].sudo().search([('id', '=', kw['id'])])
        material_list = []
        for material in materials:
            material_list.append({
                'id': material.id,
                'name': material.name,
                'code': material.code,
                'materialType': material.materialType,
                'materialBuy': material.materialBuy,
                'relatedSupplier': material.relatedSupplier,
            })
        return material_list
    
    
    # API POST
    @http.route(['/api/post'], auth='public', website=False, csrf=False,  type='json', methods=['POST'])
    def post_material(self,**params):
        name = params.get("name")
        code = params.get("code")
        materialType= params.get("materialType")
        materialBuy= params.get("materialBuy")
        relatedSupplier= params.get("relatedSupplier")
        vals_header = {
            'name': name,
            'code': code,
            'materialType': materialType,
            'materialBuy': materialBuy,
            'materialType': materialType,
            'relatedSupplier': relatedSupplier
        }
        new_material = request.env['odoo_module.odoo_module'].sudo().create(vals_header)
        data = {
            'status' : 200,
            'message' : 'success',
            'vals_header' : vals_header,
        }
        return data
    
    
    # API DELETE
    @http.route(['/api/delete'], auth='public', website=False, csrf=False,  type='json', methods=['DELETE'])
    def delete_material(self, **kw):
        materials = request.env['odoo_module.odoo_module'].sudo().search([('id', '=', kw['id'])])
        if not materials:
            Response = {'status':404, 'body':'Material not found'}
            return Response
        materials.unlink()        
        Response = {'status':204}
        return Response
    

    # API UPDATE
    @http.route(['/api/update'], auth='public', website=False, csrf=False,  type='json', methods=['POST'])
    def update_material(self, **kw):
        materials = http.request.env['odoo_module.odoo_module'].sudo().search([('id', '=', kw['id'])])
        for material in materials:
            materials.write({
                'name': kw.get('name'),
                'code': kw.get('code'),
                'materialType': kw.get('materialType'),
                'materialBuy': kw.get('materialBuy'),
                'materialType': kw.get('materialType'),
                'relatedSupplier': kw.get('relatedSupplier')
            })
        return kw

    # API FILTER materialType
    @http.route(['/api/filter'], auth='public', website=False, csrf=False,  type='json', methods=['GET'])
    def filter_material(self, **kw):
        materials = request.env['odoo_module.odoo_module'].sudo().search([('materialType', '=', kw['materialType'])])
        material_list = []
        for material in materials:
            material_list.append({
                'id': material.id,
                'name': material.name,
                'code': material.code,
                'materialType': material.materialType,
                'materialBuy': material.materialBuy,
                'relatedSupplier': material.relatedSupplier,
            })
        return material_list