<template>
  <div id="order-box" class="col-2 border border-2 rounded p-4">
    <h1>정렬기준</h1>
    <div class="btn-group d-flex flex-column aling-items-center" role="group" aria-label="Basic radio toggle button group">
        <h4>개봉 날짜 순</h4>
        <div class="d-flex justify-content-evenly">
            <input type="radio" class="btn-check" name="btnradio" id="new" autocomplete="off" value="new" v-model="order" >
            <label id="orderbtn" class="btn btn-light col-3" for="new"><i class="bi bi-caret-up"></i></label>

            <input type="radio" class="btn-check" name="btnradio" id="old" autocomplete="off" value="old" v-model="order">
            <label id="orderbtn" class="btn btn-light  col-3" for="old"><i class="bi bi-caret-down"></i></label>
        </div>
        <br>

        <h4>평점 순</h4>
        <div class="d-flex justify-content-evenly">
            <input type="radio" class="btn-check" name="btnradio" id="high" autocomplete="off" value="high" v-model="order">
            <label id="orderbtn" class="btn btn-light  col-3" for="high"><i class="bi bi-caret-up"></i></label>

            <input type="radio" class="btn-check" name="btnradio" id="low" autocomplete="off" value="low" v-model="order">
            <label id="orderbtn" class="btn btn-light  col-3" for="low"><i class="bi bi-caret-down"></i></label>
        </div>
        <br>

        <h4>좋아요 순</h4>
        <div class="d-flex justify-content-evenly">
            <input type="radio" class="btn-check" name="btnradio" id="many" autocomplete="off" value="many" v-model="order">
            <label id="orderbtn" class="btn btn-light  col-3" for="many"><i class="bi bi-caret-up"></i></label>

            <input type="radio" class="btn-check" name="btnradio" id="few" autocomplete="off" value="few" v-model="order">
            <label id="orderbtn" class="btn btn-light  col-3" for="few"><i class="bi bi-caret-down"></i></label>
        </div>
        <br>
        <button class="btn btn-danger col-12 rounded" @click="clearOrder">초기화</button>
    </div>
    <br>
    <div class="container">
    <h4>장르</h4>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="14" id="14" v-model="genre">
            <label class="form-check-label" for="14">
                판타지
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="16" id="16" v-model="genre">
            <label class="form-check-label" for="16">
                애니메이션
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="18" id="18" v-model="genre">
            <label class="form-check-label" for="18">
                드라마
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="27" id="27" v-model="genre">
            <label class="form-check-label" for="27">
                호러
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="28" id="28" v-model="genre">
            <label class="form-check-label" for="28">
                액션
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="35" id="35" v-model="genre">
            <label class="form-check-label" for="35">
                코미디
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="36" id="36" v-model="genre">
            <label class="form-check-label" for="36">
                역사
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="53" id="53" v-model="genre">
            <label class="form-check-label" for="53">
                스릴러
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="80" id="80" v-model="genre">
            <label class="form-check-label" for="80">
                범죄
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="878" id="878" v-model="genre">
            <label class="form-check-label" for="878">
                SF
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="10749" id="10749" v-model="genre">
            <label class="form-check-label" for="10749">
                로맨스
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="10752" id="10752" v-model="genre">
            <label class="form-check-label" for="10752">
                전쟁
            </label>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'OrderList',
    data() {
        return {
            order: "",
            genre: [],
        }
    },
    methods: {
        clearOrder() {
            this.order = ''
            const payload = {
                genre: this.genre,
                order: this.order
            }
            this.$store.commit('allMovieOrder', payload)
        }
    },
    watch: {
        order(value) {
            const payload = {
                genre: this.genre,
                order: value
            }
            this.$store.commit('allMovieOrder', payload)
        },
        genre(value) {
            const payload = {
                genre: value,
                order: this.order
            }
            this.$store.commit('allMovieOrder', payload)
        }
    },
}
</script>

<style>
#order-box{
    background-color: #4A3F35;
    color: white;
}
#orderbtn:active {
    background-color: #FF4301;
}
.btn-light{
    --bs-btn-active-bg : #FF4301 !important;
    --bs-btn-active-border-color: white !important;
    --bs-btn-active-color: white !important;
}
.form-check-input:checked {
    background-color: #FF4301 !important;
    border-color: #FF4301 !important;
}
</style>