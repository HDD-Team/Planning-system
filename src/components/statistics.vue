<template>
  <div class="mx-auto max-w-screen-xl px-8 py-4">
    <div>
      <div class="overflow-x-auto rounded-t-lg">
        <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <tr>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Действия</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Мероприятие</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Дата</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Участники</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Победы</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="item in items" :key="item._id">
              <td class="whitespace-nowrap px-4 py-2">
                <button
                  class="text-blue-500 hover:text-blue-700 focus:outline-none"
                  @click="editItem(item)"
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
                  @click="deleteItem(item)"
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
              <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                {{ item.eventname }}
              </td>
              <td class="whitespace-nowrap px-4 py-2 text-gray-700">
                {{ item.date }}
              </td>
              <td class="whitespace-nowrap px-4 py-2 text-gray-700">
                <span v-for="(student, index) in item.students" :key="index">
                  {{ student.surname }} {{ student.name }}
                  {{ index < item.students.length - 1 ? ', ' : '' }}
                </span>
              </td>
              <td class="whitespace-nowrap px-4 py-2 text-gray-700">
                {{ item.wins }}
              </td>
            </tr>
          </tbody>
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
      items: []
    }
  },
  async created() {
    await this.getAllItems()
  },
  methods: {
    async getAllItems() {
      try {
        // const response = await axios.get("http://localhost:3000/api/stats");

        this.items = [
          {
            _id: '1',
            eventname: 'Мероприятие 1',
            date: '2023-04-15',
            students: [
              { surname: 'Иванов', name: 'Иван' },
              { surname: 'Петров', name: 'Петр' }
            ],
            wins: '2'
          },
          {
            _id: '2',
            eventname: 'мероприятие 2',
            date: '2023-04-20',
            students: [
              { surname: 'Сидоров', name: 'Александр' },
              { surname: 'Кузнецов', name: 'Дмитрий' }
            ],
            wins: '1'
          }
        ]
      } catch (error) {
        console.error(error)
      }
    },
    editItem(item) {
      // Реализуйте логику редактирования элемента
      // Например, можно открыть модальное окно с формой редактирования
      console.log('Edit item:', item)
    },
    deleteItem(item) {
      if (confirm(`Вы точно хотите удалить с таблицы "${item.eventname}"?`)) {
        const index = this.items.findIndex((i) => i._id === item._id)
        if (index !== -1) {
          this.items.splice(index, 1)
        }
      }
    }
  }
}
</script>
