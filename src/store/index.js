import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        search: '',
        dialog: false
    },
    mutations: {
        //para poder modificar los states
        updateSearch(state, value) {
            state.search = value
        },
        toggleDialog(state, bool) {
            console.log('Coñoooo', state.dialog);
            state.dialog = bool
        }
    },
    actions: {
        //para trabajar directamnete con la api
    },
    modules: {}
})