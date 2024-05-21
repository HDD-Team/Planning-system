<template>
  <div class="mx-auto max-w-screen-xl px-8 py-4">
    <h1 class="text-2xl font-bold mb-4 text-white">Команды</h1>

    <div>
      <div class="overflow-x-auto rounded-t-lg">
        <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <tr>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Руководители</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Название команды
              </th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Участники</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Мероприятия</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"></th>
            </tr>
          </thead>

          <tbody class="divide-y divide-gray-200">
            <tr v-for="team in teams" :key="team._id">
              <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                <ul>
                  <li v-for="teacher in team.teachers" :key="teacher._id">
                    {{ teacher.surname }} {{ teacher.name }}
                  </li>
                </ul>
              </td>
              <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ team.teamname }}</td>
              <td class="whitespace-nowrap px-4 py-2 text-gray-700">
                <ul>
                  <li v-for="(student, index) in team.students" :key="index">
                    {{ student.surname }} {{ student.name }} ({{ student.group }}){{
                      index < team.students.length - 1 ? ', ' : ''
                    }}
                  </li>
                </ul>
              </td>
              <td class="whitespace-nowrap px-4 py-2 text-gray-700">
                <button
                  @click="viewDetails(item)"
                  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
                >
                  Подробнее
                </button>
              </td>
              <td class="whitespace-nowrap px-4 py-2">
                <button
                  @click="editItem(item)"
                  class="text-blue-500 hover:text-blue-700 focus:outline-none"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"
                    />
                  </svg>
                </button>
                <button
                  @click="deleteItem(item)"
                  class="text-red-500 hover:text-red-700 focus:outline-none"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V4a2 2 0 00-2-2H6zM14.586 8l-2.293-2.293a1 1 0 00-1.414 0L10 10.586 7.707 8.293a1 1 0 10-1.414 1.414L10 11.414l2.293 2.293a1 1 0 001.414 0L14.586 10l-1.293-1.293z"
                    />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="5" class="text-left">
                <button
                  @click="addNewItem"
                  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
                >
                  +
                </button>
              </td>
            </tr>
          </tfoot>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      teams: [], // измените этот массив
      editedItem: null
    }
  },
  async created() {
    await this.getTeams()
  },
  mounted() {
    this.getTeams()
  },
  methods: {
    async getTeams() {
      try {
        const response = await axios.get('http://localhost:5000/teams')
        this.teams = response.data
      } catch (error) {
        console.error(error)
      }
    },
    async createTeam() {
      try {
        const response = await axios.post('http://localhost:5000/teams', this.newTeam)
        this.teams.push(response.data)
        this.newTeam = {}
      } catch (error) {
        console.error(error)
      }
    },
    async updateTeam(id) {
      try {
        const response = await axios.put(`http://localhost:5000/teams/${id}`, this.editedTeam)
        const index = this.teams.findIndex((team) => team._id === id)
        this.teams.splice(index, 1, response.data)
        this.editedTeam = {}
      } catch (error) {
        console.error(error)
      }
    },
    async deleteTeam(id) {
      try {
        await axios.delete(`http://localhost:3000/teams/${id}`)
        const index = this.teams.findIndex((team) => team._id === id)
        this.teams.splice(index, 1)
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
