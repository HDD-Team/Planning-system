<template>
  <div class="mx-auto max-w-screen-xl sm:px-6 sm:py-8 lg:px-8 text-white">
    <h1 class="text-4xl font-bold mb-8 text-center">{{ team.teamname }}</h1>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
      <div>
        <h2 class="text-2xl font-bold mb-4">Руководители</h2>
        <ul class="list-disc pl-5">
          <li v-for="teacher in team.teachers" :key="teacher._id" class="mb-2">
            {{ teacher.surname }} {{ teacher.name }}
          </li>
        </ul>

        <h2 class="text-2xl font-bold mt-6 mb-4">Участники</h2>
        <ul class="list-disc pl-5">
          <li v-for="student in team.students" :key="student._id" class="mb-2">
            {{ student.surname }} {{ student.name }} ({{ student.group }})
          </li>
        </ul>
      </div>

      <div>
        <h2 class="text-2xl font-bold mb-4">Статистика</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div
            class="bg-green-500 p-4 rounded-lg shadow-lg text-center transform transition duration-500 hover:scale-105"
          >
            <p class="text-lg font-bold">1 место</p>
            <p class="text-3xl">{{ statistics.firstPlace }}</p>
          </div>
          <div
            class="bg-green-400 p-4 rounded-lg shadow-lg text-center transform transition duration-500 hover:scale-105"
          >
            <p class="text-lg font-bold">2 место</p>
            <p class="text-3xl">{{ statistics.secondPlace }}</p>
          </div>
          <div
            class="bg-green-300 p-4 rounded-lg shadow-lg text-center transform transition duration-500 hover:scale-105"
          >
            <p class="text-lg font-bold">3 место</p>
            <p class="text-3xl">{{ statistics.thirdPlace }}</p>
          </div>
          <div
            class="bg-red-500 p-4 rounded-lg shadow-lg text-center transform transition duration-500 hover:scale-105"
          >
            <p class="text-lg font-bold">Проиграли</p>
            <p class="text-3xl">{{ statistics.lost }}</p>
          </div>
          <div
            class="bg-gray-500 p-4 rounded-lg shadow-lg text-center transform transition duration-500 hover:scale-105"
          >
            <p class="text-lg font-bold">Не участвовали</p>
            <p class="text-3xl">{{ statistics.notParticipated }}</p>
          </div>
        </div>
      </div>
    </div>

    <h2 class="text-2xl font-bold mt-6 mb-4">Мероприятия</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="event in events" :key="event._id" class="bg-gray-800 p-6 rounded-lg shadow-lg">
        <div class="flex flex-col h-full">
          <div>
            <p class="text-xl font-semibold">{{ event.nameEvent }}</p>
            <p class="text-sm text-gray-400">
              {{ formatDate(event.startDateEvent, event.endDateEvent) }}
            </p>
            <p class="text-sm text-gray-400">Место проведения: {{ event.cityEvent }}</p>
            <p class="text-sm text-gray-400">
              Источник:
              <a :href="event.websiteEvent" target="_blank" class="text-blue-500 hover:underline">
                {{ event.websiteEvent }}
              </a>
            </p>
          </div>
          <div class="mt-auto pt-4">
            <p
              :class="getStatusClass(event.statusParticipation)"
              class="px-3 py-1 rounded-full text-sm font-semibold"
            >
              {{ event.statusParticipation }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      team: {
        teamname: '',
        teachers: [],
        students: []
      },
      events: [],
      statistics: {
        firstPlace: 0,
        secondPlace: 0,
        thirdPlace: 0,
        lost: 0,
        notParticipated: 0
      }
    }
  },
  created() {
    this.getTeamDetails()
  },
  methods: {
    async getTeamDetails() {
      const teamId = this.$route.params.id
      try {
        const response = await axios.get(`http://localhost:5000/teams/${teamId}`)
        this.team = response.data.team
        this.events = response.data.events
        this.statistics = response.data.statistics
      } catch (error) {
        console.error(error)
      }
    },
    getStatusClass(status) {
      switch (status) {
        case '1 место':
        case '2 место':
        case '3 место':
          return 'bg-green-500 text-white'
        case 'Проиграли':
        case 'Не участвовали':
          return 'bg-red-500 text-white'
        case 'Участвуют':
          return 'bg-orange-500 text-white'
        default:
          return 'bg-gray-500 text-white'
      }
    },
    formatDate(startDate, endDate) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' }
      const formattedStartDate = new Date(startDate).toLocaleDateString('ru-RU', options)
      const formattedEndDate = new Date(endDate).toLocaleDateString('ru-RU', options)
      return `${formattedStartDate} - ${formattedEndDate}`
    }
  }
}
</script>

<style scoped>
body {
  background-color: #1a202c;
}

.list-disc li {
  list-style: disc;
}

.divide-gray-700 > :not([hidden]) ~ :not([hidden]) {
  border-color: #4a5568;
}
</style>
