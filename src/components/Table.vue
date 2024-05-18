<template>
  <div class="mx-auto max-w-screen-xl px-8 py-4">
    <!-- Table code here -->
    <div>
      <div class="overflow-x-auto rounded-t-lg">
        <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <tr>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Руководитель</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Название команды
              </th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Участники</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Мероприятия</th>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Действия</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="item in items" :key="item._id">
              <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                {{ item.teacher.surname }} {{ item.teacher.name }}
              </td>
              <td class="whitespace-nowrap px-4 py-2 text-gray-700">
                {{ item.teamname }}
              </td>
              <td class="whitespace-nowrap px-4 py-2 text-gray-700">
                <span v-for="(student, index) in item.students" :key="index">
                  {{ student.surname }} {{ student.name }} ({{ student.group }}){{
                    index < item.students.length - 1 ? ', ' : ''
                  }}
                </span>
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
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="6" class="text-left">
                <button
                  @click="showNewItemForm"
                  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
                >
                  +
                </button>
              </td>
            </tr>
          </tfoot>
        </table>
      </div>
      <div class="rounded-b-lg border-t border-gray-200 px-4 py-2">
        <ol class="flex justify-end gap-1 text-xs font-medium">
          <li>
            <a
              href="#"
              class="inline-flex size-8 items-center justify-center rounded border border-gray-100 bg-white text-gray-900 rtl:rotate-180"
            >
              <span class="sr-only">Prev Page</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-3 w-3"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                  clip-rule="evenodd"
                />
              </svg>
            </a>
          </li>
          <li>
            <a
              href="#"
              class="block size-8 rounded border border-gray-100 bg-white text-center leading-8 text-gray-900"
            >
              1
            </a>
          </li>
          <li
            class="block size-8 rounded border-blue-600 bg-blue-600 text-center leading-8 text-white"
          >
            2
          </li>
          <li>
            <a
              href="#"
              class="block size-8 rounded border border-gray-100 bg-white text-center leading-8 text-gray-900"
            >
              3
            </a>
          </li>
          <li>
            <a
              href="#"
              class="block size-8 rounded border border-gray-100 bg-white text-center leading-8 text-gray-900"
            >
              4
            </a>
          </li>
          <li>
            <a
              href="#"
              class="inline-flex size-8 items-center justify-center rounded border border-gray-100 bg-white text-gray-900 rtl:rotate-180"
            >
              <span class="sr-only">Next Page</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-3 w-3"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                  clip-rule="evenodd"
                />
              </svg>
            </a>
          </li>
        </ol>
      </div>
    </div>
    <!-- Modal code here -->
    <div v-if="editedItem" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-8 rounded-lg shadow-lg">
        <h2 class="text-xl font-medium mb-4">Редактирование элемента</h2>
        <form @submit.prevent="saveEditedItem">
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="teacher"> Руководитель </label>
            <!-- You cannot directly bind an array of objects to an input field.
            You should provide a way to add/remove teamname and edit their names/surnames.
            This is a placeholder input field. -->
            <input
              type="text"
              id="teacher"
              placeholder="You cannot edit teacher directly. Use a dedicated interface."
              disabled
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="events">
              Название команды
            </label>
            <!-- You cannot directly bind an array of objects to an input field.
            You should provide a way to add/remove teamname and edit their names/surnames.
            This is a placeholder input field. -->
            <input
              type="text"
              id="teamname"
              placeholder="You cannot edit teamname directly. Use a dedicated interface."
              disabled
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="events"> Участники </label>
            <!-- You cannot directly bind an array of objects to an input field.
            You should provide a way to add/remove students and edit their names/surnames.
            This is a placeholder input field. -->
            <input
              type="text"
              id="students"
              placeholder="You cannot edit students directly. Use a dedicated interface."
              disabled
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="events"> Мероприятия </label>
            <!-- Similar to students, you cannot directly bind an array of objects to an input field.
            You should provide a way to add/remove events and edit their details.
            This is a placeholder input field. -->
            <input
              type="text"
              id="events"
              placeholder="You cannot edit events directly. Use a dedicated interface."
              disabled
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div class="flex justify-end">
            <button
              type="button"
              @click="cancelEditing"
              class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mr-2"
            >
              Отмена
            </button>
            <button
              type="submit"
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >
              Сохранить
            </button>
          </div>
        </form>
      </div>
    </div>
    <!-- Add new item form -->
    <div v-if="showNewItemForm" class="fixed inset-0 flex items-center justify-center">
      <div class="bg-white p-8 rounded-lg shadow-lg">
        <h2 class="text-xl font-medium mb-4">Add New Item</h2>
        <form @submit.prevent="addNewItem">
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="teacher"> Teacher </label>
            <input
              v-model="newItem.teacher.name"
              type="text"
              id="teacher"
              placeholder="Teacher name"
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="teamname"> Team Name </label>
            <input
              v-model="newItem.teamname"
              type="text"
              id="teamname"
              placeholder="Team name"
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <!-- Add more form inputs for students and events -->
          <div class="flex justify-end">
            <button
              type="button"
              @click="cancelAdding"
              class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mr-2"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >
              Add
            </button>
          </div>
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
      items: [],
      editedItem: null,
      newItem: {
        teacher: {},
        teamname: '',
        students: [],
        events: []
      },
      showNewItemForm: false
    }
  },
  async created() {
    // Get all items when the component is created
    await this.getAllItems()
  },
  methods: {
    async getAllItems() {
      try {
        // Send a GET request to the server
        const response = await axios.get('http://localhost:3000/api/cards')

        // Set the items data property to the response data
        this.items = response.data
      } catch (error) {
        console.error(error)
      }
    },
    editItem(item) {
      // Create a copy of the item to be edited
      this.editedItem = { ...item }
    },
    async saveEditedItem() {
      try {
        // Send a PUT request to the server
        const response = await axios.put(
          `http://localhost:3000/api/cards/${this.editedItem._id}`,
          this.editedItem
        )

        // Update the item in the items array
        const index = this.items.findIndex((item) => item._id === this.editedItem._id)
        this.items.splice(index, 1, response.data)

        // Close the modal
        this.editedItem = null
      } catch (error) {
        console.error(error)
      }
    },
    viewDetails(item) {
      // Open the details modal (not shown in the example)
    },
    showNewItemForm() {
      this.showNewItemForm = true
    },
    async addNewItem() {
      try {
        // Send a POST request to the server
        const response = await axios.post('http://localhost:3000/api/cards', this.newItem)

        // Add the new item to the items array
        this.items.push(response.data)

        // Reset the newItem form
        this.newItem = {
          teacher: {},
          teamname: '',
          students: [],
          events: []
        }

        // Close the new item form
        this.showNewItemForm = false
      } catch (error) {
        console.error(error)
      }
    },
    deleteItem(item) {
      if (confirm(`Вы точно хотите удалить с таблицы "${item.eventname}"?`)) {
        const index = this.items.findIndex((i) => i._id === item._id)
        if (index !== -1) {
          this.items.splice(index, 1)
        }
      }
    },
    cancelEditing() {
      // Close the modal and discard any changes
      this.editedItem = null
    },
    cancelAdding() {
      this.showNewItemForm = false
    }
  }
}
</script>
