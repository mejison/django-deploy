<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>AUCTION WEBSITE</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="What are you looking for?" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <router-link to="/create-auction" class="navbar-item">Create Auction</router-link>
          <router-link to="/" class="navbar-item">View Auctions</router-link>
          <router-link to="/my-auction" class="navbar-item">My Auction</router-link>


          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>

<section class="section">
  <router-view/>
</section>

<footer class="footer">
  <p class="has-text-centered">AUCTION WEBSITE</p>
</footer>
 </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      showMobileMenu: false
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
  },
  computed: {
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>
