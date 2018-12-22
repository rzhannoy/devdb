<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import types from './store/types'

export default {
  name: 'app',

  created () { this[types.INIT_APP]() },

  methods: { ...mapActions([types.INIT_APP]) },
}
</script>

<style src="buefy/dist/buefy.css" lang="css">
</style>
<style src="bulma/css/bulma.min.css" lang="css">
</style>
<style src="./app.styl" lang="stylus">
</style>
