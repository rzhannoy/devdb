export default {
  computed: {
    isMobile () { return window.innerWidth < 768 },

    isAndroid () {
      const userAgent = navigator.userAgent || navigator.vendor || window.opera

      if (
        !/windows phone/i.test(userAgent) &&
        /android/i.test(userAgent)
      ) {
        return true
      }

      return false
    },
  },

  methods: {
    disableLoading () { this.isLoading = false },

    handleObjKey (obj) {
      return obj.key ? obj.key : `${obj.id}_${this.$utils.genRandomString()}`
    }
  },
}
