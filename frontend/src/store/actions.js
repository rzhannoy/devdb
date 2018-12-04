import * as Promise from 'bluebird'
import _ from 'lodash'

import types from './types'

function getErrorData (error) {
  let err
  err = error.response || error
  err = err.data || err

  return err
}

export default {
  [types.INIT_APP] ({ commit }) {
    console.log('app: init')
    commit(types.INIT_HTTP)
    commit(types.INIT_RESOURCES)
  },

  [types.REGISTER] ({ state, commit, dispatch }, payload) {
    return new Promise((resolve, reject) => {
      state.User.post('register/', payload.data)
        .then((res) => {
          commit(types.SET_STATE_PROPERTY, {
            property: 'user',
            value: res.data.user,
          })
          dispatch(types.INIT_APP)
          resolve()
        })
        .catch((error) => {
          const data = getErrorData(error)

          if (data.message) {
            let message
            if (data.message.email_exists) {
              message = 'User with such email already exists'
            } else if (data.message.handle_exists) {
              message = 'User with such handle already exists'
            } else if (data.message.handle_length) {
              message = 'Please increase your handle to 4 characters minimum'
            }

            commit(types.SHOW_ERROR_MESSAGE, { message })
          } else {
            dispatch(types.HANDLE_GENERIC_ERROR, { error })
          }
          reject()
        })
    })
  },

  [types.LOGIN] ({ state, commit, dispatch }, payload) {
    return new Promise((resolve, reject) => {
      state.User.post('login/', payload.data)
        .then((res) => {
          commit(types.SET_STATE_PROPERTY, {
            property: 'user',
            value: res.data.user,
          })
          dispatch(types.INIT_APP)
          resolve()
        })
        .catch((error) => {
          const data = getErrorData(error)

          if (data.message === 'credentials_invalid') {
            const message = 'Invalid email or password'
            commit(types.SHOW_ERROR_MESSAGE, { message })
          } else {
            dispatch(types.HANDLE_GENERIC_ERROR, { error })
          }
          reject()
        })
    })
  },

  [types.CONFIRM_EMAIL] ({ state, commit, dispatch }, payload) {
    return new Promise((resolve, reject) => {
      state.User.post('confirm/', payload.data)
        .then((res) => {
          commit(types.SET_STATE_PROPERTY, {
            property: 'user',
            value: res.data.user,
          })
          resolve()
        })
        .catch((error) => {
          dispatch(types.HANDLE_GENERIC_ERROR, { error })
          reject()
        })
    })
  },

  [types.FETCH_USER] ({ commit, state, dispatch }, payload) {
    const handle = payload.currentUser
      ? state.user.handle
      : payload.handle

    return new Promise((resolve, reject) => {
      state.User.get(`${handle}/`)
        .then((res) => {
          if (payload.currentUser) {
            commit(types.SET_USER, { user: res.data })
          } else {
            const profiles = _.assign({}, state.profiles, {
              [handle]: res.data,
            })

            commit(types.SET_STATE_PROPERTY, {
              property: 'profiles',
              value: profiles,
            })
          }

          resolve()
        })
        .catch((error) => {
          if (error.response && error.response.status === 404) {
            reject('not_found')
          } else {
            dispatch(types.HANDLE_GENERIC_ERROR, { error })
            reject('generic_error')
          }
        })
    })
  },

  [types.UPDATE_PROFILE] ({ state, dispatch, commit }, payload) {
    return state.User
      .patch(`${payload.data.handle}/`, payload.data)
      .then((res) => {
        commit(types.SET_STATE_PROPERTY, {
          property: 'user',
          value: res.data,
        })
      })
      .catch((error) => {
        dispatch(types.HANDLE_GENERIC_ERROR, { error })
      })
  },

  [types.HANDLE_GENERIC_ERROR] ({ commit }, payload) {
    commit(types.SHOW_ERROR_MESSAGE, { message: 'Something went wrong, please try again later' })
    console.log('GENERIC ERROR', getErrorData(payload.error))
  },
}
