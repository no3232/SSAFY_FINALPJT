<template>
  <div style="height: 100%;" class="d-flex align-items-center justify-content-center">
    <div id="actors_title" class="col-3"><h4>Actor</h4></div>
    <div id="actors_list">
        <span
        v-for="(actor, idx) in movie.actors.slice(0,8)"
        :key="idx"
        class="actors">
          <a id="actor_link" class="btn btn-secondary" :href="'https://www.themoviedb.org/person/'+actor.id">
              {{actor.name}}
          </a>
        </span>
    </div>
  </div>
</template>

<script>
export default {
    name: 'ActorsSet',
    props: {
        movie:Object
    }
}
</script>

<style>
  .actors {
    margin: 0px 5px;
    font-size: 18px;
    text-align: left;
  }

  #actors_title {
      width: 80px;
      height: 90%;
      text-align: center;
      font-size: 20px;
      margin-top: 30px;
      padding-top: 50px;
      margin-bottom: 10px;
      background-color: #FF4301;
      color: black;
      border-radius: 5px;
      box-shadow: 5px 5px #ff4501a4;
  }

  #actors_list {
      margin-left: 10px;
      text-align: center;
      padding-top: 10px;
  }

  #actor_link{
      margin-top: 10px;
      height: 20% !important;
      text-decoration: none;
      color: black;
      font-weight: bold;
      font-size: 15px;
      background-color: #FA7D09;
      border: 1px solid transparent;
  }
  
  #actor_link:hover {
    opacity: 0.7;
  }
</style>