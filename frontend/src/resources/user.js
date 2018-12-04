import axios from 'axios'
import _ from 'lodash'

import vueScrollTo from 'vue-scrollto'

export default function (conf) {
  const resource = axios.create({
    baseURL: conf.apiUrl + 'user/',
    headers: conf.headers,
  })

  resource.genName = function (obj) {
    if (obj.first_name) {
      return `${obj.first_name} ${obj.last_name}`
    } else {
      return `Dev #${obj.id}`
    }
  }

  resource.DONT_DISPLAY = 'dd'

  resource.REMOTE_READY = 'rr'
  resource.REMOTE_ONLY = 'ro'
  resource.NO_REMOTE = 'nr'

  resource.REMOTE_VERBOSE = {
    [resource.DONT_DISPLAY]: `Don't display`,
    [resource.REMOTE_READY]: 'Remote OK',
    [resource.REMOTE_ONLY]: 'Remote-only',
    [resource.NO_REMOTE]: 'No remote',
  }

  resource.RELOCATION_READY = 'rr'
  resource.NO_RELOCATION = 'nr'

  resource.RELOCATION_VERBOSE = {
    [resource.DONT_DISPLAY]: `Don't display`,
    [resource.RELOCATION_READY]: 'Relocation OK',
    [resource.NO_RELOCATION]: 'No relocation',
  }

  resource.MALE = 'ma'
  resource.FEMALE = 'fe'
  resource.TRANS = 'tr'

  resource.GENDERS_SHORT = {
    [resource.MALE]: 'M',
    [resource.FEMALE]: 'F',
    [resource.TRANS]: 'T',
  }

  resource.GENDERS_VERBOSE = {
    [resource.DONT_DISPLAY]: `Don't display`,
    [resource.MALE]: 'Male',
    [resource.FEMALE]: 'Female',
    [resource.TRANS]: 'Trans*',
  }

  resource.CV_HTML_FIELDS = ['introduction', 'other_details']
  resource.PROJECT_HTML_FIELDS = ['scope', 'stack']
  resource.HTML_TEXTAREA_LIMIT = 1500

  resource.shouldDisplay = function (value) {
    return value !== resource.DONT_DISPLAY
  }

  resource.genAgeGender = function (cv) {
    let ageGender = ''

    if (cv.age) { ageGender += cv.age }
    if (cv.gender && resource.shouldDisplay(cv.gender)) {
      ageGender += resource.GENDERS_SHORT[cv.gender]
    }

    return ageGender
  }

  resource.validate = function (data) {
    const validator = {}

    _.forEach(resource.CV_HTML_FIELDS, (f) => {
      if (data.cv[f].length > resource.HTML_TEXTAREA_LIMIT) {
        validator[f] = true
      }
    })

    _.forEach(data.cv.projects, (obj) => {
      _.forEach(resource.PROJECT_HTML_FIELDS, (f) => {
        if (obj[f] && obj[f].length > resource.HTML_TEXTAREA_LIMIT) {
          if (!validator.projects) {
            validator.projects = {}
          }

          validator.projects[obj.id] = true
        }
      })
    })

    validator.isValid = _.isEmpty(validator)

    if (!validator.isValid) {
      setTimeout(() => {
        vueScrollTo.scrollTo('.is-invalid', 300, { offset: -80 })
      }, 100)
    }

    return validator
  }

  resource.htmlTextareaMessage = function (value) {
    const limit = resource.HTML_TEXTAREA_LIMIT

    if (value && value.length > limit / 2) {
      return `${value.length}/${limit}`
    }

    return null
  }

  resource.htmlTextareaInvalid = function (value) {
    return value && value.length > resource.HTML_TEXTAREA_LIMIT
  }

  return resource
}
