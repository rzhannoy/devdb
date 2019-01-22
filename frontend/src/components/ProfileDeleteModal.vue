<template>
  <div class="wrapper-delete-profile-modal">
    <div class="modal"
      :class="{'is-active': show}">
      <div class="modal-background"
        @click="handleClose"></div>
      <div class="modal-content">
        <form>
          <div class="fs18 mbs">
            You are about to permanently delete your profile from DevDB 😞 This action cannot be undone. Please confirm it with your password:
          </div>
          <b-field
            :class="{'is-invalid': errors.has('password')}"
            :message="errors.first('password')">
            <b-input placeholder="Your password" type="password" name="password"
              v-model="password"
              v-validate="'required'"></b-input>
          </b-field>
          <b-field>
            <button class="button is-danger"
              :class="{'is-loading': isLoading}"
              @click.prevent="handleDelete">
              Delete forever
            </button>
            <button class="button is-text" v-if="!isLoading"
              @click.prevent="handleClose">
              Cancel
            </button>
          </b-field>
        </form>
      </div>
      <button class="modal-close is-large" aria-label="close"
        @click="handleClose"></button>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import types from '../store/types'

import modalMixin from '../mixins/modalMixin'

export default {
  name: 'ProfileDeleteModal',

  mixins: [modalMixin],

  data () {
    return {
      isLoading: false,
      password: '',
    }
  },

  computed: {
    ...mapState(['User']),
  },

  methods: {
    handleDelete () {
      this.$validator.validateAll().then((valid) => {
        if (valid) {
          this.isLoading = true
          this.User
            .post('delete/', { password: this.password })
            .then(() => {
              this[types.RESET_STATE]()
              this[types.SHOW_SUCCESS_MESSAGE]({ message: 'Your profile was deleted from DevDB' })
              this.$router.push({ name: 'home' })
            })
            .catch(() => {
              this.isLoading = false
              this[types.SHOW_ERROR_MESSAGE]({ message: `Password's incorrect` })
            })
        }
      })
    },

    ...mapMutations([types.RESET_STATE]),
  },
}
</script>

<style scoped lang="stylus">
.button
  margin-right 8px
</style>
