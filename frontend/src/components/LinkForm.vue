<template>
  <div class="wrapper-link-form wrapper-draggable-form"
    :class="{'is-hidden': isHidden}">
    <div class="columns">
      <div class="column drag-handle is-1">
        <i class="material-icons">drag_handle</i>
        <a href="" class="link-red is-pulled-right mobile-show"
          @click.prevent="handleObjDelete(Link, 'Link will be removed')">
          <i class="material-icons">delete_outline</i>
        </a>
      </div>
      <div class="column col-upper is-4">
        <b-field>
          <b-input placeholder="Link Title"
            v-model="obj.title"></b-input>
        </b-field>
      </div>
      <div class="column is-6">
       <b-field>
         <b-input placeholder="Link URL"
          v-model="obj.url"></b-input>
       </b-field>
      </div>
      <div class="column col-controls is-1 mobile-hide">
        <a href="" class="link-red"
          @click.prevent="handleObjDelete(Link, 'Link will be removed')">
          <i class="material-icons">delete_outline</i>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

import cvObjectsMixin from '../mixins/cvObjectsMixin'

export default {
  name: 'LinkForm',

  mixins: [cvObjectsMixin],

  props: {
    obj: { type: Object, default () { return {} } }, // Link
    index: { type: Number, default: 1 },
  },

  computed: {
    ...mapState(['Link']),
  },
}
</script>

<style scoped lang="stylus">
</style>
