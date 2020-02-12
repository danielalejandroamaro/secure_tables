# -*- coding: utf-8 -*-

from openerp import models, fields, api


class RulersGenerator(models.Model):
    _name = 'rulers_generator'
    _description = 'Main view'

    name = fields.Char(
        string='Nombre',
        required=False
    )

    description = fields.Text(
        string="Descripción",
        required=False
    )

    rulers = fields.One2many(
        comodel_name='rulers',
        inverse_name='rulers_generator_id',
        string='Reglas',
        required=False
    )

    @api.multi
    def add_rule(self):

        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'rulers',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_rulers_generator_id': self.id},
            'nodestroy': True,
        }

    @api.multi
    def add_operator(self):
        pass
