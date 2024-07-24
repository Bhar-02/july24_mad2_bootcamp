<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld1 msg="Welcome to Your Vue.js App anchit"/>
    <HelloWorld msg="Welcome to Your Vue.js App anchit"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld1 from '@/components/HelloWorld.vue'
import HelloWorld from '@/components/HelloWorld_copy.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld1,
    HelloWorld
  }
}
</script>
