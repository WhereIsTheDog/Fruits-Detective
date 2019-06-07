import Vue from 'vue'
import App from './App.vue'

import ImgInputer from 'vue-img-inputer'
import 'vue-img-inputer/dist/index.css'

Vue.component('ImgInputer', ImgInputer)

Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')
