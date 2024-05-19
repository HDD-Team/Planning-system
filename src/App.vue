<script setup>
import Header from './components/Header.vue'
import Table from './components/Table.vue'
// import Search from './components/Search.vue'
// import Dropdown from './components/icons/Dropdown.vue'
// import Calendar from './Calendar.vue'
import Events from './components/Events.vue'
import statistics from './components/statistics.vue'
import Auth from './components/Auth.vue'
</script>
<template>
  <Auth />
  <Header />
  <Events />
  <div class="mx-auto max-w-screen-xl sm:px-8 lg:px-8">
    <div class="sm:flex sm:items-center sm:justify-between">
      <div class="text-center sm:text-left">
        <!-- <Dropdown /> -->
      </div>
      <div>
        <div class="mt-4 flex flex-col gap-4 sm:mt-0 sm:flex-row sm:items-center">
          <!-- <Search /> -->
        </div>
      </div>
    </div>
  </div>
  <Table />
  <statistics />
  <!-- add the statistics component here -->
</template>
