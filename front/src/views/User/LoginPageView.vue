<template>
<div class="container">
  <br>
  <br>
  <br>
  <h1 style="color:white;">Login</h1>
    <form @submit.prevent="logIn">
        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="userid" placeholder="이이디를 입력하세요" v-model="username">
            <label for="userid">아이디</label>
        </div>
        <div class="form-floating mb-3">
            <input type="password" class="form-control" id="userpassword1" placeholder="비밀번호를 입력하세요" v-model="password">
            <label for="userpassword1">비밀번호</label>
        </div>
        <input class="btn btn-primary" type="submit" value="로그인">
    </form>
</div>
</template>

<script>
export default {
    name: 'LoginPageView',
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        async logIn() {
            const username = this.username
            const password = this.password
            const userdata = {
                username, password
            }
            await this.$store.dispatch('LoginPath', userdata)
            if (this.$store.getters.userPkGetters !== null){
                this.$router.push({name: 'main'})
            }
        }
    }
}
</script>

<style>

</style>