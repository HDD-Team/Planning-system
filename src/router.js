import { createRouter, createWebHistory } from 'vue-router'
import Events from './components/Events.vue'
import Table from './components/Table.vue'
import TeamDetails from './components/TeamDetails.vue'
import Statistics from './components/Statistics.vue'
import Login from './components/Login.vue'

const routes = [
  {
    path: '/events',
    component: Events,
    name: 'Events',
    alias: '/',
    meta: { requiresAuth: true }
  },
  {
    path: '/teams',
    name: 'Teams',
    component: Table,
    meta: { requiresAuth: true }
  },
  {
    component: TeamDetails,
    path: '/team/:id',
    name: 'TeamDetails',
    meta: { requiresAuth: true }
  },
  {
    path: '/statistics',
    name: 'Statistics',
    component: Statistics,
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { requiresGuest: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem('user')

  if (to.matched.some((record) => record.meta.requiresAuth) && !loggedIn) {
    next({ name: 'Login' })
  } else if (to.matched.some((record) => record.meta.requiresGuest) && loggedIn) {
    next({ name: 'Events' })
  } else {
    next()
  }
})

export default router
