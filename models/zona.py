# -*- coding: utf-8 -*-

from odoo import models, fields, api

class zona(models.Model):
    _name = 'zoologico.zona'

    nombre_zona = fields.Char()
    
    #relacion 1 a N con animal
    idanimalesHab=fields.One2many('zoologico.animal','idanimal',string="animales")
    #N A N con zoologico
    idzonazoo=fields.Many2many(string= "zoologico",comodel_name='zoologico.zoologico',relation = 'rel_zona_zoologico',column1='zona', column2='zoologico')
  

