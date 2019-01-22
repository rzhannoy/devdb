<template>
  <div class="page-home">
    <div class="login-wrapper" v-if="!isConfirming">
      <router-link v-if="user" class="button is-white is-blue"
        :to="{ name: 'profile', params: { handle: user.handle } }">
        My profile
      </router-link>

      <button v-else class="button is-white"
        @click="initLogin">
        Log in
      </button>
    </div>

    <section class="hero is-fullheight">
      <div class="hero-body">
        <div class="container">
          <div class="lp-wrapper">
            <template v-if="isConfirming">
              <Spinner size="large" :speed="0.4"/>
            </template>

            <template v-else>
              <div v-if="!showAuthForm"
                class="lp-intro">
                <h1 class="title">
                  Modern & Opinionated<br>
                  CVs for Developers
                </h1>
                <div>
                  <a href="https://devdb.io/devdb" target="_blank"
                    class="button button-link is-main is-demo is-medium is-white">
                    See how it looks
                  </a>
                </div>
                <div>
                  <button class="button is-cta is-main is-medium has-shadow"
                    @click="showAuthForm = true">
                    Get started for free
                  </button>
                </div>
                <div class="users-count"
                  :class="{'is-invisible': !showUserCount}">
                  <small><b>{{userCount}}</b> already did</small>
                </div>
              </div>

              <div v-else>
                <AuthForm
                  :mode="authMode"
                  @changeMode="handleChangeMode"
                  @success="handleAuthSuccess"/>
              </div>
            </template>
          </div>
        </div>
      </div>

      <div class="hero-foot">
        <div class="foot-item">
          <a href="mailto:nrzhannoy@gmail.com">Contact</a>
        </div>
        <!-- <div class="foot-item">
          <a href="">Forgot password</a>
        </div> -->
        <div class="foot-item"
          v-if="!showLegal">
          <a href=""
            @click.prevent="showLegal = true">Legal</a>
        </div>
        <template v-else>
          <div class="foot-item">
            <router-link target="_blank"
              :to="{ name: 'privacy-policy' }">
              Privacy
            </router-link>
          </div>
          <div class="foot-item">
            <router-link target="_blank"
              :to="{ name: 'tos' }">
              Terms of Service
            </router-link>
          </div>
          <div class="foot-item">
            © 2019 DevDB
          </div>
        </template>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import types from '../store/types'

import Spinner from 'vue-simple-spinner'

import AuthForm from '@/components/AuthForm'

export default {
  name: 'home',

  components: { AuthForm, Spinner },

  data () {
    return {
      authMode: 'signUp',
      showAuthForm: false,
      isConfirming: false,
      showLegal: false,
      userCount: 0,
      showUserCount: false,
    }
  },

  created () {
    document.title = 'DevDB • Best CV builder for developers'
    this.handleEmailConfirmation()
    this.handleUserCount()
  },

  computed: {
    ...mapState(['user', 'User']),
  },

  methods: {
    handleUserCount () {
      this.User
        .get('count/')
        .then((res) => {
          this.userCount = res.data.count
          this.showUserCount = true
          setTimeout(() => { this.showUserCount = false }, 2500)
        })
    },

    initLogin () {
      this.authMode = 'login'
      this.showAuthForm = true
    },

    handleAuthSuccess (mode) {
      let routeParams = {
        name: 'profile',
        params: { handle: this.user.handle },
      }

      if (mode === 'signUp') {
        routeParams = { name: 'profile-edit' }
      }

      this.$router.push(routeParams)

      let partial1 = mode === 'signUp' ? 'to @devdb' : 'back'
      let partial2 = this.user.first_name ? `, ${this.user.first_name}` : ''
      const message = `Welcome ${partial1}${partial2}!`
      this[types.SHOW_SUCCESS_MESSAGE]({ message })
    },

    handleChangeMode (mode) { this.authMode = mode },

    handleEmailConfirmation () {
      const query = this.$route.query

      if (query.confirmation_token) {
        this.isConfirming = true
        this[types.CONFIRM_EMAIL]({ data: query })
          .then(() => {
            this.isConfirming = false
            this.$router.replace({ query: null })
            this.handleAuthSuccess('login')
          })
          .catch(() => { this.isConfirming = false })
      }
    },

    ...mapActions([types.CONFIRM_EMAIL]),
    ...mapMutations([types.SHOW_SUCCESS_MESSAGE]),
  },
}
</script>

<style lang="stylus">
@import "../styles/common.styl"

.page-home
  position relative

  +$mobile-only()
    .hero
      background-image: linear-gradient(0deg, #EFF1F5 0%, rgba(255,255,255,0.74) 100%)

  .is-white
    background transparent !important

.login-wrapper
  position absolute
  top 20px
  right 40px

  +$mobile-only()
    top 12px
    right 20px

.lp-wrapper
  margin -40px auto 0
  width 350px
  text-align left

  +$mobile-only()
    margin-top -60px
    width auto
    text-align center

.lp-intro
  h1.title
    margin-bottom 12px
    line-height 1.4

  .button
    height auto
    padding 9px 25px 10px

  .button.button-link
    +$desktop-only()
      padding-left 0
      padding-right 0
      padding-bottom 20px

    &:hover
      background-color #fff

.button.is-main
  padding 8px 20px
  font-weight 500
  font-size 18px

.button.is-demo
  color #004FD9 !important
  // font-weight bold

  &:hover
    opacity .75

.hero-foot
  padding-bottom 20px
  padding-right 15px
  text-align right

  +$mobile-only()
    text-align center
    padding-right 0

.foot-item
  display inline-block
  margin-right 25px
  color rgba(0,0,0,.4)
  font-size 14px

  a
    color rgba(0,0,0,.5)

    &:hover
      text-decoration underline

  +$mobile-only()
    margin-right 8px
    letter-spacing 0

    a
      letter-spacing 0

.users-count
  margin-top 12px
  color rgba(0,0,0,.6)
  line-height 1
</style>
