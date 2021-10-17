# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
	_inherit = 'res.partner'
	
	instructor = fields.Boolean(string='Is instructor')
	sessions_ids = fields.Many2many('my_modulee.sessions',string='Sessions by Partner')
	#Nuevas categorías
	teacher_level1 = fields.Boolean(string='Is Teacher / Level 1')
	teacher_level2 = fields.Boolean(string='Is Teacher / Level 2')