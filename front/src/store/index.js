import Vue from 'vue'
import Vuex from 'vuex'
import userAccount from './modules/userAccount'
import movie from './modules/movie'

// import VueCookies from 'vue-cookies'



Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    userAccount: userAccount,
    movie: movie,
  }
})
