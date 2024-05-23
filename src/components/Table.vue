<template>
  <div class="mx-auto max-w-screen-xl px-8 py-4">
    <h1 class="text-2xl font-bold mb-4 text-white">Команды</h1>

    <div class="flex justify-between items-center mb-4">
      <button
        @click="showAddTeamModal = true"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Добавить команду
      </button>
      <button
        class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
        @click="showFilterModal = true"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5 inline-block mr-2"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-.293.707L13 9.414V14a1 1 0 01-.293.707l-3 3A1 1 0 018 17v-7.586l-2.707-2.707A1 1 0 015 6V4z"
            clip-rule="evenodd"
          />
        </svg>
        Фильтр
      </button>
    </div>

    <div class="overflow-x-auto rounded-t-lg">
      <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
        <thead class="ltr:text-left rtl:text-right">
          <tr>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Название команды</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Руководители</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Участники</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Статистика</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"></th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr v-for="team in teams" :key="team._id">
            <td class="whitespace-nowrap px-4 py-2 font-medium">{{ team.teamname }}</td>

            <td class="whitespace-nowrap px-4 py-2 text-gray-900">
              <ul>
                <li v-for="teacher in team.teachers" :key="teacher._id">
                  {{ teacher.surname }} {{ teacher.name }}
                </li>
              </ul>
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              <ul>
                <li v-for="(student, index) in team.students" :key="index">
                  {{ student.surname }} {{ student.name }} ({{ student.group }}){{
                    index < team.students.length - 1 ? ' ' : ''
                  }}
                </li>
              </ul>
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              <button
                @click="viewDetails(team._id)"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
              >
                Подробнее
              </button>
            </td>
            <td class="whitespace-nowrap px-4 py-2">
              <button
                @click="editItem(team)"
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
                @click="deleteTeam(team._id)"
                class="text-red-500 hover:text-red-700 focus:outline-none ml-2"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V4a2 2 0 00-2-2H6zM14.586 8l-2.293-2.293a1 1 0 00-1.414 0L10 10.586 7.707 8.293a1 1 0 10-1.414 1.414L10 11.414l2.293 2.293a1 1 001.414 0L14.586 10l-1.293-1.293z"
                  />
                </svg>
              </button>
            </td>
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
                  d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 010-1.414l4-4a1 1 011.414-1.414L10.414 10l3.293 3.293a1 1 010 1.414z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
          </li>
        </ul>
      </nav>
    </div>

    <!-- Модальное окно фильтрации -->
    <div
      v-if="showFilterModal"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
    >
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Фильтрация команд</h2>
        <div class="mb-4">
          <input
            v-model="search"
            type="text"
            placeholder="Поиск по руководителю"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div class="mb-4">
          <input
            v-model="searchTeamName"
            type="text"
            placeholder="Поиск по названию команды"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div class="mb-4">
          <input
            v-model="searchParticipants"
            type="text"
            placeholder="Поиск по участникам"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <button
          @click="applyFilters"
          class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-4"
        >
          Применить
        </button>
        <button
          @click="resetFilters"
          class="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded mb-4"
        >
          Очистить
        </button>
        <button
          @click="showFilterModal = false"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mb-4"
        >
          Отмена
        </button>
      </div>
    </div>
    <!-- Модальное окно редактирования команды -->
    <div
      v-if="showEditTeamModal"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
    >
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Редактировать команду</h2>
        <!-- Форма редактирования команды -->
        <form @submit.prevent="saveEditedTeam">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="team-name"
              >Название команды</label
            >
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="team-name"
              type="text"
              v-model="editedTeam.teamname"
            />
          </div>

          <!-- Поле для редактирования руководителей -->
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Руководители</label>
            <div v-for="(teacher, index) in editedTeam.teachers" :key="index">
              <div class="flex mb-2">
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="text"
                  v-model="teacher.name"
                />
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ml-2"
                  type="text"
                  v-model="teacher.surname"
                />
                <button
                  class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded ml-2"
                  type="button"
                  @click="removeTeacher(index)"
                >
                  Удалить
                </button>
              </div>
            </div>
            <button
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
              type="button"
              @click="addTeacher"
            >
              Добавить руководителя
            </button>
          </div>

          <!-- Поле для редактирования участников -->
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Участники</label>
            <div v-for="(student, index) in editedTeam.students" :key="index">
              <div class="flex mb-2">
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="text"
                  v-model="student.name"
                />
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ml-2"
                  type="text"
                  v-model="student.surname"
                />
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ml-2"
                  type="text"
                  v-model="student.group"
                />
                <button
                  class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded ml-2"
                  type="button"
                  @click="removeStudent(index)"
                >
                  Удалить
                </button>
              </div>
            </div>
            <button
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
              type="button"
              @click="addStudent"
            >
              Добавить участника
            </button>
          </div>

          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
            type="submit"
          >
            Сохранить
          </button>
          <button
            class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mb-4"
            @click="showEditTeamModal = false"
          >
            Отмена
          </button>
        </form>
      </div>
    </div>

    <!-- Модальное окно создания команды -->
    <div
      v-if="showAddTeamModal"
      class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
    >
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Создать команду</h2>
        <!-- Форма создания команды -->
        <form @submit.prevent="createTeam">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="team-name"
              >Название команды</label
            >
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="team-name"
              type="text"
              v-model="newTeam.teamname"
              placeholder="Введите название команды"
            />
          </div>

          <!-- Поле для добавления руководителей -->
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Руководители</label>
            <div v-for="(teacher, index) in newTeam.teachers" :key="index">
              <div class="flex mb-2">
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="text"
                  v-model="teacher.name"
                  placeholder="Введите имя"
                />
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ml-2"
                  type="text"
                  v-model="teacher.surname"
                  placeholder="Введите фамилию"
                />
                <button
                  class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded ml-2"
                  type="button"
                  @click="removeTeacherFromNewTeam(index)"
                >
                  Удалить
                </button>
              </div>
            </div>
            <button
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
              type="button"
              @click="addTeacherToNewTeam"
            >
              Добавить руководителя
            </button>
          </div>

          <!-- Поле для добавления участников -->
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Участники</label>
            <div v-for="(student, index) in newTeam.students" :key="index">
              <div class="flex mb-2">
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="text"
                  v-model="student.name"
                  placeholder="Введите имя"
                />
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ml-2"
                  type="text"
                  v-model="student.surname"
                  placeholder="Введите фамилию"
                />
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ml-2"
                  type="text"
                  v-model="student.group"
                  placeholder="Введите группу"
                />
                <button
                  class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded ml-2"
                  type="button"
                  @click="removeStudentFromNewTeam(index)"
                >
                  Удалить
                </button>
              </div>
            </div>
            <button
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
              type="button"
              @click="addStudentToNewTeam"
            >
              Добавить участника
            </button>
          </div>

          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
            type="submit"
          >
            Создать
          </button>
          <button
            class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mb-4"
            @click="showAddTeamModal = false"
          >
            Отмена
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      teams: [],
      page: 1,
      limit: 10,
      totalPages: 1,
      search: '',
      searchTeamName: '',
      searchParticipants: '',
      newTeam: {
        teamname: '',
        teachers: [],
        students: []
      },
      editedTeam: {
        teamname: '',
        teachers: [],
        students: []
      },
      showAddTeamModal: false,
      showEditTeamModal: false,
      showFilterModal: false
    }
  },
  created() {
    const savedPage = localStorage.getItem('currentPage')
    if (savedPage) {
      this.page = parseInt(savedPage, 10)
    }
    this.getTeams(this.page, this.limit)
  },
  methods: {
    async getTeams(page = 1, limit = 10) {
      try {
        const response = await axios.get('http://localhost:5000/teams/paginate', {
          params: {
            page,
            limit
          }
        })
        this.teams = response.data.teams
        this.totalPages = response.data.total_pages
        this.page = response.data.current_page
      } catch (error) {
        console.error(error)
      }
    },
    viewDetails(teamId) {
      this.$router.push({ name: 'TeamDetails', params: { id: teamId } })
    },
    async applyFilters() {
      try {
        const response = await axios.get('http://localhost:5000/teams/filter', {
          params: {
            page: this.page,
            limit: this.limit,
            search: this.search,
            searchTeamName: this.searchTeamName,
            searchParticipants: this.searchParticipants
          }
        })
        this.teams = response.data.teams
        this.totalPages = response.data.total_pages
        this.page = response.data.current_page
        this.showFilterModal = false
      } catch (error) {
        console.error(error)
      }
    },
    resetFilters() {
      this.search = ''
      this.searchTeamName = ''
      this.searchParticipants = ''
      this.page = 1
      this.getTeams(this.page, this.limit)
      this.showFilterModal = false
    },
    goToPage(page) {
      this.page = page
      localStorage.setItem('currentPage', page)
      this.getTeams(this.page, this.limit)
    },
    prevPage() {
      if (this.page > 1) {
        this.page -= 1
        localStorage.setItem('currentPage', this.page)
        this.getTeams(this.page, this.limit)
      }
    },
    nextPage() {
      if (this.page < this.totalPages) {
        this.page += 1
        localStorage.setItem('currentPage', this.page)
        this.getTeams(this.page, this.limit)
      }
    },
    async createTeam() {
      try {
        const response = await axios.post('http://localhost:5000/teams', this.newTeam)
        this.teams.unshift(response.data)
        this.showAddTeamModal = false
        this.newTeam = {
          teamname: '',
          teachers: [],
          students: []
        }
        this.getTeams(this.page, this.limit)
      } catch (error) {
        console.error(error)
      }
    },
    async deleteTeam(teamId) {
      if (confirm('Вы уверены, что хотите удалить эту команду?')) {
        try {
          await axios.delete(`http://localhost:5000/teams/${teamId}`)
          this.getTeams(this.page, this.limit)
        } catch (error) {
          console.error(error)
        }
      }
    },
    editItem(team) {
      this.editedTeam = { ...team }
      this.showEditTeamModal = true
    },
    async saveEditedTeam() {
      try {
        const response = await axios.put(
          `http://localhost:5000/teams/${this.editedTeam._id}`,
          this.editedTeam
        )
        this.showEditTeamModal = false
        this.getTeams(this.page, this.limit)
      } catch (error) {
        console.error(error)
      }
    },
    addTeacher() {
      this.editedTeam.teachers.push({ name: '', surname: '' })
    },
    removeTeacher(index) {
      this.editedTeam.teachers.splice(index, 1)
    },
    addStudent() {
      this.editedTeam.students.push({ name: '', surname: '', group: '' })
    },
    removeStudent(index) {
      this.editedTeam.students.splice(index, 1)
    },
    addTeacherToNewTeam() {
      this.newTeam.teachers.push({ name: '', surname: '' })
    },
    removeTeacherFromNewTeam(index) {
      this.newTeam.teachers.splice(index, 1)
    },
    addStudentToNewTeam() {
      this.newTeam.students.push({ name: '', surname: '', group: '' })
    },
    removeStudentFromNewTeam(index) {
      this.newTeam.students.splice(index, 1)
    }
  }
}
</script>
