<template>
  <div class="container">
    <div class="row d-flex justify-content-between align-items-center" @click="recommentOpen = !recommentOpen">
    <!-- 댓글 -->
    <span class="col">{{ commentThis?.user.username }} 님</span>
    <span class="col"> {{ commentThis?.content}}</span>
    <div class="col">
        <button  @click.stop="updateCommentOpen = !updateCommentOpen">댓글수정</button>
        <button  @click.stop="deleteComment(commentThis.review, commentThis.id)">댓글삭제</button>
    </div>
    <!-- 댓글 수정폼 -->
    <form @submit.prevent="updateComment(commentThis.review, commentThis.id)" v-show="updateCommentOpen">
        <div class="form-floating m-3">
            <input type="text" class="form-control" id="updateCommentInput" placeholder="댓글수정" v-model.trim="updateCommentInput">
            <label for="updateCommentInput" style="color: black">댓글수정</label>
        </div>
        <input class="btn btn-success" type="submit" value="댓글수정">
    </form>
    </div>
    <!-- 대댓글 -->
    <CommunityRecomment 
        v-for="recomment in recomments" 
        :key="recomment.id" 
        :recomment=recomment 
        @deleteRecomment="deleteReComment"
        @updateRecomment="updateRecomment"
    />
    <!-- 대댓글 작성폼 -->
    <form @submit.prevent="createRecomment" v-show="recommentOpen">
        <div class="form-floating m-3">
            <input type="text" class="form-control" id="recommentInput" placeholder="대댓글" v-model.trim="recommentInput">
            <label for="recommentInput" style="color: black">대댓글</label>
        </div>
        <input class="btn btn-success" type="submit" value="대댓글작성">
    </form>
    
  </div>
</template>

<script>
import axios from 'axios'
import CommunityRecomment from '@/components/Community/CommunityRecomment'

export default {
    name: 'CommunityComment',
    components: {
        CommunityRecomment
    },
    data() {
        return {
            // 댓글
            commentThis: this.comment,
            updateCommentOpen: false,
            updateCommentInput: this.comment.content,
            // 대댓글
            recommentOpen: false,
            recommentInput: null,
            updateRecommentOpen: false,
            updateRecommentInput: null,
        }
    },
    computed: {
        recomments() {
            return this.commentThis.childcomment
        },
    },
    props: {
        comment: Object,
    },
    methods: {
        // 댓글 수정
        updateComment(reviewId, commentId) {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = reviewId
            const commentid = commentId
            const content = this.updateCommentInput
            axios({
                method: 'put',
                url: `${DJANGO_API_URL}/api/v1/community/review/${reviewid}/comments/${commentid}/`,
                data: {
                    content
                },
            })
            .then((res) => {
                this.commentThis = res.data
                this.updateCommentOpen = false
            })
            .catch(err => alert(err))
        },
        // 댓글 삭제
        deleteComment(reviewId, commentId) {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = reviewId
            const commentid = commentId
            axios({
                method: 'delete',
                url: `${DJANGO_API_URL}/api/v1/community/review/${reviewid}/comments/${commentid}/`,
            })
            .then(res => {
                console.log(res.data)
                this.$emit('deleteComment', commentId)
            })
            .catch(err => console.log(err))
        },
        // 대댓글 작성
        createRecomment() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = this.comment.review
            const content = this.recommentInput
            const user = this.$store.getters.userPkGetters
            const parent = this.comment.id
            axios({
                method: 'post',
                url: `${DJANGO_API_URL}/api/v1/community/review/${reviewid}/comments/`,
                data: {
                    content, user, parent
                },
            })
            .then(res => {
                console.log(res.data)
                this.commentThis.childcomment.push(res.data)
                this.recommentInput = null
                this.recommentOpen = false
            })
            .catch(err => console.log(err))
        },
        // 대댓글 삭제
        deleteReComment(reviewId, commentId) {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = reviewId
            const commentid = commentId
            axios({
                method: 'delete',
                url: `${DJANGO_API_URL}/api/v1/community/review/${reviewid}/comments/${commentid}/`,
            })
            .then(res => {
                console.log(res.data)
                this.commentThis.childcomment = this.commentThis.childcomment.filter(el => {
                    if (el.id !== commentId) {
                        return el
                    }
                })
            })
            .catch(err => console.log(err))
        },
        // 대댓글 수정
        updateRecomment(reviewId, commentId, contentUp) {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = reviewId
            const commentid = commentId
            const content = contentUp
            axios({
                method: 'put',
                url: `${DJANGO_API_URL}/api/v1/community/review/${reviewid}/comments/${commentid}/`,
                data: {
                    content
                },
            })
            .then((res) => {
                this.commentThis.childcomment = this.commentThis.childcomment.filter(el => {
                    if (el.id === res.data.id) {
                        return res.data
                    } else {
                        return el
                    }
                })
            })
            .catch(err => alert(err))
        },
    }
}
</script>

<style>

</style>