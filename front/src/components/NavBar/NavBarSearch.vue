<template>
  <form class="d-flex" @submit.prevent="searchPush">
    <input 
        class="form-control nav-search me-2" 
        placeholder="search" 
        :class="{ searchClicked : searchClick }" 
        @click="sClick"
        v-model.trim="searchKeyword"
        >
    <button class="btn btn-dark nav-search-btn" :class="{ 'btn-light' : searchClick }">검색</button>
    <div class="overlay" @click="sClick" v-show="searchClick"></div>
  </form>
</template>

<script>
export default {
    name: 'NavBarSearch',
    data() {
        return {
            searchClick: false,
            searchKeyword: ''
        }
    },
    methods: {
        sClick () {
            this.searchClick = !this.searchClick
        },
        searchPush() {
            if (this.searchKeyword) {
                this.searchClick = false
                this.$router.push({name: 'search', params: { keyword : this.searchKeyword }})
                this.searchKeyword = null
            } else {
                alert('검색어를 입력해주세요!')
            }
            
        }
    },
}
</script>

<style>
    .nav-search{
        width: 20rem !important;
        background-color: #FF4301 !important;
        z-index: 10;
        -webkit-transition: background-color 150ms linear !important;
        -ms-transition: background-color 150ms linear !important;
        transition: background-color 150ms linear !important;
    }
    .nav-search-btn{
        background-color: #FF4301 !important;
        z-index: 10;
    }
    .searchClicked {
        background-color: #F8EDE3 !important;
        -webkit-transition: background-color 150ms linear !important;
        -ms-transition: background-color 150ms linear !important;
        transition: background-color 150ms linear !important;
    }
    .nav-search::-webkit-input-placeholder{
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='%23808080' class='bi bi-search'%3E%3Cpath d='M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z'/%3E%3C/svg%3E");
        background-size: contain;
        background-position:  1px center;
        background-repeat: no-repeat;
        color: #F8EDE3 !important;
        text-indent: 0;
        padding-left: 1.5rem;
    }
    .overlay {
        width: 100%;
        height: 100%;
        position: fixed;
        left: 0;
        top: 0;
        opacity: 0.5;
        background-color: black;
        z-index: 9;
    }
</style>