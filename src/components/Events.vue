<template>
  <div class="mx-auto max-w-screen-xl px-8 py-4">
    <h1 class="text-2xl font-bold mb-4 text-white">Мероприятия</h1>

    <div class="flex justify-between items-center mb-4">
      <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        @click="showCreateEventModal = true"
      >
        Создать мероприятие
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
                    d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V4a2 2 0 00-2-2H6zM14.586 8l-2.293-2.293a1 1 0 00-1.414 0L10 10.586 7.707 8.293a1 1 0 10-1.414 1.414L10 11.414l2.293 2.293a1 1 001.414 0L14.586 10l-1.293-1.293z"
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
            <td
              class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 cursor-pointer"
              :class="{ 'cursor-pointer': event.statusEvent === 'Завершено' }"
              @click="showEventReportModal(event)"
            >
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
                <strong>
                  {{ getTeamDataById(team.team_id)?.teamname }}
                  <span
                    :class="getStatusColor(team.statusParticipation)"
                    @click="showChangeStatusModal(event, team)"
                    class="cursor-pointer"
                  >
                    {{ team.statusParticipation }}
                  </span>
                </strong>
                (Руководитель: {{ getTeamDataById(team.team_id)?.teachers }} Участники:
                {{ getTeamDataById(team.team_id)?.students }})
              </div>
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
                'text-gray-700 hover:text-gray-900': n !== page
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
                  d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 010-1.414l4-4a1 1 011.414 1.414L5.414 10l3.293 3.293a1 1 010 1.414z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
          </li>
        </ul>
      </nav>
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
              Чтобы вернуть к предыдущему статусу выберите его в списке.
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
        <h2 class="text-xl font-bold mb-4">Управление командами</h2>
        <div class="mb-4 max-h-60 overflow-y-auto">
          <div v-for="team in availableTeams" :key="team._id" class="flex items-center">
            <input type="checkbox" :value="team._id" v-model="selectedTeams" class="mr-2" />
            <label class="block text-gray-700 text-sm font-bold mb-2" for="team">{{
              team.teamname
            }}</label>
          </div>
        </div>
        <button
          @click="addTeamToEvent"
          class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Сохранить изменения
        </button>
        <button
          @click="showAddTeamModalVisible = false"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Отмена
        </button>
      </div>
    </div>

    <!-- Модальное окно изменения статуса команды -->
    <div v-if="showChangeStatusModalVisible" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Изменить статус команды</h2>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="status"> Статус </label>
          <select
            class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            id="status"
            v-model="selectedTeam.statusParticipation"
          >
            <option value="">Выберите статус</option>
            <option>Участвуют</option>
            <option>1 место</option>
            <option>2 место</option>
            <option>3 место</option>
            <option>Проиграли</option>
            <option>Не участвовали</option>
          </select>
        </div>
        <button
          @click="changeTeamStatus"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Сохранить
        </button>
        <button
          @click="showChangeStatusModalVisible = false"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Отмена
        </button>
      </div>
    </div>

    <!-- Модальное окно фильтрации -->
    <div v-if="showFilterModal" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Фильтрация мероприятий</h2>
        <div class="mb-4">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Поиск названия мероприятия, города"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="startDate">
            Дата начала
          </label>
          <input
            v-model="filter.startDate"
            type="date"
            id="startDate"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="endDate">
            Дата конца
          </label>
          <input
            v-model="filter.endDate"
            type="date"
            id="endDate"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="status"> Статус </label>
          <select
            v-model="filter.status"
            id="status"
            class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
          >
            <option value="">Выберите статус</option>
            <option>Активно</option>
            <option>Неактивно</option>
            <option>Завершено</option>
            <option>Отменено</option>
          </select>
        </div>
        <button
          @click="applyFilters"
          class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Применить
        </button>
        <button
          @click="clearFilters"
          class="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Очистить
        </button>
        <button
          @click="showFilterModal = false"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Отмена
        </button>
      </div>
    </div>

    <!-- Модальное окно отчета мероприятия -->
    <div v-if="showEventReportModalVisible" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-6 rounded shadow shadow-lg">
        <h2 class="text-xl font-bold mb-4">Отчет мероприятия</h2>
        <div class="mb-4">
          <p><strong>Мероприятие:</strong> {{ currentEvent.nameEvent }}</p>
          <p><strong>Город:</strong> {{ currentEvent.cityEvent }}</p>
          <p>
            <strong>Даты:</strong>
            {{ formatDate(currentEvent.startDateEvent, currentEvent.endDateEvent) }}
          </p>
          <div v-for="team in currentEvent.teams" :key="team.team_id">
            <p><strong>Команда:</strong> {{ getTeamDataById(team.team_id)?.teamname }}</p>
            <p><strong>Руководители:</strong> {{ getTeamDataById(team.team_id)?.teachers }}</p>
            <p><strong>Участники:</strong> {{ getTeamDataById(team.team_id)?.students }}</p>
            <p><strong>Статус:</strong> {{ team.statusParticipation }}</p>
          </div>
        </div>
        <button
          @click="showEventReportModalVisible = false"
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded rounded mb-4"
        >
          Закрыть
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Events',
  data() {
    return {
      events: [],
      teams: [],
      showCreateEventModal: false,
      showAddTeamModalVisible: false,
      showFilterModal: false,
      currentEvent: null,
      page: 1,
      limit: 10,
      totalPages: 1,
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
      selectedTeams: [],
      availableTeams: [],
      searchQuery: '', // Поле для поискового запроса
      filter: {
        startDate: '',
        endDate: '',
        status: ''
      }, // Фильтры для даты и статуса
      showChangeStatusModalVisible: false,
      showEventReportModalVisible: false
    }
  },
  created() {
    this.page = parseInt(this.$route.query.page) || 1
    this.limit = parseInt(this.$route.query.limit) || 10
    this.getEvents()
    this.getTeams()
    this.getAvailableTeams()
  },
  watch: {
    '$route.query.page'(newPage) {
      this.page = parseInt(newPage) || 1
      this.getEvents()
    },
    '$route.query.limit'(newLimit) {
      this.limit = parseInt(newLimit) || 10
      this.getEvents()
    }
  },
  methods: {
    getTeamDataById(team_id) {
      const team = this.teams.find((team) => team._id.toString() === team_id)
      if (team) {
        const teachers = team.teachers.map((t) => `${t.name} ${t.surname}`).join(' ')
        const students = team.students.map((s) => `${s.name} ${s.surname} (${s.group})`).join(' ')
        return {
          teamname: team.teamname,
          teachers: teachers,
          students: students,
          statusParticipation: team.statusParticipation
        }
      }
      return null
    },
    async getEvents(page = this.page, limit = this.limit) {
      console.log(`Getting events for page ${page} with limit ${limit}`)

      try {
        const response = await axios.get('http://localhost:5000/events', {
          params: {
            page,
            limit,
            search: this.searchQuery,
            startDate: this.filter.startDate,
            endDate: this.filter.endDate,
            status: this.filter.status
          }
        })
        this.events = response.data.events
        this.totalPages = response.data.total_pages
        this.page = response.data.current_page
        this.$router.push({ query: { page: this.page, limit: this.limit } })
      } catch (error) {
        console.error(error)
      }
    },
    nextPage() {
      if (this.page < this.totalPages) {
        this.page++
        this.getEvents(this.page, this.limit)
      }
    },
    prevPage() {
      if (this.page > 1) {
        this.page--
        this.getEvents(this.page, this.limit)
      }
    },
    goToPage(page) {
      if (page !== this.page) {
        this.page = page
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
      if (confirm(`Вы точно хотите удалить мероприятие "${eventId}"?`)) {
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

      // Добавление нового мероприятия
      axios
        .post('http://localhost:5000/events', { ...this.newEvent, teams: [] }) // Инициализация массива teams
        .then((response) => {
          console.log(response)
          // Добавление нового мероприятия в начало массива events
          const newEvent = response.data
          this.events.unshift(newEvent)
          this.currentEvent = newEvent // Установить текущее мероприятие на новое
          this.getAvailableTeams()
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
    async addTeamToEvent() {
      const currentEvent = this.currentEvent

      if (!currentEvent.teams) {
        currentEvent.teams = []
      }

      try {
        // Добавление новых команд
        for (const team_id of this.selectedTeams) {
          const exists = currentEvent.teams.some((t) => t.team_id === team_id)
          if (!exists) {
            console.log(`Adding team with ID: ${team_id}`)
            await axios.put(`http://localhost:5000/events/${currentEvent._id}/teams/${team_id}`, {
              statusParticipation: 'Участвуют'
            })
            currentEvent.teams.push({
              team_id: team_id,
              statusParticipation: 'Участвуют'
            })
          }
        }

        // Удаление команд, которые были убраны из выбранных
        const removedTeams = currentEvent.teams.filter(
          (t) => !this.selectedTeams.includes(t.team_id)
        )
        for (const team of removedTeams) {
          try {
            console.log(`Removing team with ID: ${team.team_id}`)
            const response = await axios.delete(
              `http://localhost:5000/events/${currentEvent._id}/teams/${team.team_id}`
            )
            if (response.status === 200) {
              currentEvent.teams = currentEvent.teams.filter((t) => t.team_id !== team.team_id)
            }
          } catch (error) {
            console.error(
              'Error removing team from event:',
              error.response ? error.response.data : error
            )
          }
        }

        this.getEvents()
      } catch (error) {
        console.error('Error adding team to event:', error.response ? error.response.data : error)
      } finally {
        this.showAddTeamModalVisible = false
        this.selectedTeams = []
      }
    },
    showAddTeamModal(event) {
      this.currentEvent = event
      this.selectedTeams = (event.teams || []).map((team) => team.team_id)
      this.showAddTeamModalVisible = true
    },
    showChangeStatusModal(event, team) {
      this.currentEvent = event
      this.selectedTeam = { ...team } // Создаем копию объекта команды
      this.showChangeStatusModalVisible = true
    },
    async changeTeamStatus() {
      const team = this.currentEvent.teams.find((t) => t.team_id === this.selectedTeam.team_id)
      if (team) {
        team.statusParticipation = this.selectedTeam.statusParticipation
        try {
          await axios.put(
            `http://localhost:5000/events/${this.currentEvent._id}/teams/${team.team_id}`,
            {
              statusParticipation: team.statusParticipation
            }
          )
          this.getEvents()
        } catch (error) {
          console.error(error)
        }
      }
      this.showChangeStatusModalVisible = false
    },
    getStatusColor(status) {
      const colorMap = {
        '1 место': 'text-green-500',
        '2 место': 'text-green-500',
        '3 место': 'text-green-500',
        Участвуют: 'text-orange-500',
        'Не участвовали': 'text-red-500',
        Проиграли: 'text-red-500'
      }

      return colorMap[status] || ''
    },
    async deleteTeamFromEvent(event_id, team_id) {
      try {
        const response = await axios.delete(
          `http://localhost:5000/events/${event_id}/teams/${team_id}`
        )
        if (response.status === 200) {
          const event = this.events.find((e) => e._id === event_id)
          if (event) {
            event.teams = event.teams.filter((t) => t.team_id !== team_id)
          }
        }
      } catch (error) {
        console.error(error)
      }
    },
    toggleFilterModal() {
      this.showFilterModal = !this.showFilterModal
    },
    applyFilters() {
      this.page = 1
      this.getEvents()
      this.showFilterModal = false
    },
    clearFilters() {
      this.filter = {
        startDate: '',
        endDate: '',
        status: ''
      }
      this.getEvents()
      this.showFilterModal = false
    },
    showEventReportModal(event) {
      if (event.statusEvent === 'Завершено') {
        this.currentEvent = event
        this.showEventReportModalVisible = true
      }
    }
  }
}
</script>
