# -*- coding: utf-8 -*-

from openerp import models, fields, api


class OperatorFields(models.Model):
    _name = 'operator_fields'
    _description = 'Operadores de Campo'

    name = fields.Char()
