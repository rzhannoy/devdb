<template>
  <div class="wrapper-skill-group-form"
    :class="{'is-hidden': isHidden}">
    <div class="card-brand card-skills">
      <div class="card-heading">
        {{genObjTitle('Skills')}}
      </div>
      <CvObjectsControls
        deleteMessage="Skill Group will be removed"
        :obj="obj"
        :resource="SkillGroup"
        @move="handleMove"
        @hide="handleHide"
        @deleted="handleDeleted"/>
      <div class="columns">
        <div class="column is-6">
          <b-field label="Title">
            <b-input placeholder="Frontend"
              v-model="obj.title"
              :maxlength="100"
              ref="title"
              :has-counter="false"
              @blur="handleBlur"></b-input>
          </b-field>
        </div>
      </div>

      <div class="label mb0">Skills</div>
      <div class="columns-skills">
        <Draggable
          v-model="obj.skills"
          :options="draggableOptions"
          @end="reorderObjs(obj.skills)">
          <SkillForm v-for="(skill, index) in obj.skills"
            :key="handleObjKey(skill)" :obj="skill"
            :index="index"
            @deleted="handleSkillDeleted"/>
        </Draggable>
        <div class="mts">
          <button class="button is-card"
            @click.prevent="handleAddSkill">
            Add skill
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

import { mapState } from 'vuex'
import conf from '../conf'

import cvObjectsMixin from '../mixins/cvObjectsMixin'

import Draggable from 'vuedraggable'

import SkillForm from './SkillForm'
import CvObjectsControls from './CvObjectsControls'

export default {
  name: 'SkillGroupForm',

  mixins: [cvObjectsMixin],

  components: {
    SkillForm, Draggable,
    CvObjectsControls,
  },

  props: {
    obj: { type: Object, default () { return {} } }, // SkillGroup
    index: { type: Number, default: 1 },
  },

  data () {
    return {
      draggableOptions: conf.DRAGGABLE_OPTIONS,
      refocused: false,
    }
  },

  computed: {
    ...mapState(['SkillGroup']),
  },

  methods: {
    handleAddSkill () {
      const skill = {
        group: this.obj.resource_uri,
        key: `sk_${this.$utils.genRandomString()}`,
        position: this.obj.skills.length + 1,
        level: 1,
      }

      this.obj.skills.push(skill)
    },

    handleSkillDeleted (key) {
      this.obj.skills = _.filter(this.obj.skills, (obj) => {
        return obj.key !== key
      })
    },

    handleBlur (e) {
      if (this.refocused === false && e.target.value.length === 1) {
        this.$refs.title.focus()
        this.refocused = true
      }
    },
  },
}
</script>

<style scoped lang="stylus">
.card-skills
  margin-bottom 20px
</style>
