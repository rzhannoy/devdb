import _ from 'lodash'

import Vue from 'vue'

import types from './types'
import initialState from './state'

import UserResource from '../resources/user'
import MessageResource from '../resources/message'
import SkillResource from '../resources/skill'
import SkillGroupResource from '../resources/skillGroup'
import ProjectResource from '../resources/project'
import LinkResource from '../resources/link'

const DEFAULT_MESSAGE_DURATION = 3000

export default {
  [types.RESET_STATE] (state) {
    state = _.assign(state, initialState)
  },

  [types.INIT_HTTP] (state) {
    const hostname = document.location.hostname
    let apiUrl

    if (hostname.indexOf('localhost') > -1) {
      apiUrl = 'http://127.0.0.1:8000/api/'
    } else {
      apiUrl = 'https://api.devdb.io/'
    }

    const headers = {}

    if (state.user) {
      headers.Authorization = `ApiKey ${state.user.token}`
    }

    state.conf = { apiUrl, headers }
  },

  [types.INIT_RESOURCES] (state) {
    state.User = UserResource(state.conf)
    state.Message = MessageResource(state.conf)
    state.Skill = SkillResource(state.conf)
    state.SkillGroup = SkillGroupResource(state.conf)
    state.Project = ProjectResource(state.conf)
    state.Link = LinkResource(state.conf)
  },

  [types.SET_STATE_PROPERTY] (state, payload) {
    state[payload.property] = payload.value
  },

  [types.SHOW_ERROR_MESSAGE] (state, payload) {
    const duration = payload.duration ? payload.duration : DEFAULT_MESSAGE_DURATION

    Vue.toasted.error(payload.message, {
      duration: duration,
      icon: 'error',
    })
  },

  [types.SHOW_SUCCESS_MESSAGE] (state, payload) {
    const duration = payload.duration ? payload.duration : DEFAULT_MESSAGE_DURATION

    Vue.toasted.success(payload.message, {
      duration: duration,
      icon: 'check_circle',
    })
  },

  [types.SET_NOTIFICATIONS] (state, payload) {
    state.notifications = _.assign(
      state.notifications,
      payload.data
    )
  },

  [types.SET_USER] (state, payload) {
    state.user = _.assign({}, payload.user, {
      token: state.user.token,
    })
  },
}
