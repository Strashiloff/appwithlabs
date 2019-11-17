import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import storeConfig from './store/index.js'

Vue.config.productionTip = false
Vue.config.keyCodes.enter = 13
Vue.use(Vuex)

document.addEventListener('DOMContentLoaded', function (event) {
  let store = new Vuex.Store(storeConfig)
  global['store'] = store

  window.vm = new Vue({
    store,
    render: h => h(App)
  }).$mount('#app')

  store.dispatch('ui/setView', 'main')
})
