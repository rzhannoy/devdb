import { mapMutations } from 'vuex'
import types from '../store/types'

export default {
  props: {
    show: { type: Boolean, default: false },
  },

  data () {
    return {
      isLoading: false,
      objData: {},
    }
  },

  methods: {
    handleClose () {
      this.$emit('close')
    },

    ...mapMutations([types.SHOW_ERROR_MESSAGE, types.SHOW_SUCCESS_MESSAGE]),
  },
}
