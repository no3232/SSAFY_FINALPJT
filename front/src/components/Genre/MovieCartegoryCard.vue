<template>
<div class="col-2">
  <div class="card border-0" id="cartegory-card" @click="getGenreMovie">
    <img class="card-img" :src="require(`@/assets/genre/${genre.id}.png`)">
  </div>
</div>
</template>

<script>
export default {
    name: 'MovieCartegoryCard',
    props: {
        genre: Object,
    },
    methods: {
      getGenreMovie() {
        this.$store.commit('SELECT_GENRE', this.genre.id)
        this.$store.commit('BG_GET', this.genre.id)
      }
    }
}
</script>

<style>
  .card-img {
    object-fit: cover;
  }
  #cartegory-card:hover {
    transform: scale(1.2);
    transition: transform 330ms ease-in-out;
    z-index: 1;
  }
</style>