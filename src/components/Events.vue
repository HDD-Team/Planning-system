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
          <tr v-for="event in events" :key="event.id">
            <td class="whitespace-nowrap px-4 py-2">
              <button
                class="text-blue-500 hover:text-blue-700 focus:outline-none"
                @click="showEditEventModal(event)"
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
                @click="deleteEvent(event)"
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
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">{{ event.title }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ event.location }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ event.date }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700 relative inline-block text-left">
              <div>
                <span class="text-gray-700">{{ event.selectedStatus || event.status }}</span>
              </div>

              <div>
                <!-- Status Dropdown -->
                <div
                  v-if="event.showStatusDropdown"
                  class="absolute mt-2 w-32 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5"
                >
                  <div
                    class="py-1"
                    role="menu"
                    aria-orientation="vertical"
                    aria-labelledby="options-menu"
                  >
                    <a
                      v-for="status in statuses"
                      :key="status"
                      @click="selectStatus(event, status)"
                      class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900"
                      role="menuitem"
                    >
                      {{ status }}
                    </a>
                  </div>
                </div>
              </div>
              <!-- Status Dropdown -->
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-sm text-gray-500">
              <!-- Изменение для отображения источника в виде ссылки -->
              <a :href="event.source" target="_blank" class="text-blue-500 hover:text-blue-700"
                >Источник</a
              >
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-sm text-gray-500">
              <!-- Команды мероприятия -->
              <div v-for="team in event.teams" :key="team.id">
                <strong>{{ team.name }}</strong> (Руководитель: {{ team.leader }}, Участники:
                {{ team.members }}, Статус: {{ team.status }})
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Модальное окно создания мероприятия -->
    <div v-if="showCreateEventModal" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Создать мероприятие</h2>
        <!-- Форма создания мероприятия -->
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mt-4"
          @click="showCreateEventModal = false"
        >
          Отмена
        </button>
      </div>
    </div>

    <!-- Модальное окно добавления команды -->
    <div v-if="showAddTeamModalVisible" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Добавить команду</h2>
        <!-- Форма добавления команды -->
        <form @submit.prevent="addTeam">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="team">
              Name of the team
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="team"
              type="text"
              v-model="newTeamName"
            />
          </div>
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
            type="submit"
          >
            Добавить
          </button>
          <button
            class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mt-4"
            @click="showAddTeamModalVisible = false"
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
              v-model="currentEvent.title"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="location"> Место </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="location"
              type="text"
              v-model="currentEvent.location"
            />
          </div>
          <div class="mb-4 cursor-pointer">
            <label class="block text-gray-700 text-sm font-bold mb-2 cursor-pointer" for="date">
              Дата
            </label>
            <input
              class="cursor-pointer shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="date"
              type="date"
              v-model="currentEvent.date"
            />
          </div>
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
            type="submit"
          >
            Сохранить
          </button>
          <button
            class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mt-4"
            @click="showEditEventModalVisible = false"
          >
            Отмена
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      events: [
        // Первое мероприятие
        {
          id: 1,
          title: 'Мероприятие 1',
          location: 'Москва',
          date: '2023-04-01',
          status: 'Активно',
          selectedStatus: '',
          showStatusDropdown: false,
          source: 'https://example.com',
          teams: [
            // Пример команды
            {
              id: 1,
              name: 'Команда 1',
              leader: 'Иван Иванов',
              members: 'Петр Петров, Сидор Сидоров',
              status: 'Заняли 1 место'
            }
          ]
        },
        // Второе мероприятие
        {
          id: 2,
          title: 'Мероприятие 2',
          location: 'Санкт-Петербург',
          date: '2023-05-15',
          status: 'Неактивно',
          selectedStatus: '',
          showStatusDropdown: false,
          source: 'https://example.org',
          teams: [
            // Пример команды
            {
              id: 1,
              name: 'Команда 2',
              leader: 'Александр Александров',
              members: 'Алексей Алексеев, Мария Марина',
              status: 'Проиграли'
            }
          ]
        },
        {
          id: 1,
          title: 'Мероприятие 1',
          location: 'Москва',
          date: '2023-04-01',
          status: 'Активно',
          selectedStatus: '',
          showStatusDropdown: false,
          source: 'https://example.com',
          teams: [
            // Пример команды
            {
              id: 1,
              name: 'Команда 1',
              leader: 'Иван Иванов',
              members: 'Петр Петров, Сидор Сидоров',
              status: 'Заняли 1 место'
            },
            // Новая команда
            {
              id: 2,
              name: 'Команда 3',
              leader: 'Алексей Алексеев',
              members: 'Мария Марина, Сергей Сергеев',
              status: 'Заняли 3 место'
            }
          ]
        }
      ],
      showCreateEventModal: false,
      showAddTeamModalVisible: false,
      currentEvent: null,
      showEditEventModalVisible: false,
      showDeleteEventModal: false,
      statuses: ['Активно', 'Неактивно', 'Завершено', 'Отменено'],
      showAddTeamMemberModalVisible: false,
      newTeamName: '',
      currentTeam: null
    }
  },
  mounted() {
    this.updateEventStatus()
  },
  methods: {
    showAddTeamModal(event) {
      this.currentEvent = event
      this.showAddTeamModalVisible = true
    },
    showEditEventModal(event) {
      this.currentEvent = event
      this.showEditEventModalVisible = true
    },
    showStatusDropdown(event) {
      event.showStatusDropdown = !event.showStatusDropdown
    },
    selectStatus(event, status) {
      event.selectedStatus = status
      event.showStatusDropdown = false
    },
    deleteEvent(event) {
      if (confirm(`Вы точно хотите удалить с таблицы "${event.title}"?`)) {
        const index = this.events.findIndex((e) => e.id === event.id)
        if (index !== -1) {
          this.events.splice(index, 1)
        }
      }
    },
    editEvent() {
      const index = this.events.findIndex((event) => event.id === this.currentEvent.id)
      if (index !== -1) {
        this.events.splice(index, 1, this.currentEvent)
      }
      this.showEditEventModalVisible = false
      this.updateEventStatus()
    },
    addTeam() {
      if (this.newTeamName) {
        this.currentEvent.teams.push({
          id: this.currentEvent.teams.length + 1,
          name: this.newTeamName,
          leader: '',
          members: '',
          status: ''
        })
        this.newTeamName = ''
        this.showAddTeamModalVisible = false
      }
    },
    updateEventStatus() {
      const currentDate = new Date().toISOString().slice(0, 10)

      this.events.forEach((event) => {
        if (event.date < currentDate) {
          event.status = 'Завершено'
          event.selectedStatus = 'Завершено'
        } else {
          event.status = 'Неактивно'
          event.selectedStatus = 'Неактивно'
        }
      })
    }
  }
}
</script>
