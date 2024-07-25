<template>
    <form>
        <input type="number" placeholder="name field" v-model="this.name">
        <button type="button" @click="AddCategoryfn">add category</button>
    </form>
    <h1>{{ this.name }}
    {{ this.desc }}</h1>

    <p>{{ token }}</p>
    <p>{{ var12 }}</p>
    

</template>

<script>
// from flask_restful import Resource
import axios from 'axios';
export default {
    name: 'activate',
    data() {
        return {
            name: null,
            desc: null,
            var12: null,
            token: null
        }
    },
    created() {
        this.token = localStorage.getItem('authToken')
        if (!this.token) {
            this.$router.push('/login')
        }
    },
    methods: {
        printonconsole() {
            console.log("name: ", this.name);
            console.log("desc: ", this.desc);
    },
    AddCategoryfn(){
        axios
            .post('http://localhost:5000/api/activate', {
                id: this.name,
                desc: this.desc
            }, {headers: {Authorization: `${this.token}`}})
            .then(response => {
                console.log("response block", response)
                if (response.status == 200) {
                    this.var12 = response.data
                    this.name = null
                    this.desc = null
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