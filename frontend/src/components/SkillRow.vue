<template>
  <div class="wrapper-skill-row">
    <div class="skill-row">
      <div class="is-pulled-left">
        {{obj.title}}
      </div>
      <div class="skill-leds is-pulled-right">
        <div class="skill-led"
          v-for="i in fullLedsCount"
          :key="'f' + i"></div>
        <div class="skill-led empty"
          v-for="i in emptyLedsCount"
          :key="'e' + i"></div>
      </div>
      <div class="is-clearfix"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SkillRow',

  props: {
    obj: { type: Object, default () { return {} } }, // Skill
  },

  data () {
    return {}
  },
  
  computed: {
    fullLedsCount () {
      return this.obj.level < 5 ? this.obj.level : 4
    },

    emptyLedsCount () { return 4 - this.fullLedsCount },
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/common.styl"

.skill-row
  font-size 16px !important
  padding 12px 25px

  +$mobile-only()
    padding-left 15px
    padding-right 15px

  *
    line-height 1 !important
    letter-spacing 1px !important

.skill-led
  display inline-block
  margin-top 2px
  height 12px
  width 5px
  margin-left 5px
  border-radius 5px
  background-color #00F28D

  &.empty
    background-color #E3E3E3
</style>
