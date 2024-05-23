<template>
  <div class="mx-auto max-w-screen-xl sm:px-6 sm:py-8 lg:px-8 text-black">
    <h1 class="text-4xl font-bold mb-8 text-center text-white">Статистика</h1>

    <div class="mb-8">
      <label for="timePeriod" class="block text-gray-700 text-sm font-bold mb-2 text-white"
        >Выберите период:</label
      >
      <select
        v-model="selectedPeriod"
        @change="fetchTopTeams"
        class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        id="timePeriod"
      >
        <option value="all">За все время</option>
        <option value="year">За год</option>
        <option value="month">За текущий месяц</option>
      </select>
    </div>

    <div class="mt-8">
      <h2 class="text-2xl font-bold mb-4 text-white">Таблица баллов</h2>
      <table class="min-w-full bg-white rounded-lg">
        <thead>
          <tr>
            <th class="py-2 px-4 border-b border-gray-300">Команды</th>
            <th class="py-2 px-4 border-b border-gray-300">Баллы</th>
            <th class="py-2 px-4 border-b border-gray-300">1 место</th>
            <th class="py-2 px-4 border-b border-gray-300">2 место</th>
            <th class="py-2 px-4 border-b border-gray-300">3 место</th>
            <th class="py-2 px-4 border-b border-gray-300">Проиграли</th>
            <th class="py-2 px-4 border-b border-gray-300">Не участвовали</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="team in topTeams" :key="team._id">
            <td
              class="py-2 px-4 border-b border-gray-300 cursor-pointer hover:underline text-black font-bold"
              @click="goToTeamDetails(team._id)"
            >
              {{ team.teamname }}
            </td>
            <td class="py-2 px-4 border-b border-gray-300">{{ team.totalPoints }}</td>
            <td class="py-2 px-4 border-b border-gray-300">{{ team.firstPlace }}</td>
            <td class="py-2 px-4 border-b border-gray-300">{{ team.secondPlace }}</td>
            <td class="py-2 px-4 border-b border-gray-300">{{ team.thirdPlace }}</td>
            <td class="py-2 px-4 border-b border-gray-300">{{ team.lost }}</td>
            <td class="py-2 px-4 border-b border-gray-300">{{ team.notParticipated }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="mx-auto max-w-screen-xl px-8 py-4 flex justify-end">
      <nav aria-label="Pagination">
        <ul class="flex items-center space-x-2">
          <li v-if="page > 1">
            <button
              @click="prevPage"
              class="text-gray-500 hover:text-gray-700 transition duration-300 ease-in-out"
            >
              <span class="sr-only">Previous</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M12.293 14.293a1 1 0 010 1.414l-4-4a1 1 010-1.414l4-4a1 1 011.414 1.414L10.414 10l3.293 3.293a1 1 01-1.414 1.414z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
          </li>
          <li v-for="n in totalPages" :key="n">
            <button
              @click="goToPage(n)"
              :class="{
                'bg-blue-500 text-white': n === page,
                'text-gray-700 hover:text-gray-900 text-white': n !== page
              }"
              class="px-3 py-1 rounded-md transition duration-300 ease-in-out"
            >
              {{ n }}
            </button>
          </li>
          <li v-if="page < totalPages">
            <button
              @click="nextPage"
              class="text-gray-500 hover:text-gray-700 transition duration-300 ease-in-out"
            >
              <span class="sr-only">Next</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 010-1.414l4-4a1 1 011.414 1.414L5.414 10l3.293 3.293a1 1 01-1.414 1.414z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      topTeams: [],
      selectedPeriod: 'all',
      page: parseInt(this.$route.query.page) || 1,
      limit: 6,
      totalPages: 1
    }
  },
  watch: {
    '$route.query.page': 'fetchTopTeams',
    '$route.query.period': 'fetchTopTeams'
  },
  created() {
    this.fetchTopTeams()
  },
  methods: {
    async fetchTopTeams() {
      try {
        const response = await axios.get('http://localhost:5000/stats/top-teams', {
          params: {
            period: this.selectedPeriod,
            page: this.page,
            limit: this.limit
          }
        })
        this.topTeams = response.data.teams
        this.totalPages = response.data.total_pages
      } catch (error) {
        console.error(error)
        alert(`Error fetching top teams: ${error.response?.data?.error || error.message}`)
      }
    },
    nextPage() {
      if (this.page < this.totalPages) {
        this.page++
        this.updateRoute()
      }
    },
    prevPage() {
      if (this.page > 1) {
        this.page--
        this.updateRoute()
      }
    },
    goToPage(page) {
      if (page !== this.page) {
        this.page = page
        this.updateRoute()
      }
    },
    updateRoute() {
      this.$router.push({ query: { page: this.page, period: this.selectedPeriod } })
    },
    goToTeamDetails(teamId) {
      this.$router.push({ path: `/team/${teamId}` })
    }
  }
}
</script>

<style scoped>
body {
  background-color: #1a202c;
}

.bg-white {
  background-color: #ffffff;
}

.text-black {
  color: #000000;
}

.bg-gray-800 {
  background-color: #2d3748;
}

.bg-gray-200 {
  background-color: #edf2f7;
}

.border-gray-300 {
  border-color: #d1d5db;
}
</style>
