import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home'
import Profile from './views/Profile'
import ProfileEdit from './views/ProfileEdit'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/:handle',
      name: 'profile',
      component: Profile,
    },
    {
      path: '/my/edit',
      name: 'profile-edit',
      component: ProfileEdit,
    },
  ]
})
