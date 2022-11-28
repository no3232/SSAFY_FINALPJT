<template>
<div class="col-2 my-2">
    <div class="card h-100" id="FirstSigncard">
    <img class="h-100 rounded-start card-img" :src="'https://image.tmdb.org/t/p/w500/'+ `${movie?.poster_path}`" alt="">
    <button class="btn btn-danger" @click="clickCard">삭제</button>
    </div>
 </div>
</template>

<script>

export default {
    name: 'FirstSignCard',
    props: {
        movie: Object,
    },
    methods: {
        clickCard() {
            this.$emit('movieId', this.movie)
        }
    }
}
</script>

<style>
</style>