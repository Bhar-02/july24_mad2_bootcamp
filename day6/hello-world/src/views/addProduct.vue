<template>
    <div id="addProd">
        <form>
            <input type="text" placeholder="Product Name" v-model="this.productName">
            <input type="text" placeholder="Product Description" v-model="this.productDesc">
            <input type="number" placeholder="Product stock" v-model="this.productStock">
            <input type="number" placeholder="Product Price" v-model="this.productPrice">
            <select name="category" v-model="this.cate_id">
                <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
            </select>
            <input type="file" @change="addImg">
            <button type="button" @click="addProduct">Add Product</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default{
    name: 'addProduct',
    data(){
        return{
            productName: '',
            productDesc: '',
            productStock: '',
            productPrice: '',
            categories: '',
            token: null,
            cate_id: null,
            image: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken')
        if (!this.token) {
            this.$router.push('/login')
        }
        this.getCategory()
    },
    methods:{
        getCategory(){
            axios
            .get(`http://localhost:5000/api/category`,
            {headers: {Authorization: `${this.token}`}})
            .then(response => {
                console.log("response block", response)
                if (response.status == 200) {
                    this.categories = response.data.data
                }
            })
            .catch(error => {
                console.log("error block", error)
            })
        },
        addProduct(){
            let formData = new FormData()
            formData.append('name', this.productName)
            formData.append('description', this.productDesc)
            formData.append('stock', this.productStock)
            formData.append('price', this.productPrice)
            formData.append('category_id', this.cate_id)
            formData.append('img', this.image)
            axios
            .post(`http://localhost:5000/api/product`,
            formData,
            {headers: {Authorization: `${this.token}`}})
            .then(response => {
                console.log("response block", response)
                if (response.status == 201) {
                    this.$router.push('/')
                }
            })
            .catch(error => {
                console.log("error block", error)
            }) 
        },
        addImg(event){
            // console.log(event)
            this.image = event.target.files[0]
            console.log(this.image);
        }
    },
}
</script>


<style></style>