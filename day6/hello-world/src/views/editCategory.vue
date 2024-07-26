<template>
    <h2>edit category with id: {{ this.id }}</h2>
    <form>
        <input type="text" placeholder="name field" v-model="this.name">
        <input type="text" placeholder="desc field" v-model="this.desc">
        <button type="button" @click="AddCategoryfn">add category</button>
    </form>
    <h1>{{ this.name }}
    {{ this.desc }}</h1>

    <p>{{ var12 }}</p>
    

</template>

<script>
// from flask_restful import Resource
import axios from 'axios';
export default {
    name: 'AddCategory',
    data() {
        return {
            name: null,
            desc: null,
            var12: null,
            token: null,
            id: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken')
        this.id = this.$route.params.bootcampId
        if (!this.token) {
            this.$router.push('/login')
        }
        this.getCategoryfn()
    },

    methods: {
        printonconsole() {
            console.log("name: ", this.name);
            console.log("desc: ", this.desc);
    },
    AddCategoryfn(){
        axios
            .put(`http://localhost:5000/api/category/${this.id}`, {
                name: this.name,
                description: this.desc
            }, {headers: {Authorization: `${this.token}`}})
            .then(response => {
                console.log("response block", response)
                if (response.status == 201) {
                    this.var12 = response.data
                    this.name = null
                    this.desc = null
                    this.$router.push('/')
                }
            })
            .catch(error => {
                console.log("error block", error)
            })
    },
    getCategoryfn(){
        axios
            .get(`http://localhost:5000/api/category/${this.id}`,
            {headers: {Authorization: `${this.token}`}})
            .then(response => {
                console.log("response block", response)
                if (response.status == 200) {
                    this.var12 = response.data
                    this.name = response.data.data.name
                    this.desc = response.data.data.description
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