<template>
  <div class="wrapper-project-form"
    :class="{'is-hidden': isHidden}">
    <div class="card-brand card-project">
      <div class="card-heading">
        {{genObjTitle('Project')}}
      </div>
      <CvObjectsControls
        deleteMessage="Project will be removed"
        :obj="obj"
        :resource="Project"
        @move="handleMove"
        @hide="handleHide"
        @deleted="handleDeleted"/>
      <div class="is-clearfix"></div>
      <div class="columns">
        <div class="column is-8">
          <b-field label="Project Title">
            <b-input placeholder="My Project"
              v-model="obj.title"
              :maxlength="100"
              :has-counter="false"></b-input>
          </b-field>
        </div>

        <div class="column is-4">
          <b-field label="Tag">
            <b-input placeholder="Work/Personal"
              v-model="obj.tag"
              :maxlength="20"
              :has-counter="false"></b-input>
          </b-field>
        </div>
      </div>

      <div class="columns">
        <div class="column is-6">
          <b-field label="Project website">
            <b-input placeholder="http//example.com"
              v-model="obj.website"
              :maxlength="1000"
              :has-counter="false"></b-input>
          </b-field>
        </div>

        <div class="column is-6">
          <b-field label="Your Role">
            <b-input placeholder="Frontend Developer"
              v-model="obj.role"
              :maxlength="100"
              :has-counter="false"></b-input>
          </b-field>
        </div>
      </div>

      <b-field label="Technology Stack"
        :class="{'is-invalid': User.htmlTextareaInvalid(obj.stack)}"
        :message="User.htmlTextareaMessage(obj.stack)">
        <div class="editor-wrapper">
          <vue-editor id="id-project-stack"
            v-model="obj.stack"
            :editor-toolbar="editorToolbar"></vue-editor>
        </div>
      </b-field>

      <b-field label="Role Scope"
        :class="{'is-invalid': User.htmlTextareaInvalid(obj.scope)}"
        :message="User.htmlTextareaMessage(obj.scope)">
        <div class="editor-wrapper">
          <vue-editor id="id-project-scope"
            v-model="obj.scope"
            :editor-toolbar="editorToolbar"></vue-editor>
        </div>
      </b-field>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import conf from '../conf'

import cvObjectsMixin from '../mixins/cvObjectsMixin'

import { VueEditor } from 'vue2-editor'

import CvObjectsControls from './CvObjectsControls'

export default {
  name: 'ProjectForm',

  mixins: [cvObjectsMixin],

  components: { VueEditor, CvObjectsControls },

  props: {
    obj: { type: Object, default () { return {} } },
    index: { type: Number, default: 1 },
  },

  data () {
    return {
      editorToolbar: conf.EDITOR_TOOLBAR,
    }
  },

  computed: {
    ...mapState(['User', 'Project']),
  },
}
</script>

<style scoped lang="stylus">
.card-project
  margin-bottom 20px
</style>
