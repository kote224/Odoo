# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class zoologico(models.Model):
    _name = 'zoologico.zoologico'

    nombre = fields.Char()
    ubicacion = fields.Selection(
        selection=[('es', 'espana'), ('al', 'alemania'), ('fr', 'baguette')])
    cap_maxima = fields.Integer()

    idanimales=fields.One2many('zoologico.animal','idanimal',string="animal")

    idzoozona=fields.Many2many(string= "zona",comodel_name='zoologico.zona',relation = 'rel_zoologico_zona',column1='zoologico', column2='zona')
  
    #relacion con conductores n n 
    #idsconductores=fields.Many2many(string= "conductores",comodel_name='concesionario.conductor',relation = 'rel_conductores_vehiculos',column1='vehiculo', column2='conductor')


    #relacion con viajes uno a muchos
    #idsviajes=fields.One2many('concesionario.viaje','idvehiculo',string="viaje")
    #relacion con seguros uno a muchos
    #idseguro=fields.Many2one('base.empresa',string="Seguro")

    #campo computado
    #fecha_revision = fields.Date(compute="comprobar", store=True)

   # @api.onchange('cap_maxima')
    #def comprobar(self):
     #   fechaActual=datetime.now()
      #  if( self.cap_maxima > 4):
       #     self.fecha_revision = fechaActual + timedelta(days=1500)
