# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Rulers(models.Model):
    _name = 'rulers'
    _description = 'Rulers'
    _order = 'sequence'

    """
    En el campo name estará la estructura que se mostrará al usuario 
    en forma de texto com:
    Del modelo: "X", el campo: "Y", es igual a el valor: "Z"
    
    TODO: hay que implementar una opción para permitir 
    comparar dos campos de modelos ejemplo:

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
        string='Rulers_Generator_id',
        required=True,
        ondelete='cascade'
    )

    sequence = fields.Integer(
        string='Secuencia',
        default=0,
        required=False
    )

    rule_model = fields.Many2one(
        comodel_name='ir.model',
        string='Rule_model',
        required=False)

    rule_field = fields.Many2one(
        comodel_name='ir.model.fields',
        string='Rule_field',
        required=False)

    rule_operator = fields.Many2one(
        comodel_name='operators',
        string='operator_fields',
        required=False)

    # @api.multi
    # def create_rule(self):
    #     pass
    #
    # @api.multi
    # def edit_rule(self):
    #     pass
