# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class estudiante(models.Model):
     _name = 'academia.estudiante'
     _description = 'Estudiante'
	
     name = fields.Char('Código estudiante',required=True)
     nombre = fields.Char(string='Estudiante',required=True)
     apellidos = fields.Char(string='Apellidos',required=True)
     fecha_nacimiento = fields.Date(string='Fecha de nacimiento',required=True)
     anios = fields.Integer("Años", compute="_get_anios")

     #relaciones
     matriculas_estudiantes_ids = fields.Many2many('academia.matricula',string='Matricula')

     @api.depends('fecha_nacimiento')
     def _get_anios(self):
          for estudiante in self:
               hoy = date.today()
               estudiante.anios = relativedelta(hoy, estudiante.fecha_nacimiento).years


class curso(models.Model):
     _name = 'academia.curso'
     _description = 'Curso'

     name = fields.Char('Código curso',required=True)
     nombre = fields.Char(string='Código curso',required=True)
     numero_examenes = fields.Integer('Número exámenes',required=True)

     #relaciones
     matriculas_cursos_ids = fields.Many2many('academia.matricula',string='Matricula')

	
class examen(models.Model):
     _name = 'academia.examen'
     _description = 'Examen'

     name = fields.Char('Número examen', required=True)
     fecha_examen = fields.Date(string='Fecha examen', required=True)
     nota = fields.Float('Nota examen', default='0')

     #relaciones
     matricula_id = fields.Many2one('academia.matricula',string='Examen')


class matricula(models.Model):
     _name = 'academia.matricula'
     _description = 'Matricula'

     name = fields.Char("Código", required=True)

     #relaciones
     estudiantes_ids = fields.Many2many('academia.estudiante','matriculas_estudiantes_id',string='Estudiante')
     cursos_ids = fields.Many2many('academia.curso','matriculas_cursos_ids',string='Curso')
     examenes_ids = fields.One2many('academia.examen','matricula_id',string='Matricula')

