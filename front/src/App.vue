<template>
  <div id="app">
    <NavBar />
    <!-- 슬라이드 트랜지션 -->
    <div style="margin-top: 80px; min-height: 100vh;">
      <transition  mode="out-in">
      <router-view style=""/>
      </transition>
    </div>
    
    <FooterFoot/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar/NavBar.vue'
import FooterFoot from '@/components/FooterFoot/FooterFoot.vue'

export default {
    name: 'App',
    components: {
      NavBar,
      FooterFoot,
    },
    created() {
        this.$store.dispatch('getMovieList')
        if (this.$cookies.get('token')) {
          this.$store.dispatch('getUserPk')
        }
    },
}
</script>

<style>
@font-face {
    font-family: 'LINESeedKR-Bd';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/LINESeedKR-Bd.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
}
#app {
  font-family: 'LINESeedKR-Bd', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: unset;
  color: black;
  background-color: #130f0a;
  z-index: 0;
}

/* 슬라이드 페이드 */
.v-enter-active {
  transition: all 1.5s ease;
}
.v-leave-active {
  transition: all 1.5s ease;
}
.v-enter{
  opacity: 0;
} 
.v-leave-to {
  opacity: 0;
}

body::-webkit-scrollbar{
  display: none;
}
body{
  background-color: #130f0a !important;
}
</style>
