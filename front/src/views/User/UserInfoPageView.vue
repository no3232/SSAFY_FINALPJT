<template>
  <div>
    <br>
    <div class="container d-flex justify-content-center align-items-center">
      <br>
      <br>
      <div class="card text-center userinfo_box">
          <div id="card-header-bg" class="card-header pt-5 pb-4">
            <h2>(☞ﾟヮﾟ)☞<b>{{ userInformation?.username }}</b>'s ROOM ☜(ﾟヮﾟ☜)</h2>
          </div>
          <div id="card-body-bg" class="card-body d-flex flex-column align-items-center">
              <div class="follow_box">
                followings : {{userInformation?.followings?.length}}<br>
                followers : {{userInformation?.followers?.length}}
              </div>
              <div>
                <span style="color:#2F2519;" href="#" @click="favoriteGenre" class="btn btn-warning">당신이 가장 좋아하는 장르는?</span>
              </div>
              <div id="favorite_genre_box">
                <button id="genre_choice" type="button" v-if="favorite_genre" @click="goToGenre" class="btn btn-outline-secondary">{{favorite_genre}}</button>
                <button type="button" v-if="!favorite_genre" class="btn btn-outline-secondary"> 장르를 클릭하면 해당 페이지로 넘어가요! d=====(￣▽￣*)b </button>
              </div>
          </div>
          <div id="card-footer-bg" class="card-footer text-muted d-flex justify-content-between">
            <button id="userUpdate" class="btn btn-secondary" v-show="$store.getters.userPkGetters" @click="updateShow=!updateShow">UPDATE</button>
            <button id="userFollow" class="btn btn-success" @click="followUser" v-show="$store.getters.userPkGetters && $store.getters.userPkGetters !== this.userInformation.id"><i id="user_follow" class="bi bi-hand-index-thumb-fill"></i> FOLLOW</button>
            <button id="userDelete" class="btn btn-danger" v-show="$store.getters.userPkGetters" @click="removeUser">USERBYE</button>
          </div>
      </div>
      <br>
      <div style="height:60%; border: none !important; margin-top: 40px;" class="card text-center" v-show="updateShow" id="updateform">
        <div class="card-header" id="card-header-bg">
          UserInfo UPDATE
        </div>
        <div class="card-body d-flex flex-column align-items-center" id="card-body-bg">
          <div id="userInfoUpdate">
            <form @submit.prevent="updateUser"  v-show="updateShow">
                <div id="updateinput" class="form-floating mb-3">
                    <input type="text" class="form-control" id="userFirstName" placeholder="FirstName을 입력하세요" v-model="userFirstName">
                    <label for="userFirstName" style="color: white;">FirstName</label>
                </div >
                <div class="form-floating mb-3" id="updateinput">
                    <input type="text" class="form-control" id="userLastName" placeholder="LastName을 입력하세요" v-model="userLastName">
                    <label for="userLastName" style="color: white;">LastName</label>
                </div>
                <div class="form-floating mb-3" id="updateinput">
                    <input type="text" class="form-control" id="userEmail" placeholder="Email을 입력하세요" v-model="userEmail">
                    <label for="userEmail" style="color: white;">Email</label>
                </div>
                <div>
                </div>
                <div class="card-footer text-muted">
                  <input class="btn btn-primary" type="submit" value="UPDATE">
                </div>
            </form>
          </div>
        </div>
      </div>
      <br>
    </div>
      <div class="container pt-5" v-show="$store.getters.userPkGetters">
        <div class="row">
          <div id="like_movies_title" class="col-3">My Review</div>
          <br>

          <div class="row">
            <div class="col review_body">
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
                  <tbody class="table_body">
                    <MyReview
                        v-for="re in userInformation.review"
                        :key="re.id"
                        :review="re"
                    />
                  </tbody>
                </table>
              </div>
            </div>
          </div>

        </div>
        <div class="row mt-5">
          <div id="like_movies_title" class="col-3">LIKE MOVIE</div>
          <br>
          <div class="col-3"></div><div class="col-3"></div><div class="col-3"></div>
        </div>
        <div class="row">
          <transition-group name="flip" mode="flip" class="row">
            <MyCard 
              v-for="movie in getLikeMovieListShow"
              :key = movie.id
              :movie = movie
            />
          </transition-group>
        </div>
      </div>
      <br>
    </div>
</template>

<script>
import MyCard from '@/components/MyCard.vue'
import MyReview from '@/components/MyReview.vue'

