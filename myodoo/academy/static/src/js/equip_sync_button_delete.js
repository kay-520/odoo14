odoo.define('academy_teachers.list_sync_equip_button_delete', function (require) {
    "use strict";
    var ListView = require('web.ListView');
    var viewRegistry = require('web.view_registry');
    var core = require('web.core');
    var  qweb = core.qweb;
    var ListController = require('web.ListController');
    ListController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            // 自定义按钮click事件绑定处理方法
            if (this.$buttons) {
                this.$buttons.on('click', '.o_list_tender_bt_sync_delete', this._sync_equip.bind(this));
            }
        },
        _sync_equip: function () {
            var self = this;
            var records = this.getSelectedIds();
            self._rpc({
                // 数据库名
                model: 'academy.teachers',
                // 方法名
                method: 'sync_delete',
                args: [records]
            },
                []
            );
        }
    });
});
