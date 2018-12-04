<template>
  <div class="wrapper-willing-to-try">
    <div class="card-brand">
      <b-field label="Willing to try">
        <b-input placeholder="Node.js, Vue.js, Django" type="textarea"
          v-model="obj.willing_to_try"
          :maxlength="500"
          :has-counter="false"></b-input>
      </b-field>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CvWillingToTryWrapper',

  props: {
    obj: { type: Object, default () { return {} } }, // Cv
  },

  data () {
    return {}
  },
}
</script>

<style scoped lang="stylus">
</style>
