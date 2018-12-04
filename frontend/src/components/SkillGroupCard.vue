<template>
  <div class="wrapper-skill-group-card wrapper-card">
    <div class="card-brand card-skills"
      :class="{'height-auto': showAll}">
      <div class="card-heading">
        {{obj.title || `Skill Group #${obj.id}`}}
      </div>
      <div class="is-clearfix"></div>
      <div class="skill-rows">
        <SkillRow v-for="(skill, i) in obj.skills.slice(0, 5)"
          v-if="skill.title"
          :key="skill.id"
          :obj="skill"
          :class="{'row-highlighted': i % 2 === 0}"/>
        <div v-if="showAll">
          <SkillRow v-for="(skill, i) in obj.skills.slice(5)"
            v-if="skill.title"
            :key="skill.id"
            :obj="skill"
            :class="{'row-highlighted': i % 2 !== 0}"/>
        </div>
        <div class="actions"
          v-if="obj.skills.length > 5 && !showAll"
          @click="showAll = true">
          <i class="material-icons">arrow_drop_down</i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SkillRow from './SkillRow'

export default {
  name: 'SkillGroupCard',

  components: { SkillRow },

  props: {
    obj: { type: Object, default () { return {} } }, // SkillGroup
  },

  data () {
    return {
      showAll: false,
    }
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/common.styl"

.card-skills
  padding 0
  height 288px
  margin-bottom 25px

  +$mobile-only()
    height auto

  &.height-auto
    height auto

  .card-heading
    font-size 14px
    margin 15px 25px 12px

    +$mobile-only()
      margin-left 15px
      margin-right 15px

  .actions
    text-align center
    padding-top 3px
    cursor pointer

    &:hover
      background #EBEBEB

    i
      line-height 1
      color #808080
      line-height 1

.row-highlighted
  background-color #FCFCFC
</style>
