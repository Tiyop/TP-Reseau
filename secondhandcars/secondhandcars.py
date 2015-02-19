# -*- coding: utf-8 -*-
##############################################################################
#
#    Second Hand Cars module for OpenERP
#    Copyright (C) 2013 Guillaume RIVIERE.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
import time

class secondhandcars_brand(osv.osv):
    """ Brand of cars """
    _name = "secondhandcars.brand"
    _description = "Brands of cars"
    _columns = {
        'id' : 
        'name': fields.char('Brand name', size=64, required=True),
        'web_siteI' : fields.char('International Web Site', size=128, required=True),
        'web_siteL' : fields.char('Local Web Site', size=128, required=True),
        'web_siteM' : fields.char('Models Web Page', size=128, required=True),
    }
    _sql_constraints = [
        ('name', 'unique(name)', 'The name of the brand must be unique')
    ]
    _order = 'name asc'

class secondhandcars_model(osv.osv):

    _name = "secondhandcars_model"
    _description = "Models of cars"
    _columns = {
        'name': fields.char('Model name', size=64, required=True),
        'brand_id' : fields.int('Identifiant de la marque', size=128, required=True),
        'last_year' : fields.int('Derniere annee de production', size=128, required=True),
    }

