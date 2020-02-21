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


class RulerWizard(models.TransientModel):
    _name = 'ruler.wizard'
    _description = 'Ruler Wizard'
    _inherit = 'rulers'

    @api.depends('ruler_field')
    def _compute_fields_type(self):
        if self.ruler_field:
            self.fields_type = self.ruler_field.ttype

    @api.onchange('ruler_field')
    def onchange_method(self):

        if self.fields_type:
            self.fields_type = self.ruler_field.ttype

        if self.fields_type in ['selection', 'many2many', 'many2one']:
            self.many2many_value = False

            transient_ids = []

            if self.fields_type == 'selection':
                ruler_model = self.ruler_model.model
                ruler_field = self.ruler_field.name

                selection_values = self.env[ruler_model]._fields[ruler_field].selection

                for value in selection_values:
                    key_id = value[0]
                    name = value[1]

                    transient = self.env['transient.selection'].create(
                        {
                            'name': name,
                            'key_id': key_id,
                        }
                    )

                    transient_ids.append(transient.id)
            else:

                model_id = self.ruler_field.relation  # esto es el modelo
                records = self.env[model_id].search([])

                for record in records:
                    transient = self.env['transient.selection'].create(
                        {
                            'name': record.name,
                            'model_id': record.id,
                        }
                    )

                    transient_ids.append(transient.id)

            return {'domain': {'many2many_value': [('id', 'in', transient_ids)]}}

    @api.multi
    def create_ruler(self):

        context = self.env.context
        ruler_generator_id = self.ruler_generator_id

        if context and ruler_generator_id:
            self.env['rulers'].create(
                {
                    'name': "Temp Name!!",
                    'generator_id': ruler_generator_id,
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
                    'many2many_value': self.many2many_value,
                }
            )
            return True
        return False
