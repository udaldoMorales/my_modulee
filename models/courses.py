# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Courses(models.Model):
	_name = "my_modulee.courses"
	_description = "my_modulee.courses"

	title = fields.Char(string='Title',required=True)
	description = fields.Text(string='Description')
	
	responsible_user_id = fields.Many2one(
		'res.users',
		string='Responsible User',
		ondelete='set null'
	)
	sessions_ids = fields.One2many(
		'my_modulee.sessions',
		'courses_id',
		string='Sessions depending',
	)

	_sql_constraints = [
		('courses_different_title_description', 'CHECK (title != description)', _("Title and description must be differents.")), #Título de curso y descripción deben de ser distintos.
	    ('courses_title_uniq', 'UNIQUE (title)', _("The course name must be unique!")) #Los nombres de curso deben ser únicos.
	]

	#Este método se sobreescribe para cambiar la acción de duplicado en la interfaz
	@api.returns('self', lambda value: value.id)
	#def copy(self, default=None):
	def copy(self, default = {}):
		default['title'] = _("Copy of ")+"%s"%(self.title)
		new = super(Courses, self).copy(default=default) #Courses es el mismo nombre de la clase.
		print("Return: %s"%(new))

		return new