<template>
  <div>
    <span 
        v-for="(actor, idx) in movie[actors]"
        :key="idx"
        class="actors">{{actor}}
    >
    </span>
  </div>
</template>

<script>
export default {
    name: 'Actors',
    props: {
        movie:Object
    }
}
</script>

<style>
  .actors {
    margin: 5px 10px;
    font-size: 30px;
  }
</style>