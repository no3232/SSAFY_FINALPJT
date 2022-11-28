<template>
  <div style="d-flex align-items-center">
    <div id="background-genre" :style="{ backgroundImage: 'url(' + require(`@/assets/genre/${backgroundImages}.png`)+')'}" ></div>
        <MovieCartegory />
        <div class="circ" v-show="!this.$store.getters.genreSelectListgetters">
          <div class="load">Loading . . . </div>
          <div class="hands"></div>
          <div class="body"></div>
          <div class="head">
            <div class="eye"></div>
          </div>
        </div>
        <div class="container ">
            <div class="row">
                <transition-group name="group" mode="out-in" class="row">
                <MyCard 
                v-for="movie in allMovieList"
                :key = movie.id
                :movie = movie
                />
                </transition-group>
            </div>
        </div>
  </div>
</template>

<script>
import MyCard from '@/components/MyCard'
import MovieCartegory from '@/components/Genre/MovieCartegory'

export default {
    name: 'GenrePageView',
    components: {
        MyCard,
        MovieCartegory,
    },
    data() {
      return {
      }
    },
    computed: {
        allMovieList() {
            return this.$store.getters.movieListCutting
        },
        backgroundImages() {
            return this.$store.getters.backgroundGetters
        }
    },
}
</script>

<style>
.group-enter-active {
  transition: all 1s ease;
  transition-delay: 1s;
}
.group-leave-active {
  transition: all 1s ease;
}
.group-enter{
  opacity: 0;
} 
.group-leave-to {
  opacity: 0;
}
#background-genre{
    position: fixed;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    transition: background-image 0.5s;
    background-position: 0% 0%;
    background-size: 100vw 1920px ;
}

/* 로딩 */
.eye{
  width: 20px; height: 8px;
  background-color: rgba(240,220,220,1);
  border-radius:0px 0px 20px 20px;
  position: relative;
  left: 10px; top: 40px;
  box-shadow:  40px 0px 0px 0px rgb(255, 255, 255);              
}

.head{
  backface-visibility: hidden;
  position: relative;
  margin: -250px auto;
  width: 80px; height: 80px;
  background-color: #111;
  border-radius:50px;
  box-shadow: inset -4px 2px 0px 0px rgb(255, 255, 255);
  animation:headAnim 1.5s infinite alternate;
  animation-timing-function:ease-out;
}

.body{ 
  position: relative;
  margin: 90px auto;
  width: 140px; height: 120px;
  background-color: #111;
  border-radius: 50px/25px ;
  box-shadow: inset -5px 2px 0px 0px rgb(255, 255, 255);
  animation:bodyAnim 1.5s infinite alternate;
  animation-timing-function:ease-out;  
}

  @keyframes headAnim{
         0%{ top:0px; }
         50%{ top:10px; }
         100% { top:0px;} 
  }

  @keyframes bodyAnim{
         0%{ top:-5px; }
         50%{ top:10px; }
         100% { top:-5px;} 
  }

.circ{
  backface-visibility: hidden;
  margin: 60px auto;
  width: 180px; height: 180px;
  background-color: #111;
  border-radius: 0px 0px 50px 50px;
  position: relative;
  z-index: -1;  
  left: 0%; top: 20%;
  overflow: hidden;
}

.hands{
  backface-visibility: hidden;
  margin-top: 140px;
  width: 120px;height: 120px;
  position: absolute;
  background-color: #111;
  border-radius:20px;
  box-shadow:-1px -4px 0px 0px rgb(255, 255, 255);
  transform:rotate(45deg);
  top:75%;left: 16%;
  z-index: 1;
  animation:bodyAnim 1.5s infinite alternate;
  animation-timing-function:ease-out;
}

.load{  
  position: absolute;
  width: 7ch; height: 32px;
  text-align: left;
  line-height: 32px;
  margin: -10px auto;
  font-smoothing: antialiased;
  font-family: 'Julius Sans One', sans-serif;
  font-size:28px;
  font-weight:400;
  color:rgb(255, 255, 255);
  left: 2%; top: 5%;
  animation:fontAnim 3.75s infinite;
  animation-timing-function:ease-out;
  word-wrap: break-word;
  display:block;
  overflow: hidden;
}

  @keyframes fontAnim{
        0%{ width:7ch; }
       16%{ width:8ch; }
       32%{ width:9ch; }
       48%{ width:10ch; }
       64%{ width:11ch; }
       80%{ width:12ch; }
     100% { width:13ch;} 
  }
</style>