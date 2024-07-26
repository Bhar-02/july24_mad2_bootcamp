<template>
    <h1>login page</h1>
    <form>
        <input type="text" placeholder="email" v-model="this.name">
        <input type="text" placeholder="password" v-model="this.desc">
        <button type="button" @click="AddCategoryfn">add category</button>
    </form>
    <p>{{ var12 }}</p>
    

</template>

<script>
// from flask_restful import Resource
import axios from 'axios';
export default {
    name: 'loginview',
    data() {
        return {
            name: null,
            desc: null,
            var12: null
        }
    },
    methods: {
        printonconsole() {
            console.log("name: ", this.name);
            console.log("desc: ", this.desc);
    },
    AddCategoryfn(){
        axios
            .post('http://localhost:5000/api/login', {
                email: this.name,
                password: this.desc
            })
            .then(response => {
                console.log("response block", response)
                if (response.status == 200) {
                    this.var12 = response.data
                    this.name = null
                    this.desc = null
                    localStorage.setItem('authToken', response.data.authToken)
                    this.$router.push('/activate')
                }
            })
            .catch(error => {
                console.log("error block", error)
            })
    }
}

}
</script>

<style>
</style>