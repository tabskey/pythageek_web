<template>
  <div id="app">
       <div id="nav">
      <AppNav />
    </div>
    <router-view/>
    <AppFooter />
  </div>
</template>

<script>
import AppNav from './components/AppNav.vue'
import AppFooter from './views/AppFooter.vue'

export default {
  name: 'App',
  components: {
    AppNav,
    AppFooter
  }
}
</script>

<style>
#nav {
  background-color: rgb(121, 87, 213);
}

</style>
