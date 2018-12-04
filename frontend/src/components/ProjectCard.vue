<template>
  <div class="wrapper-project-card">
    <div class="card-brand card-project">
      <div class="card-heading">
        {{obj.title || `Project #${obj.id}`}}
      </div>
      <!-- <div class="is-clearfix mobile-show"></div> -->
      <span class="tag" v-if="obj.tag">
        {{obj.tag}}
      </span>
      <div class="is-clearfix"></div>
      <div class="project-website" v-if="obj.website">
        <a :href="obj.website" target="_blank" rel="nofollow">
          {{stripProtocol(obj.website)}}
        </a>
      </div>
      <div v-else class="mb20"></div>
      <div class="card-body">
        <div class="project-section" v-if="obj.role">
          <div class="section-content">
            <b>Role</b>: {{obj.role}}
          </div>
        </div>
        <div class="columns is-gapless"
          v-if="obj.stack || obj.scope">
          <div class="column column-left" v-if="obj.stack">
            <div class="project-section">
              <div class="section-heading">
                Stack
              </div>
              <div class="section-content" v-html="obj.stack">
              </div>
            </div>
          </div>

          <div class="column" v-if="obj.scope">
            <div class="project-section">
              <div class="section-heading">
                Scope
              </div>
              <div class="section-content" v-html="obj.scope">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectCard',

  props: {
    obj: { type: Object, default () { return {} } }, // Project
  },

  data () {
    return {}
  },

  methods: {
    stripProtocol (url) {
      return url.replace(/(^\w+:|^)\/\//, '')
    },
  },
}
</script>

<style scoped lang="stylus">
@import "../styles/common.styl"

.card-project
  margin-bottom 25px
  padding-top 25px
  padding-bottom 25px

  +$mobile-only()
    padding-top 20px
    padding-bottom 1px

  .card-heading
    font-size 16px
  
  .tag
    font-weight bold
    margin-left 12px
    background rgba(0,0,0,.08)

    // +$mobile-only()
    //   margin-top 8px
    //   margin-left 0

  .project-website
    margin-top 8px
    margin-bottom 20px

    a
      color #033fff
      font-size 18px

      &:hover
        text-decoration underline

  .card-body
    font-size 18px

  .columns
    margin-top 20px

    .column-left
      padding-right 20px !important

  .project-section >>>
    +$mobile-only()
      margin-bottom 20px

    .section-heading
      font-weight bold
      margin-bottom 5px

    ul
      margin-top 8px
      margin-left 1.2em !important
      line-height 1.66
      font-size 17px
</style>
