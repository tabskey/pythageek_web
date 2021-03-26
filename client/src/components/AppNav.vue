<template>
     <div class="column">
        <b-navbar class="navbar is-primary">
          <template #brand>
              <b-navbar-item tag="router-link" :to="{ path: '/theory' }">
                  <img src="../assets/Pythageek.png">
              </b-navbar-item>
          </template>
          <template #start>
           
              <b-navbar-item tag="router-link" :to="{ path: '/' }">
                  Home
              </b-navbar-item>
              <b-navbar-item tag="router-link" :to="{ path: '/theory' }">
                  Calculte it!
              </b-navbar-item>
              <b-navbar-item href="#">
                Last Results 
              </b-navbar-item>
              <b-navbar-dropdown label="About">
                  <b-navbar-item tag="router-link" :to="{ path: '/about' }">
                      After all, what's Pythagorean theorem?
                  </b-navbar-item>
                  <b-navbar-item href="https://github.com/tabskey">
                      Contact
                  </b-navbar-item>
              </b-navbar-dropdown>
          </template>
        </b-navbar>
      </div>
</template>
<script>
export default {
  name: "AppNav"
}



</script>
