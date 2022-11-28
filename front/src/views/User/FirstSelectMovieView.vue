<template>
  <div class="container text-center">
    <br>
    <br>
    <br>
    <h1 style="color:white;">좋아하시는 영화를 선택 해주세요!</h1>
    <div class="container">
      <div class="btn-group mt-3 mb-3" role="group" aria-label="Basic mixed styles example">
        <button type="button" class="btn btn-danger btngroup" @click="updateSelect(1)">뒤로!</button>
        <button type="button" class="btn btn-warning btngroup" @click="updateSelect(2)">다음으로!</button>
        <button type="button" class="btn btn-success btngroup" @click="likeMovieEnd">선택완료!</button>
      </div>
      <h2 style="color:white;">선택된 영화</h2>
        <FirstSelectScroll 
          :selected=selectedShow
          @movieId="selectMovie"
        />
        <div class="row">
            <transition-group name="flip" mode="flip" class="row">
            <FirstSignCard 
              :class="{ 'is-first-clicked' : isSelcted(movie.id) }"
              v-for="movie in allMovieList"
              :key = movie.id
              :movie = movie
              @movieId="selectMovie"
            />
            </transition-group>
        </div>
    </div>
  </div>
</template>

<script>
import FirstSignCard from '@/components/FirstSign/FirstSignCard.vue'
import FirstSelectScroll from '@/components/FirstSign/FirstSelectScroll.vue'
import axios from 'axios'

export default {
    name: 'FirstSelectMovieView',
    components: {
      FirstSignCard,
      FirstSelectScroll,
    },
    data() {
      return {
        selected: [],
        selectedShow: [],
        nums: 8
      }
    },
    computed: {
        allMovieList() {
            return this.$store.getters.selectMovieCutting
        },
    },
    methods: {
      updateSelect(fb) {
        if (fb === 1 && this.nums !== 8) {
          this.nums -= 8
          this.$store.commit('GET_FIRST_SELECT', this.nums)
        } else if (fb===2) {
          this.nums += 8
          this.$store.commit('GET_FIRST_SELECT', this.nums)
        }
      },
      selectMovie(movie) {
        if (this.selected.includes(movie.id)) {
          this.selected = this.selected.filter(el => {
            if (el !== movie.id) {
              return el
            }
          })
          this.selectedShow = this.selectedShow.filter(el => {
            if (el.id !== movie.id) {
              return el
            }
          })
        } else {
          this.selected.push(movie.id)
          this.selectedShow.push(movie)
        }
      },
      likeMovieEnd() {
        const likemovies = this.selected
        const DJANGO_API_URL = 'http://127.0.0.1:8000'
        axios({
            method: 'post',
            url: `${DJANGO_API_URL}/api/accounts/user/${this.$store.getters.userPkGetters}/likemovies/`,
            data: {
                likemovies
            },
        })
        .then(() => {
          this.$router.push({name: 'main'})
        })
        .catch(err => {
            console.log(err.response)
            console.log(err.request)
            console.log(err.message)
        })
      },
      isSelcted(id) {
        return this.selected.includes(id)
      }
    },
}
</script>

<style>
.is-first-clicked{
  opacity: 0.2 !important;
  transition: all 0.3s ease-in-out
}
#FirstSigncard {
  opacity: 1;
  transition: all 0.3s ease-in-out
}
.btngroup {
  background-color: #FF4301;
}
</style>