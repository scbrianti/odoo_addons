# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Smile (<http://www.smile.fr>). All Rights Reserved
#                       author cyril.gaspard@smile.fr
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import orm, fields


class PaymentTermsPartner(orm.Model):
    _inherit = 'payment.terms.partner'

    _columns = {
        'property_account_journal': fields.property('account.journal', type='many2one', relation='account.journal',
                                                    domain=[('type', 'in', ['bank', 'cash'])],
                                                    string="Account journal", view_load=True,
                                                    help="Define the account journal associated to this payment type"
                                                    " for the logued company"),
        'code': fields.char('Code', size=8),
    }