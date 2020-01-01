# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Rulers(models.Model):
    _name = 'rulers'
    _description = 'Rulers'
    _order = 'sequence'

    """
    aqui estara la estructura que se mostrara al usuario en foma de textocom:
    Del modelo: "X", el campo: "Y", es igual a el valor: "Z"
    
    TODO: hay que implemetar una opcion para permitir comparar dos campos de modelos ejemplo:

    """
    name = fields.Char(
        string='Name',
        required=False
    )

    description = fields.Text(
        string="Descripción",
        required=False)

    rulers_generator_id = fields.Many2one(
        comodel_name='rulers_generator',
        string=' rulers_generator_id',
        required=True,
        ondelete='cascade'
    )

    sequence = fields.Integer(
        string='Secuencia',
        default=0,
        required=False
    )