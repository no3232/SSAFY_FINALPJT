<template>
<div class="col-3 my-2">
    <div class="card h-100" id="FirstSigncard"  @click="clickCard">
    <img class="h-100 rounded-start card-img" :src="'https://image.tmdb.org/t/p/w500/'+ `${movie?.poster_path}`" alt="">
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