<template>
  <div class="wrapper-message-form">
    <form class="menu-form">
      <b-field
        :class="{'is-invalid': errors.has('message')}"
        :message="errors.first('message')">
        <b-input name="message" type="textarea"
          maxlength="500"
          v-model="objData.message"
          v-validate="'required'"
          :has-counter="false">
        </b-input>
      </b-field>
      <div class="actions">
        <button type="submit" class="button is-cta"
          :class="{'is-loading': isLoading}"
          @click.prevent="handleSubmit">
          Send
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
import _ from 'lodash'
import { mapState, mapMutations } from 'vuex'
import types from '../store/types'

export default {
  name: 'MessageForm',

  props: {
    toId: { type: Number, required: true }, // User.id
  },

  data () {
    return {
      isLoading: false,
      objData: {},
    }
  },

  computed: {
    ...mapState(['Message']),
  },

  methods: {
    handleSubmit () {
      this.$validator.validateAll().then((valid) => {
        if (valid) {
          const data = _.assign({}, this.objData, { to_id: this.toId })

          this.isLoading = true
          this.Message
            .post('', data)
            .then(() => {
              this.isLoading = false
              this.$emit('close')
              this[types.SHOW_SUCCESS_MESSAGE]({ message: 'Message sent' })
            })
        }
      })
    },

    ...mapMutations([types.SHOW_SUCCESS_MESSAGE]),
  },
}
</script>

<style scoped lang="stylus">
</style>
