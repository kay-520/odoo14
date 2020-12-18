//小模块系统，需要首先加载该文件
odoo.define('academy_teachers.list_sync_equip_button_create', function (require) {
    "use strict";
    // web客户端，可以在其中查看和编辑业务数据，它的职责是协调所有的子组件
    var ListView = require('web.ListView');
    var viewRegistry = require('web.view_registry');
    var core = require('web.core');
    var qweb = core.qweb;
    var ajax = require('web.ajax');
    var ListController = require('web.ListController');
    // include方法修改现有的类, extend 方法是在原来的基础上进行扩展
    var ContactListController  = ListController.include({
        // template: 'DemoAge',
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            // 自定义按钮click事件绑定处理方法, 结合.o_list_tender_bt_sync_equip的类标签绑定点击事件
            if (this.$buttons) {
                //这⾥找到刚才定义的class名为create_by_xf的按钮
                var btn = this.$buttons.find('.o_list_tender_bt_sync_equip');
                //给按钮绑定click事件和⽅法create_data_by_dept
                btn.on('click', this.proxy('_sync_equip'));
                // this.$buttons.on('click', '.o_list_tender_bt_sync_equip', this._sync_equip.bind(this));
            }
        },
        _sync_equip: function () {
            var self = this;
            var records = this.getSelectedIds();
            // var state = self.model.get(self.handle, {raw: true});
            //
            // var context = state.getContext()
            //
            // context['type'] = 'in_invoice'
            // console.log('create makeup apply！！！！！！');
            self._rpc({
                model: "reload.teachers",
                method: "creat_teacher",
                args: [records],
            }).then(function (view_id, context) {
                // 打开form视图
                self.do_action({
                    name: '教师de详情',
                    type: 'ir.actions.act_window',  //动作类型
                    target: 'current',  // 打开方式,
                    // res_id: self.res_id,
                    res_model: 'reload.teachers',  //视图的model
                    // view_id: view_id,  //新视图的id
                    context: context,
                    views: [
                        [view_id[1], 'form']
                    ],
                    // flags: {initial_mode: view,action_buttons:false},  //target: ‘new‘弹出框默认为编辑模式，需要只读模式的可以加上这句
                    flags: {'form':{'action_buttons':true, 'options':{'mode':'edit'}}},
                    view_mode: 'form',
                }).then(function (){
                    console.log('显示新视图');
                    console.log(self);
                });

            })




        }
    });

    // add方法对动作进行注册，第一个参数表示注册的动作名，第二个参数是要注册的动作对象；
    core.action_registry.add('academy_teachers.list_sync_equip_button_create', ContactListController);
    return ContactListController;


});
// 定义模块的另一种方法是在第二个参数中明确给出依赖项的列表
// odoo.define('module.Something', ['module.A', 'module.B'], function (require) {
//     "use strict";
//
//     var A = require('module.A');
//     var B = require('module.B');
//
//     // some code
// });


