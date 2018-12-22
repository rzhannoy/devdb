import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home'
import Profile from './views/Profile'
import ProfileEdit from './views/ProfileEdit'
import PrivacyPolicy from './views/PrivacyPolicy'
import Tos from './views/Tos'

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
    {
      path: '/i/privacy-policy',
      name: 'privacy-policy',
      component: PrivacyPolicy,
    },
    {
      path: '/i/terms-of-service',
      name: 'tos',
      component: Tos,
    },
  ]
})
