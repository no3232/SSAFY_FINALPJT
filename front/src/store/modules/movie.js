import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'
// import VueCookies from 'vue-cookies'

const DJANGO_API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

const movie = {
  state: {
    movieList: [],
    orderMovieList: [],
    orderMovieListPage: [],
    movieVoteAvgList: [],
    movieVoteCntList: [],
    genreSelectList: [],
    firstSelectList: [],
    likeMovieList: [],
    userReviewList: [],
    backgroundImg: '0',
    reviewId: []
  },
  getters: {
      getAllMovies(state) {
        return state.movieList
      },
      selectMovieCutting(state) {
        return state.firstSelectList
      },
      movieListCutting: (state) => {
        return _.sampleSize(state.genreSelectList, 20)
      },
      movieVoteAvgListCutting: (state) => {
        const avglist = state.movieList.filter((movie)=> {
          if (state.movieVoteAvgList.includes(movie.id)) {
            return movie
          }
        })
        return _.sampleSize(avglist, 12)
      },
      movieVoteCntListCutting: (state) => {
        const avgCnt = state.movieList.filter((movie) => {
          if (state.movieVoteCntList.includes(movie.id)){
            return movie
          }
        })
        return _.sampleSize(avgCnt, 12)
      },
      moviesLikeListGetters: (state) => {
        const likedmovie = state.movieList.filter((movie) => {
          if (state.likeMovieList.includes(movie.id)){
              return movie
          }
        })
        return likedmovie
      },
      genreSelectListgetters: (state) => {
        return state.genreSelectList
      },
      backgroundGetters(state) {
        return state.backgroundImg
      },
      orderMovieGetters(state) {
        return state.orderMovieListPage
      },
      orderAllMovieGetters(state) {
        return state.orderMovieList
      },
      getReviewMovie(state) {
        const rMovie = state.movieList.filter((movie) => {
          if (state.reviewId === movie.id){
            console.log(movie)
            return movie
          }
        })
        console.log(rMovie)
        return rMovie[0]
      }
  },
  mutations: {
      GET_MOVIE_LIST(state, payload) {
        state.movieList = payload
        state.genreSelectList = payload
      },
      GET_VOTE_AVG_MOVIE_LIST(state, payload) {
        state.movieVoteAvgList = payload
      },
      GET_VOTE_CNT_MOVIE_LIST(state, payload) {
        state.movieVoteCntList = payload
      },
      GET_LIKE_MOVIE_LIST(state, payload) {
        state.likeMovieList = payload
      },
      SELECT_GENRE(state, genreId) {
        if (genreId !== 0) {
          state.genreSelectList = state.movieList.filter((el) => {
            let isGenre = false
            el.genres.forEach(genre => {
              if (genre.id === genreId) {
                isGenre = true
              }
            })
            if (isGenre) {
              return el
            }
        })
        } else {
          state.genreSelectList = _.sampleSize(state.movieList, 20)
        }
      },
      BG_GET(state, genreId) {
        state.backgroundImg = genreId
      },
      GET_FIRST_SELECT(state, nums) {
        state.firstSelectList = state.movieList.slice(nums-8, nums)
      },
      TO_LIKING(state, payload) {
        // movie의 like_users 에 추가하거나 빼려는 작업
        state.movieList.forEach((movie) => {
          if (movie.id == payload.moviePk){
            // console.log(12323534252)
            if (movie.like_users.includes(payload.userPk)){
              movie.like_users = movie.like_users.filter((el)=> {
                if (el !== payload.userPk) {
                  return el 
                }
              })
              console.log(movie)
            }else{
              // console.log(movie)
              movie.like_users.push(payload.userPk)
              console.log(movie)
            }
          }
        })
      },
      MY_REVIEWS_SETTING(state, payload){
          state.userReviewList = payload
      },
      allMovieOrder(state, payload) {
        const genreOrder = payload.genre
        const order = payload.order
        let orderList = []
        if (genreOrder.length) {
          orderList = state.movieList.filter((el) => {
            let isPass = false
            el.genres.forEach(g => {
              if (genreOrder.includes(JSON.stringify(g.id))) {
                isPass = true
              }
            })
            if (isPass) {
              return el
            }
          })
        } else {
          orderList = state.movieList
        }
        if (order === 'new') {
          orderList.sort(function(a, b) {
            const yearA = a.release_date
            const yearB = b.release_date
            if(yearA > yearB) return 1;
            if(yearA < yearB) return -1;
            if(yearA === yearB) return 0;
          })
        } else if (order === "old") {
          orderList.sort(function(a, b) {
            const yearA = a.release_date
            const yearB = b.release_date
            if(yearA < yearB) return 1;
            if(yearA > yearB) return -1;
            if(yearA === yearB) return 0;
          })
        } else if (order === "high") {
          orderList.sort(function(a, b) {
            const voteA = a.vote_average
            const voteB = b.vote_average
            if(voteA > voteB) return 1;
            if(voteA < voteB) return -1;
            if(voteA === voteB) return 0;
          })
        } else if (order === "low") {
          orderList.sort(function(a, b) {
            const voteA = a.vote_average
            const voteB = b.vote_average
            if(voteA < voteB) return 1;
            if(voteA > voteB) return -1;
            if(voteA === voteB) return 0;
          })
        } else if (order === "many") {
          orderList.sort(function(a, b) {
            const likeA = a.like_users.length
            const likeB = b.like_users.length
            if(likeA > likeB) return 1;
            if(likeA < likeB) return -1;
            if(likeA === likeB) return 0;
          })
        } else if (order === "few") {
          orderList.sort(function(a, b) {
            const likeA = a.like_users.length
            const likeB = b.like_users.length
            if(likeA < likeB) return 1;
            if(likeA > likeB) return -1;
            if(likeA === likeB) return 0;
          })
        } else {
          orderList.sort(function(a, b) {
            const likeA = a.popularity
            const likeB = b.popularity
            if(likeA < likeB) return 1;
            if(likeA > likeB) return -1;
            if(likeA === likeB) return 0;
          })
        }
        state.orderMovieList = orderList
        state.orderMovieListPage = orderList.slice(0, 8)
      },
      pageMove(state, pageNum) {
        state.orderMovieListPage = state.orderMovieList.slice(pageNum*8 - 8,pageNum*8)
      },
      REVIEW_NUMS_GET(state, review) {
        state.reviewId = review
      },
      CREATE_REVIEW(state, review) {
        state.movieList.forEach(el => {
          if (el.id === review.movie.id) {
            el.reviews.push(review)
          }
        })
      },
      DELETE_REVIEW(state, review) {
        state.movieList.forEach(el => {
          console.log('1', el)
          if (el.id === review.movie.id) {
            console.log('2', el.reviews)
            el.reviews = el.reviews.filter(re => {
              if (re.id !== review.id) {
                return re
              }
            })
          }
        })
      }
  },
  actions: {
    getMovieList(context) {
        // const TMDB_API_KEY = process.env.VUE_APP_TMDBKEY
        // const API_URL =`https://api.themoviedb.org/3/movie/popular?api_key=${TMDB_API_KEY}&language=ko-KR&page=1`
        return axios({
          method: 'get',
          url: `${DJANGO_API_URL}/api/v1/movies/`
        })
          .then(res => {
            context.commit('GET_MOVIE_LIST', res.data)
            context.commit('GET_FIRST_SELECT', 8)
          })
          .catch(err => console.log(err))
      }, 
      getVoteAvgMovieList(context, userPk) {
        return axios({
          method: 'post',
          url: `${DJANGO_API_URL}/api/v1/movies/${userPk}/recommended_vote_average/`,
          headers: {
            Authorization: `Token ${Vue.$cookies.get("token")}`
          }
        })
          .then(res => {
            // 뽑아온 배열
            const voteAvg = res.data
            const idlist = []
            voteAvg.forEach((el)=> {
              idlist.push(el.id)
            })
            context.commit('GET_VOTE_AVG_MOVIE_LIST', idlist)
          })
          .catch(err => console.log(err))
      },
      getVoteCntMovieList(context, userPk) {
        return axios({
          method: 'post',
          url: `${DJANGO_API_URL}/api/v1/movies/${userPk}/recommended_vote_count/`,
          headers: {
            Authorization: `Token ${Vue.$cookies.get("token")}`
          }
        })
          .then(res => {
            const voteCnt = res.data
            const idlist2 = []
            voteCnt.forEach((el) => {
              idlist2.push(el.id)
            })
            context.commit('GET_VOTE_CNT_MOVIE_LIST', idlist2)
          })
          .catch(err => console.log(err))
      },
      getLikeMovieList(context, userPk) {
        return axios({
          method: 'post',
          url: `${DJANGO_API_URL}/api/v1/movies/${userPk}/like_movies/`,
          headers: {
            Authorization: `Token ${Vue.$cookies.get("token")}`
          }
        })
          .then(res => {
            const likeMovies = res.data
            const idlist3 = []
            likeMovies.forEach((el) => {
              idlist3.push(el.id)
            })
            context.commit('GET_LIKE_MOVIE_LIST', idlist3)
          })
          .catch(err => console.log(err))
      },
      myReviewsSetting(context, payload){
          // console.log(context)
          console.log(payload)
          context.commit('MY_REVIEWS_SETTING', payload)
      },
      async startMovieOrder (context, payload) {
        if (!context.state.movieList.length) {
          await context.dispatch('getMovieList')
        }
        await context.commit('allMovieOrder', payload)
      }
  },
  modules: {
  }
}

export default movie