import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import vuetify from './plugins/vuetify';
import '@babel/polyfill'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)
Vue.use({
    install(Vue) {
        Vue.prototype.$mokeServices = {
            getTables() {
                return ['table1', 'table2', 'table3']
            },
            getDefinitions() {
                return [
                    { 'id': 1, 'table_name': 'table1', 'method': 'GET', 'groups': 'admin', 'is_active': false, 'locked': true },
                    { 'id': 2, 'table_name': 'table1', 'method': 'POST', 'groups': 'admin', 'is_active': true, 'locked': true },
                    { 'id': 3, 'table_name': 'table1', 'method': 'PUT', 'groups': '', 'is_active': true, 'locked': false },
                    { 'id': 4, 'table_name': 'table1', 'method': 'DELETE', 'groups': 'admin', 'is_active': true, 'locked': false },
                    { 'id': 5, 'table_name': 'table1', 'method': 'GET', 'groups': 'agent', 'is_active': true, 'locked': false },
                    { 'id': 6, 'table_name': 'table2', 'method': 'GET', 'groups': '', 'is_active': true, 'locked': false },
                    { 'id': 7, 'table_name': 'table2', 'method': 'DELETE', 'groups': 'agent', 'is_active': false, 'locked': true },
                    { 'id': 8, 'table_name': 'table2', 'method': 'PUT', 'groups': 'admin', 'is_active': true, 'locked': true },
                    { 'id': 9, 'table_name': 'table3', 'method': 'GET', 'groups': 'agent', 'is_active': false, 'locked': false },
                    { 'id': 10, 'table_name': 'table3', 'method': 'POST', 'groups': 'admin', 'is_active': false, 'locked': true },
                    { 'id': 11, 'table_name': 'table3', 'method': 'POST', 'groups': 'agent', 'is_active': true, 'locked': false },
                    { 'id': 12, 'table_name': 'table3', 'method': 'DELETE', 'groups': '', 'is_active': true, 'locked': false }
                ]
            }
        }
    }
})

new Vue({
    router,
    axios,
    vuetify,
    render: h => h(App)
}).$mount('#app')