import axios from 'axios'
export default {
    name: 'UserInfoPageView',
    components: {
      MyCard,
      MyReview,
    },
    data() {
        return {
            userInformation: '',
            updateShow: false,
            userFirstName: '',
            userLastName: '',
            userEmail: '',
            favorite_genre: '',
            myReviewList: [],
            genre_category: [
                {
                    "id": 12,
                    "name": "모험"
                },
                {
                    "id": 28,
                    "name": "액션"
                },
                {
                    "id": 16,
                    "name": "애니메이션"
                },
                {
                    "id": 35,
                    "name": "코미디"
                },
                {
                    "id": 80,
                    "name": "범죄"
                },
                {
                    "id": 99,
                    "name": "다큐멘터리"
                },
                {
                    "id": 18,
                    "name": "드라마"
                },
                {
                    "id": 10751,
                    "name": "가족"
                },
                {
                    "id": 14,
                    "name": "판타지"
                },
                {
                    "id": 36,
                    "name": "역사"
                },
                {
                    "id": 27,
                    "name": "공포"
                },
                {
                    "id": 10749,
                    "name": "로맨스"
                },
                {
                    "id": 10402,
                    "name": "음악"
                },
                {
                    "id": 9648,
                    "name": "미스터리"
                },
                {
                    "id": 878,
                    "name": "SF"
                },
                {
                    "id": 10770,
                    "name": "TV 영화"
                },
                {
                    "id": 53,
                    "name": "스릴러"
                },
                {
                    "id": 10752,
                    "name": "전쟁"
                },
                {
                    "id": 37,
                    "name": "서부"
                }
            ],
        }
    },
    computed: {
      getLikeMovieListShow() {
        return this.$store.getters.moviesLikeListGetters
      },
    },
    methods: {
        getUserInfo() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const userpk = this.$route.params.userPk
            axios({
                method: 'get',
                url: `${DJANGO_API_URL}/api/accounts/user/${userpk}/`,
                // url: `${DJANGO_API_URL}/accounts/user/`,
                // headers: {
                //     Authorization: `Token ${this.$store.state.token.key}`
                // }
            })
            .then(res => {
                this.userInformation = res.data
                this.userFirstName = res.data.first_name
                this.userLastName = res.data.last_name
                this.userEmail = res.data.email
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        removeUser() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'delete',
                url: `${DJANGO_API_URL}/api/accounts/user/remove/${this.$store.getters.userPkGetters}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get('token')}`
                },
                // data: {
                //     is_active: false
                // }
            })
            .then(res => {
                console.log(res)
                this.$cookies.remove('token')
                this.$store.state.userAccount.userPk = null
                this.$router.push({name: 'main'})
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        followUser() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'post',
                url: `${DJANGO_API_URL}/api/accounts/user/follow/${this.userInformation.id}/${this.$store.getters.userPkGetters}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get("token")}`
                },
            })
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        updateUser() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const first_name = this.userFirstName
            const last_name = this.userLastName
            const email = this.userEmail
            axios({
                method: 'put',
                url: `${DJANGO_API_URL}/api/accounts/user/${this.$route.params.userPk}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get('token')}`
                },
                data: {
                    first_name, last_name, email
                }
            })
            .then(res => {
              this.updateShow = false
              console.log(res.data)
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        favoriteGenre() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'post',
                url: `${DJANGO_API_URL}/api/v1/movies/${this.$route.params.userPk}/favorite_genre/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get('token')}`
                },
            })
            .then(res => {
              this.genre_category.forEach((genre) => {  
                if (genre.id === res.data.favorite_genre_num){
                  this.favorite_genre = genre.name
                  console.log(123124132521)
                }
              })
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        goToGenre() {
          this.$router.push({name:'genre'})
        }
    },
    mounted() {
        this.$store.dispatch('getUserPk')
        this.getUserInfo()
        this.userPk = this.$store.getters.userPkGetters
        this.$store.dispatch('getLikeMovieList', this.$route.params.userPk)
        this.myReviewList = this.$state.userReviewList.filter((user) => {
          if (user.id == this.userInformation.id) {
            return user
            }
        })
    }
}
</script>

<style>
  #userFirstName,
  #userLastName,
  #userEmail {
    color: white;
    background-color: #2F2519;
    border: none;
  }
  #favorite_genre_box {
    padding: 10px 30px;
    width: 50%;
    font-size: 20px;
  }
  .follow_box{
    border: 1px solid #2F2519;
    background-color: #2F2519;
    border-radius: 5px;
    padding: 10px 40px;
    margin-top: 5px;
    margin-bottom: 20px;
    width: 50%;
    font-size: 20px;
    color: white;
  }

  .follow_box:hover{
    animation: shake 0.5s;
    animation-iteration-count: infinite;
  }

  .userinfo_box {
    border: 1px solid #130f0a !important;
    border-radius: 15px !important;
    margin-top: 100px;
    width: 80% !important;
  }
  .like_movies {
    margin-top: 20px;
  }

  #like_movies_title{
  width: 300px;
  height: 50px;
  text-align: center;
  font-size: 30px;
  padding-top: 5px;
  margin-left: 15px;
  margin-bottom: 50px;
  background-color: black;
  color: white;
  border-radius: 5px;
}

#genre_choice{
  width: 300px;
  font-size: 20px;
}

#genre_choice:hover,
#userUpdate:hover,
#userFollow:hover {
  /* Start the shake animation and make the animation last for 0.5 seconds */
  animation: shake 0.5s;

  /* When the animation is finished, start again */
  animation-iteration-count: infinite;
}
/* 
#userDelete {
  animation: shake 0.5s;
  animation-iteration-count: infinite;
} */

/* #userDelete:focus {
  animation: hardshake 1s;
  animation-iteration-count: infinite;
} */

@keyframes avoidedmouse {
  0% {
    transform: translateX(0px);
  }
  100% {
    transform: translateX(200px);
    pointer-events: none;
  }
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

@keyframes hardshake {
  0% { transform: translate(30px, 30px) rotate(0deg); }
  10% { transform: translate(-30px, -60px) rotate(-1deg); }
  20% { transform: translate(-90px, 90px) rotate(1deg); }
  30% { transform: translate(90px, 60px) rotate(0deg); }
  40% { transform: translate(30px, -30px) rotate(1deg); }
  50% { transform: translate(-30px, 60px) rotate(-1deg); }
  60% { transform: translate(-90px, 30px) rotate(0deg); }
  70% { transform: translate(90px, 30px) rotate(-1deg); }
  80% { transform: translate(-30px, -30px) rotate(1deg); }
  90% { transform: translate(30px, 60px) rotate(0deg); }
  100% { transform: translate(30px, -60px) rotate(-1deg); }
}

/* 리뷰 관련 */

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

  #card-header-bg {
    background-color: rgb(199, 199, 199);
    background-color: #2F2519;
    color: white;
  }

  #card-body-bg {
    background-color: #4A3F35;
  }

  #card-footer-bg {
    background-color: #4A3F35;
  }
</style>