# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
	_name = 'my_modulee.wizard'

	""" Para el campo many2one
	session_id = fields.Many2one(
	    'my_modulee.sessions',
	    string='Session Associated',
	    default='_default_session'
	)
	"""

	sessions_ids = fields.Many2many(
	    'my_modulee.sessions',
	    string='Sessions Associated',
	    #default='_default_sessions'
	)

	partner_ids = fields.Many2many(
	    'res.partner',
	    string='Partners Associated',
	)

	"""
	def _default_session(self):
		return self.env['my_modulee.sessions'].browse(self._context.get('active_id'))
	"""
	
	def _default_sessions(self):
		return self.env['my_modulee.sessions'].browse(self._context.get('active_ids'))

	"""
	@api.multi
	def suscribe(self):
		self.session_id.atendees_ids |= self.partner_ids
		return {}
	"""

	#@api.multi
	def suscribe(self):
		for session in self.sessions_ids:
			session.atendees_ids |= self.partner_ids
		return {}