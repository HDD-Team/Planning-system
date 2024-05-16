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
            </td>
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">{{ event.title }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ event.location }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ event.date }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700 relative inline-block text-left">
              <div>
                <span class="text-gray-700">{{ event.selectedStatus || event.status }}</span>
              </div>
              <div>
                <button
                  class="text-blue-500 hover:text-blue-700 focus:outline-none ml-2"
                  @click="showStatusDropdown(event)"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.343 4.343 7.757l5.656 5.657z"
                    />
                  </svg>
                </button>
              </div>
              <!-- Status Dropdown -->
              <div class="relative">
                <!-- Status Dropdown -->
                <div
                  v-if="event.showStatusDropdown"
                  class="absolute mt-2 w-40 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5"
                >
                  <div class="py-1">
                    <a
                      v-for="status in statusOptions"
                      :key="status"
                      href="#"
                      class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      @click.prevent="selectStatus(event, status)"
                      >{{ status }}</a
                    >
                  </div>
                </div>
              </div>
            </td>
            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
              <a :href="event.source" target="_blank" class="text-blue-500">Источник</a>
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
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mt-4"
          @click="showAddTeamModalVisible = false"
        >
          Отмена
        </button>
      </div>
    </div>
    <!-- Модальное окно редактирования мероприятия -->
    <div v-if="showEditEventModalVisible" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Редактировать мероприятие</h2>
        <!-- Форма редактирования мероприятия -->
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mt-4"
          @click="showEditEventModalVisible = false"
        >
          Отмена
        </button>
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
          selectedStatus: '', // Add this property
          showStatusDropdown: false, // Add this property
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
          selectedStatus: '', // Add this property
          showStatusDropdown: false, // Add this property
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
          selectedStatus: '', // Add this property
          showStatusDropdown: false, // Add this property
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
      statusOptions: ['Активно', 'Неактивно', 'Ожидание'] // Update the status options
    }
  },
  methods: {
    showAddTeamModal(event) {
      this.currentEvent = event
      this.showAddTeamModalVisible = true
    },
    showEditEventModal(event) {
      // Добавьте этот метод
      this.currentEvent = event
      this.showEditEventModalVisible = true
    },
    // Добавьте метод для обработки ввода команды и добавления ее в мероприятие
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
    }
  }
}
</script>
