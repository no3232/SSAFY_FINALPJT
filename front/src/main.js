import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import VueCookies from "vue-cookies"
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'
import "bootstrap-icons/font/bootstrap-icons.css";

//  로그인 상태 저장을 위해 쿠키를 사용
Vue.use(VueCookies);
Vue.$cookies.config("1d")

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
