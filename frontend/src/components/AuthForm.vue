<template>
  <div class="wrapper-auth-form">
    <form>
      <b-field
        :class="{'is-invalid': errors.has('email')}"
        :message="errors.first('email')">
        <b-input name="email" placeholder="email" type="email"
          maxlength="254"
          v-model="objData.email"
          v-validate="'required|email'"
          :has-counter="false">
        </b-input>
      </b-field>
      <b-field v-if="mode === 'signUp'"
        :class="{'is-invalid': errors.has('handle')}"
        :message="errors.first('handle')">
        <b-input name="handle" placeholder="handle"
          maxlength="25"
          v-model="objData.handle"
          v-validate="'required|min:4'"
          :has-counter="false">
        </b-input>
      </b-field>
      <b-field
        :class="{'is-invalid': errors.has('password')}"
        :message="errors.first('password')">
        <b-input name="password" type="password" placeholder="password"
          v-model="objData.password"
          v-validate="'required'">
        </b-input>
      </b-field>
      <div class="mbs">
        <button type="submit" class="button is-cta is-fullwidth"
          :class="{'is-loading': isLoading}"
          @click.prevent="handleSubmit">
          {{actionLabel}}
        </button>
      </div>
      <div class="has-text-centered"
        v-if="!isLoading">
        <a href="" class="button is-text"
          @click.prevent="changeMode">
          {{altActionLabel}}
        </a>
      </div>
    </form>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import types from '../store/types';

export default {
  name: 'AuthForm',

  props: {
    mode: { type: String, default: 'signUp' },
  },

  data () {
    return {
      isLoading: false,
      objData: {},
    }
  },

  computed: {
    actionLabel () {
      return this.mode === 'signUp' ? 'Get Started' : 'Log In'
    },

    altActionLabel () {
      return this.mode === 'signUp' ? 'Log In' : 'Sign Up'
    },

    ...mapState(['User']),
  },

  methods: {
    changeMode () {
      const newMode = this.mode === 'signUp' ? 'logIn' : 'signUp'
      this.$emit('changeMode', newMode)
    },

    handleSubmit () {
      this.$validator.validateAll().then((valid) => {
        if (valid) {
          const action = this.mode === 'signUp'
            ? types.REGISTER 
            : types.LOGIN

          this.isLoading = true
          this[action]({ data: this.objData })
            .then(() => {
              this.isLoading = false
              this.$emit('success', this.mode)
            })
            .catch(() => { this.isLoading = false })
        }
      })
    },

    ...mapActions([types.REGISTER, types.LOGIN]),
  },
}
</script>

<style scoped lang="stylus">
.field
  margin-bottom 1.25rem !important
  text-align left !important
</style>
