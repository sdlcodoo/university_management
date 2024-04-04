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
{
    'name': ' University Management',
    'version': '17.0.1.0.0',
    'category': 'Industries',
    'summary': """This modules helps to manage the university 
     education system""",
    'description': """This module serves as a comprehensive solution for
     efficiently managing the education system of a university enhancing
     its overall functionality and user experience.""",
    'author': 'SDLC Corp',
    'company': 'SDLC Corp',
    'maintainer': 'SDLC Corp',
    'website': 'https://www.sdlccorp.com',
    'depends': ['mail', 'hr_recruitment', 'account', 'website'],
    'data': [
        'security/university_management_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/online_application_menu_data.xml',
        'data/mail_template_data.xml',
        'wizard/application_reject_views.xml',
        'views/university_management_menus.xml',
        'views/res_partner_views.xml',
        'views/fee_category_views.xml',
        'views/account_journal_views.xml',
        'views/fee_types_views.xml',
        'views/fee_structure_views.xml',
        # 'views/account_move_views.xml',
        'views/timetable_period_views.xml',
        'views/university_exam_type_views.xml',
        'views/university_exam_views.xml',
        'views/exam_valuation_views.xml',
        'views/exam_result_views.xml',
        'views/university_timetable_views.xml',
        'views/timetable_schedule_line_views.xml',
        'views/university_application_views.xml',
        'views/university_attendace_views.xml',
        'views/university_attendance_line_views.xml',
        'views/university_student_views.xml',
        'views/university_document_type_views.xml',
        'views/university_document_views.xml',
        'views/reject_reason_views.xml',
        'views/university_course_views.xml',
        'views/university_department_views.xml',
        'views/university_subject_views.xml',
        'views/university_semester_views.xml',
        'views/university_syllabus_views.xml',
        'views/university_academic_year_views.xml',
        'views/university_batch_views.xml',
        'views/university_faculty_views.xml',
        'views/student_portal_templates.xml',
        'views/online_application_templates.xml',
    ],
    'demo': ['demo/university_management_demo.xml'],
    'assets': {
        'web.assets_frontend': [
            '/university_management/static/src/js/online_application_website.js'
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
