<template>
  <div class="max-w-2xl mx-auto md:px-40 mt-4 px-8 py-4">
    <div class="relative inline-block text-left">
      <button
        @click="toggleDropdown"
        class="inline-flex justify-center w-full px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-blue-500"
      >
        Мероприятие
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-5 h-5 ml-2 -mr-1"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
        >
          <path
            fill-rule="evenodd"
            d="M6.293 9.293a1 1 0 011.414 0L10 11.586l2.293-2.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z"
            clip-rule="evenodd"
          />
        </svg>
      </button>
      <div
        :class="{ hidden: !isDropdownOpen }"
        class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5"
      >
        <div
          class="py-2 p-2"
          role="menu"
          aria-orientation="vertical"
          aria-labelledby="dropdown-button"
        >
          <a
            href="#"
            class="block px-4 py-2 mb-1 text-sm text-gray-700 rounded-md bg-white hover:bg-gray-100"
            role="menuitem"
            >Item 1</a
          >
          <a
            href="#"
            class="block px-4 py-2 mb-1 text-sm text-gray-700 rounded-md bg-white hover:bg-gray-100"
            role="menuitem"
            >Item 2</a
          >
          <a
            href="#"
            class="block px-4 py-2 mb-1 text-sm text-gray-700 rounded-md bg-white hover:bg-gray-100"
            role="menuitem"
            >Item 3</a
          >

          <!-- Input field and submit button inside the dropdown -->
          <input
            type="text"
            id="input-field"
            class="w-full px-4 py-2 border rounded-md mb-2 focus:outline-none focus:border-blue-500"
            placeholder="Добавить мероприятие"
          />
          <button
            id="submit-button"
            class="w-full px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            Add
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isDropdownOpen: false
    }
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen
    }
  },
  mounted() {
    window.addEventListener('click', (event) => {
      if (!this.$el.contains(event.target)) {
        this.isDropdownOpen = false
      }
    })
  }
}
</script>
