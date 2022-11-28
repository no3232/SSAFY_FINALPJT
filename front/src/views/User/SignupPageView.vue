<template>
  <div class="container">
    <br>
    <br>
    <br>
    <h1 style="color:white;">Signup</h1>
    <form @submit.prevent="signUp">
        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="userid" placeholder="이이디를 입력하세요" v-model="username">
            <label for="userid">아이디</label>
        </div>
        <div class="form-floating mb-3">
            <input type="password" class="form-control" id="userpassword1" placeholder="비밀번호를 입력하세요" v-model="password1">
            <label for="userpassword1">비밀번호</label>
        </div>
        <div class="form-floating mb-3">
            <input type="password" class="form-control" id="userpassword2" placeholder="비밀번호를 입력하세요" v-model="password2">
            <label for="userpassword2">비밀번호 확인</label>
        </div>
        <input class="btn btn-primary" type="submit" value="회원가입">
    </form>
  </div>
</template>

<script>
export default {
    name: 'SignupPageView',
    data() {
        return {
            username: null,
            password1: null,
            password2: null,
        }
    },
    methods: {
        async signUp() {
            if (!this.username) {
                alert('아이디를 입력해주세요!')
                return
            } else if (!this.password1) {
                alert('비밀번호를 입력해주세요!')
                return
            } else if (!this.password2) {
                alert('확인할 비밀번호를 입력해주세요!')
                return
            }
            const username = this.username
            const password1 = this.password1
            const password2 = this.password2
            const userdata = {
                username, password1, password2
            }
            await this.$store.dispatch('SignupPath', userdata)
            await this.$router.push({name: 'firstselect'})
        }
    }
}
</script>

<style>

</style>