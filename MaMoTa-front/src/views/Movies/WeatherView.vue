<template>
  <div class="icon">
    <div v-if="weatherStatus === 'Rain'" @click="handleWeatherIconClick('Rain')">
      <font-awesome-icon :icon="['fas', 'umbrella']" size="2xl" flip style="color: #acb9ec;" />
    </div>
    <div v-else-if="weatherStatus === 'Snow'" @click="handleWeatherIconClick('Snow')">
      <font-awesome-icon :icon="['fas', 'snowflake']" size="2xl" bounce style="color: #f7f7f7;" />
    </div>
    <div v-else-if="weatherStatus === 'Clear'" @click="handleWeatherIconClick('Clear')">
      <font-awesome-icon :icon="['fas', 'sun']" spin size="2xl" style="color: #fef5be;" />
    </div>
    <div v-else-if="weatherStatus === 'Sunny'" @click="handleWeatherIconClick('Sunny')">
      <font-awesome-icon :icon="['fas', 'sun']" spin size="2xl" style="color: #fef5be;" />
    </div>
    <div v-else-if="weatherStatus === 'Clouds'" @click="handleWeatherIconClick('Clouds')">
      <font-awesome-icon :icon="['fas', 'cloud']" beat-fade size="2xl" style="color: #0055ff;" />
    </div>
    <div v-else-if="weatherStatus === 'Mist'" @click="handleWeatherIconClick('Mist')">
      <font-awesome-icon :icon="['fas', 'smog']" beat-fade size="2xl" style="color: #ffffff;" />    
    </div>
    <div v-else-if="weatherStatus === 'Haze'" @click="handleWeatherIconClick('Haze')">
      <font-awesome-icon :icon="['fass', 'smog']" fade size="2xl" style="color: #e17b70;" />    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';

const key = import.meta.env.VITE_TMDB_API_KEY;
const weatherApiKey = import.meta.env.VITE_WEATHER_API_KEY;

const recommendedMovie = ref(null);
const weatherStatus = ref('');
const route = useRoute();
const router = useRouter();
console.log(weatherStatus)

const fetchWeather = async () => {
  const url = `http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=${weatherApiKey}`;
  try {
    const response = await axios.get(url);
    weatherStatus.value = response.data.weather[0].main;
    return weatherStatus.value;
  } catch (error) {
    alert('날씨정보 요청 실패');
    return null;
  }
};

const selectGenreByWeather = (weather) => {
  switch (weather) {
    case 'Mist':
      return 80
    case 'Haze':
      return 10752
    case 'Sunny':
      return 35
    case 'Rain':
      return 27;
    case 'Snow':
      return 10749;
    case 'Clear':
      return 12;
    case 'Clouds':
      return 53;
    default:
      return null;
  }
};

const fetchMovie = async () => {
  const weather = await fetchWeather();
  const genre = selectGenreByWeather(weather);

  if (genre !== null) {
    const url = `https://api.themoviedb.org/3/discover/movie?with_genres=${genre}&language=ko-KR&page=1`;
    const headers = {
      accept: 'application/json',
      Authorization: `Bearer ${key}`,
    };
    try {
      const response = await axios.get(url, { headers });
      const movies = response.data.results.slice(0, 10);
      recommendedMovie.value = movies[Math.floor(Math.random() * movies.length)];
    } catch (error) {
      console.error('TMDB 서버 요청 간 에러 발생:', error);
    }
  }
};

const handleWeatherIconClick = async (weather) => {
  const genre = selectGenreByWeather(weather);
  if (genre !== null) {
    // 여기에서 MovieDetail 페이지로 이동하는 로직 추가
    router.push({ name: 'movie', params: { id: recommendedMovie.value.id } });
  }
};

onMounted(fetchMovie);
</script>

<style scoped>


</style>
