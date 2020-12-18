odoo.define('custom_page.demo', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');

    var CustomPageDemo = AbstractAction.extend({
        template: 'DemoPage',
        events: {'click .oe_assess_commit': 'onSubmitClick'},

        onSubmitClick: function () {
            var self = this;
            console.log('cal data！！！！！！');

            var start_date = document.getElementsByName('start_date')[0].value
            var end_date = document.getElementsByName('end_date')[0].value
            if (start_date != '' && end_date != '') {
                this._rpc({
                    model: 'academy_teachers',
                    method: 'creat_teacher',
                    args: [start_date, end_date]
                }).then(function () {
                    location.reload();
                });
            } else {
                alert('请填写开始和结束日期');
            }
        }
    });

    core.action_registry.add('custom_page.demo', CustomPageDemo);

    return CustomPageDemo;

});
