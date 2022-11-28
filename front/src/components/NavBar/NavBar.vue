<template>
<div>
  <nav class="navbar navbar-dark fixed-top">
    <div class="container-fluid">
      <div class="nav">
        <a @click="goToHome" class="navbar-brand" id="head">
          <img src="../../assets/logo_transparent.png" height="60px">
        </a>
      </div>
      <div class="nav">
        <button class="navbar-toggler mx-2" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
          <i class="bi bi-search"></i>
        </button>
        <router-link class="nav-link fs-4 ms-2" :to="{ name: 'main'}">Home</router-link>
        <router-link class="nav-link fs-4 ms-2" :to="{ name: 'allmovie'}">AllMovie</router-link>
        <router-link class="nav-link fs-4 ms-2" :to="{ name: 'genre'}">Genre</router-link>
        <router-link class="nav-link fs-4 ms-2" :to="{ name: 'community'}">Reviews</router-link>
        <router-link class="nav-link fs-4 ms-2" :to="{ name: 'login'}" v-show="!isLogin">Login</router-link>
        <a class="nav-link fs-4 ms-2" v-show="$store.getters.userPkGetters" @click="userLogout">Logout</a>
        <router-link class="nav-link fs-4 ms-2" v-show="!$store.getters.userPkGetters" :to="{ name: 'signup'}">Signup</router-link>
        <router-link class="nav-link fs-4 ms-2" v-if="$store.getters.userPkGetters" :to="{ name: 'userinfo', params: { userPk: isLogin } }">UserInfo</router-link>
      </div>
    </div>
  </nav>
  <div class="collapse m-5" id="navbarToggleExternalContent">
    <div class="d-flex justify-content-end p-1">
      <NavBarSearch class="d-flex" />
    </div>
  </div>
</div>
</template>

<script>
import NavBarSearch from '@/components/NavBar/NavBarSearch'

export default {
    name: 'NavBar',
    components: {
      NavBarSearch
    },
    computed: {
      isLogin() {
        return this.$store.getters.userPkGetters
      }
    },
    methods: {
      userLogout() {
        this.$store.dispatch('userLogout')
        this.$router.push({name: 'main'})
      },
      goToHome() {
        return this.$router.push({name:'main'})
      }
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Black+Han+Sans:400');
@import url('https://fonts.googleapis.com/css?family=Black+Han+Sans&display=swap&subset=korean');
  #head{
    font-family: 'Black Han Sans', sans-serif !important;
    color: #C0FD5B;
  }

  .nav-link{
    font-size: large;
    color: white !important
  }
  .nav-link:hover{
    border: 1px solid #2F2519;
    border-radius: 10px;
    background-color: #2F2519;
  }

  .nav-link:focus{
    border: 1px solid #2F2519;
    border-radius: 10px;
    background-color: #2F2519;
  }

  .router-link{
    color: black !important
  }
  .router-link-exact-active {
    color: #FF4301 !important;
    background-color: white;
    border-radius: 10px;
  }
  #navbarToggleExternalContent {
    position: fixed;
    right: 0;
    width: 100%;
    z-index: 10;
  }
  .navbar{
    background-color: #FF4301;
    animation: navfade 5s;
    height:5rem;
  }
  @keyframes navfade {
    from {
      background-color: rgb(143, 38, 38);
    }
    70% {
      background-color: rgb(143, 38, 38);
    }
    to {
      
    }
  }

  .nav-link:hover, 
  a:hover {
  /* Start the shake animation and make the animation last for 0.5 seconds */
  animation: shake 0.5s;

  /* When the animation is finished, start again */
  animation-iteration-count: infinite;
}

@keyframes shake {
  0% { transform: translate(1px, 1px) rotate(0deg); }
  10% { transform: translate(-1px, -2px) rotate(-1deg); }
  20% { transform: translate(-3px, 0px) rotate(1deg); }
  30% { transform: translate(3px, 2px) rotate(0deg); }
  40% { transform: translate(1px, -1px) rotate(1deg); }
  50% { transform: translate(-1px, 2px) rotate(-1deg); }
  60% { transform: translate(-3px, 1px) rotate(0deg); }
  70% { transform: translate(3px, 1px) rotate(-1deg); }
  80% { transform: translate(-1px, -1px) rotate(1deg); }
  90% { transform: translate(1px, 2px) rotate(0deg); }
  100% { transform: translate(1px, -2px) rotate(-1deg); }
}
</style>