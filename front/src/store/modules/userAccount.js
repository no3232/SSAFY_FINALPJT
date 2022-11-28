import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import VueCookies from 'vue-cookies'

const DJANGO_API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

const userAccount = {
  state: {
    // token: null,
    userPk: null,
  },
  getters: {
    userPkGetters(state) {
        return state.userPk
    }
  },
  mutations: {
    // 토큰 저장
    SET_TOKEN(state, token) {
      // state.token = token
      // 쿠키에 토큰을 저장
      // 향후 쓸 때는 this.$cookies.get(test)
      Vue.$cookies.set("token", token.key)
    },
    // 유저 PK저장
    SET_PK(state, userPk){
      state.userPk = userPk
    },
    // 로그아웃
    REMOVE_USER(state) {
      state.userPk = null
    },
  },
  actions: {
    // 회원가입만
    signUp(context, userdata) {
      const username = userdata.username
      const password1 = userdata.password1
      const password2 = userdata.password2
      return axios({
        method: 'post',
        url: `${DJANGO_API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then(res => {
        context.commit('SET_TOKEN', res.data)
      })
      .catch(err => {
        console.log(err.response)
        console.log(err.request)
        alert(err.request.responseText)
        console.log(err.message)
      })
    },
    // 로그인만
    logIn(context, userdata) {
      const username = userdata.username
      const password = userdata.password
      return axios({
        method: 'post',
        url: `${DJANGO_API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then(res => {
        context.commit('SET_TOKEN', res.data)
      })
      .catch(err => {
        alert('유저 정보를 다시 확인해 주세요!')
        console.log(err.response)
        console.log(err.request)
        console.log(err.message)
      })
    },
    // 유저 pk를 state에 저장
    getUserPk(context) {
      const DJANGO_API_URL = 'http://127.0.0.1:8000'
      const key = Vue.$cookies.get("token")
      return axios({
          method: 'get',
          url: `${DJANGO_API_URL}/accounts/user/`,
          headers: {
              Authorization: `Token ${key}`
          }
      })
      .then(res => {
        context.commit('SET_PK', res.data.pk)
      })
      .catch(err => {
          console.log(err.response)
          console.log(err.request)
          console.log(err.message)
      })
    },

    // 로그인, 회원가입 => 유저정보 저장까지 한번에 하기
    async LoginPath (context, userdata) {
      await context.dispatch('logIn', userdata)
      await context.dispatch('getUserPk')
    },
    async SignupPath (context, userdata) {
      await context.dispatch('signUp', userdata)
      await context.dispatch('getUserPk')
    },

    // 로그아웃 기능
    userLogout(context) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/logout/',
        headers: {
          Authorization: `Token ${Vue.$cookies.get("token")}`
        }
      })
      .then((res) => {
        context.commit('REMOVE_USER')
        Vue.$cookies.remove("token")
        alert(res.data.detail)
      })
      .catch(err => {
        console.log(err.response)
        console.log(err.request)
        console.log(err.message)
      })
    }
    
  },
  modules: {
  }
}

export default userAccount