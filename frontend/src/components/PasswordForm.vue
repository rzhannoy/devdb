<template>
  <div class="wrapper-password-form">
    <form class="menu-form">
      <!-- r start -->
      <div class="columns">
        <div class="column">
          <b-field
            :class="{'is-invalid': errors.has('oldPassword')}"
            :message="errors.first('oldPassword')">
            <b-input name="oldPassword" placeholder="Old password"
              v-model="objData.old_password"
              v-validate="'required'">
            </b-input>
          </b-field>
        </div>

        <div class="column">
          <b-field
            :class="{'is-invalid': errors.has('newPassword')}"
            :message="errors.first('newPassword')">
            <b-input name="newPassword" placeholder="New password"
              v-model="objData.new_password"
              v-validate="'required'">
            </b-input>
          </b-field>
        </div>
      </div>
      <!-- r end -->
      <div class="actions">
        <button type="submit" class="button is-cta"
          :class="{'is-loading': isLoading}"
          @click.prevent="handleSubmit">
          Change
        </button>
        <button class="button is-text"
          v-if="!isLoading"
          @click.prevent="$emit('close')">
          Cancel
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import types from '../store/types'

export default {
  name: 'PasswordForm',

  data () {
    return {
      isLoading: false,
      objData: {},
    }
  },

  computed: {
    ...mapState(['User']),
  },

  methods: {
    handleSubmit () {
      this.$validator.validateAll().then((valid) => {
        if (valid) {
          this.isLoading = true
          this.User
            .post('change-password/', this.objData)
            .then((res) => {
              console.log('SUCCESS', res)
              this.isLoading = false
              this.$emit('close')
              this[types.SHOW_SUCCESS_MESSAGE]({ message: 'Password changed!' })
            })
            .catch((err) => {
              console.log('ERROR', err)
            })
        }
      })
    },

    ...mapMutations([types.SHOW_SUCCESS_MESSAGE]),
  },
}
</script>

<style scoped lang="stylus">
.actions
  margin-top 0
</style>
