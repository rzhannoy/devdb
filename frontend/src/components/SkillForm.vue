<template>
  <div class="wrapper-skill-form wrapper-draggable-form"
    :class="{'is-hidden': isHidden}">
    <div class="columns">
      <div class="column drag-handle is-1">
        <i class="material-icons">drag_handle</i>
        <a href="" class="link-red is-pulled-right mobile-show"
          @click.prevent="handleObjDelete(Skill, 'Skill will be removed')">
          <i class="material-icons">delete_outline</i>
        </a>
      </div>
      <div class="column col-upper is-6">
        <b-field>
          <b-input placeholder="Skill name"
            v-model="obj.title"
            :maxlength="100"
            :has-counter="false"></b-input>
        </b-field>
      </div>
      <div class="column is-4">
        <b-field>
          <b-select placeholder="Experience"
            v-model="obj.level">
            <option v-for="(value, key) in Skill.LEVEL_OPTIONS"
              :key="key" :value="key">
              {{value}}
            </option>
          </b-select>
        </b-field>
      </div>
      <div class="column col-controls is-1 mobile-hide">
        <a href="" class="link-red"
          @click.prevent="handleObjDelete(Skill, 'Skill will be removed')">
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
  name: 'SkillForm',

  mixins: [cvObjectsMixin],

  props: {
    obj: { type: Object, default () { return {} } }, // Skill
    index: { type: Number, default: 1 },
  },

  computed: {
    ...mapState(['Skill']),
  },
}
</script>

<style scoped lang="stylus">
</style>
