<template>
<div class="col-3 my-2 ">
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="card h-100 border-0 flip-card-front" id="mycard" @click="modal.show()" >
      <img class="h-100 rounded-start card-img" :src="'https://image.tmdb.org/t/p/w500/'+ `${movie?.poster_path}`" alt="">
      </div>
      <div class="flip-card-back rounded border-light p-4 overflow-hidden" id="mycard" @click="modal.show()">
        <h1>{{movie.title}}</h1>
        <h2>{{movie.vote_average}}</h2>
        <br>
        {{movie.overview.slice(0, 190) + "..."}}
      </div>
    </div>
  </div>
  
  <!-- Detail -->
  <div class="modal fade zoom-in" ref="exampleModal" tabindex="-1" aria-hidden="true"  style="overflow: hidden;">
    <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-xl">
      <div class="modal-content" style="height: 100vh;">
        <div class="modal-header">
          <span class="modal-title" id="exampleModalLabel"></span>
          <button type="button" class="btn-close" @click="modal.hide()" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="container d-flex flex-column justify-content-center">
            <div id="Detail_title_vote" class="row">
              <div id="detail_title" class="col-4">
                <h3>{{ movie?.title }}</h3>
              </div>
              <div id="avg_cnt_like_set" class="col-4">
                <div class="avg_cnt_like">
                  평점<br>
                  {{movie?.vote_average}}
                </div>
                <div class="avg_cnt_like">
                  평론수<br>
                  {{movie?.vote_count}}
                </div>
                <div class="avg_cnt_like" @click="ToLiking" v-show="!this.movie?.like_users.includes($store.getters.userPkGetters)">
                  좋아요<br>
                  <i class="bi bi-hand-thumbs-up-fill"></i>
                </div>
                <div class="avg_cnt_like selected" @click="ToLiking" v-show="this.movie?.like_users.includes($store.getters.userPkGetters)">
                  싫어요<br>
                  <i class="bi bi-hand-thumbs-up-fill"></i>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col-4">
                <img id="detail_img" :src="'https://www.themoviedb.org/t/p/w600_and_h900_bestv2' + `${movie?.poster_path}`">
              </div>
              <div class="col-8">
                <div style="height: 70%;" class="row">
                  <div style="height: 100%;" id="iframe_img" class="col">
                    <iframe id="player" type="text/html" class="iframe_wid_hei"
                      :src="videoUrl+videoKey"
                    frameborder="0" v-if="videoKey"></iframe>
                    <img class="img_wid_hei" src="https://www.tooli.co.kr/files/attach/images/571601/933/121/001/b3fb122e830eeb9a3a8a916f1c87fd69.gif" alt="안나올 뜨는 이미지" v-if="!videoKey">
                  </div>
                </div>
                <div style="height: 30%; " class="row">
                  <div style="width: 100%;" class="col">
                    <Actors
                      style="height: 100%;"
                      :movie="movie"
                    />
                  </div>
                </div>
              </div>
            </div>
            
            <div class="row">
              <div id="detail_content" class="col">
                {{movie.overview}}
              </div>
            </div>

            <div class="row">
              <div class="col review_body">
                <div class="row justify-content-between">
                  <div id="reviews_title" @click="goToReview" class="col-3">
                    <h4>Review</h4>
                  </div>
                </div>
                <div class="row d-flex justify-content-center mt-3 mb-3">
                  <table class="table">
                    <thead>
                      <tr>
                        <th style="width: 10%" scope="col">ID</th>
                        <th style="width: 45%" scope="col">Title</th>
                        <th style="width: 30%" scope="col">movie</th>
                        <th style="width: 15%" scope="col">time</th>
                      </tr>
                    </thead>
                    <DetailReviews
                    
                    :movie="movie"
                    @closemodal="modal.hide()"
                    />
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Actors from '@/components/Actors/ActorsSet.vue'
import DetailReviews from '@/components/DetailReviews/DetailReviews.vue'

import { Modal } from 'bootstrap'
import axios from 'axios'
const DJANGO_API_URL = 'http://127.0.0.1:8000'
// import Vue from 'vue'
const TMDB_API_KEY = '0802a25be8939d20e57e4d6621c62927'

export default {
    name: 'MyCard',
    components: {
      Actors,
      DetailReviews,
    },
    props: {
        movie: Object,
    },
    data () {
      return {
        modal: null,
        userPk : null,
        like_choiced : false,
        videoUrl : "http://www.youtube.com/embed/",
        videoKey : null,
      }
    },
    computed: {
        allMovieList() {
              return this.$store.getters.movieListCutting
        },
    },
    async mounted() {
      this.modal = await new Modal(this.$refs.exampleModal)
      await this.videoLoad()
    },
    methods : {
      // 영화 좋아요
      async ToLiking() {
        if (this.$store.getters.userPkGetters) {
          console.log(this.movie)
          await this.$store.dispatch('getUserPk')
          this.userPk = await this.$store.getters.userPkGetters
          const payload = {
            'userPk' : this.userPk,
            'moviePk' : this.movie.id
          }
          return axios({
            method: 'post',
            url: `${DJANGO_API_URL}/api/v1/movies/${payload.userPk}/like/`,
            headers: {
              Authorization: `Token ${this.$cookies.get("token")}`
            },
            data : {
              movie: this.movie.id
            }
          })
          .then(() => {
              console.log(payload)
              this.$store.commit('TO_LIKING', payload)
            })
          .catch(err => console.log(err))
        } else {
          this.modal.hide()
          alert("로그인 하셔야겠는데요?")
          this.$router.push({name: 'login'})
        }
      },
      // 비디오 불러오기
      videoLoad() {
        const TMDB_URL = `https://api.themoviedb.org/3/movie/${this.movie.tmdb_id}/videos?api_key=${TMDB_API_KEY}&language=ko-KR`
        axios({
          method: 'get',
          url: TMDB_URL,
        })
        .then(res => {
            this.videoKey = res.data.results[0].key
          })
        .catch(err => console.log(err))
      },
      goToReview() {
        const movieId = this.movie.id
        const movieTitle = this.movie.title
        this.$router.push({ name: "communitycreate", params : { movieId, movieTitle } })
        this.modal.hide()
      }
    },
  }

