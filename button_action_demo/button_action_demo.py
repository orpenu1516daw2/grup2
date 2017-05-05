from openerp import models, fields, api

#Non-odoo library
import random
from random import randint
import string

class button_action_demo(models.Model):
    _name = 'button.demo'
    name = fields.Float()
    milles = fields.Float()
    peus = fields.Float()
    polzades = fields.Float()
    iardes = fields.Float()
    
    


    @api.multi
    @api.depends('name')
    def generate_record_password(self):
	 
	milles = 0.000621371
	peus = 3.28084
	iardes = 1.0936
	polzades = 39.370
	
	
	millesOperation = int(self.name) * milles
	peusOperation = int(self.name) * peus
	iardesOperation = int(self.name) * iardes
	polzadesOperation = int(self.name) * polzades
	self.ensure_one()

	self.write({
	    'milles': millesOperation,
	    'peus': peusOperation,
	    'iardes': iardesOperation,
	    'polzades': polzadesOperation
	})

    @api.multi
    def clear_record_data(self):
	self.ensure_one()
	self.write({
	    'name': '0',
	    'milles': '0',
	    'peus': '0',
	    'iardes': '0',
	    'polzades': '0'
	})
