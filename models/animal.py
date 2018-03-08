# -*- coding: utf-8 -*-

from odoo import models, fields, api

class animal (models.Model):
    _name = 'zoologico.animal'
    _inherit = 'base.entidad'

    name = fields.Char()
    cod_animal = fields.Char()
    #relacion con vehiculos n n
    #idsvehiculos=fields.Many2many(string= "vehiculos",comodel_name='concesionario.vehiculo',relation = 'rel_conductores_vehiculos',column1='conductor', column2='vehiculo')
    idanimal=fields.Many2one('zoologico.zoologico',string="Zoo")
    idanimalHab=fields.Many2one('zoologico.zona',string="Zona")
