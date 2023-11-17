# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
    # Estandar: Nombre del modelo y el nombre de la clase
    _name = 'custom_crm.visit'
    _description = 'visit'

    # Campos
    name = fields.Char(string="Description")
    customer = fields.Char(string="Customer")
    # DateTime: Almacenado la fecha y la hora
    date = fields.Datetime(string="Date")
    type = fields.Selection([('P', 'Presencial'), ('V', 'Virtual')], string="Type", required=True)
    done = fields.Boolean(string="Done", readonly=True)

