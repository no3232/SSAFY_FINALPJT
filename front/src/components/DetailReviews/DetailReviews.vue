<template>
  <tbody class="table_body">
    <tr class="reviews detailReview_tr"
      v-for="(review) in movie.reviews"
      :key="review.id"
      @click="GoToTheReview(review.movie.id, review.id)"
      >
      <th style="width: 10%" scope="row">{{review.user.username}}</th>
      <td style="width: 45%">{{review.title}}</td>
      <td style="width: 30%">{{review.movie.title}}</td>
      <td style="width: 15%">{{review.created_at.slice(0, 10)}}</td>
    </tr>
  </tbody>
</template>
  
<script>
export default {
    name: 'DetailReviews',
    props: {
        movie:Object,
    },
    methods: {
      GoToTheReview(movieid, reviewid) {
          this.$router.push({ name: 'communitydetail', params: {movieid, reviewid,} })
          this.$emit('closemodal')
      },
    }
}
</script>

<style>
  .reviews {
    border-radius: 5px;
    background-color: #1d1812;
    width: 90%;
    font-size: 18px;
    text-align: left;
  }

  #reviews_title {
      width: 200px;
      height: 30px;
      font-size: 20px;
      margin-left: 5px;
      margin-top: 10px;
      margin-bottom: 10px;
      background-color: green;
      color: white;
      border-radius: 5px;
  }

  #reviews_list {
      text-align: left;
  }

  #actor_link{
      text-decoration: none;
      color: black;
      font-weight: bold;
  }

  .review_detail_movie_title,
  .review_detail_title,
  .review_detail_user,
  .review_detail_created_at{
      border: 1px solid black;
  }

  .review_detail_movie_title{
    padding: 15px 30px;
  }

  .table_body th,
  .table_body td {
    text-align: left;
  }

  .detailReview_tr:hover {
    opacity: 0.7;
  }
</style>