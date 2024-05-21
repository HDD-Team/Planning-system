<template>
  <div class="mx-auto max-w-screen-xl px-8 py-4">
    <h1 class="text-2xl font-bold mb-4">Мероприятия</h1>

    <button
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
      @click="showCreateEventModal = true"
    >
      Создать мероприятие
    </button>

    <div class="overflow-x-auto rounded-t-lg">
      <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
        <thead class="ltr:text-left rtl:text-right">
          <tr>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Действия</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Название</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Место</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Дата</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Статус</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Источник</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Команды</th>
          </tr>
        </thead>

        <tbody class="divide-y divide-gray-200">
          <tr v-for="event in events" :key="event._id">
            <td class="whitespace-nowrap px-4 py-2">
              <button
                @click="showEditEventModal(event)"
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
                class="text-red-500 hover:text-red-700 focus:outline-none ml-2"
                @click="deleteEvent(event._id)"
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
              <button
                class="text-green-500 hover:text-green-700 focus:outline-none ml-2"
                @click="showAddTeamModal(event)"
              >
                <svg
                  fill="currentColor"
                  viewBox="0 0 32 32"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                >
                  <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                  <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                  <g id="SVGRepo_iconCarrier">
                    <title>plus-user</title>
                    <path
                      d="M2.016 28q0 0.832 0.576 1.44t1.408 0.576h14.016v-0.352q-1.792-0.608-2.912-2.176t-1.088-3.488q0-2.016 1.184-3.584t3.072-2.112q0.384-1.216 1.216-2.176t2.016-1.504q0.512-1.376 0.512-2.624v-1.984q0-3.328-2.368-5.664t-5.632-2.336-5.664 2.336-2.336 5.664v1.984q0 2.112 1.024 3.904t2.784 2.912q-1.504 0.544-2.912 1.504t-2.496 2.144-1.76 2.624-0.64 2.912zM18.016 24q0 0.832 0.576 1.44t1.408 0.576h2.016v1.984q0 0.864 0.576 1.44t1.408 0.576 1.408-0.576 0.608-1.44v-1.984h1.984q0.832 0 1.408-0.576t0.608-1.44-0.608-1.408-1.408-0.576h-1.984v-2.016q0-0.832-0.608-1.408t-1.408-0.576-1.408 0.576-0.576 1.408v2.016h-2.016q-0.832 0-1.408 0.576t-0.576 1.408z"
                    ></path>
                  </g>
                </svg>
              </button>
            </td>
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
              {{ event.nameEvent }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ event.cityEvent }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              {{ formatDate(event.startDateEvent, event.endDateEvent) }}
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              <div>
                {{ event.statusEvent }}
              </div>
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-sm text-gray-500">
              <div v-if="event.websiteEvent">
                <a
                  :href="event.websiteEvent"
                  target="_blank"
                  class="text-blue-500 hover:text-blue-700"
                >
                  Источник
                </a>
              </div>
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              <div v-for="team in event.teams" :key="team.team_id">
                <strong
                  >{{ getTeamDataById(team.team_id)?.teamname }}
                  {{ team.statusParticipation }}</strong
                >
                (Руководитель: {{ getTeamDataById(team.team_id)?.teachers }}, Участники:
                {{ getTeamDataById(team.team_id)?.students }}
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="mx-auto max-w-screen-xl px-8 py-4">
      <div class="flex items-center justify-center mt-4">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
          @click="prevPage"
          :disabled="page === 1"
        >
          Предыдущая
        </button>

        <span class="mx-2">{{ page }}</span>

        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
          @click="nextPage"
        >
          Следующая
        </button>
      </div>
    </div>

    <!-- Модальное окно создания мероприятия -->
    <div v-if="showCreateEventModal" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Создать мероприятие</h2>
        <!-- Форма создания мероприятия -->
        <form @submit.prevent="createEvent">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="nameEvent">
              Название мероприятия
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="nameEvent"
              type="text"
              v-model="newEvent.nameEvent"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="cityEvent">
              Город мероприятия
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="cityEvent"
              type="text"
              v-model="newEvent.cityEvent"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="startDateEvent">
              Дата начала мероприятия
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="startDateEvent"
              type="date"
              v-model="newEvent.startDateEvent"
            />
          </div>

          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="endDateEvent">
              Дата конца мероприятия
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="endDateEvent"
              type="date"
              v-model="newEvent.endDateEvent"
            />
          </div>

          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="websiteEvent">
              Источник мероприятия
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="websiteEvent"
              type="text"
              v-model="newEvent.websiteEvent"
            />
          </div>
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
            type="submit"
          >
            Создать
          </button>
          <button
            class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
            @click="showCreateEventModal = false"
          >
            Отмена
          </button>
        </form>
      </div>
    </div>

    <!-- Модальное окно редактирования мероприятия -->
    <div v-if="showEditEventModalVisible" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Редактировать мероприятие</h2>
        <!-- Форма редактирования мероприятия -->
        <form @submit.prevent="editEvent">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="title"> Название </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="title"
              type="text"
              v-model="currentEvent.nameEvent"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="location"> Место </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="location"
              type="text"
              v-model="currentEvent.cityEvent"
            />
          </div>
          <div class="mb-4 cursor-pointer">
            <label
              class="block text-gray-700 text-sm font-bold mb-2 cursor-pointer"
              for="start-date"
            >
              Дата начала
            </label>
            <input
              class="cursor-pointer shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="start-date"
              type="date"
              v-model="currentEvent.startDateEvent"
            />
          </div>
          <div class="mb-4 cursor-pointer">
            <label class="block text-gray-700 text-sm font-bold mb-2 cursor-pointer" for="end-date">
              Дата окончания
            </label>
            <input
              class="cursor-pointer shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="end-date"
              type="date"
              v-model="currentEvent.endDateEvent"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="status"> Статус </label>
            <select
              class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              id="status"
              v-model="currentEvent.statusEvent"
            >
              <option value="">Выберите статус</option>
              <option>Активно</option>
              <option>Неактивно</option>
              <option>Завершено</option>
              <option>Отменено</option>
            </select>
            <p v-if="currentEvent.statusEvent === 'Отменено'" class="text-xs text-gray-500">
              Чтобы вернуть к предыдущему статусу, выберите его в списке.
            </p>
          </div>

          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="source">
              Источник
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="source"
              type="text"
              v-model="currentEvent.websiteEvent"
            />
          </div>
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
            type="submit"
          >
            Сохранить
          </button>
          <button
            class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
            @click="cancelEditEvent"
          >
            Отмена
          </button>
        </form>
      </div>
    </div>

    <!-- Модальное окно добавления команды к мероприятию -->
    <div v-if="showAddTeamModalVisible" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Добавить команду к мероприятию</h2>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="team">Команда</label>
          <select
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="team"
            v-model="selectedTeam"
          >
            <option v-for="team in availableTeams" :key="team._id" :value="team._id">
              {{ team.teamname }}
            </option>
          </select>
        </div>
        <button
          @click="addTeamToEvent"
          class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Добавить
        </button>
        <button
          @click="showAddTeamModalVisible = false"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Отмена
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DataTable',
  data() {
    return {
      events: [],
      teams: [],
      showCreateEventModal: false,
      showAddTeamModalVisible: false,
      currentEvent: null,
      page: 1,
      limit: 2,
      showEditEventModalVisible: false,
      showDeleteEventModal: false,
      statuses: ['Активно', 'Неактивно', 'Завершено', 'Отменено'],
      showAddTeamMemberModalVisible: false,
      newTeamName: '',
      originalEvent: null,
      currentTeam: null,
      newEvent: {
        nameEvent: '',
        cityEvent: '',
        statusEvent: '',
        websiteEvent: '',
        startDateEvent: '', // Новое поле для даты начала
        endDateEvent: '' // Новое поле для даты окончания
      },
      selectedTeam: null,
      availableTeams: []
    }
  },
  created() {
    this.getEvents()
    this.getTeams()
    this.getAvailableTeams()
  },
  methods: {
    getTeamDataById(team_id) {
      const team = this.teams.find((team) => team._id.toString() === team_id)
      if (team) {
        const teachers = team.teachers.map((t) => `${t.name} ${t.surname}`).join(', ')
        const students = team.students.map((s) => `${s.name} ${s.surname} (${s.group})`).join(', ')
        return {
          teamname: team.teamname,
          teachers: teachers,
          students: students,
          statusParticipation: team.statusParticipation
        }
      }
      return null
    },
    async getEvents(page = 1, limit = 2) {
      console.log(`Getting events for page ${page} with limit ${limit}`)

      // Вычисление значения параметра skip
      const skip = (page - 1) * limit

      try {
        const response = await axios.get('http://localhost:5000/events', {
          params: {
            page,
            limit,
            skip // Добавление параметра skip в запрос
          }
        })
        this.events = response.data
      } catch (error) {
        console.error(error)
      }
    },

    nextPage() {
      console.log('Next page button clicked')

      this.page++
      this.getEvents(this.page, this.limit)
    },

    prevPage() {
      if (this.page > 1) {
        this.page -= 1
        this.getEvents(this.page, this.limit)
      }
    },

    getTeams() {
      axios
        .get('http://localhost:5000/teams')
        .then((response) => {
          this.teams = response.data
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getAvailableTeams() {
      axios
        .get('http://localhost:5000/teams')
        .then((response) => {
          this.availableTeams = response.data
        })
        .catch((error) => {
          console.error(error)
        })
    },
    formatDate(startDate, endDate) {
      const formattedStartDate = new Date(startDate).toLocaleDateString()
      const formattedEndDate = new Date(endDate).toLocaleDateString()
      return `${formattedStartDate} - ${formattedEndDate}`
    },

    showEditEventModal(event) {
      this.currentEvent = event
      this.originalEvent = { ...event } // сохраняем исходное состояние
      this.showEditEventModalVisible = true
    },

    showStatusDropdown(event) {
      event.showStatusDropdown = !event.showStatusDropdown
    },

    deleteEvent(eventId) {
      if (confirm(`Вы точно хотите удалить с таблицы "${event.title}"?`)) {
        axios
          .delete(`http://localhost:5000/events/${eventId}`)
          .then((response) => {
            console.log(response)
            this.getEvents()
          })
          .catch((error) => {
            console.error(error)
          })
      }
    },
    editEvent() {
      axios
        .put(`http://localhost:5000/events/${this.currentEvent._id}`, this.currentEvent)
        .then((response) => {
          console.log(response)
          this.getEvents()
        })
        .catch((error) => {
          console.error(error)
        })
      this.showEditEventModalVisible = false
      this.updateEventStatus()
    },
    createEvent() {
      const currentDate = new Date()
      const eventStartDate = new Date(this.newEvent.startDateEvent)
      const eventEndDate = new Date(this.newEvent.endDateEvent)

      // Устанавливаем значение statusEvent по умолчанию
      if (eventEndDate < currentDate) {
        this.newEvent.statusEvent = 'Завершено'
      } else if (eventStartDate <= currentDate && eventEndDate >= currentDate) {
        this.newEvent.statusEvent = 'Активно'
      } else {
        this.newEvent.statusEvent = 'Неактивно'
      }

      axios
        .post('http://localhost:5000/events', this.newEvent)
        .then((response) => {
          console.log(response)
          this.getEvents()
          this.newEvent.nameEvent = ''
          this.newEvent.cityEvent = ''
          this.newEvent.dateEvent = ''
          this.newEvent.statusEvent = ''
          this.newEvent.websiteEvent = ''
        })
        .catch((error) => {
          console.error(error)
        })
      this.showCreateEventModal = false
      this.updateEventStatus()
    },
    cancelEditEvent() {
      this.currentEvent = this.editedEvent // восстанавливаем исходное состояние
      this.showEditEventModalVisible = false // закрываем модальное окно
      this.getEvents() // обновляем таблицу
    },
    updateEventStatus() {
      const currentDate = new Date()

      this.events.forEach((event) => {
        const eventStartDate = new Date(event.startDateEvent)
        const eventEndDate = new Date(event.endDateEvent)

        // Если статус мероприятия уже 'Отменено', не изменяем его
        if (event.statusEvent === 'Отменено') {
          return
        }

        if (eventEndDate < currentDate) {
          event.statusEvent = 'Завершено'
        } else if (eventStartDate <= currentDate && eventEndDate >= currentDate) {
          event.statusEvent = 'Активно'
        } else {
          event.statusEvent = 'Неактивно'
        }

        // Сохраняем обновленный статус в базе данных
        axios
          .put(`http://localhost:5000/events/${event._id}`, event)
          .then((response) => {
            console.log(response)
          })
          .catch((error) => {
            console.error(error)
          })
      })
    },
    addTeamToEvent() {
      // Найти выбранную команду в списке доступных команд
      const selectedTeam = this.availableTeams.find((team) => team._id === this.selectedTeam)

      // Получить текущее событие
      const currentEvent = this.events.find((event) => event._id === this.currentEvent._id)

      // Отправить запрос PUT на сервер, чтобы добавить новую команду в существующее событие
      axios
        .put(`http://localhost:5000/events/${currentEvent._id}/teams/${selectedTeam._id}`, {
          statusParticipation: 'Участвуют'
        })
        .then((response) => {
          console.log(response)

          // Обновить текущее событие на клиентской стороне
          currentEvent.teams.push({
            team_id: selectedTeam._id,
            statusParticipation: 'Участвует'
          })

          // Обновить таблицу событий
          this.getEvents()

          // Скрыть модальное окно
          this.showAddTeamModalVisible = false
        })
        .catch((error) => {
          console.error(error)
        })
    },

    showAddTeamModal(event) {
      this.currentEvent = event
      this.showAddTeamModalVisible = true
    }
  },
  getStatusColor(status) {
    const colorMap = {
      Участвуют: 'text-yellow-500',
      Проиграли: 'text-red-500',
      '1 место': 'text-green-500',
      '2 место': 'text-green-500',
      '3 место': 'text-green-500'
    }

    return colorMap[status] || ''
  }
}
</script>
