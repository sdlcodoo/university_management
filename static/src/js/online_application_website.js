/** @odoo-module **/

import { jsonrpc } from "@web/core/network/rpc_service";
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.OnlineApplication = publicWidget.Widget.extend({
    selector: '#online_appl_form',
    events: {
        'change select[name="course"]': '_onCourseChange',
        'change select[name="department"]': '_onDepartmentChange',
    },

    _onCourseChange: function (ev) {
        var self = this

        var course = ev.currentTarget.value;
        self.$el.find('select[name="department"]').find('option').remove()
        self.$el.find('select[name="department"]').append("<option value=0></option>");
        jsonrpc(`/get_department_ids/${course}`, {
                course_id: course,
            }).then(function (results) {
                console.log(results)
                for (const item of results) {
                    console.log('item----');
                    console.log(item);
                    self.$el.find('select[name="department"]').append("<option value=" + item['id'] + ">" +item['name'] + "</option>");
                }
            })

    },
    _onDepartmentChange: function (ev) {
        var self = this
        var department = ev.currentTarget.value;
        self.$el.find('select[name="semester"]').find('option').remove()
        self.$el.find('select[name="semester"]').append("<option value=0></option>");
        jsonrpc(`/get_semester_ids/${department}`, {
                department_id: department,
            }).then(function (results) {
                console.log(results)
                for (const item of results) {
                    console.log('item----');
                    console.log(item);
                    self.$el.find('select[name="semester"]').append("<option value=" + item['id'] + ">" +item['name'] + "</option>");
                }
            })

});