import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'
import MainPageView from '@/views/Main/MainPageView'
import SearchPageView from '@/views/Search/SearchPageView'
import LoginPageView from '@/views/User/LoginPageView'
import SignupPageView from '@/views/User/SignupPageView'
import UserInfoPageView from '@/views/User/UserInfoPageView'
import GenrePageView from '@/views/Genre/GenrePageView'
import FirstSelectMovieView from '@/views/User/FirstSelectMovieView'
import CommunityView from '@/views/Community/CommunityView'
import CommunityCreateView from '@/views/Community/CommunityCreateView'
import CommunityDetailView from '@/views/Community/CommunityDetailView'
import AllMoviePageView from '@/views/AllMovie/AllMoviePageView'
import My404Error from '@/views/My404Error'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainPageView
  },
  {
    path: '/search/:keyword',
    name: 'search',
    component: SearchPageView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupPageView,
    beforeEnter: function(to, from, next) {
      if (store.getters.userPkGetters || Vue.$cookies.get('token')) {
        alert('이미 로그인 되어있으세요!')
        next({ name: 'main' })
      } else {
        next()
      }
    }
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPageView,
    beforeEnter: function(to, from, next) {
      if (store.getters.userPkGetters || Vue.$cookies.get('token')) {
        alert('이미 로그인 되어있으세요!')
        next({ name: 'main' })
      } else {
        next()
      }
    }
  },
  {
    path: '/userinfo/:userPk',
    name: 'userinfo',
    component: UserInfoPageView,
  },
  {
    path: '/genre',
    name: 'genre',
    component: GenrePageView
  },
  {
    path: '/firstselect',
    name: 'firstselect',
    component: FirstSelectMovieView,
    beforeEnter: function(to, from, next) {
      if (store.getters.userPkGetters || Vue.$cookies.get('token')) {
        next()
      } else {
        alert('로그인 하셔야겠는데요?')
        next({ name: 'login'})
      }
    }
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/reviewcreate',
    name: 'communitycreate',
    component: CommunityCreateView,
    beforeEnter: function(to, from, next) {
      if (store.getters.userPkGetters || Vue.$cookies.get('token')) {
        next()
      } else {
        alert('로그인 하셔야겠는데요?')
        next({ name: 'login'})
      }
    }
  },
  {
    path: '/communitydetail/:movieid/:reviewid',
    name: 'communitydetail',
    component: CommunityDetailView
  },
  {
    path: '/allmovie',
    name: 'allmovie',
    component: AllMoviePageView
  },
  {
    path: '*',
    name: '404',
    component: My404Error
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
