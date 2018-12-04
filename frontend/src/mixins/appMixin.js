export default {
  methods: {
    disableLoading () { this.isLoading = false },

    handleObjKey (obj) {
      return obj.key ? obj.key : `${obj.id}_${this.$utils.genRandomString()}`
    }
  },
}
