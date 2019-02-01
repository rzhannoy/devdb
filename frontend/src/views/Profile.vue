<template>
  <div class="page-cv">
    <div v-if="isFetching" class="spinner-wrapper">
      <Spinner size="large" :speed="0.4"/>
    </div>

    <div v-if="obj">
      <div v-if="obj.email_confirmed">
        <Header :obj="obj"/>
        <Column class="section-main content">
          <h2>Quickstart</h2>
          <CvTags class="tags"
            :obj="cv"/>
          <p class="mbb content-brand"
            v-if="cv.introduction"
            v-html="cv.introduction"></p>
          <h2>Skills</h2>
          <div class="tsp"
            v-if="cv.skills_intro"
            v-html="cv.skills_intro">
          </div>
          <div class="cards-float cards-skills">
            <SkillGroupCard v-for="obj in cv.skill_groups"
              :key="obj.id"
              :obj="obj"/>
          </div>
          <div class="is-clearfix"></div>
          <div class="skills-footnote" v-if="obj.show_skills_legend">
            <small>* Bars represent experience in years.</small>
          </div>
          <div class="is-clearfix"></div>
          <div class="card-brand card-open-to"
            v-if="cv.willing_to_try">
            <b>Willing to try</b>:
            {{cv.willing_to_try}}
          </div>
          <h2>Latest Projects</h2>
          <div class="cards-project">
            <ProjectCard v-for="obj in cv.projects"
              :key="obj.id"
              :obj="obj"/>
          </div>
          <div v-if="cv.other_details">
            <h2 class="mt50">Other Details</h2>
            <div class="other-details content-brand"
              v-html="cv.other_details">
            </div>
          </div>
          <CvLinks v-if="cv.links.length" :objs="cv.links"/>
        </Column>
      </div>

      <div v-else>
        <Column class="col-inactive">
          <div class="notification">
            <template v-if="isCurrentUser">
              Please open a confirmation link from your registration email to activate your profile.
            </template>

            <template v-else>This profile is inactive.</template>
          </div>
        </Column>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapMutations } from 'vuex'
import types from '../store/types'

import Spinner from 'vue-simple-spinner'

import Header from '../components/UIHeader'
import Column from '../components/UIColumn'
import CvTags from '../components/CvTags'
import SkillGroupCard from '../components/SkillGroupCard'
import ProjectCard from '../components/ProjectCard'
import CvLinks from '../components/CvLinks'

export default {
  name: 'profile',

  components: {
    Header, Column,
    CvTags, SkillGroupCard,
    ProjectCard, CvLinks,
    Spinner,
  },

  data () {
    return {
      isFetching: false,
    }
  },

  created () { this.init() },

  watch: {
    obj: 'setPageTitle',
  },

  computed: {
    handle () { return this.$route.params.handle },
    obj () { return this.profiles[this.handle] },
    cv () { return this.obj.cv },

    isCurrentUser () {
      return this.user && this.user.handle === this.handle
    },

    ...mapState(['profiles', 'user']),
  },

  methods: {
    init () {
      this.setPageTitle()

      if (!this.profiles[this.handle]) { this.isFetching = true }

      this[types.FETCH_USER]({ handle: this.handle })
        .then(() => { this.isFetching = false })
        .catch((err) => {
          this.isFetching = false

          if (err === 'not_found') {
            this.$router.push({ name: 'home' })
            this[types.SHOW_ERROR_MESSAGE]({ message: 'CV does not exist' })
          }
        })
    },

    setPageTitle () {
      if (this.obj && this.obj.first_name) {
        document.title = `${this.obj.first_name}'s CV | DevDB`
      }
    },

    ...mapMutations([types.SHOW_ERROR_MESSAGE]),
    ...mapActions([types.FETCH_USER]),
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/common.styl"

.spinner-wrapper
  padding-top 120px

.card-open-to
  margin-bottom 40px
  line-height 1.66

.section-main
  padding-top 96px !important

.other-details >>>
  font-size 18px
  color #000

  p
    margin-bottom .75em !important

.col-inactive
  padding-top 50px

  .notification
    text-align center
    font-size 20px
    letter-spacing 1px

.tsp >>>
  border-left 3px solid rgba(0,0,0,.08)
  padding-top 8px
  padding-bottom 8px
  padding-left 16px
  margin-top 25px
  margin-bottom 25px
  font-size 16px
  line-height 1.66
  color rgba(0,0,0,.66)

  +$mobile-only()
    margin-top 0px
    margin-bottom 20px
    font-size 15px

    br
      display none

.skills-footnote
  float left
  margin-top -18px
  margin-bottom 18px

  small
    color rgba(0,0,0,.5)
</style>
