<template>
  <section class="bg-white">
    <div class="lg:grid lg:min-h-screen lg:grid-cols-12">
      <section
        class="relative flex h-32 items-end bg-gray-900 lg:col-span-5 lg:h-full xl:col-span-6"
      >
        <img
          alt=""
          src="https://i4.photo.2gis.com/images/geo/24/3377699734388128_ca93.jpg"
          class="absolute inset-0 h-full w-full object-cover opacity-80"
        />

        <div class="hidden lg:relative lg:block lg:p-12">
          <a class="block text-white" href="/login">
            <span class="sr-only">login</span>
            <img
              alt=""
              viewBox="0 0 28 24"
              fill="none"
              src="https://doklad-diploma.ru/wp-content/uploads/2022/05/rgeu-scaled.jpg"
              class="h-8 sm:h-10"
            />
          </a>

          <h2 class="mt-6 text-2xl font-bold text-white sm:text-3xl md:text-4xl">
            Приветсвую в системе планирования 📝
          </h2>

          <p class="mt-4 leading-relaxed text-white/90">Веб приложение разработано командой HDD</p>
        </div>
      </section>

      <main
        class="flex items-center justify-center px-8 py-8 sm:px-12 lg:col-span-7 lg:px-16 lg:py-12 xl:col-span-6"
      >
        <div class="max-w-xl lg:max-w-3xl">
          <div class="relative -mt-16 block lg:hidden">
            <a
              class="inline-flex size-16 items-center justify-center text-blue-600 sm:size-20"
              href="/login"
            >
              <span class="sr-only">login</span>

              <img
                alt=""
                src="https://doklad-diploma.ru/wp-content/uploads/2022/05/rgeu-scaled.jpg"
                class="h-8 sm:h-10"
              />
            </a>

            <h1 class="mt-2 text-2xl font-bold text-gray-900 sm:text-3xl md:text-4xl">
              Приветсвую в системе планирования 📝
            </h1>

            <p class="mt-4 leading-relaxed text-gray-500">
              Веб приложение разработано командой HDD
            </p>
          </div>

          <form @submit.prevent="login" class="mt-8 grid grid-cols-6 gap-6">
            <div class="col-span-6">
              <label for="Email" class="block text-sm font-medium text-gray-700"> Почта </label>
              <input
                type="email"
                id="Email"
                name="email"
                v-model="email"
                class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
              />
            </div>

            <div class="col-span-6 sm:col-span-3">
              <label for="Password" class="block text-sm font-medium text-gray-700"> Пароль </label>
              <input
                type="password"
                id="Password"
                name="password"
                v-model="password"
                class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
              />
            </div>

            <div class="col-span-6 sm:flex sm:items-center sm:gap-4">
              <button
                class="inline-block shrink-0 rounded-md border border-blue-600 bg-blue-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-transparent hover:text-blue-600 focus:outline-none focus:ring active:text-blue-500"
                type="submit"
              >
                Войти в аккаунт
              </button>
            </div>
          </form>
          <div v-if="errorMessage" class="col-span-6 mt-4 text-red-500">
            {{ errorMessage }}
          </div>
        </div>
      </main>
    </div>
  </section>
</template>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      email: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
    async login() {
      this.errorMessage = ''
      try {
        const response = await axios.post('http://localhost:5000/login', {
          email: this.email,
          password: this.password
        })
        if (response.status === 200) {
          localStorage.setItem('user', JSON.stringify(response.data.user))
          this.$router.push({ name: 'Events' })
        } else {
          this.errorMessage = response.data.message
        }
      } catch (error) {
        this.errorMessage = 'Введен неверно пароль или логин'
      }
    }
  }
}
</script>
