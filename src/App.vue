<template>
  <div>
    <Header v-if="showHeader" />
    <router-view></router-view>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Header from './components/Header.vue'

const route = useRoute()

const showHeader = computed(() => route.name !== 'Login')
</script>