</script>

<style>
  /* #mycard:hover {
    transform: scale(1.1);
    transition: transform 330ms ease-in-out;
    z-index: 1;
  } */

  /* The flip card container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
  .flip-card {
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
    border-radius: 10px;
    background-color: transparent;
    width: 100%;
    height: 100%;
    perspective: 1000px; /* Remove this if you don't want the 3D effect */
  }

  /* This container is needed to position the front and back side */
  .flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.4s ease-in-out;
    transform-style: preserve-3d;
  }

  /* Do an horizontal flip when you move the mouse over the flip box container */
  .flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
  }

  /* Position the front and back side */
  .flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden; /* Safari */
    backface-visibility: hidden;
  }

  /* Style the front side (fallback if image is missing) */
  .flip-card-front {
    background-color: #bbb;
    color: black;
  }

  /* Style the back side */
  .flip-card-back {
    text-align: unset;
    position: fixed;
    top: 0;
    background-color: #FF4301;
    color: white;
    transform: rotateY(180deg);
  }
  /* 모달 애니메이션 */
  .modal.fade .modal-dialog{
    -webkit-transform: translate(0,0)!important;
    transform: translate(0,0)!important;
  }

  .zoom-in {
    transform: translateY(100vh)!important;
    opacity: 1!important;
    -webkit-transition: .5s all ease-in-out!important;
    -moz-transition: .5s all ease-in-out!important;
    -ms-transition: .5s all ease-in-out!important;
    -o-transition: .5s all ease-in-out!important;
    transition: .5s all ease-in-out!important;
    display: block !important;
  }

  .zoom-in.show {
    opacity: 1!important;
    transform: translateY(0)!important;
    transform:none!important;
  }

  /* 배경색 맞추기 */
  .modal-header{
    background-color: #FF4301;
    border-bottom: 1px solid #FF4301 !important;
  }
  .modal-body{
    background-color: #130f0a;
  }

  .modal-title {

    font-weight: 900;
    font-size: 25px;
    margin-left: 20px;
  }

  
  #avg_cnt_like_set {
    width: 400px;
    display: flex;
  }
  
  .avg_cnt_like {
    width: 250px;
    height: 80px;
    border: 1px solid #FF4301;
    background-color: #FF4301;
    color: white;
    padding-top: 15px;
    text-align: center;
    border-radius: 50%;
    box-shadow: 5px 5px gainsboro;
    margin: 20px;
    animation: like 3s ease-out;
  }

  @keyframes like {
    to {
      transform: rotate3d(100, 100, 100, 30turn);
    }
  }

  #Detail_title_vote {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  #detail_title {
    display: flex;
    justify-content: center;
    font-size: 30px;
    color: white;
    font-weight: 900;
  }

  #detail_img {
    width: 100%;
    height: 100%;
    border-radius: 5px;
  }

  #detail_content {
    text-align: left;
    margin-left: 10px;
    margin-right: 20px;
    margin-top: 30px;
    margin-bottom: 30px;
    padding: 30px 20px;
    border: 1px inset transparent;
    background-color: #1d1812;
    color: white;
    border-radius: 5px;
    box-shadow: 2px 2px #444444;
  }

  .review_body {
    background-color: #1d1812;
    width:80%;
    margin-left: 10px;
    margin-right: 20px;
    padding: 10px 20px !important;
    border: 1px inset transparent;
    border-radius: 5px;
    box-shadow: 2px 2px #444444;
  }

  .review_body th,
  .review_body td {
    color: white;
  }

  #reviews_title {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 200px;
    height: 50px;
    text-align: center;
    font-size: 20px;
    margin-left: 5px;
    margin-top: 10px;
    margin-bottom: 10px;
    padding-top: 10px;
    background-color: #FF4301;
    box-shadow: 5px 5px #ff4501a4;
    color: black;
    border-radius: 5px;
  }

  #reviews_title:hover {
    scale: 1.2;
    transform: rotateX(720deg) translateX(20px);
    transition: all 1s;
    /* animation: reviewbtn normal; */
  }

  /* @keyframes reviewbtn {
    to {
      transform: rotateX(3600deg) translateX(30px);
    }
  } */

  .selected {
    border: 1px solid #2F2519;
    background-color: #2F2519;
    box-shadow: none;

  }

  .avg_cnt_like:hover{
    opacity: 0.7;
  }

  .iframe_wid_hei {
    width: 100%;
    height: 100%;
  }

  #iframe_img{
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .img_wid_hei {
    height: 100%;
    animation: heundlehundle 10s;
    animation-iteration-count: infinite;
  }
  @keyframes heundlehundle {
    0%{
      transform: translateX(10%);
    }
    10%{
      transform: translateX(-10%);
    }
    20%{
      transform: translateX(10%);
    }
    30%{
      transform: translateX(-10%);
    }
    40%{
      transform: translateX(10%);
    }
    50%{
      transform: translateX(-10%);
    }
    60%{
      transform: translateX(10%);
    }
    70%{
      transform: translateX(-10%);
    }
    80%{
      transform: translateX(10%);
    }
    90%{
      transform: translateX(-10%);
    }
    100%{
      transform: translateX(10%);
    }
    
  }
</style>