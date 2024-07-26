import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddCategory from '../views/addCategory.vue'
import activate from '../views/activate.vue'



const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/addCategory',
    name: 'addCategory',
    component: AddCategory
  },
  {
    path: '/editCategory/:bootcampId',
    name: 'editCategory',
    component: () => import('@/views/editCategory.vue')
  },
  {
    path: '/addProduct',
    name: 'addProduct',
    component: () => import('@/views/addProduct.vue')
  },
  {
    path: '/',
    name: 'adminDash',
    component: () => import('@/views/adminDashboard.vue')
  },
  {
    path: '/activate',
    component: activate
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/loginView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
