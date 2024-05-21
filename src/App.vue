<script setup>
import Header from './components/Header.vue'
import Table from './components/Table.vue'
// import Search from './components/Search.vue'
// import Dropdown from './components/icons/Dropdown.vue'
// import Calendar from './Calendar.vue'
import Events from './components/Events.vue'
import Auth from './components/Auth.vue'
</script>
<template>
  <!-- <Auth /> -->
  <Header />
  <!-- <Events />
  <Table /> -->
  <router-view> </router-view>
</template>
