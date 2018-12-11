<template>
  <div class="wrapper-header">
    <header :class="{'auto-height': showMessageForm}">
      <Column>
        <div class="header-inner">
          <h1 class="title">
            {{User.genName(obj)}}
          </h1>
          <div class="header-menu">
            <template v-if="showProfileButtons">
              <router-link class="button is-white is-blue"
                :to="{ name: 'profile-edit' }">
                Edit
              </router-link>
              <button class="button is-white is-red"
                @click="handleLogout">
                Log out
              </button>
            </template>

            <router-link v-else-if="showViewButton"
              class="button is-cta is-outlined"
              :to="{ name: 'profile', params: { handle: user.handle } }">
              Back
            </router-link>

            <template v-else>
              <button v-if="!showMessageForm"
                class="button is-cta is-outlined"
                @click="showMessageForm = true">
                <span class="mobile-hide">Message</span>
                <i class="material-icons mobile-show">mail</i>
              </button>
            </template>
          </div>
        </div>
        <div class="is-clearfix"></div>
        <MessageForm v-if="showMessageForm"
          :toId="obj.id"
          @close="showMessageForm = false"/>
      </Column>
    </header>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import types from '../store/types'

import Column from './UIColumn'
import MessageForm from './MessageForm'

export default {
  name: 'Header',

  components: { Column, MessageForm },

  props: {
    obj: { type: Object, default () { return {} } }, // User
  },

  data () {
    return {
      showMessageForm: false,
    }
  },

  computed: {
    showProfileButtons () {
      const route = this.$route

      return this.user &&
        route.name === 'profile' &&
        route.params.handle === this.user.handle
    },

    showViewButton () {
      return this.user && this.$route.name === 'profile-edit'
    },

    ...mapState(['User', 'user']),
  },

  methods: {
    handleLogout () {
      this[types.RESET_STATE]()
      this.$router.push({ name: 'home' })
      this[types.SHOW_SUCCESS_MESSAGE]({ message: 'Logged out!' })
    },

    ...mapMutations([types.RESET_STATE, types.SHOW_SUCCESS_MESSAGE]),
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/common.styl"

header
  padding-top 20px
  position fixed
  width 100%
  height 68px
  top 0
  left 0
  background #fff
  z-index 10

  &.auto-height
    height auto

  .title
    margin-bottom 0
    overflow hidden
    white-space nowrap

.header-inner
  position relative

.header-menu
  background-color #fff
  position absolute
  top 0
  right 0

.button
  margin-left 8px

  +$mobile-only()
    margin-left 4px

    &.is-white
      padding-left 6px
      padding-right 6px
</style>
