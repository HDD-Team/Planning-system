<template>
  <div class="relative">
    <button
      class="flex items-center justify-center text-gray-900"
      @click="showCalendar = !showCalendar"
    >
      <svg
        class="h-6 w-6"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
        />
      </svg>
    </button>
    <div
      v-if="showCalendar"
      class="mt-10 text-center lg:col-start-8 lg:col-end-13 lg:row-start-1 lg:mt-9 xl:col-start-9"
      style="transform: scale(0.75)"
    >
      <div class="flex items-center justify-center text-gray-900">
        <button
          type="button"
          @click="previousMonth"
          class="-m-1.5 flex flex-none items-center justify-center p-1.5 text-gray-400 hover:text-gray-500"
        >
          <span class="sr-only">Previous month</span>
          <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path
              fill-rule="evenodd"
              d="M12.79 5.23a.75.75 0 01-.02 1.06L8.832 10l3.938 3.71a.75.75 0 11-1.04 1.08l-4.5-4.25a.75.75 0 010-1.08l4.5-4.25a.75.75 0 011.06.02z"
              clip-rule="evenodd"
            />
          </svg>
        </button>
        <div class="flex-auto text-sm font-semibold">{{ monthAndYear }}</div>
        <button
          type="button"
          @click="nextMonth"
          class="-m-1.5 flex flex-none items-center justify-center p-1.5 text-gray-400 hover:text-gray-500"
        >
          <span class="sr-only">Next month</span>
          <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path
              fill-rule="evenodd"
              d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.5 4.25a.75.75 0 010 1.08l-4.5 4.25a.75.75 0 01-1.06-.02z"
              clip-rule="evenodd"
            />
          </svg>
        </button>
      </div>
      <div class="mt-6 grid grid-cols-7 text-xs leading-6 text-center text-gray-500">
        <div>Sun</div>
        <div>Mon</div>
        <div>Tue</div>
        <div>Wed</div>
        <div>Thu</div>
        <div>Fri</div>
        <div>Sat</div>
      </div>
      <div
        class="isolate mt-2 grid grid-cols-7 gap-px rounded-lg bg-gray-200 text-sm shadow ring-1 ring-gray-200"
        style="width: 300px; height: 300px"
      >
        <div
          v-for="(day, index) in firstDayOfMonth + daysInMonth"
          :key="index"
          :class="[
            'py-1.5',
            index < firstDayOfMonth ? 'bg-gray-50' : 'hover:bg-gray-100',
            getDayClass(index - firstDayOfMonth + 1)
          ]"
          style="height: 40px; display: flex; align-items: center; justify-content: center"
        >
          <time
            v-if="index >= firstDayOfMonth"
            :datetime="`${currentYear}-${currentMonth + 1}-${index - firstDayOfMonth + 1}`"
            class="mx-auto flex h-7 w-7 items-center justify-center rounded-full"
            >{{ index - firstDayOfMonth + 1 }}</time
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showCalendar: false,
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear()
    }
  },
  computed: {
    monthAndYear() {
      const monthNames = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
      ]
      return `${monthNames[this.currentMonth]} ${this.currentYear}`
    },
    daysInMonth() {
      return new Date(this.currentYear, this.currentMonth + 1, 0).getDate()
    },
    firstDayOfMonth() {
      return new Date(this.currentYear, this.currentMonth, 1).getDay()
    }
  },
  methods: {
    previousMonth() {
      this.currentMonth--
      if (this.currentMonth < 0) {
        this.currentMonth = 11
        this.currentYear--
      }
    },
    nextMonth() {
      this.currentMonth++
      if (this.currentMonth > 11) {
        this.currentMonth = 0
        this.currentYear++
      }
    },
    getDayClass(day) {
      const today = new Date()
      if (
        today.getFullYear() === this.currentYear &&
        today.getMonth() === this.currentMonth &&
        today.getDate() === day
      ) {
        return 'bg-blue-500 text-white'
      }
      return 'h-14'
    }
  }
}
</script>
