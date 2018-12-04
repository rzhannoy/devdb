<template>
  <div class="wrapper-cv-general-info-form">
    <div class="card-brand">
      <div class="columns">
        <div class="column">
          <b-field label="Specialty">
            <b-input placeholder="Full-Stack Dev"
              v-model="obj.specialty"
              :maxlength="50"
              :has-counter="false"></b-input>
          </b-field>
        </div>

        <div class="column">
          <b-field label="Age">
            <b-input placeholder="29" type="number"
              v-model="obj.age"></b-input>
          </b-field>
        </div>
      </div>

      <div class="columns">
        <div class="column">
          <b-field label="Remote">
            <b-select placeholder="Ready to go remote?"
              v-model="obj.remote">
              <option v-for="(value, key) in User.REMOTE_VERBOSE"
                :key="key"
                :value="key">
                {{value}}
              </option>
            </b-select>
          </b-field>
        </div>

        <div class="column">
          <b-field label="Relocation">
            <b-select placeholder="Ready to relocate?"
              v-model="obj.relocation">
              <option v-for="(value, key) in User.RELOCATION_VERBOSE"
                :key="key"
                :value="key">
                {{value}}
              </option>
            </b-select>
          </b-field>
        </div>
      </div>

      <div class="columns">
        <div class="column">
          <b-field label="City">
            <b-input placeholder="New York"
              v-model="obj.city"
              :maxlength="50"
              :has-counter="false"></b-input>
          </b-field>
        </div>

        <div class="column">
          <b-field label="Languages">
            <b-input placeholder="EN, RU"
              v-model="obj.languages"
              :maxlength="50"
              :has-counter="false"></b-input>
          </b-field>
        </div>
      </div>

      <div class="columns">
        <div class="column">
          <b-field label="Timezone">
            <b-input placeholder="UTC+7"
              v-model="obj.timezone"
              :maxlength="20"
              :has-counter="false"></b-input>
          </b-field>
        </div>

        <div class="column">
          <b-field label="Gender">
            <b-select placeholder="Select your gender"
              v-model="obj.gender">
              <option v-for="(value, key) in User.GENDERS_VERBOSE"
                :key="key"
                :value="key">
                {{value}}
              </option>
            </b-select>
          </b-field>
        </div>
      </div>

      <b-field label="Introduction Text"
        :class="{'is-invalid': User.htmlTextareaInvalid(obj.introduction)}"
        :message="User.htmlTextareaMessage(obj.introduction)">
        <div class="editor-wrapper">
          <vue-editor id="id-cv-introduction"
            v-model="obj.introduction"
            :editor-toolbar="editorToolbar"></vue-editor>
        </div>
      </b-field>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import conf from '../conf'

import { VueEditor } from 'vue2-editor'

export default {
  name: 'CvGeneralInfoForm',

  components: { VueEditor },

  props: {
    obj: { type: Object, default () { return {} } }, // Cv
  },

  data () {
    return {
      editorToolbar: conf.EDITOR_TOOLBAR,
    }
  },

  computed: {
    ...mapState(['User']),
  },
}
</script>

<style scoped lang="stylus">
</style>
