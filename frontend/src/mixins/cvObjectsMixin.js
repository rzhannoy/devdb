import _ from 'lodash'

import { mapActions, mapMutations } from 'vuex'
import types from '../store/types'

export default {
  data () {
    return {
      isHidden: false,
    }
  },

  methods: {
    reorderObjs (objs) {
      _.forEach(objs, (obj, i) => { obj.position = i + 1 })
    },

    handleObjDelete (Resource, confirmMessage) {
      if (!this.obj.id || confirm(confirmMessage)) {
        if (this.obj.id) {
          this.isHidden = true
          this.$emit('hide')
          this[types.SHOW_SUCCESS_MESSAGE]({
            message: 'Removed!',
            duration: 800,
          })

          Resource.delete(`${this.obj.id}/`)
            .then(() => {
              this[types.FETCH_USER]({ currentUser: true })
            })
        } else {
          this.$emit('deleted', this.obj.key)
        }
      }
    },

    genObjTitle (objName) {
      return this.obj.title || `${objName} Card #${this.obj.position}`
    },

    handleMove (direction) {
      this.$emit('move', {
        direction,
        index: this.index,
        obj: this.obj,
      })
    },

    handleHide () {
      this.isHidden = true
    },

    handleDeleted (key) {
      this.$emit('deleted', key)
    },

    ...mapMutations([types.SHOW_SUCCESS_MESSAGE]),
    ...mapActions([types.FETCH_USER]),
  },
}
