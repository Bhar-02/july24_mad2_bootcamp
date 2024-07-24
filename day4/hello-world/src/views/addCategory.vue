<template>
    <form>
        <input type="text" placeholder="name field" v-model="this.name">
        <input type="text" placeholder="desc field" v-model="this.desc">
        <button type="button" @click="printonconsole">add category</button>
    </form>
    <h1>{{ this.name }}
    {{ this.desc }}</h1>
    

</template>

<script>
// from flask_restful import Resource
import axios from 'axios';
export default {
    name: 'AddCategory',
    data() {
        return {
            name: null,
            desc: null
        }
    },
    methods: {
        printonconsole() {
            console.log("name: ", this.name);
            console.log("desc: ", this.desc);
    }
}

}
</script>

<style>
</style>