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


class ResPartner(models.Model):
    """Inherited model for adding two fields to determine
                    whether the partner student or parent"""
    _inherit = 'res.partner'

    is_student = fields.Boolean(string="Is a Student",
                                help="Enable if the partner is a student")
    is_parent = fields.Boolean(string="Is a Parent",
                               help="Enable if the partner is a parent")
