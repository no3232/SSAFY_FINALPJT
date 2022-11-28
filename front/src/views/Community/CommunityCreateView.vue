<template>
  <div class="container">
    <div style="margin-top: 10vh; color: white;">
      <h1 >리뷰 작성입니다.</h1>
    </div>
    <form @submit.prevent="createReview">
      <div class="form-floating mb-3">
        <input type="text" class="form-control" id="titleInput" placeholder="게시글 제목" v-model.trim="titleInput">
        <label for="titleInput">Title</label>
      </div>
      <div class="form-floating mb-3">
        <input type="text" class="form-control dropdown-toggle" id="titleInput" placeholder="영화" data-bs-toggle="dropdown" aria-expanded="false" v-model.trim="movieInput" @input="seachMovie(movieInput)">
        <label for="titleInput">Movie</label>
        <ul class="dropdown-menu dropdown-menu-dark w-100" aria-labelledby="dropdownMenuButton2">
          <li 
            v-for="movie in movieSelect"
            :key="movie.id"
          >
            <a class="dropdown-item" @click.prevent="titleGo(movie)">{{ movie.title }}</a>
          </li>
        </ul>
      </div>
      <div class="form-floating mb-3">
        <textarea class="form-control" placeholder="내용을 작성하세요" id="contentInput" style="height: 400px" v-model.trim="contentInput"></textarea>
        <label for="contentInput">Content</label>
      </div>
      <input type="submit" class="btn btn-success" value="리뷰 작성!">
    </form>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CommunityCreateView',
    data() {
      return {
        titleInput: null,
        movieInput: null,
        movieId: null,
        contentInput: null,
        movieSelect: this.$store.getters.getAllMovies.slice(0, 5),
      }
    },
    methods: {
      createReview() {
        const DJANGO_API_URL = 'http://127.0.0.1:8000'
        const title = this.titleInput
        const content = this.contentInput
        const moviepk = this.movieId
        const user = this.$store.getters.userPkGetters
        axios({
          method: 'post',
          url: `${DJANGO_API_URL}/api/v1/community/movie/${moviepk}/`,
          data: {
            title, content, user
          }
        })
        .then(res => {
          console.log(res)
          if (res.status === 201) {
            this.$router.push({name: 'communitydetail', params: {
              movieid: this.movieId ,reviewid: res.data.id
            }})
            this.$store.commit('CREATE_REVIEW', res.data)
          }
        })
        .catch(err => {
          console.log(err.request)
          console.log(err.message)
        })
      },
      seachMovie(title) {
        const mlist = this.$store.getters.getAllMovies.filter(el => {
          if (el.title.includes(title)) {
            return el
          }
        })
        this.movieSelect = mlist.slice(0, 5)
      },
      titleGo(movie) {
        this.movieInput = movie.title
        this.movieId = movie.id
      }
    },
    created() {
      console.log(this.$route.params.movieId, this.$route.params.movieTitle)
      if (this.$route.params.movieId && this.$route.params.movieTitle) {
        this.movieInput = this.$route.params.movieTitle
        this.movieId = this.$route.params.movieId
      }
    }
}
</script>

<style>

</style>