<template>
    <!-- 테이블 꾸미기 -->
      <tr class="myReview_tr" @click="goToReview">
        <th style="width: 10%" scope="row">{{review.user.username}}</th>
        <td style="width: 45%">{{review.title}}</td>
        <td style="width: 30%">{{review.movie.title}}</td>
        <td style="width: 15%">{{review.created_at.slice(0, 10)}}</td>
      </tr>
</template>

<script>
export default {
  name:'MyReview',
  props: {
    review:Object,
  },
  methods: {
    goToReview() {
      this.$router.push({ name: "communitydetail", params: {movieid: this.review.movie.id ,reviewid: this.review.id }})
    }
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

  .table_body th,
  .table_body td {
    text-align: left;
  }

  .myReview_tr:hover {
    opacity: 0.7;
  }
</style>