import { createApp } from 'vue'; // Импортируем createApp из Vue 3
import App from './App.vue'; // Импортируем корневой компонент
import axios from 'axios'; // Импортируем axios

// Создаем экземпляр приложения
const app = createApp(App);

// Настройка axios
axios.defaults.baseURL = 'http://localhost:8000/api'; // Указываем базовый URL для API

// Добавляем axios в глобальные свойства приложения
app.config.globalProperties.$http = axios;

// Монтируем приложение в элемент с id="app"
app.mount('#app');