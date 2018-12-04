<template>
  <div class="wrapper-cv-links">
    <footer>
      <div class="footer-section">
        <a class="item link" target="_blank" rel="nofollow"
          v-for="obj in objs"
          :key="obj.id"
          :href="obj.url">
          {{obj.title}}
        </a>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'CvLinks',

  props: {
    objs: { type: Array, default () { return [] } }, // Cv.links
  },

  data () {
    return {}
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/common.styl"

footer
  margin 40px 0 12px

  +$mobile-only()
    margin-bottom 0

.footer-section
  margin-bottom 12px

  .item
    margin-right 20px
    margin-bottom 12px
    display inline-block

  .subheading
    color rgba(0,0,0,.33)
    text-transform uppercase
    font-weight bold
    letter-spacing 1px

  .item.link
    color rgba(0,0,0,.66)

    &:hover
      text-decoration underline
</style>
