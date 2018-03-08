# -*- coding: utf-8 -*-

from odoo import models, fields, api

class viaje(models.Model):
    _name = 'concesionario.viaje'
    #relacion con vehiculos uno a muchos
    idvehiculo=fields.Many2one('concesionario.vehiculo',string="vehiculo")
    #relacion con provincia 1 a muchos
    provincia_origen=fields.Many2one('concesionario.provincia',string="provincia origen")
    provincia_destino=fields.Many2one('concesionario.provincia',string="provincia destino")

    fecha_realizacion = fields.Date()
    duracion =fields.Integer()
    masDeDos =fields.Boolean(compute="_value_pc", store=True)

    @api.onchange('duracion')
    def _value_pc(self):
        if( self.duracion > 2 ):
            self.masDeDos = True
        else:
            self.masDeDos = False
