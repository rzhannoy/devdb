<template>
  <div class="wrapper-cv-objects-controls">
    <div class="card-controls">
      <a href="" class="link-red"
        @click.prevent="handleObjDelete(resource, deleteMessage)">
        <i class="material-icons">delete_outline</i>
      </a>
      <a href=""
        @click.prevent="$emit('move', 'up')">
        <i class="material-icons">arrow_upward</i>
      </a>
      <a href=""
        @click.prevent="$emit('move', 'down')">
        <i class="material-icons">arrow_downward</i>
      </a>
    </div>
    <div class="is-clearfix"></div>
  </div>
</template>

<script>
import cvObjectsMixin from '../mixins/cvObjectsMixin'

export default {
  name: 'CvObjectsControls',

  mixins: [cvObjectsMixin],

  props: {
    obj: { type: Object, require: true },
    resource: { type: Function, required: true },
    deleteMessage: { type: String, default: 'Object will be removed' },
  },

  data () {
    return {}
  },
}
</script>

<style scoped lang="stylus">
</style>
