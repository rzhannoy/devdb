<template>
  <div class="page-cv-edit">
    <Header :obj="user"/>
    <ProfileForm :obj="user"/>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Header from '../components/UIHeader'
import ProfileForm from '../components/ProfileForm'

export default {
  name: 'profile-edit',

  components: { Header, ProfileForm },

  created () {
    document.title = 'Edit Your Profile | DevDB'
    this.init()
  },

  methods: {
    init () {
      if (!this.user) {
        this.$router.push({ name: 'home' })
      }
    },
  },

  computed: {
    ...mapState(['user']),
  },
}
</script>

<style scoped lang="stylus">
.page-cv-edit
  position relative
  padding-top 93px
  padding-bottom 50px
</style>
