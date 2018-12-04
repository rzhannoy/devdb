import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'
import utils from './utils'

import Buefy from 'buefy'
import VeeValidate from 'vee-validate'
import Toasted from 'vue-toasted'

import appMixin from './mixins/appMixin'

Vue.config.productionTip = false
Vue.prototype.$utils = utils

Vue.use(Buefy)
Vue.use(VeeValidate, { events: 'blur' })

const fullWidth = window.innerWidth < 768
Vue.use(Toasted, {
  position: 'top-center',
  singleton: true,
  duration: 3000,
  fullWidth,
})

Vue.mixin(appMixin)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
