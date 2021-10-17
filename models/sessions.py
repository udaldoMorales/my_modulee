# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Sessions(models.Model):
	_name = "my_modulee.sessions"
	_description = "my_modulee.sessions"

	name = fields.Text(
		string='Name'
	)
	start_date = fields.Date(
		string='Start Date',
		default=lambda self: fields.Date.context_today(self)
	)
	duration = fields.Float(
		digits=(6,2),
		string='Duration (days)'
	)
	seats = fields.Integer(
		string='Number of Seats'
	)
	instructor_id = fields.Many2one(
		'res.partner',
		string='Instructor',
		ondelete='set null',
		domain=['|', ('instructor','=',True),'|',('teacher_level1','=',True),('teacher_level2','=',True)]
		#domain=['|',('teacher_level1','=',True),('teacher_level2','=',True)]
	)
	courses_id = fields.Many2one(
		'my_modulee.courses',
		required=True,
		string='Course Id',
	)
	#Many to many
	atendees_ids = fields.Many2many(
		'res.partner',
		string='Attendees',
	)
	#Porcentaje de asientos tomados en comparación a la cantidad de asientos.
	percentage_taken_seats = fields.Float(
		string='Taken Seats Percentage', compute='_compute_taken_seats'
	)
	#Atributo de sesión "activa"
	active = fields.Boolean(string='Active',default=True)

	#Atributo para tener el número de asistentes a una sesión.
	atendees_num = fields.Float(
		string='Number of Attendees',
		compute='_compute_atendees_number',
		store=True
	)

	#This stuff is for the Kanban view
	color = fields.Integer()

	#Computar un campo.
	@api.depends('atendees_ids')
	def _compute_taken_seats(self):
		for record in self:
			if((record.seats is None) or (record.seats <= 0)):
				record.percentage_taken_seats = 0
			else:
				record.percentage_taken_seats = (len(record.atendees_ids)*100)/(record.seats)

	#Computar el número de asistentes a una sesión
	@api.depends('atendees_ids')
	def _compute_atendees_number(self):
		for record in self:
			#if(record.atendees_ids):
			record.atendees_num = len(record.atendees_ids)

	#Cada que se haga un cambio en los campos del registro "self" indicados en el onchange, se va a llamar a este método.
	@api.onchange('atendees_ids','seats')
	def _onchange_percentage_taken_seats(self):
		if (len(self.atendees_ids) > self.seats):
			return {
			'warning': {
			'title': _("That's not possible"),
			'message': _('You cannot have more attendees than seats in a session.')
			}
			}
		elif (self.seats < 0):
			return {
			'warning': {
			'title': _("That's not possible"),
			'message': _('You cannot have a session with less than 0 persons.')
			}
			}

	#Este es un check, pero con Python, no con SQL.
	@api.constrains('instructor_id', 'atendees_ids')
	def _check_method(self):
		for record in self: #Recorrer todos los registros
			if (record.instructor_id in record.atendees_ids):
				raise ValidationError(_('The instructor ') + '%s'%record.instructor_id.name + _(' cannot be in his/her session as an attendee too.'))