# -*- coding: utf-8 -*-
###############################################################################
#
#    SDLC Corp Pvt. Ltd.
#
#    Copyright (C) 2024-Today SDLC Corp(<https://www.sdlccorp.com>)
#    Author: Abhishek Ingole (sales@sdldcorp.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import fields, models


class FeeTypes(models.Model):
    """For managing payment method or type of student fees"""
    _name = 'fee.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {'product.product': 'product_id'}
    _description = 'University fees'

    product_id = fields.Many2one('product.product', string='Product',
                                  required=True)
    payment_type = fields.Selection([
        ('onetime', 'One Time'),
        ('permonth', 'Per Month'),
        ('peryear', 'Per Year'),
        ('sixmonth', '6 Months'),
        ('threemonth', '3 Months')],
        string='Payment Type', default='permonth',
        help='Payment type describe how much a payment effective')
    category_id = fields.Many2one('fee.category', string='Category',
                                  help="Category of fee types",
                                  required=True)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=lambda
                                      self: self.env.user.company_id.currency_id.id,
                                  help="Currency of current company")
