# -*- coding: utf-8 -*-
from email.policy import default
from math import trunc

from odoo import models, fields, api
from pkg_resources import require


class examen_repaso(models.Model):
    _name = 'examen_repaso.examen_repaso'
    _description = 'examen_repaso.examen_repaso'

    nombre = fields.Char(string="Nombre",required=True)
    apellidos = fields.Char(string="Apellidos",required=True)
    proyecto = fields.Text(string="Proyecto",required=True)
    tutor = fields.Selection([
        ('diego','Diego Alonso'),
        ('manuelG','Manuel Guimarey'),
        ('manuelA','Manuel Araujo'),
        ('damián','Damián Nogueiras'),
        ('sin','Sin Tutor'),
    ], string="Tutor",default="Sin Tutor")
    horasDia = fields.Integer(string="Horas al día",required=True)
    horasMes = fields.Integer(string="Horas al mes",compute="_compute_horas_mes")

    @api.depends('horasDia')
    def _compute_horas_mes(self):
        for record in self:
            record.horasMes = record.horasDia * 30
