<template>
  <div class="mx-auto max-w-screen-xl px-8 py-4">
    <h1 class="text-2xl font-bold mb-4 text-gray-800">Статистика команд</h1>

    <div class="mb-4">
      <label for="startDate" class="block text-sm font-medium text-gray-700">Начало периода</label>
      <input
        type="date"
        id="startDate"
        v-model="startDate"
        @change="fetchTopTeams"
        class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
      />

      <label for="endDate" class="block text-sm font-medium text-gray-700 mt-4"
        >Конец периода</label
      >
      <input
        type="date"
        id="endDate"
        v-model="endDate"
        @change="fetchTopTeams"
        class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
      />
    </div>

    <div v-if="topTeams && topTeams.length">
      <h2 class="text-xl font-semibold mb-2">
        Лучшие команды за период с {{ startDate }} по {{ endDate }}
      </h2>
      <div class="overflow-x-auto rounded-t-lg">
        <table class="min-w-full divide-y divide-gray-200 bg-white text-sm">
          <thead>
            <tr>
              <th class="px-4 py-2 text-left text-gray-500">Название команды</th>
              <th class="px-4 py-2 text-left text-gray-500">Количество побед</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="team in topTeams" :key="team._id">
              <td class="px-4 py-2">{{ team.teamname }}</td>
              <td class="px-4 py-2">{{ team.wins }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-else>
      <p class="text-gray-500">Нет данных за выбранный период.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      startDate: '',
      endDate: '',
      topTeams: []
    }
  },
  methods: {
    fetchTopTeams() {
      if (!this.startDate || !this.endDate) return
      console.log(`Fetching top teams from ${this.startDate} to ${this.endDate}`)
      axios
        .get(`http://localhost:5000/top-teams`, {
          params: {
            startDate: this.startDate,
            endDate: this.endDate
          }
        })
        .then((response) => {
          console.log('Top teams response:', response.data)
          this.topTeams = response.data
        })
        .catch((error) => {
          console.error('Error fetching top teams:', error)
        })
    }
  }
}
</script>

<style scoped>
/* Ваши стили */
</style>
