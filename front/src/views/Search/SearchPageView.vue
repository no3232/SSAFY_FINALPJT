<template>
  <div>
    <div class="container">
        <div class="row">
            <MyCard 
            v-for="movie in searchMovieList"
            :key = movie.id
            :movie = movie
            />
        </div>
    </div>
  </div>
</template>

<script>
import MyCard from '@/components/MyCard'
import axios from 'axios'
export default {
    name: 'SearchPageView',
    components: {
        MyCard
    },
    data() {
      return {
        searchMovieList: [],
        searchMovieKeyword: this.$route.params.keyword
      }
    },
    methods: {
      searchMovie(searchMovieKeyword) {
        const keyword = searchMovieKeyword
        const TMDB_API_KEY = process.env.VUE_APP_TMDBKEY
        const API_URL =`https://api.themoviedb.org/3/search/movie?api_key=${TMDB_API_KEY}&language=ko-KR&query=${keyword}&page=1&include_adult=false`
        axios({
          method: 'get',
          url: API_URL
        })
          .then(res => {
            this.searchMovieList = res.data.results
          })
          .catch(err => console.log(err))
      },
      searchMovieVue(searchMovieKeyword) {
        const sList = this.$store.getters.getAllMovies.filter(el => {
          if (el.title.includes(searchMovieKeyword)) {
            return el
          }
        })
        this.searchMovieList = sList.sort((a, b) => {
          if (a.vote_average < b.vote_average) {
            return 1
          }
          if (a.vote_average > b.vote_average) {
            return -1
          }
          return 0
        })
      }
    },
    watch: {
      searchMovieKeyword (value, oldValue) {
        oldValue
        this.searchMovieVue(value)
      }
    },
    created() {
      this.searchMovieVue(this.$route.params.keyword || this.searchMovieKeyword)
    },
    beforeRouteUpdate(to, from, next) {
      console.log(to.params.keyword)
      this.searchMovieKeyword = to.params.keyword
      next()
    }
}
</script>

<style>

</style>