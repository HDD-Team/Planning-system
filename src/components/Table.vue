<template>
  <div class="mx-auto max-w-screen-xl px-8 py-4">
    <h1 class="text-2xl font-bold mb-4 text-white">Команды</h1>
    <button
      @click="addNewItem"
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
    >
      Добавить команду
    </button>

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
              <td class="whitespace-nowrap px-4 py-2 text-gray-900">
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
              <td colspan="5" class="text-left"></td>
            </tr>
          </tfoot>
        </table>
      </div>
    </div>
  </div>
  <!-- Модальное окно редактирования команды -->
  <div v-if="showEditTeamModal" class="fixed inset-0 flex items-center justify-center">
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
                class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded rounded ml-2"
                type="button"
                @click="removeTeacher(index)"
              >
                Удалить
              </button>
            </div>
          </div>
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded rounded"
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
                class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded rounded ml-2"
                type="button"
                @click="removeStudent(index)"
              >
                Удалить
              </button>
            </div>
          </div>
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded rounded"
            type="button"
            @click="addStudent"
          >
            Добавить участника
          </button>
        </div>

        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
          type="submit"
        >
          Сохранить
        </button>
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
          @click="showEditTeamModal = false"
        >
          Отмена
        </button>
      </form>
    </div>
  </div>
  <!-- Модальное окно создания команды -->
  <div v-if="showAddTeamModal" class="fixed inset-0 flex items-center justify-center">
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
                class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded rounded rounded rounded ml-2"
                type="button"
                @click="removeTeacherFromNewTeam(index)"
              >
                Удалить
              </button>
            </div>
          </div>
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded rounded rounded rounded"
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
                class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded rounded rounded rounded ml-2"
                type="button"
                @click="removeStudentFromNewTeam(index)"
              >
                Удалить
              </button>
            </div>
          </div>
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded rounded rounded rounded"
            type="button"
            @click="addStudentToNewTeam"
          >
            Добавить участника
          </button>
        </div>

        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded rounded rounded rounded mb-4"
          type="submit"
        >
          Создать
        </button>
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded rounded rounded rounded mb-4"
          @click="showAddTeamModal = false"
        >
          Отмена
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      teams: [],
      editedItem: null,
      showEditTeamModal: false,
      newTeam: {
        teamname: '',
        teachers: [],
        students: []
      },
      showAddTeamModal: false
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
        this.showAddTeamModal = false
      } catch (error) {
        console.error(error)
      }
    },
    editItem(team) {
      this.editedTeam = { ...team } // Создаем копию объекта team
      this.showEditTeamModal = true // Отображаем модальное окно
    },
    async saveEditedTeam() {
      try {
        const response = await axios.put(
          `http://localhost:5000/teams/${this.editedTeam._id}`,
          this.editedTeam
        )
        const index = this.teams.findIndex((team) => team._id === this.editedTeam._id)
        this.teams.splice(index, 1, response.data)
        this.showEditTeamModal = false
      } catch (error) {
        console.error(error)
      }
    },
    addTeacher() {
      this.editedTeam.teachers.push({
        name: '',
        surname: ''
      })
    },

    removeTeacher(index) {
      this.editedTeam.teachers.splice(index, 1)
    },

    addStudent() {
      this.editedTeam.students.push({
        name: '',
        surname: '',
        group: ''
      })
    },

    removeStudent(index) {
      this.editedTeam.students.splice(index, 1)
    },
    addTeam() {
      this.teams.push(this.newTeam)
      this.newTeam = {
        teamname: '',
        teachers: [],
        students: []
      }
      this.showAddTeamModal = false
    },
    addTeacherToNewTeam() {
      this.newTeam.teachers.push({
        name: '',
        surname: ''
      })
    },
    removeTeacherFromNewTeam(index) {
      this.newTeam.teachers.splice(index, 1)
    },
    addStudentToNewTeam() {
      this.newTeam.students.push({
        name: '',
        surname: '',
        group: ''
      })
    },
    removeStudentFromNewTeam(index) {
      this.newTeam.students.splice(index, 1)
    },
    addNewItem() {
      this.showAddTeamModal = true
    },

    async deleteTeam(id) {
      // Найти команду по ее идентификатору
      const team = this.teams.find((team) => team._id === id)

      if (team) {
        // Отобразить диалоговое окно подтверждения удаления с названием команды
        if (confirm(`Вы точно хотите удалить команду "${team.teamname}"?`)) {
          try {
            await axios.delete(`http://localhost:5000/teams/${id}`)
            const index = this.teams.findIndex((team) => team._id === id)
            this.teams.splice(index, 1)
          } catch (error) {
            console.error(error)
          }
        }
      }
    }
  }
}
</script>
