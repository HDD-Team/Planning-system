<template>
  <header class="bg-gray-50">
    <div class="mx-auto max-w-screen-xl sm:px-6 sm:py-8 lg:px-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <div class="text-center sm:text-left">
          <h1 class="text-2xl font-bold text-gray-900 sm:text-3xl">Система планирования</h1>

          <p class="mt-1.5 text-sm text-gray-500">Разработано командой HDD🎉</p>
        </div>

        <nav class="mt-4 sm:mt-0 sm:flex sm:items-center sm:justify-center">
          <a
            href="/events"
            class="inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mx-2"
          >
            Мероприятия
          </a>

          <a
            href="/teams"
            class="inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mx-2"
          >
            Команды
          </a>

          <a
            href="#"
            class="inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mx-2"
          >
            Статистика
          </a>
        </nav>

        <div>
          <div class="mt-4 flex flex-col gap-4 sm:mt-0 sm:flex-row sm:items-center">
            <img
              src="https://pushinka.top/uploads/posts/2023-04/1680574699_pushinka-top-p-avatarka-khottabich-avatarka-pinterest-47.jpg"
              alt="Avatar"
              class="w-12 h-12 rounded-full mr-4"
            />
            <div>
              <p class="font-bold text-lg">Далиба Богдан</p>
              <p class="text-sm">HDD@gmail.com</p>
              <button
                class="mt-2 inline-flex items-center justify-center px-2 py-1 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                @click="logout"
              >
                <i class="fas fa-sign-out-alt mr-1"></i>
                Выйти
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
