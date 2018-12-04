<template>
  <div class="wrapper-profile-form form-brand">
    <div class="actions-fixed">
      <button class="button is-cta"
        :class="{'is-loading': isLoading}"
        @click="handleSubmit">
        Save
      </button>
      <router-link class="button is-text"
        target="_blank"
        :class="{'disabled': isLoading}"
        :to="{ name: 'profile', params: { handle: objData.handle } }">
        View
      </router-link>
    </div>
    <Column>
      <div class="notification is-brand mbb"
        v-if="notifications.profileEditIntro">
        <button class="delete"
          @click="setNotifications({ data: { profileEditIntro: false } })"></button>
        All fields are optional!
      </div>
      <form class="cv-form">

        <div class="card-brand">
          <div class="columns">
            <div class="column">
              <b-field label="First Name">
                <b-input placeholder="John/Jane"
                  v-model="objData.first_name"
                  :maxlength="50"
                  :has-counter="false"></b-input>
              </b-field>
            </div>
            <div class="column">
              <b-field label="Last Name">
                <b-input placeholder="Doe"
                  v-model="objData.last_name"
                  :maxlength="50"
                  :has-counter="false"></b-input>
              </b-field>
            </div>
          </div>
        </div>

        <CvGeneralInfoForm
          :obj="objData.cv"/>

        <SkillGroupForm v-for="(skillGroup, index) in obj.cv.skill_groups"
          :key="handleObjKey(skillGroup)" :obj="skillGroup"
          :index="index"
          :id="genId(skillGroup, 'skillGroup')"
          @move="handleSkillGroupMove"
          @deleted="handleSkillGroupDeleted"/>
        <div class="add-card-button">
          <button class="button is-light"
            @click.prevent="handleAddSkillGroup">
            Add Skills Card
          </button>
        </div>

        <CvWillingToTryWrapper :obj="objData.cv"/>

        <ProjectForm v-for="(project, index) in objData.cv.projects"
          :key="handleObjKey(project)" :obj="project"
          :index="index"
          :id="genId(project, 'project')"
          @move="handleProjectMove"
          @deleted="handleProjectDeleted"/>
        <div class="add-card-button">
          <button class="button is-light"
            @click.prevent="handleAddProject">
            Add Project Card
          </button>
        </div>

        <div class="card-brand">
          <CvOtherDetailsWrapper :obj="objData.cv"/>
          <div class="label">Footer Links</div>
          <div class="columns-skills">
            <Draggable
              v-model="objData.cv.links"
              :options="draggableOptions"
              @end="reorderObjs(objData.cv.links)">
              <LinkForm v-for="(link, index) in objData.cv.links"
                :key="handleObjKey(link)" :obj="link"
                :index="index"
                @deleted="handleLinkDeleted"/>
            </Draggable>
            <div class="mt5">
              <button class="button is-card"
                @click.prevent="handleAddLink">
                Add Link
              </button>
            </div>
          </div>
        </div>
      </form>
    </Column>
  </div>
</template>

<script>
import _ from 'lodash'
import arrayMove from 'array-move'
import vueScrollTo from 'vue-scrollto'

import { mapState, mapMutations, mapActions } from 'vuex'
import types from '../store/types'

import cvObjectsMixin from '../mixins/cvObjectsMixin'

import Draggable from 'vuedraggable'

import Column from './UIColumn'
import CvGeneralInfoForm from './CvGeneralInfoForm'
import CvWillingToTryWrapper from './CvWillingToTryWrapper'
import CvOtherDetailsWrapper from './CvOtherDetailsWrapper'
import SkillGroupForm from './SkillGroupForm'
import ProjectForm from './ProjectForm'
import LinkForm from './LinkForm'

