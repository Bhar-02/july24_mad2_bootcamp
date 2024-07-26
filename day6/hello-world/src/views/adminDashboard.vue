<template>
    <h1>Admin Dashboard</h1>

    <h2>category</h2>
    <table>
        <thead>
            <th>id</th>
            <th>name</th>
            <th>description</th>
            <th>status</th>
            <th>delete</th>
            <th>actions</th>
        </thead>
        <tbody>
            <tr v-for="row in categories" :key="row.id">

                <td>{{ row.id }}</td>
                <td>{{ row.name }}</td>
                <td>{{ row.description }}</td>
                <td>{{ row.status }}</td>
                <td>{{ row.delete }}</td>
                <td><router-link :to="{name: 'editCategory', params: {bootcampId: row.id}}">edit</router-link> 
                    | 
                    <a @click="deleteCategory(row.id)" v-if="!row.delete"> delete</a>
                </td>
            </tr>
        </tbody>
    </table>

    <h2>product</h2>
    <table>
        <thead>
            <th>id</th>
            <th>name</th>
            <th>description</th>
            <th>status</th>
            <th>actions</th>
        </thead>
        <tbody>
            <tr v-for="row in products" :key="row.id">
            <td>{{ row.id }}</td>
            <td>{{ row.name }}</td>
            <td>{{ row.description }}</td>
            <td>{{ row.status }}</td>
            <td><img :src="`http://localhost:8000/${row.id}.jpg`" height="20" width="20"  alt="prod img"></td>
            </tr>
        </tbody>
    </table>
    <!-- {{ categories }}
    {{ products }} -->
</template>

<script>
import axios from 'axios';
export default {
    name: 'AdminDashboard',
    data() {
        return {
            categories: null,
            products: null,
            var12: null,
            token: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken')
        if (!this.token) {
            this.$router.push('/login')
        }
        this.getCategoryfn()
        this.getProductsfn()
    },

    methods: {
    getCategoryfn(){
        axios
            .get(`http://localhost:5000/api/category`,
            {headers: {Authorization: `${this.token}`}})
            .then(response => {
                console.log("response block", response)
                if (response.status == 200) {
                    this.var12 = response.data
                    this.categories = response.data.data
                }
            })
            .catch(error => {
                console.log("error block", error)
            })
        },
        getProductsfn(){
        axios
            .get(`http://localhost:5000/api/product`,
            {headers: {Authorization: `${this.token}`}})
            .then(response => {
                console.log("response block", response)
                if (response.status == 200) {
                    this.var12 = response.data
                    this.products = response.data.data
                }
            })
            .catch(error => {
                console.log("error block", error)
            })
    },
    deleteCategory(id){
        axios
            .delete(`http://localhost:5000/api/category/${id}`,
            {headers: {Authorization: `${this.token}`}})
            .then(response => {
                console.log("response block", response)
                if (response.status == 201) {
                    this.getCategoryfn()
                }
            })
            .catch(error => {
                console.log("error block", error)
            })
    }
}

}
</script>