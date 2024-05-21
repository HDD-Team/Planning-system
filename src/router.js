import { createRouter, createWebHistory } from 'vue-router'
import Events from './components/Events.vue'
import Table from './components/Table.vue'

const routes = [
  {
    path: '/events',
    component: Events,
    alias: '/'
  },
  {
    path: '/teams',
    component: Table
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