export default {
  name: 'ProfileForm',

  mixins: [cvObjectsMixin],

  components: {
    Column, CvOtherDetailsWrapper,
    SkillGroupForm, ProjectForm,
    LinkForm, Draggable,
    CvGeneralInfoForm, CvWillingToTryWrapper,
  },

  props: {
    obj: { type: Object, default () { return {} } }, // User
  },

  created () {
    this.init()
  },

  // destroyed () {
  //   clearTimeout(this.handleSubmitTimer)
  // },

  watch: {
    obj: 'updateObjData',
  },

  data () {
    return {
      isLoading: false,
      objData: {},
      draggableOptions: conf.DRAGGABLE_OPTIONS,
    }
  },

  computed: {
    ...mapState(['notifications', 'User', 'user']),
  },

  methods: {
    updateObjData () {
      this.objData = _.assign({}, this.obj)
    },

    init () {
      this.updateObjData()
      this[types.FETCH_USER]({ currentUser: true }).then(
        this.genInitData
      )

      // this.handleSubmitTimer = setInterval(() => {
      //   this.handleSubmit('auto')
      // }, 30000)
    },

    genInitData () {
      const cv = this.objData.cv

      if (!cv.skill_groups.length) {
        this.handleAddSkillGroup(null, true)
      }

      if (!cv.projects.length) {
        this.handleAddProject(null, true)
      }
    },

    handleSubmit (mode) {
      const validator = this.User.validate(this.objData)

      if (validator.isValid) {
        this.isLoading = true
        this[types.UPDATE_PROFILE]({ data: this.objData })
          .then(() => {
            const message = mode === 'auto' ? 'Auto-saved!' : 'Saved!'

            this.isLoading = false
            this[types.SHOW_SUCCESS_MESSAGE]({
              message,
              duration: 800,
            })
          })
      }
    },

    genId (obj, prefix, withHash) {
      let id = obj.id ? `id-${prefix}-${obj.id}` : obj.key
      id = withHash ? `#${id}` : id
      return id
    },

    scrollToAdded (elem) {
      this.$nextTick(() => {
        vueScrollTo.scrollTo(elem, 400, { offset: -100 })
      })
    },

    handleAddSkillGroup (e, noScroll) {
      const cv = this.objData.cv
      const skillGroup = {
        cv: cv.resource_uri,
        key: `sg_${this.$utils.genRandomString()}`,
        position: cv.skill_groups.length + 1,
        skills: [],
      }

      this.objData.cv.skill_groups.push(skillGroup)

      if (!noScroll) {
        this.scrollToAdded(this.genId(skillGroup, 'skillGroup', true))
      }
    },

    handleSkillGroupMove (data) {
      const to = data.direction === 'up'
        ? data.index - 1
        : data.index + 1

      this.objData.cv.skill_groups = arrayMove(
        this.objData.cv.skill_groups,
        data.index,
        to
      )
      this.reorderObjs(this.objData.cv.skill_groups)
    },

    handleSkillGroupDeleted (key) {
      this.objData.cv.skill_groups = _.filter(
        this.objData.cv.skill_groups, (obj) => {
          return obj.key !== key
        }
      )
    },

    handleAddProject (e, noScroll) {
      const cv = this.objData.cv
      const project = {
        cv: cv.resource_uri,
        key: `pr_${this.$utils.genRandomString()}`,
        position: cv.projects.length + 1,
      }

      this.objData.cv.projects.push(project)

      if (!noScroll) {
        this.scrollToAdded(this.genId(project, 'project', true))
      }
    },

    handleProjectMove (data) {
      const to = data.direction === 'up'
        ? data.index - 1
        : data.index + 1

      this.objData.cv.projects = arrayMove(
        this.objData.cv.projects,
        data.index,
        to
      )
      this.reorderObjs(this.objData.cv.projects)
    },

    handleProjectDeleted (key) {
      this.objData.cv.projects = _.filter(
        this.objData.cv.projects, (obj) => {
          return obj.key !== key
        }
      )
    },

    handleAddLink () {
      const cv = this.objData.cv
      const link = {
        cv: cv.resource_uri,
        key: `li_${this.$utils.genRandomString()}`,
        position: cv.links.length + 1,
      }

      this.objData.cv.links.push(link)
    },

    handleLinkDeleted (key) {
      this.objData.cv.links = _.filter(
        this.objData.cv.links,
        (obj) => { return obj.key !== key }
      )
    },

    ...mapActions([types.UPDATE_PROFILE, types.FETCH_USER]),
    ...mapMutations([types.SET_NOTIFICATIONS, types.SHOW_SUCCESS_MESSAGE]),
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/common.styl"

.actions-fixed
  position fixed
  width 100%
  bottom 0
  left 0
  padding 16px 0 12px
  padding-left 250px
  background-color #fff
  z-index 10

  .button
    margin-right 25px

  .is-cta
    padding-left 50px
    padding-right 50px
    font-weight 500

  +$mobile-only()
    padding-left 24px

    .button
      margin-right 15px

    .is-cta
      padding-left 33px
      padding-right 33px
</style>
