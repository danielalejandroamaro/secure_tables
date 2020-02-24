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
    sequence = fields.Integer(
        string='Secuencia',
        default=0,
        required=True,
    )

    name = fields.Char(
        string='Name',
        required=True,
    )

    description = fields.Text(
        string="Descripción",
        required=False,
    )

    ruler_generator_id = fields.Many2one(
        comodel_name='rulers.generator',
        string='Rulers Generator id',
        required=True,
        ondelete='cascade',
    )

    ruler_type = fields.Selection(
        string='Rule_type',
        selection=[('ruler', 'Regla'),
                   ('operator', 'Operador'), ],
        required=True,
    )

    fields_type = fields.Char(
        compute='_compute_fields_type',
        store=True,
    )

    ruler_model = fields.Many2one(
        comodel_name='ir.model',
        # string='Rule_model',
        required=True
    )

    ruler_field = fields.Many2one(
        comodel_name='ir.model.fields',
        string='Rule_field',
        required=True,
    )

    logical_operator = fields.Many2one(
        comodel_name='logical.operators',
        string='logical_operator',
        required=True
    )

    date_value = fields.Date(
        string='Date',
        required=False,
    )

    date_time_value = fields.Datetime(
        string='Date_time_value',
        required=False,
    )

    integer_value = fields.Integer(
        string='integer_value',
        required=False,
    )

    bool_value = fields.Boolean(
        string='Bool_value',
        required=False,
    )

    char_value = fields.Char(
        string='Char_value',
        required=False,
    )

    float_value = fields.Float(
        string='Float_value',
        required=False,
    )

    # este campo es para los many2one, many2many y selection
    many2many_value = fields.Many2many(
        comodel_name='transient.selection',
        string='Many2many_value',
    )

    @api.multi
    def edit(self):
        fields_type = self.fields_type.encode('ascii', 'ignore')
        #
        # ruler_values = {
        #     'date': self.date_value,
        #     'datetime': self.date_time_value,
        #     'integer': self.integer_value,
        #     'boolean': self.bool_value,
        #     'char': self.char_value,
        #     'float': self.float_value,
        #     'monetary': self.date_value,
        #     'many2many': self.date_value,
        #     'many2one': self.many2many_value,
        #     'selection': self.many2many_value,
        # }
        #
        # ruler_value = ruler_values[fields_type]

        #     if fields_type == 'date':
        #         ruler["date_value"] = self.date_value
        #
        #     elif fields_type == 'datetime':
        #         ruler["date_time_value"] = self.date_time_value
        #
        #     elif fields_type == 'integer':
        #         ruler["integer_value"] = self.integer_value
        #
        #     elif fields_type == 'boolean':
        #         ruler["bool_value"] = self.bool_value
        #
        #     elif fields_type == 'char':
        #         ruler["char_value"] = self.char_value
        #
        #     elif fields_type in ['float', 'monetary']:
        #         ruler["float_value"] = self.float_value
        #
        #     elif fields_type in [' many2many', 'many2one']:
        #         ruler["many2many_value"] = self.many2many_value
        # else:
        #     return False

        ruler_wizard = self.env['ruler.wizard'].create(
            {
                'name': "Temp Name!!",
                'generator_id': self.ruler_generator_id.id,
                'ruler_model': self.ruler_model.id,
                'ruler_field': self.ruler_field.id,
                'ruler_type': self.ruler_type,
                'logical_operator': self.logical_operator.id,
                'fields_type': self.fields_type,
                'date_value': self.date_value,
                'integer_value': self.integer_value,
                'bool_value': self.bool_value,
                'char_value': self.char_value,
                'float_value': self.float_value,
                'many2many_value': self.many2many_value.ids,
            }
        )

        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'rule.wizard',
            'res_id': ruler_wizard.id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_ruler_wizard': self.id, },
            'nodestroy': True,
        }


class TransientSelection(models.TransientModel):
    _name = 'transient.selection'
    _description = 'Transient Selection'

    name = fields.Char(
        string='Nombre',
    )

    model_id = fields.Integer(
        string='Model_id',
        required=False,
    )

    key_id = fields.Char(
        string='Key_id',
        required=False,
    )