<template>
  <div class="container d-flex flex-column justify-content-center" id="reviewlist" >
    <div class="row justify-content-between" style="margin-top: 90px;">
        <h2 class="col-3">리뷰 페이지</h2>
        <router-link class="btn col-2 fs-3" :to="{ name: 'communitycreate'}" id="reviewcreatebtn">리뷰 작성</router-link>
    </div>
    <div class="container mt-2">
        <table class="table table-light table-hover">
            <thead>
                <tr>
                <th scope="col" id="rNum">번호</th>
                <th scope="col" id="rmovie">영화</th>
                <th scope="col" id="rtitle">제목</th>
                <th scope="col" id="rRecommend">추천수</th>
                <th scope="col" id="rWriter">작성자</th>
                </tr>
            </thead>
            <tbody>
                <tr 
                    v-for="review in communityList.slice(presentPage*12-12, presentPage*12)"
                    :key="review.id"
                    @click="moveToDetail(review.id, review.movie.id)"
                >
                <td scope="col" id="rNum">{{ review.id }}</td>
                <td scope="col" id="rmovie">{{ review.movie.title.slice(0, 12) + '...' }}</td>
                <td scope="col" id="rtitle">{{ review.title }}</td>
                <td scope="col" id="rRecommend">{{ review.like_users.length }}</td>
                <td scope="col" id="rWriter">{{ review.user.username }}</td>
                </tr>
            </tbody>
        </table>
    </div>
    <nav aria-label="Page navigation example">
                <ul class="pagination justify-content-center mt-5">
                    <!-- 처음으로 -->
                    <li class="page-item">
                    <a class="page-link" @click.prevent="presentPage = 1"><i class="bi bi-chevron-double-left"></i></a>
                    </li>
                    <!-- 뒤로 -->
                    <li class="page-item ">
                    <a class="page-link" @click.prevent="pMinus"><i class="bi bi-chevron-left" style="all: unset;"></i></a>
                    </li>
                    <!-- ... -->
                    <li class="page-item disabled" v-show="presentFirstPage !== 1">
                    <a class="page-link"><i class="bi bi-three-dots"></i></a>
                    </li>
                    <!-- 시작 -->
                    <li 
                        v-for="n in pageRange"
                        :key=n.id
                        class="page-item"
                        :class="{ 'active' : n === presentPage }"
                        @click.prevent="presentPage=n"
                    >
                        <a class="page-link" href="#">{{ n }}</a>
                    </li>
                    <!-- 끝 -->
                    <li class="page-item disabled" v-show="orderListmaxPage !== presentLastPage">
                    <a class="page-link"><i class="bi bi-three-dots"></i></a>
                    </li>
                    <!-- 앞으로 -->
                    <li class="page-item">
                    <a class="page-link" href="#" @click.prevent="pPlus"><i class="bi bi-chevron-right" style="all: unset;"></i></a>
                    </li>
                    <!-- 끝으로 -->
                    <li class="page-item" @click.prevent="presentPage = orderListmaxPage">
                    <a class="page-link" href="#"><i class="bi bi-chevron-double-right"></i></a>
                    </li>
                </ul>
            </nav>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CommunityView',
    data() {
        return{
            communityList: null,
            presentPage: 1,
            pageRange: [1]
        }
    },
    methods: {
        getCommunityList() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            return axios({
                method: 'get',
                url: `${DJANGO_API_URL}/api/v1/community/`
            })
            .then(res => {
              this.communityList = res.data
              const payload = []
              payload.push(res.data)
              this.$store.dispatch('myReviewsSetting', payload)
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        moveToDetail(reviewid, movieid) {
            this.$router.push({ name : 'communitydetail', params : {reviewid: reviewid, movieid: movieid}})
        },
        pMinus() {
            if (this.presentPage > 2) {
                this.presentPage -= 1
            }
        },
        pPlus() {
            if (this.presentPage < this.orderListmaxPage) {
                this.presentPage += 1
            }
        }
    },
    computed: {
        orderListmaxPage() {
            return Math.ceil(this.communityList.length/12)
        },
        presentFirstPage() {
            if (this.presentPage - 2 < 1) {
                return 1
            } else {
                return this.presentPage -2 
            }
            
        },
        presentLastPage() {
            if (this.presentFirstPage + 4 < this.orderListmaxPage) {
                return this.presentFirstPage + 4
            } else {
                return this.orderListmaxPage
            }
        },
    },
    async created() {
        await this.getCommunityList()
        this.pageRange = []
        for(let i = this.presentFirstPage; i<=this.presentLastPage ; i++) {
            console.log(i)
            this.pageRange.push(i)
            console.log(this.pageRange)
        }
    },
    watch: {
        orderListmaxPage() {
            this.pageRange = []
            for(let i = this.presentFirstPage; i<=this.presentLastPage ; i++) {
                console.log(i)
                    this.pageRange.push(i)
            }
        }
    }
}


</script>

<style>

#reviewlist {
    color: white;
}
#rNum {
    width: 10%;
}
#rmovie {
    width: 20%
}
#rtitle {
    width: 50%;
}
#rRecommend {
    width: 10%;
}
#rWriter {
    width: 10%;
}
#reviewcreatebtn {
    margin-right: 22px;
    background-color: #FF4301;
}
#reviewcreatebtn:hover {
    background-color: #FA7D09;
    transition: all 2s;
}

</style>