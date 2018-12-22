<template>
  <div class="wrapper-cv-tags">
    <div class="tags tags-medium">
      <div class="tag" v-if="obj.specialty">
        {{obj.specialty}}
      </div>
      <!-- <div class="tag" v-if="User.genAgeGender(obj)">
        {{User.genAgeGender(obj)}}
      </div> -->
      <div class="tag" v-if="User.shouldDisplay(obj.remote)">
        {{User.REMOTE_VERBOSE[obj.remote]}}
      </div>
      <div class="tag" v-if="User.shouldDisplay(obj.relocation)">
        {{User.RELOCATION_VERBOSE[obj.relocation]}}
      </div>
      <div class="tag" v-if="obj.timezone">
        {{obj.timezone}}
      </div>
      <div class="tag" v-if="obj.city">
        {{obj.city}}
      </div>
      <div class="tag" v-if="obj.languages">
        {{obj.languages}}
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'CvTags',

  props: {
    obj: { type: Object, default () { return {} } }, // Cv
  },

  data () {
    return {}
  },

  computed: {
    ...mapState(['User']),
  },
}
</script>

<style scoped lang="stylus">
</style>
