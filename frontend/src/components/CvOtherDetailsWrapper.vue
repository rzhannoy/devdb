<template>
  <div class="wrapper-other-details">
    <b-field label="Other Details"
      :class="{'is-invalid': User.htmlTextareaInvalid(obj.other_details)}"
      :message="User.htmlTextareaMessage(obj.other_details)">
      <div class="editor-wrapper">
        <vue-editor id="id-other-details"
          v-model="obj.other_details"
          :editor-toolbar="editorToolbar"></vue-editor>
      </div>
    </b-field>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import conf from '../conf'

import { VueEditor } from 'vue2-editor'

export default {
  name: 'CvOtherDetailsWrapper',

  components: { VueEditor },

  props: {
    obj: { type: Object, default () { return {} } }, // Cv
  },

  data () {
    return {
      editorToolbar: conf.EDITOR_TOOLBAR,
    }
  },

  computed: {
    ...mapState(['User']),
  },
}
</script>

<style scoped lang="stylus">
</style>
