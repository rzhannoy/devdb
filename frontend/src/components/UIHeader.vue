<template>
  <div class="wrapper-header">
    <header :class="{
      'auto-height': anyFormActive,
      'header-compact': isCompact,
    }">
      <Column>
        <div class="header-inner">
          <h1 class="title">
            {{User.genName(obj)}}
          </h1>
          <div class="header-menu">
            <template v-if="showMenu">
              <b-dropdown v-if="!anyFormActive" position="is-bottom-left"
                :mobile-modal="false">
                <span slot="trigger" class="button is-white is-blue" href="">
                  Menu
                </span>

                <b-dropdown-item
                  :has-link="true">
                  <router-link 
                    :to="{ name: 'profile-edit' }">
                    Edit profile
                  </router-link>
                </b-dropdown-item>
                <b-dropdown-item
                  :has-link="true">
                  <router-link
                    :to="{ name: 'profile', params: { handle: user.handle } }">
                    View profile
                  </router-link>
                </b-dropdown-item>
                <!-- <b-dropdown-item
                  @click="showPasswordForm = true">
                  Change password
                </b-dropdown-item> -->
                <b-dropdown-item
                  @click="handleLogout">
                  Log out
                </b-dropdown-item>
              </b-dropdown>
              <!-- <router-link class="button is-white is-blue"
                :to="{ name: 'profile-edit' }">
                Edit
              </router-link>
              <button class="button is-white is-red"
                @click="handleLogout">
                Log out
              </button> -->
            </template>

            <!-- <router-link v-else-if="showViewButton"
              class="button is-cta is-outlined"
              :to="{ name: 'profile', params: { handle: user.handle } }">
              Back
            </router-link> -->

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
        <PasswordForm v-if="showPasswordForm"
          @close="showPasswordForm = false"/>
      </Column>
    </header>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import types from '../store/types'

import Column from './UIColumn'
import MessageForm from './MessageForm'
import PasswordForm from './PasswordForm'

export default {
  name: 'Header',

  components: {
    Column, MessageForm,
    PasswordForm,
  },

  props: {
    obj: { type: Object, default () { return {} } }, // User
  },

  data () {
    return {
      showMessageForm: false,
      showPasswordForm: false,
    }
  },

  computed: {
    anyFormActive () {
      return this.showMessageForm || this.showPasswordForm
    },

    showMenu () {
      const route = this.$route

      return route.name === 'profile-edit' || (this.user &&
        route.name === 'profile' &&
        route.params.handle === this.user.handle)
    },

    // showViewButton () {
    //   return this.user && this.$route.name === 'profile-edit'
    // },

    isCompact () {
      return this.$route.name === 'profile-edit' &&
        this.isMobile &&
        this.isAndroid
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

  &.header-compact
    padding-top 8px
    padding-bottom 8px
    height auto

    .title
      font-size 1.33rem

    .button
      height 1.5rem

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
