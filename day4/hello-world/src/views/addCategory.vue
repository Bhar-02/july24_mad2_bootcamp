<template>
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
            .post('http://localhost:5000/test', {
                name: this.name,
                desc: this.desc
            })
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